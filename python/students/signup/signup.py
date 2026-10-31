import datetime

def signup(dictionary):
    while True:
            name = input("please enter the name:")
            if len(name)>4:
                if name.isalpha():
                    break
                else:
                    print("Invalid Your Name")
            else:
                print("Invalid Your Name")
    while True:
            age = input("please enter the age:")
            if len(age)>0:
                if age.isdigit():
                    break
                else:
                    print("Invalid Your Age")
            else:
                print("Please Age 0 to Greater")
    while True:
             
            address=input("Enter Address: ")
            if len(address)>4:
                if address.isalpha():
                    break
                else:
                    print("Invalid Your Address")
            print("Invalid Your Address")
    while True:
            email=input("Enter Email ID: ")
            if len(email)>6:
                if "@" in email and ".com" in email:
                    break
                else:
                    print("Invalid Your Email ID")
            else:
                print("Invalid Your Email ID")   
    while True:
        qualifications = []
        qualification = input("Enter Qualification: ")
        qualifications.append(qualification)

        choice = input("Add qualificatio (yes/no): ")

        if choice.lower() != "yes":
            break

        print("Your Qualifications:")
        
        for q in qualifications:
            print(q)

            qualification=input("Enter Qualification: ")
            if len(qualification)>1:
                if qualification.isalnum():
                    break
                else:
                    print("Invalid Your Qualification")           
    while True:
            password=input("Enter Password: ")
            if len(password)>6:
                if password.isalnum():
                    break
                else:
                    print("Invalid Your Password")
            else:
                print("Please 6 character password try again")
                
                
    print("------------------------------------------------------------")
    print("*********************STUDENTS DESHBOARD*********************")      
    print("------------------------------------------------------------")
    
    date = datetime.datetime.now()
    print(date)
    dictionary["name"]=name
    dictionary["age"]=age
    dictionary["address"]=address
    dictionary["qualification"]=qualification
    dictionary["email"]=email
    dictionary["password"]=password
    print ("students signup succesfull")
    print(dictionary)
