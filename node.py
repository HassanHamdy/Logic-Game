class node :#el m7toa bta3 elnod elwa7da fe eltree
    def __init__(self,person1,person2,rever_side):
        self.person1=person1
        self.person2=person2
        self.rever_side=rever_side#lw d5ltha be 1 yeb2a kda el markeb 3al yemen lw d5ltha be 2 yeb2a elmarkeb 3al shemal
        self.right_list=[]
        self.left_list=[]
        self.timer=0
        self.childeren=[]
        self.parent=[]

    def add_childeren(self,childeren):
        for i in childeren:
            self.childeren.append(i)
    def calculate_time(self,time):
        if(self.person1>self.person2):
            a=self.person1
        else:
            a=self.person2
        self.timer=time+a

    def set_lists(self,right_list,left_list):
        if(self.person1==0 and self.person2==0):
            self.right_list=[1,3,6,8,12]
            self.left_list=[]
        else:
            self.right_list=right_list
            self.left_list=left_list
            if(self.rever_side==1):
                self.right_list.remove(self.person1)
                self.right_list.remove(self.person2)
                self.left_list.append(self.person1)
                self.left_list.append(self.person2)
            else:
                self.left_list.remove(self.person1)
                self.right_list.append(self.person1)
        self.right_list.sort()
        self.left_list.sort()
        print(self.person1,self.person2)
        print(self.left_list,self.right_list)#kont bat2kd en el lists bttmly sa7