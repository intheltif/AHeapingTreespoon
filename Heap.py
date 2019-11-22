from PathNode import PathNode


class Heap:
    """ A heap. """

    # TODO Most of the stuff below is just stubs for methods and accompanying 
    #      documentation. This may need to be changed as well any instance
    #      or class variables may need to be adjusted.
    
    # Temporary storage for the paths starting at temp_path[1]
    def __init__(self):
        self.temp_path = []
        self.tree = None

    def go(self, input_file):
        self.read_paths(input_file)

    def get_temp_path(self):
        """
        Returns the temporary path.
        :return: The temporary path class variable.
        """
        return self.temp_path

    def read_paths(self, input_file):
        """ 
        Reads inputFile given at the command line and places the contents of 
        each line into the path field found in each PathNode object. The order 
        is the same as found in the text file. Adds the PathNode object to the 
        temp_path starting at temp_path[1].
        
        :param input_file: The file to read the data from.
        """
        # FIXME: Takes in all paths but only builds the first two levels of the tree
        # Note to Evert: Should we just have this function take in the list and then
        #                write another function to turn the list into a binary tree
        # Open the file using 'with' keyword which auto closes file
        with open(input_file) as file_to_read:
            # recommended style for reading line by line. Memory efficient.
            for line in file_to_read:
                self.temp_path.append(PathNode(line))
                # if the list is a multiple of 3, we can set parent, left, right.
                if (len(self.temp_path) % 3) == 0:
                    # Get the unset nodes
                    parent = self.temp_path[-3]
                    left_child = self.temp_path[-2]
                    right_child = self.temp_path[-1]
                    # Set their parent/child status based on position in list
                    parent.set_left_child(left_child)
                    parent.set_right_child(right_child)
                    left_child.set_parent(parent)
                    right_child.set_parent(parent)
                    right_child.set_level_end(True)
            last_node = self.temp_path[-1]
            last_node.set_is_last_node(True)

    def build_complete_tree(self, index, parent):
        """
        Recursively builds a complete binary tree. Places PathNode objects in 
        temp_path into a complete binary tree in order of appearance in the text
        file. The left child of a parent located at temp_path[index] is found at
        temp_path[2 * index] and the right child is found at
        temp_path[(2 * index) + 1].

        :param index: The current index in the tree. TODO Is that right?
        :param parent: The node that is the parent of this node.
        """
        pass
        # TODO Finish buildCompleteTree function
        
    def set_level_end(self, root):
        """ 
        Recursive method that sets isLevelEnd.

        :param root: The root node of this tree or subtree.
        """
        pass
        # TODO Finish setLevelEnd function

    def set_generation_links(self, root):
        """
        Recursive method that sets the "generation" link of PathNode object
        from left-to-right. Generation is a term used to indicate a node on
        the same level (these may be siblings or cousins).

        :param root: The root node of this tree or subtree.
        """
        pass
        # TODO Finish setGenerationLinks function

    def print_tree_levels(self, root):
        """
        Prints the path lengths from left-to-right at each level in the tree in 
        the form specified by the instructions.

        :param root: The root node of this tree or subtree.
        """
        pass
        # TODO Finish printTreeLevels function
