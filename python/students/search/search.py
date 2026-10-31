def search(dictionary):
    name = input("Enter student name: ").strip().lower()


    if isinstance(dictionary, dict):
        if dictionary.get("name", "").strip().lower() == name:
            print("Total students found: 1")
            print("\nStudent Details:")
            print("Name:", dictionary.get("name", ""))
            print("Age:", dictionary.get("age", ""))
            print("Address:", dictionary.get("address", ""))
            print("Qualification:", dictionary.get("qualification", ""))
            print("Email:", dictionary.get("email", ""))
        else:
            print("Total students found: 0")
            print("Student not found.")

    
    elif isinstance(dictionary, list):
        result = [
            student for student in dictionary
            # if isinstance(student, dict)
            # and student.get("name", "").strip().lower() == name
        ]

        print("Total students found:", len(result))

        for student in result:
            print("\nStudent Details:")
            print("Name:", student.get("name", ""))
            print("Age:", student.get("age", ""))
            print("Address:", student.get("address", ""))
            print("Qualification:", student.get("qualification", ""))
            print("Email:", student.get("email", ""))

    else:
        print("Invalid student data.")