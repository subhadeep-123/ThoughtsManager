import database
import time
# USERNAME = input("Enter your Username - ")
# PASSWORD = input("Enter Your Password - ")
USERNAME = "matri"
PASSWORD = "iammatrix"
FLAG = 0


def sign_up():
    if len(USERNAME) != 0 and len(PASSWORD) != 0:
        print("Creating Database...")
        time.sleep(1)
        database.toJSON(USERNAME, PASSWORD)


def log_in():
    if len(USERNAME) != 0 and len(PASSWORD) != 0:
        val = database.check_acc_exists(USERNAME, PASSWORD)
        if val == 1:
            print("You are logged in")
            return True
        else:
            sign_up()
    else:
        print("Enter Username or Password is Incorrect")
        return False


def main():
    print("""
    OPTIONS
    1. SignUp
    2. LogIn
    3. Read
    4. Update
    5. Delete
    """)
    read = int(input())
    if read == 1:
        sign_up()
    elif read == 2:
        log_in()
    elif read == 3:
        if log_in() == True:
            database.read(USERNAME, PASSWORD)
        else:
    elif read == 4:
        var = input("Enter What you wanna Update - ")
        if var != 'age':
            new_val = input(f"Enter the new value of {var}")
        else:
            new_val = int(input(f"Enter the new value of {var}"))
        database.update(USERNAME, PASSWORD, var, new_val)
    elif read == 5:
        var = input("Enter What you want to Delete - ")
        # database.delete(var)
    else:
        print("Enter Something Usefule dude!")


if __name__ == "__main__":
    main()
