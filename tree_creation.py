import node
import DFS_search
import State_Space_Generator
class  tree_creation :
    def __init__(self):
      pass

    def getPath(self):
        listOfLevel=[]
        generator=State_Space_Generator.State_Space_Generator()
        start_state=node.node(0, 0, 2)#bncreat el start state we bndeha el 2 persons ely haetn2lo we ely hena heb2o be zero tab3an + hanedeha el level ely hea wa2fa feh we ely hena heyb2a fe level zero we handeha 2 fe a5er parameter le2nha fe even level
        start_state.set_lists([],[])
        generator.generate_childeren(start_state)
        for k in start_state.childeren:
            subList=generator.generate_childeren(k)
            for i in subList:
                listOfLevel.append(i)
            subList=[]
        while(listOfLevel!=[]):
            state=listOfLevel.pop(0)
            subList=generator.generate_childeren(state)
            if(subList==[]):
                break
            for i in subList:
                listOfLevel.append(i)
        print('done')
        solution_path=[]
        worked_solution_path=[]
        search=DFS_search.DFS_search()
        search.DFS(start_state,solution_path,0)
        for i in solution_path:
            print(i.person1,i.person2,i.rever_side,i.timer)
            path_node_contains = (i.person1, i.person2, i.rever_side, i.timer)
            # put each node in the list for GUI
            worked_solution_path.append(path_node_contains)

        return worked_solution_path
