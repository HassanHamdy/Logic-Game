import node
class DFS_search:
    def __init__(self):
        pass
    def DFS(self,S,solution_path,time):
        S.calculate_time(time)
        if(S.timer==29 and S.right_list==[] and S.left_list==[1,3,6,8,12]):
            solution_path.append(S)
            return True
        if(S.childeren==[]):
            return False
        for x in S.childeren:
            for k in S.childeren:
                list1 = []
                list2 = []
                for i in S.right_list:
                    list1.append(i)
                for i in S.left_list:
                    list2.append(i)
            a=self.DFS(x,solution_path,S.timer)
            if(a==True):
                solution_path.append(S)
                return True
        return False
             
            
         
        
        
    
       
    
