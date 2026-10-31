print("1.aditional:")
print("2.subtraction:")
print("3.multiplication:")
print("4.division:")
choice =int(input("please enter the choice:"))      
a= int(input("please enter the number:"))
b = int(input("please enter the number:"))    
       
if choice==1:
    print(a+b)
elif choice==2:
    print(a-b)
elif choice==3:
    print(a*b)
elif choice==4:
    print(a/b)
        
else:
    print("invalid")                
