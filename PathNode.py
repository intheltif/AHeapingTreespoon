"""
PathNode.py

A class to represent a node in our heap application

Author: Evert Ball
Author: Chris Wolf
Version: 1.0.0 (December 6, 2019)
"""
class PathNode:
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

    def __str__(self):
        """
        Creates the string representation of this PathNode

        :return: This pathnode as a string.
        """
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
