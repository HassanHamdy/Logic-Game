import itertools
import copy
# tree and nodes definition using OOP
# data => 1, 3, 6, 8, 12
# maximum of 7 levels

class rootNode:
    # constructor
    def __init__(self):
        self.root = True
        self.children = []

class oddLevelNode:
    # constructor
    def __init__(self, number1, level):
        self.number1 = number1
        self.level = level
        self.children = []

class evenLevelNode:
    # contructor
    def __init__(self, number1, number2, level):
        self.number1 = number1
        self.number2 = number2
        self.level = level
        self.children = []

class Tree:
    # constructor
    def __init__(self):
        self.root = rootNode()

    # methods
    def insert(self):
        # placeholder
        print ("placeholder")


def generateCombinations(data, numberOfElements):
    # this method/function returns all possible combinations list
    # according to the number of elements needed

    return list(itertools.combinations(data, numberOfElements))


def duplicateList(dataList, numberOfTimes):
    # this method/function duplicates the list inside itself

    duplicatedList = []
    for item in dataList:
        for i in range(numberOfTimes):
            duplicatedList.append(copy.deepcopy(item))

    return duplicatedList


def initializeList(dataList, numberOfChoices):
    # this method/function initializes the list with empty lists
    for i in range(numberOfChoices):
        dataList.append([])


def configureDataList(data, chosenDataList, numberOfChoices):
    dataList = []
    initializeList(dataList, numberOfChoices)
    # this method/function copies data into a list of data for the next step
    # keeping the original input data unchanged
    for i in range(numberOfChoices):
        # the data is copied to the dataList to keep the original input unchanged
        dataList[i] = copy.deepcopy(data)
        for j in [0, 1]:
            # in this for loop the data chosen is removed from the data list
            # the range is 2 because the length of the tuple is 2 (e.g. (1, 3) )
            # you can access a tuple by calling tuple[index] (e.g. tuple[0] = 1 if tuple is (1, 3) )
            dataList[i].remove(chosenDataList[i][j])
            # can add a condition to print for checking
            # if j == 1, so the input is sent only once

    return dataList

def completeDataList(dataList, returnList):
    # this method/function adds choices back to the duplicated data list
    for i in range(len(dataList)):
        dataList[i].append(returnList[i])

    return dataList

def generateReturnList(sailList):
    # this method/function configures the return list based on the sail list
    # the sail list is the list of the step before the return step
    returnList = []
    for item in sailList:
        for i in [0, 1]:
            returnList.append(item[i])

    return returnList

def generateChildren(parentList):
    # this method/function configures the list of children
    children = []
    initializeList(children, len(parentList))
    for i in range(len(parentList)):
        children[i] = list(parentList[i])

    return children

def generateStep(data):
    # this method/function generates the state space of a list of input data
    # it returns a list containing 4 elements
    # element 1 is the sailing states (part 1 of a given step)
    # element 2 is the returning states (part 2 of a given step)
    # element 3 is the children of the previous step (the parents are the sailing states if step 1)
    # element 4 is the list of data to be used in the next step 
    completeList = []
    
    sailList = generateCombinations(data, 2)

    completeList.append(sailList)
    """print sailList
    print "\n\nStep 1 Results\n##############" """

    # dataList is the remaining data in the list(data) after the choices are done
    dataList = configureDataList(data, sailList, len(sailList))

    # create the list of the returning states
    returnList = generateReturnList(sailList)
    completeList.append(returnList)

    """     The List of Return States of the 1st level of nodes is done      """
    
    # generate list of children
    children = generateChildren(sailList)
    completeList.append(children)

    """     The List of Children of the 1st level of nodes is done      """

    # duplicate data list for each child of the first level
    # to start the next step
    # dataList is duplicated inside itself
    # without use of another variable to save memory space
    dataList = duplicateList(dataList, 2)
    
    # add choices back to the list
    dataList = completeDataList(dataList, returnList)
    completeList.append(dataList)    

    """     Ready to Start Step 2      """

    return completeList    

# ####################################################################

# data is the original set of inputs
data = [1, 3, 6, 8, 12]
# initialize lists which will hold separate lists from each step
"""completeSailList = []
completeReturnList = []
completeChildrenList = []"""

stepList = generateStep(data)

print ("\nlist of Options to sail from Shore A to Shore B")
print ("-----------------------------------------------")
print (stepList[0])
print ("\n\nlist of Options to sail from Shore B to Shore A")
print ("------------------------------------------------")
print (stepList[1])
print ("\n\nlist of Children of the previous step(the sailing list is the parents if step 1)")
print ("--------------------------------------------------------------------------------")
print (stepList[2])
print ("\n\nlist of Data to be used in the next step")
print ("----------------------------------------")
print (stepList[3])

"""completeSailList.append(stepList[0])
completeReturnList.append(stepList[1])
completeChildrenList.append(stepList[2])"""

        















