from PathNode import PathNode


class Heap:
    """ A heap. """

    # TODO Most of the stuff below is just stubs for methods and accompanying 
    #      documentation. This may need to be changed as well any instance
    #      or class variables may need to be adjusted.
    
    # Temporary storage for the paths starting at tempPath[1]
    def __init__(self):
        self.tempPath = []
        self.tree = None

    def get_temp_path(self):
        """
        Returns the temporary path.
        :return: The temporary path class variable.
        """
        return self.tempPath

    def read_paths(self, input_file):
        """ 
        Reads inputFile given at the command line and places the contents of 
        each line into the path field found in each PathNode object. The order 
        is the same as found in the text file. Adds the PathNode object to the 
        tempPath starting at tempPath[1].
        
        :param input_file: The file to read the data from.
        """
        # Open the file using 'with' keyword which auto closes file
        with open(input_file) as file_to_read:
            # recommended style for reading line by line. Memory efficient.
            for line in file_to_read:
                if tree is None:
                    tree = PathNode(line)
                else:
                    self.tree.insert(line)

    def build_complete_tree(self, index, parent):
        """
        Recursively builds a complete binary tree. Places PathNode objects in 
        tempPath into a complete binary tree in order of appearance in the text 
        file. The left child of a parent located at tempPath[index] is found at 
        tempPath[2 * index] and the right child is found at 
        tempPath[(2 * index) + 1].

        :param index: The current index in the tree. TODO Is that right?
        :param parent: The node that is the parent of this node.
        """
        # TODO Finish buildCompleteTree function
        
    def set_level_end(self, root):
        """ 
        Recursive method that sets isLevelEnd.

        :param root: The root node of this tree or subtree.
        """

        # TODO Finish setLevelEnd function

    def set_generation_links(self, root):
        """
        Recursive method that sets the "generation" link of PathNode object
        from left-to-right. Generatoin is a term used to indicate a node on
        the same level (these may be siblings or cousions).

        :param root: The root node of this tree or subtree.
        """

        # TODO Finish setGenerationLinks function

    def print_tree_levels(self, root):
        """
        Prints the path lengths from left-to-right at each level in the tree in 
        the form specified by the instructions.

        :param root: The root node of this tree or subtree.
        """

        # TODO Finish printTreeLevels function
