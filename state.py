# This is a very primitive implementation of the state object.
class state(object):

    def __init__(self, _type, _id):
        self.type = _type
        self.id = _id

    def __hash__(self):
        return self.id