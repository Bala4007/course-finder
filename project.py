from ex import find
from ex import bala
class course(bala):
    def branch(self):
        #Add
        if self.n==1:
            p=input("enter the branch place : ")
            #call find function
            b=find(p,self.a)
            if b==1:
                self.a.append(p)
                return p
            else:
                print("already exist")
                return "NULL"
        #view
        elif self.n==2:
            for i in self.a:
                print(i)
            g=input("enter the place : ")
            return g
        else:
            print("enter valid number")
    def course(self,m):
        #add
        if self.n==1:
            #call find
            b=find(m,self.d.keys())
            if b==1:
                self.d[m]=[]
                #course add
                x=int(input("how many couse you want to add : "))
                for i in range(x):
                    course=input("enter the course : ")
                    self.d[m].append(course)
                print(self.d[m])
                return self.d[m]
            else:
                print("already exist")
        #view
        elif self.n==2:
            c=1
            while(c<3):
                s=input("enter the course : ")
                if s in self.d[m]:
                    c=4
                    return s
        
                else:
                    for i,k in self.d.items():
                        for j in k:
                            if j==s:
                                print("this course available in :"+str(i))
        else:
            return "enter valid number"
        
    def amount(self,o):
        #Add
        if self.n==1:
            for i in o:
                b=find(i,self.k.keys())
                if b==1:
                    nv=input("enter the amount "+i+": ")
                    self.k[i]=nv
                    print(self.k)
                else:
                    print("already exist course  "+str(i))
        #view
        elif self.n==2:
            print("the course fee is : ",self.k[o])
        else:
            return "enter valid number"