if __package__:
    from .students.signup.signup import signup
    from .students.login.login import login
    from .students.profile.profile import profile
    from .students.course.course import course
    from .students.search.search import search
    from .students.fees.fees import fees
else:
    from students.signup.signup import signup
    from students.login.login import login
    from students.profile.profile import profile
    from students.course.course import course
    from students.search.search import search
    from students.fees.fees import fees

dictionary = {}

def menu():
    while True:
        print("1.signup")
        print("2.login")
        print("3.profile")
        print("4.course")
        print("5.search")
        print("6. fees")
        print("7.logout")
        choice = input("please enter the choice:").strip()

        if choice == "1":
            signup(dictionary)
        elif choice == "2":
            login(dictionary)
        elif choice == "3":
            if "name" in dictionary:
                profile(dictionary)
            else:
                print("Please sign up first.")
        elif choice == "4":
            course()
        elif choice == "5":
            search(dictionary)
        elif choice == "6":
            fees()
        elif choice == "7":
            print("logout")
            break
        else:
            print("invalid choice")


if __name__ == "__main__":
    menu()
                               