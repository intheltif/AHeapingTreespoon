from __future__ import print_function
from PathNode import PathNode
import sys


class Heap:
    """ A heap. """
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
        self.set_root()
        self.set_level_end()
        self.set_last_node()
        self.set_generation_links(self.root)
        self.set_parents(self.root)

        print('---------- Before Heapify ----------')
        self.print_tree_levels(self.root, 0)
        print()  # newline

        self.heapify(self.root)
        self.set_generation_links(self.root)

        print('---------- After Heapify ----------')
        self.print_tree_levels(self.root, 0)

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

    def set_root(self):
        """
        Sets the root of the tree
        """
        self.root = self.temp_path[0]
        self.temp_path[0].is_root = True

    def set_level_end(self):
        """ 
        Recursive method that sets isLevelEnd.

        :param root: The root node of this tree or subtree.
        """
        current_node = self.temp_path[0]
        current_node.is_level_end = True
        while current_node.right is not None:
            current_node = current_node.right
            current_node.is_level_end = True

    def set_generation_links(self, root):
        """
        Recursive method that sets the "generation" link of PathNode object
        from left-to-right. Generation is a term used to indicate a node on
        the same level (these may be siblings or cousins).

        :param root: The root node of this tree or subtree.
        """
        if root is None:
            return

        current = root
        current_index = self.find_node_index(current)

        while not current.is_level_end:
            current.generation = self.temp_path[current_index + 1]
            current = current.generation
            current_index += 1

        self.set_generation_links(root.left)

    def set_last_node(self):
        """
        Sets the last node of the tree
        """
        self.temp_path[-1].is_last_node = True
        # last node in the tree must also be the last node of its level
        self.temp_path[-1].is_level_end = True

    def print_tree_levels(self, root, level):
        """
        Prints the path lengths from left-to-right at each level in the tree in 
        the form specified by the instructions.

        :param root: The root node of this tree or subtree.
        :param level: The current level of the tree we are on
        """
        if root is None:
            return
        
        if level == 0:
            print("Root:    ", end="")
        else:
            print("Level " + str(level)+ ": ", end="")
        
        current = root

        while current is not None:
            if current.generation is None:
                print(current, "", end="")
            else:
                print(current, "--> ", end="")
            current = current.generation
        
        print()  # new line
        
        self.print_tree_levels(root.left, level + 1)

    def find_node_index(self, node):
        for i in range(len(self.temp_path)):
            if node == self.temp_path[i]:
                return i

    def heapify(self, root):
        """
        Translates our binary tree into a minimum binary heap

        :param root: The root of the tree we are heapifying
        """
        current = root
        previous = None

        # while we are not on the deepest level
        while current.left.left is not None:
            current = current.left
        
        # for each node in the heap
        next_level_above = current.parent
        while current is not None:
            next_node = current.generation
            self.should_swap(current)
            if current.generation is None:
                current = next_level_above
                next_level_above = current.parent
                previous = None
            else:
                previous = current
                current = next_node

        
    def set_parents(self, root):
        """
        Goes through our entire heap and sets the parents for each node

        :param root: The root of the tree we are setting parents for
        """
        if root is None:
            return
        
        # Set the parents of the specific children
        if root.left is not None:
            root.left.parent = root
        if root.right is not None:
            root.right.parent = root
        
        # Recursively set cparents
        self.set_parents(root.left)
        self.set_parents(root.right)

    def find_weight(self, node):
        """
        Evaluates the weight of the specific node

        :param node: the node we are evaulating the weight for
        :return: the weight of the node if it is not None
                 system's max size if it is None
        """
        if node is None:
            return sys.maxsize
        else:
            return node.path_len
    
    def swap_nodes(self, parent, child):
        """
        Swaps two nodes in our heap

        :param parent: the parent that is being swapped
        :param child: the child that is being swapped
        """
        if parent.left == child:
            child.parent = parent.parent
            child.left, parent.left = parent, child.left
            parent.parent = child
            child.right, parent.right = parent.right, child.right
        else:
            child.parent = parent.parent
            child.right, parent.right = parent, child.right
            parent.parent = child
            child.left, parent.left = parent.left, child.left
        
        # set the new parent's parent to be aware of the change
        if child.parent is not None:
            if child.parent.left == parent:
                child.parent.left = child
            else:
                child.parent.right = child
        
        # swap the remaining values
        child.is_root, parent.is_root = parent.is_root, child.is_root
        child.is_level_end, parent.is_level_end = parent.is_level_end, child.is_level_end
        child.is_last_node, parent.is_last_node = parent.is_last_node, child.is_last_node
        child.generation, parent.generation = parent.generation, child.generation

        # if the child is the new root of the tree, inform the root field
        if child.is_root:
            self.root = child

    def should_swap(self, node):
        """
        Determines whether or not a node should be swapped with its child
        Swaps them if it should

        :param node: the node we are determining whether or not to swap
        """
        left_weight = self.find_weight(node.left)
        right_weight = self.find_weight(node.right)
        current_weight = self.find_weight(node)
        min_weight = min(left_weight, right_weight, current_weight)

        if min_weight == left_weight and not min_weight == current_weight:
            self.swap_in_list(node, node.left)
            self.swap_nodes(node, node.left)
            self.should_swap(node)
        elif min_weight == right_weight and not min_weight == current_weight:
            self.swap_in_list(node, node.right)
            self.swap_nodes(node, node.right)
            self.should_swap(node)
        
    def swap_in_list(self, first_node, second_node):
        first_node_index = self.find_node_index(first_node)
        second_node_index = self.find_node_index(second_node)
        self.temp_path[first_node_index] = second_node
        self.temp_path[second_node_index] = first_node
            
# BUG: (0,4,1,2,3) and (0, 2, 3) are not swapping