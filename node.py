

class Node():

    def __init__(self, parent_node):
        self.parent = parent_node
        self.new_child = False

    def query_parent(self):

        if self.parent:
            return self.parent.new_child

        return False

