def isEmpty(stk):
    if stk==[]:
        return True
    else:
        return False

def Push(stk,elt):
    stk.append(elt)
    print("element inserted")
    print(stk)

def Pop(stk):
    if isEmpty(stk):
        print("stack is empty")
    else:
        print("deleted element is:",stk.pop())

def Peek(stk):
    if isEmpty(stk):
        print("stack empty")
    else:
        print("element at top:",stk[-1])

def Display(stk):
    a=stk[::-1]
    print(a)
    
Stack=[]
while True:
    print(".......STACK OPERATIONS....")
    print("1.PUSH")
    print("2.POP")
    print("3.PEEK")
    print("4.DISPLAY")
    print("5.EXIT")
    ch=int(input("Enter Your Choice:"))
    if ch==1:
        element=int(input("enter element:"))
        Push(Stack,element)
    if ch==2:
        Pop(Stack)
    if ch==3:
        Peek(Stack)
    if ch==4:
        Display(Stack)
        
    elif ch==5:
        break
        
           
     
