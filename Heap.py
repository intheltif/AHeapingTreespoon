from __future__ import print_function
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
        self.set_last_node()

        print('---------- Before Heapify ----------')
        self.print_tree_levels()
        print()  # newline

        self.heapify(self.temp_path[0])

        print('---------- After Heapify ----------')
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
        while not current_node.right is None:
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

    def set_last_node(self):
        self.temp_path[-1].is_last_node = True
        # last node in the tree must also be the last node of its level
        self.temp_path[-1].is_level_end = True

    def print_tree_levels(self):
        """
        Prints the path lengths from left-to-right at each level in the tree in 
        the form specified by the instructions.

        :param root: The root node of this tree or subtree.
        """
        print('Root:     ', end='')
        current_level = 0
        for node in self.temp_path:
            print(node, end='')
            if node.is_level_end and not node.is_last_node:
                print()  # print a new line
                current_level += 1
                print('Level ' + str(current_level) + ':  ', end='')
            elif not node.is_last_node:
                print('--> ', end='')
            else:
                print()  # print a new line

    def find_node_index(self, node):
        for i in range(len(self.temp_path)):
            if node == self.temp_path[i]:
                return i

    def heapify(self, node):
        """
        Translates our binary tree into a minimum binary heap

        :param node: The node we are currently heapifying
        """
        # pdb.set_trace()
        if not node.left is None:
            self.heapify(node.left)
        if not node.right is None:
            self.heapify(node.right)
        if (not node.parent is None) and node.path_len < node.parent.path_len:
            # store the parent to avoid corruption as we swap
            parent = node.parent

            # get the indices of the nodes
            child_index = self.find_node_index(node)
            parent_index = self.find_node_index(parent)

            # store all of the child's pointers into temporary variables
            temp_left = node.left
            temp_right = node.right
            temp_parent = parent
            temp_is_last_node = node.is_last_node
            temp_is_level_end = node.is_level_end

            # move all of the parent's pointers to the child
            node.left = parent.left
            node.right = parent.right
            node.parent = parent.parent
            node.is_last_node = parent.is_last_node
            node.is_level_end = parent.is_level_end

            # move all of the temp's pointers to the parent
            parent.left = temp_left
            parent.right = temp_right
            parent.parent = temp_parent
            parent.is_last_node = temp_is_last_node
            parent.is_level_end = temp_is_level_end

            # switch the node's indices in the list
            tmp = self.temp_path[child_index]
            self.temp_path[child_index] = self.temp_path[parent_index]
            self.temp_path[parent_index] = tmp

            # update child information
            if node.left is not None:
                node.left.parent = node
            if node.right is not None:
                node.right.parent = node

            # reassign the node's new parent's children data
            if node.parent is not None:
                if node.parent.left == node.left or node.parent.left == node.right:
                    node.parent.left = node
                elif node.parent.right == node.left or node.parent.right == node.right:
                    node.parent.right = node
