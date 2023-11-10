from typing import Optional

from .definitions import DefTranslator
from .tokens import Token, TokenType

"""
-------------
STATE MACHINE
-------------
"""


class StateMachine:
    # TODO: Final state checker (if in transition keys)
    # TODO: Duplicate transition input checker
    def __init__(
        self,
        initial: int,
        transitions: dict,
        final: dict,
        fallback: Optional["StateMachine"] = None,
    ):
        self.initial = initial
        self.final = final
        self.transitions = transitions
        self.fallback = fallback

    def tokenize_first(
        self, code, translator=DefTranslator(), verbose=True
    ) -> tuple[Optional[Token], str]:
        machine = self
        state = machine.initial
        tmp_code = code + "\0"
        token = None
        val = ""
        cur_char = ""

        while tmp_code != "" and code != "":
            cur_char = tmp_code[0]

            assert translator is not None, "Translator can't be None"
            ids = translator.translate(cur_char)
            new_state = machine._next(state, ids)

            if new_state is None:
                if verbose:
                    print(
                        f"No path found from state {state} with input {repr(cur_char)}"
                    )
                break

            if isinstance(new_state, tuple):
                machine = new_state[0]
                new_state = new_state[1]

            state = new_state
            tmp_code = tmp_code[1:]
            val += cur_char

            if verbose:
                print(f"Went to state {state}")

        if state in machine.final.keys():
            final_state = machine.final[state]

            if final_state.retract:
                val = val[:-1]

            token = Token(final_state.token_type, val)

            if verbose:
                print(f"Tokenized {repr(val)} with {token.type}")
        else:
            if verbose:
                print(f"Ended in a non-terminal state {state}")

        return token, val

    def _next(self, state, ids) -> Optional[int]:
        for id in ids:
            try:
                next_state = self.transitions[(state, id)]
                if next_state is not None:
                    return next_state
            except:
                continue

        return None

    def is_accepting_char(self, char) -> bool:
        translator = DefTranslator()
        ids = translator.translate(char)

        for id in ids:
            try:
                self.transitions[(self.initial, id)]
                if self.transitions[(self.initial, id)] is not None:
                    return True
            except:
                continue

        return False


class MachineGroup:
    def __init__(self, machines: list[StateMachine]):
        self.machines = machines

    def get_machine(self, char) -> Optional[StateMachine]:
        for machine in self.machines:
            if machine.is_accepting_char(char):
                return machine

        return None

    def tokenize_first(self, code, verbose=True) -> tuple[Optional[Token], str]:
        token = None
        val = ""
        machine = self.get_machine(code)

        if machine is not None:
            token, val = machine.tokenize_first(code, verbose=verbose)

        return token, val


class FinalState:
    def __init__(self, token_type: TokenType, retract: bool = True):
        self.token_type = token_type
        self.retract = retract
