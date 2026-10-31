print("------------add student data--------------")
uid = int(input("please enter the uid: "))
name = input("please enter the name: ")
age=int(input("please enter the age: "))
qualification = input("please enter the qualification: ")
address = input("please enter the address:")

dictionary = {
    "uid":uid,
    "name":name,
    "age":age,
    "qualification":qualification,
    "address":address
}
print("----------------------------------------------")
print("============ STUDENTS REGISTRATION============")
print("----------------------------------------------")
print(dictionary)