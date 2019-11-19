class Heap:
    """ A heap. """

    # TODO Most of the stuff below is just stubs for methods and accompanying 
    #      documentation. This may need to be changed as well any instance
    #      or class variables may need to be adjusted.
    
    # Creating a Linked List structure.
    class LinkedList:
        """
        A class to represent our linked list
        """
    
        def __init__(self):
            self.head = None
            self.tail = None
    
    class Node:
        """
        A class to represent a node in our linked list
        """
        def __init__(self, data):
            self.data = data
            self.next = None

    # Temporary storage for the paths starting at tempPath[1]
    def __init__(self):
        self.tempPath = []

    def getTempPath(self):
        """
        Returns the temporary path
        """
        return self.tempPath

    def readPaths(inputFile):
        """ 
        Reads inputFile given at the command line and places the contents of 
        each line into the path field found in each PathNode object. The order 
        is the same as found in the text file. Adds the PathNode object to the 
        tempPath starting at tempPath[1].
        
        TODO Add paramater and return documentation

        """
        # Open the file using 'with' keyword which auto closes file
        with open(inputFile, r) as fileToRead:
            # recommended style for reading line by line. Memory efficient.
            for line in fileToRead:
                node = PathNode()
                node.setPath(line)
                tempPath.append(node)


    
    def buildCompleteTree(index, parent):
        """
        Recursively builds a complete binary tree. Places PathNode objects in 
        tempPath into a complete binary tree in order of appearance in the text 
        file. The left child of a parent located at tempPath[index] is found at 
        tempPath[2 * index] and the right child is found at 
        tempPath[(2 * index) + 1].

        TODO Add paramater and return documentation

        """
        # TODO Finish buildCompleteTree function
        
    def setLevelEnd(root):
        """ 
        Recursive method that sets isLevelEnd.

        TODO Add parameter documentation
        """

        # TODO Finish setLevelEnd function

    def setGenerationLinks(root):
        """
        Recursive method that sets the "generation" link of PathNode object
        from left-to-right. Generatoin is a term used to indicate a node on
        the same level (these may be siblings or cousions).

        TODO Add parameter documentation
        """

        # TODO Finish setGenerationLinks function

    def printTreeLevels(root)
        """
        Prints the path lengths from left-to-right at each level in the tree in 
        the form specified by the instructions.

        TODO Add parameter documentation.
        """

        # TODO Finish printTreeLevels function
