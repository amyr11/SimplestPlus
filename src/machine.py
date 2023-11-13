from typing import Optional
from uu import Error

from .definitions import DefTranslator
from .tokens import Token, TokenType

"""
-------------
STATE MACHINE
-------------
"""


class StateMachine:
    # TODO: Final state checker (if in transition keys)
    def __init__(
        self,
        name: str,
        initial: int,
        transitions: dict,
        final: dict,
        fallback: Optional["StateMachine"] = None,
        translator: DefTranslator | None = None,
    ):
        self._name = name
        self._initial = initial
        self._final = final
        self._transitions = transitions
        self._fallback = fallback

        if translator is None:
            self._translator = DefTranslator()

        self._check_transition_duplicates()

    def tokenize_first(self, code: str, verbose=True) -> tuple[Optional[Token], str]:
        machine = self
        state = machine._initial
        tmp_code = code + "\0"
        token = None
        val = ""
        cur_char = ""

        while tmp_code != "" and code != "":
            cur_char = tmp_code[0]

            ids = self._translator.translate(cur_char)
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

        if state in machine._final.keys():
            final_state = machine._final[state]

            if final_state.retract:
                val = val[:-1]

            token = Token(final_state.token_type, val)

            if verbose:
                print(f"Tokenized {repr(val)} with {token.type}")
        else:
            if verbose:
                print(f"Ended in a non-terminal state {state}")

        return token, val

    def _next(self, state: int, ids: list[str]) -> Optional[int]:
        for id in ids:
            try:
                next_state = self._transitions[(state, id)]
                if next_state is not None:
                    return next_state
            except:
                continue

        return None

    def is_accepting_char(self, char: str) -> bool:
        translator = DefTranslator()
        ids = translator.translate(char)

        for id in ids:
            try:
                self._transitions[(self._initial, id)]
                if self._transitions[(self._initial, id)] is not None:
                    return True
            except:
                continue

        return False

    def _check_transition_duplicates(self):
        states = {key[0] for key in self._transitions.keys()}

        for state in states:
            transition_inputs = [
                key[1] for key in self._transitions.keys() if key[0] == state
            ]

            if len(transition_inputs) == 1:
                continue

            inputs = []

            for transition_input in transition_inputs:
                cur_inputs = []

                if transition_input in self._translator.definitions:
                    cur_inputs = self._translator.definitions[transition_input]
                else:
                    cur_inputs = [transition_input]

                duplicates = set(inputs) & set(cur_inputs)

                if len(duplicates) > 0:
                    raise Exception(
                        f"('{self._name}' machine) Duplicate input/s {duplicates} in state {state}'s transitions."
                    )

                inputs.extend(cur_inputs)


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
