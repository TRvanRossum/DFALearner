# Rudimentary implementation of a DFA.
# The DFA should have this:
#   - A set of states
#   - A transition function
#   - An alphabet
#   - A start state
#   - A set of accepting states (this last one is not necessary as states have a flag to check whether they are accepting or rejecting).
class DFA(object):

    def __init__(self, _start, _alphabet):
        self.start = _start
        self.states = set()
        self.states.add(_start)
        self.alphabet = _alphabet
        self.transitions = dict()

    