from PathNode import PathNode


class Heap:
    """ A heap. """

    # TODO Most of the stuff below is just stubs for methods and accompanying 
    #      documentation. This may need to be changed as well any instance
    #      or class variables may need to be adjusted.

    # Temporary storage for the paths starting at temp_path[1]
    def __init__(self):
        # Create a temp_path with None as first element so that
        # build_complete_tree math will work correctly.
        self.temp_path = []

    def go(self, input_file):
        root_index = 0
        first = 1
        self.read_paths(input_file)
        self.build_complete_tree(first, root_index)
        self.set_level_end()
        self.print_tree_levels()

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
            for line in file_to_read:
                self.temp_path.append(PathNode(line))

    def build_complete_tree(self, index, parent):
        """
        Recursively builds a complete binary tree. Places PathNode objects in 
        temp_path into a complete binary tree in order of appearance in the text
        file. The left child of a parent located at temp_path[index] is found at
        temp_path[2 * index] and the right child is found at
        temp_path[(2 * index) + 1].

        :param index: Index of the current node in temp_path
        :param parent: index of the parent of the current node
        """
        left_index = (2*index)-1
        right_index = 2 * index

        if not left_index >= len(self.temp_path):
            self.temp_path[parent].set_left_child(self.temp_path[left_index])
            self.temp_path[left_index].set_parent(self.temp_path[parent])
        if not right_index >= len(self.temp_path):
            self.temp_path[parent].set_right_child(self.temp_path[right_index])
            self.temp_path[right_index].set_parent(self.temp_path[parent])

        # self.build_complete_tree(index+1, self.temp_path[index+1])
        if index <= len(self.temp_path):
            self.build_complete_tree(index+1, index)

    def set_level_end(self):
        """ 
        Recursive method that sets isLevelEnd.

        :param root: The root node of this tree or subtree.
        """
        current_node = self.temp_path[0]
        current_node.is_level_end = True
        while not current_node.right == None:
            current_node = current_node.right
            current_node.is_level_end = True

    def set_generation_links(self, root):
        """
        Recursive method that sets the "generation" link of PathNode object
        from left-to-right. Generation is a term used to indicate a node on
        the same level (these may be siblings or cousins).

        :param root: The root node of this tree or subtree.
        """
        pass
        # TODO Finish setGenerationLinks function

    def print_tree_levels(self):
        """
        Prints the path lengths from left-to-right at each level in the tree in 
        the form specified by the instructions.

        :param root: The root node of this tree or subtree.
        """
        # temporarily just print every node
        for node in self.temp_path:
            print(node)
