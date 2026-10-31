def search(dic):
    name = input("Please enter the name to search: ")

    # found = False

    # for key, data in dic.items():
    #     if data["name"].lower() == name.lower():
    #         print("Student ID:", key)
    print("Name:", dic["name"])
    print("age:", dic["age"])
    print("qualification:",dic["qualification"])
    print("address:", dic["address"])
    print("email:",dic["email"])
    print("password:",dic["password"])
    print(dic)


    # if not found:
    #     print("Student not found!")