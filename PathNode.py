class PathNode:
    """ A node in a tree data structure. """
    def __init__(self, line):
        # An array of vertex IDs ordered by appearance in the path
        self.path = line.split()

        # An integer value representing the length of the path
        self.path_len = len(self.path) - 1

        # Reference to the left child
        self.left = None

        # Reference to the right child
        self.right = None
        
        # Reference to the parent
        self.parent = None

        # Reference to the node directly to the right on the same tree level
        self.generation = None # left to right sibling or cousin

        # The number of children that this node has
        self.num_children = 0

        # True if the node is the last in the level
        self.isLevelEnd = False

        # True if the node is the right most node
        self.isLastNode = False

    def get_node_size(self):
        """
        Returns the length of the path list which represents the size of this
        node. The node size is used to determine the node's ID.
        
        TODO Add in param/return documentation
        """
        return len(self.path)

    def get_path(self):
        """
        Returns an array of vertex IDs ordered by appearence in the path
        """
        return self.path

    def get_left_child(self):
        """
        Return the left node in this tree.
        """
        return self.left

    def get_right_child(self):
        """
        Return the right node in this tree.
        """
        return self.right

    def get_parent(self):
        """
        Return the parent of this node.
        """
        return self.parent

    def get_generation(self):
        """
        Returns the node directly to the right of this node on the same 
        tree level.
        """
        return self.generation

    def set_path(self, path=[]):
        """
        Returns an array of vertex IDs ordered by appearence in the path
        """
        self.path = path

    def set_path_len(self):
        """
        Sets the length of the path field.

        :return:
        """
        self.path_len = len(self.path) - 1

    def set_left_child(self, node):
        """
        Return the left node in this tree.
        """
        self.left = node

    def set_right_child(self, node):
        """
        Set the right node in this tree.

        :param node: The node to set the right child of this node to.
        """
        self.right = node

    def set_parent(self, node):
       """
       Set the parent of this node.

       :param node: The node to set the parent of this node to.
       """
       self.parent = node

    def set_generation(self, node):
        """
        Returns the node directly to the right of this node on the same 
        tree level.

        :param node: The node directly to the right of this node.
        :return: None.
        """
        self.generation = node

    def insert(self, line):
        """
        Inserts a new node into our tree.

        :param line: The next line read from the file.
        :return: None
        """
        if self.left is None:
            self.left = PathNode(line)
        elif self.right is None:
            self.right = PathNode(line)
        elif (self.left.num_children - self.right.num_children) > 1:
            self.right.insert(line)
        else:
            self.left.insert(line)
        self.num_children = self.num_children + 1

