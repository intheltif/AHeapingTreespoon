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
        self.generation = None  # left to right sibling or cousin

        # The number of children that this node has
        self.num_children = 0

        # True if the node is the last in the level
        self.is_level_end = False

        # True if the node is the right most node
        self.is_last_node = False

        # True if the node is the root of the overall heap
        self.is_root = False

        # This node's parent
        self.parent = None

    def get_node_size(self):
        """
        Returns the length of the path list which represents the size of this
        node. The node size is used to determine the node's ID.
        
        :return: the length of the path
        """
        return len(self.path)

    def get_path(self):
        """
        Returns an array of vertex IDs ordered by appearance in the path

        :return: self.path
        """
        return self.path

    def get_left_child(self):
        """
        Return the left node in this tree.

        :return: self.left
        """
        return self.left

    def get_right_child(self):
        """
        Return the right node in this tree.

        :return: self.right
        """
        return self.right

    def get_parent(self):
        """
        Return the parent of this node.

        :return: self.parent
        """
        return self.parent

    def get_generation(self):
        """
        Returns the node directly to the right of this node on the same 
        tree level.
        
        :return: self.generation
        """
        return self.generation

    def set_path(self, path=[]):
        """
        Set a list of vertex IDs ordered by appearance in the path

        :param path: A list of vertex IDs ordered by appearance in the path.
        """
        self.path = path

    def set_path_len(self):
        """
        Set the number of vertices in path which is the length of the path - 1.
        """
        self.path_len = len(self.path) - 1

    def set_left_child(self, node):
        """
        Set the left node in this tree.
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
        Set the node directly to the right of this node on the same
        tree level.

        :param node: The node directly to the right of this node.
        """
        self.generation = node

    def set_level_end(self, boolean):
        """
        Setter for level_end

        :param boolean: the new value for level_end
        """
        self.is_level_end = boolean

    def set_is_last_node(self, boolean):
        """
        Setter for is_last_node

        :param boolean: the new value for is_last_node
        """
        self.is_last_node = boolean

    def __str__(self):
        verts = ""

        for num in self.path:
            verts += num + ","
        
        # remove the last comma
        verts = verts[:-1]

        return "" + str(self.path_len) + "(" + verts + ")"
    
    def __eq__(self, other):
        """
        Determines whether or not two nodes are the same

        :param other: the other node we are comparing
        :return: True if the nodes are the same, False otherwise
        """
        if other is None:
            return False
        return self.path == other.path


