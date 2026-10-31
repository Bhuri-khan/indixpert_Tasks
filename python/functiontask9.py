def func():
    uid = int(input("please enter the uid:"))
    name = input("please enter the name :")
    age = int(input("please enter the age:"))
    address = input("please enter the address:")
    dictionary ={
        "uid":uid,
        "name":name,
        "age":age,
        "address":address,   
    }
    
    print(dictionary)
func()