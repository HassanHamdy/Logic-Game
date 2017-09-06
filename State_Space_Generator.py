import node
class  State_Space_Generator:
    def __init__(self):
        pass
    def generate_childeren(self,object):
        childeren   = []
        myRightList = []
        myLeftList  = []
        if (object.right_list == [] and object.left_list == [1, 3, 6, 8, 12]):
            return []
        if (object.rever_side == 2):
            i = 0
            while (True):
                j = i + 1
                while (True):
                    for c in object.right_list:
                        myRightList.append(c)
                    for c in object.left_list:
                        myLeftList.append(c)
                    #print(myRightList[i],myRightList[j])
                    child = node.node(myRightList[i], myRightList[j], 1)
                    child.set_lists(myRightList,myLeftList)
                    myRightList=[]
                    myLeftList=[]
                    childeren.append(child)
                    j = j + 1
                    if (j == len(object.right_list)):
                        break
                i = i + 1
                if (i == len(object.right_list)-1):
                    break
            object.add_childeren(childeren)
            return childeren
        if (object.rever_side == 1):
                for k in object.left_list:
                    for c in object.right_list:
                        myRightList.append(c)
                    for c in object.left_list:
                        myLeftList.append(c)
                        #print(k,0)
                    child = node.node(k, 0, 2)
                    child.set_lists(myRightList,myLeftList)
                    myRightList = []
                    myLeftList = []

                    childeren.append(child)
                object.add_childeren(childeren)
                return childeren