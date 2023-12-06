from operator import itemgetter
from .tokens import TokenType
from .grammar import CFG


class GrammarHelper:
    def __init__(self):
        self.cfg = CFG
        self.first_set = self._first_set()
        self.follow_set = self._follow_set()

    def _first_set(self):
        def get_first_set(production, cfg):
            first_set = set()

            assert (
                production in cfg.keys()
            ), f"Production {production} not found in CFG."

            for right_prod in cfg[production]:
                first = right_prod[0]

                if first is None or self._is_terminal(first):
                    # Terminal
                    first_set.add(first)
                else:
                    # Non-terminal
                    first_set.update(get_first_set(first, cfg))

            return first_set

        all_first_set = {}

        for production in self.cfg.keys():
            all_first_set[production] = get_first_set(production, self.cfg)

        return all_first_set

    def _follow_set(self):
        all_follow_set_cache = {}

        def get_follow_set(production, cfg, all_first_set, from_production=None):
            if from_production is not None:
                tmp_log = f"Resolving pending {production} from {from_production}:\n"
            else:
                tmp_log = f"{production}:\n"
            line = "-" * len(tmp_log) + "\n"
            log = line + tmp_log + line

            follow_set = set()
            pending_follow_sets = []

            production_row_no = 0
            for left, right in cfg.items():
                for right_prod in right:
                    production_row_no += 1
                    # Skip if current production is not found on the right side
                    if production not in right_prod:
                        continue

                    production_indeces = []

                    for i, item in enumerate(right_prod):
                        if item == production:
                            production_indeces.append(i)

                    next_item = None

                    for production_index in production_indeces:
                        next_item_index = production_index + 1
                        resolved = False

                        while not resolved and next_item_index < len(right_prod):
                            # Set the next item to the immediate item after the current non-terminal
                            next_item = right_prod[next_item_index]

                            if self._is_terminal(next_item):
                                follow_set.add(next_item)
                                log += f"From production {production_row_no}, added terminal `{next_item.value}` to {production}'s follow set ({production} -> {next_item.value}).\n"
                                resolved = True
                            else:
                                # Add the first set of the next non-terminal without the null
                                next_first_set = all_first_set[next_item]
                                follow_set.update(
                                    [
                                        item
                                        for item in next_first_set
                                        if item is not None
                                    ]
                                )
                                log += f"From production {production_row_no}, added {next_first_set} to {production}'s follow set ({production} -> FIRST({next_item})).\n"

                                # If the first set of the next non-terminal contains null
                                if None in next_first_set:
                                    next_item_index += 1
                                    log += f"From production {production_row_no}, {next_item} contains null, moving to the next item.\n"
                                else:
                                    resolved = True

                        if not resolved and left != from_production:
                            if next_item is None:
                                log += f"From production {production_row_no}, {production} is the last item, adding {left}'s follow set to {production}'s follow set ({production} -> FOLLOW({left})).\n"
                            else:
                                log += f"From production {production_row_no}, {next_item} is the last item, adding {left}'s follow set to {production}'s follow set ({production} -> FOLLOW({left})).\n"
                            if left in all_follow_set_cache:
                                # Add to the follow set the follow set of the left production of the current production row
                                follow_set.update(all_follow_set_cache[left])
                                log += f"Added {left}'s cached follow set {all_follow_set_cache[left]} to {production}'s follow set ({production} -> FOLLOW({left})).\n"
                            else:
                                # Add the left production to the pending follow sets
                                if left not in pending_follow_sets:
                                    pending_follow_sets.append(left)
                                    log += f"Added {left} to pending follow sets.\n"
                                else:
                                    log += f"{left} is already in pending follow sets, skipping.\n"
                        elif not resolved and left == from_production:
                            log += f"From production {production_row_no}, {from_production} is not yet resolved, skipping.\n"

            # Find the follow set of the pending productions
            if len(pending_follow_sets) > 0:
                log += f"Resolving pending follow sets from {production}: {pending_follow_sets}\n"
            for pending_production in pending_follow_sets:
                pending_follow_set, pending_log = get_follow_set(
                    pending_production, cfg, all_first_set, production
                )
                follow_set.update(pending_follow_set)
                log += pending_log
                log += f"Added {pending_production}'s follow set {all_follow_set_cache[pending_production]} to {production}'s follow set ({production} -> FOLLOW({pending_production})).\n"

            # Add the follow set of the current production to cache
            all_follow_set_cache[production] = follow_set
            log += f"Added {production}'s follow set {follow_set} to cache.\n"

            return follow_set, log

        all_follow_set = {}
        logs = ""

        for production in self.cfg.keys():
            all_follow_set[production], log = get_follow_set(
                production, self.cfg, self.first_set
            )
            logs += log + "\n\n\n"

        # write log to text file
        with open("./dump/follow_set_log.txt", "w") as f:
            f.write(logs)

        return all_follow_set

    def _is_terminal(self, item):
        return isinstance(item, TokenType)

    def display_first_set(self):
        print(self._set_str(self.first_set, "FIRST SET"), end="\n\n")

    def display_follow_set(self):
        print(self._set_str(self.follow_set, "FOLLOW SET"), end="\n\n")

    def displaycfg(self):
        print(self.cfg_str(), end="\n\n")

    def exportcfg_first_follow(self, path):
        with open(path, "w") as f:
            f.write(self.cfg_str())
            f.write("\n\n")
            f.write(self._set_str(self.first_set, "FIRST SET"))
            f.write("\n\n")
            f.write(self._set_str(self.follow_set, "FOLLOW SET"))

    def export_all_md(self, path):
        with open(path, "w") as f:
            f.write(self._all_md())

    def _all_md(self):
        out = ""
        out += "## CFG\n\n"
        out += "| No. | Production | -> | Right Side |\n"
        out += "| --- | ---------- | -- | ---------- |\n"
        counter = 1
        for left, right in self.cfg.items():
            for right_prod in right:
                out += f"| {counter} | \{left} | -> | "
                counter += 1
                for i, right_prod_item in enumerate(right_prod):
                    if i > 0:
                        out += " "
                    if self._is_terminal(right_prod_item):
                        if right_prod_item.value in ["\\n", "\\t"]:
                            out += f"\{right_prod_item.value}"
                        else:
                            out += f"{right_prod_item.value}"
                    else:
                        if right_prod_item is None:
                            out += "λ"
                        else:
                            out += f"\{right_prod_item}"
                out += " |\n"
        out += "\n\n"
        out += "## FIRST SET\n\n"
        out += "| No. | Production | First Set |\n"
        out += "| --- | ---------- | --------- |\n"
        counter = 1
        for left, right in self.first_set.items():
            out += f"| {counter} | \{left} | "
            counter += 1
            out += "{"
            for i, item in enumerate(
                sorted(
                    right,
                    key=(
                        lambda x: x
                        if isinstance(x, str)
                        else x.value
                        if self._is_terminal(x)
                        else "λ"
                    ),
                )
            ):
                if i > 0:
                    out += ", "
                if self._is_terminal(itemgetter):
                    if item.value in ["\\n", "\\t"]:
                        out += f"\{item.value}"
                    else:
                        out += f"{item.value}"
                else:
                    if item is None:
                        item = "λ"
                    out += f"{item}"
            out += "}"
            out += " |\n"
        out += "\n\n"
        out += "## FOLLOW SET\n\n"
        out += "| No. | Production | Follow Set |\n"
        out += "| --- | ---------- | ---------- |\n"
        counter = 1
        for left, right in self.follow_set.items():
            out += f"| {counter} | \{left} | "
            counter += 1
            out += "{"
            for i, item in enumerate(
                sorted(
                    right,
                    key=(
                        lambda x: x
                        if isinstance(x, str)
                        else x.value
                        if self._is_terminal(x)
                        else "λ"
                    ),
                )
            ):
                if i > 0:
                    out += ", "
                if self._is_terminal(item):
                    if item.value in ["\\n", "\\t"]:
                        out += f"\{item.value}"
                    else:
                        out += f"{item.value}"
                else:
                    if item is None:
                        item = "λ"
                    out += f"{item}"
            out += "}"
            out += " |\n"
        return out

    def _set_str(self, s, name):
        out = ""
        out += "-" * len(name) + "\n"
        out += name + "\n"
        out += "-" * len(name) + "\n"
        counter = 1
        max_len = len(max(s.keys(), key=(lambda x: len(x))))
        max_counter_text = f"{len(s.keys()) + 1}. "
        for left, right in s.items():
            counter_text = f"{counter}. "
            spaces = " " * (
                (len(max_counter_text) + max_len) - (len(counter_text) + len(left)) + 2
            )
            out += f"{counter_text}{left}{spaces}->  "
            counter += 1
            out += "{"
            for i, item in enumerate(
                sorted(
                    right,
                    key=(
                        lambda x: x
                        if isinstance(x, str)
                        else x.value
                        if self._is_terminal(x)
                        else "λ"
                    ),
                )
            ):
                if i > 0:
                    out += ", "
                if self._is_terminal(item):
                    out += f"{item.value}"
                else:
                    if item is None:
                        item = "λ"
                    out += f"{item}"
            out += "}"
            out += "\n"

        return out

    def cfg_str(self):
        out = ""
        out += "---" + "\n"
        out += "CFG" + "\n"
        out += "---" + "\n"
        counter = 1
        max_len = len(max(self.cfg.keys(), key=(lambda x: len(x))))
        max_counter_text = f"{len(self.cfg.keys()) + 1}. "
        for left, right in self.cfg.items():
            for right_prod in right:
                counter_text = f"{counter}. "
                spaces = " " * (
                    (len(max_counter_text) + max_len)
                    - (len(counter_text) + len(left))
                    + 2
                )
                out += f"{counter_text}{left}{spaces}->  "
                counter += 1
                for i, right_prod_item in enumerate(right_prod):
                    if i > 0:
                        out += " "
                    if self._is_terminal(right_prod_item):
                        out += f"{right_prod_item.value}"
                    else:
                        if right_prod_item is None:
                            right_prod_item = "λ"
                        out += f"{right_prod_item}"
                out += "\n"

        return out
