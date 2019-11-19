class PathNode:
    """ A node in a tree data structure. """
    def __init__(self):
        # An array of vertex IDs ordered by appearance in the path
        self.path = []

        # An integer value representing the length of the path
        self.path_len = 0

        # Reference to the left child
        self.left = None

        # Reference to the right child
        self.right = None
        
        # Reference to the parent
        self.parent = None

        # Reference to the node directly to the right on the same tree level
        self.generation = None # left to right sibling or cousion

        # True if the node is the last in the level
        self.isLevelEnd = False

        # True if the node is the right most node
        self.isLastNode = False

    def getNodeSize(self):
        """
        Returns the length of the path list which represents the size of this
        node. The node size is used to determine the node's ID.
        
        TODO Add in param/return documentation
        """
        return len(self.path)

    def getPath(self):
        """
        Returns an array of vertex IDs ordered by appearence in the path
        """
        return self.path

    def getLeftChild(self):
        """
        Return the left node in this tree.
        """
        return self.left

    def getRightChild(self):
        """
        Return the right node in this tree.
        """
        return self.right

    def getParent(self):
        """
        Return the parent of this node.
        """
        return self.parent

    def getGeneration(self):
        """
        Returns the node directly to the right of this node on the same 
        tree level.
        """
        return self.generation

    def setPath(self, path=[]):
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

    def setLeftChild(self, node):
        """
        Return the left node in this tree.
        """
        self.left = node

    def setRightChild(self, node):
        """
        Return the right node in this tree.
        """
        self.right = node

    def setParent(self, node):
       """
       Return the parent of this node.
       """
       self.parent = node

    def setGeneration(self, node):
        """
        Returns the node directly to the right of this node on the same 
        tree level.
        """
        self.generation = node
