def find(p,a):
    b=1
    for i in a:
        if i==p:
            b=2
    return b
class bala():
    def __init__(self):
        self.a=["thambaram","omr","velacherry"]
        self.d={"thambaram":["python","c"],"omr":["linux","sql"],"velacherry":["devops","aws"]}
        self.k={"python":15000,"aws":16000,"devops":17000,"linux":12000,"sql":8000,"c":14000}
        print("1.add""\n2.view")
        self.n=int(input("enter your option : "))
    