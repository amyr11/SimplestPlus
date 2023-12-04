from .tokens import TokenType
from .grammar import CFG


class GrammarHelper:
    def __init__(self):
        self._cfg = CFG
        self.first_set = self._first_set()
        self.follow_set = self._follow_set()

    def _first_set(self):
        all_first_set_cache = {}

        def get_first_set(production, cfg):
            all_first_set_cache[production] = set()

            assert (
                production in cfg.keys()
            ), f"Production {production} not found in CFG."

            for right_prod in cfg[production]:
                index = 0
                resolved = False

                while not resolved and index < len(right_prod):
                    first = right_prod[index]

                    if first is None or self._is_terminal(first):
                        # Terminal
                        all_first_set_cache[production].add(first)
                        resolved = True
                    else:
                        # Non-terminal
                        if first in all_first_set_cache.keys():
                            tmp_first_set = all_first_set_cache[first]
                        else:
                            tmp_first_set = get_first_set(first, cfg)

                        # Add the first set of the non-terminal without the null
                        all_first_set_cache[production].update(
                            [item for item in tmp_first_set if item is not None]
                        )

                        # If the current first set contains null, get the first set of the next item
                        if None in tmp_first_set:
                            index += 1
                        else:
                            resolved = True

                # If null is in first set of all items
                if not resolved:
                    all_first_set_cache[production].add(None)

            return all_first_set_cache[production]

        all_first_set = {}

        for production in self._cfg.keys():
            all_first_set[production] = get_first_set(production, self._cfg)

        return all_first_set

    def _follow_set(self):
        all_follow_set_cache = {}

        def get_follow_set(production, cfg, all_first_set):
            all_follow_set_cache[production] = set()

            for left, right in cfg.items():
                for right_prod in right:
                    # Skip if current production is not found on the right side
                    if production not in right_prod:
                        continue

                    next_item_index = right_prod.index(production) + 1
                    resolved = False

                    while not resolved and next_item_index < len(right_prod):
                        # Set the next item to the immediate item after the current non-terminal
                        next_item = right_prod[next_item_index]

                        if self._is_terminal(next_item):
                            all_follow_set_cache[production].add(next_item)
                            resolved = True
                        else:
                            # Add the first set of the next non-terminal without the null
                            next_first_set = all_first_set[next_item]

                            all_follow_set_cache[production].update(
                                [item for item in next_first_set if item is not None]
                            )

                            # If the first set of the next non-terminal contains null
                            if None in next_first_set:
                                next_item_index += 1
                            else:
                                resolved = True

                    if not resolved:
                        # Add to the follow set the follow set of the left production of the current production row
                        if left in all_follow_set_cache.keys():
                            all_follow_set_cache[production].update(
                                all_follow_set_cache[left]
                            )
                        else:
                            all_follow_set_cache[production].update(
                                get_follow_set(left, cfg, all_first_set)
                            )

            return all_follow_set_cache[production]

        all_follow_set = {}

        for production in self._cfg.keys():
            all_follow_set[production] = get_follow_set(
                production, self._cfg, self.first_set
            )

        return all_follow_set

    def _is_terminal(self, item):
        return isinstance(item, TokenType)

    def display_first_set(self):
        print(self._set_str(self.first_set, "FIRST SET"), end="\n\n")

    def display_follow_set(self):
        print(self._set_str(self.follow_set, "FOLLOW SET"), end="\n\n")

    def display_cfg(self):
        print(self._cfg_str(), end="\n\n")

    def export_cfg_first_follow(self, path):
        with open(path, "w") as f:
            f.write(self._cfg_str())
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
        for left, right in self._cfg.items():
            for right_prod in right:
                out += f"| {counter} | \{left} | -> | "
                counter += 1
                for i, right_prod_item in enumerate(right_prod):
                    if i > 0:
                        out += " "
                    if isinstance(right_prod_item, TokenType):
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
                        if isinstance(x, TokenType)
                        else "λ"
                    ),
                )
            ):
                if i > 0:
                    out += ", "
                if isinstance(item, TokenType):
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
                        if isinstance(x, TokenType)
                        else "λ"
                    ),
                )
            ):
                if i > 0:
                    out += ", "
                if isinstance(item, TokenType):
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
                        if isinstance(x, TokenType)
                        else "λ"
                    ),
                )
            ):
                if i > 0:
                    out += ", "
                if isinstance(item, TokenType):
                    out += f"{item.value}"
                else:
                    if item is None:
                        item = "λ"
                    out += f"{item}"
            out += "}"
            out += "\n"

        return out

    def _cfg_str(self):
        out = ""
        out += "---" + "\n"
        out += "CFG" + "\n"
        out += "---" + "\n"
        counter = 1
        max_len = len(max(self._cfg.keys(), key=(lambda x: len(x))))
        max_counter_text = f"{len(self._cfg.keys()) + 1}. "
        for left, right in self._cfg.items():
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
                    if isinstance(right_prod_item, TokenType):
                        out += f"{right_prod_item.value}"
                    else:
                        if right_prod_item is None:
                            right_prod_item = "λ"
                        out += f"{right_prod_item}"
                out += "\n"

        return out
