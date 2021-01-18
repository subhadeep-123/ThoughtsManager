import database
import time

USERNAME = input("Enter your Username - ")
PASSWORD = input("Enter Your Password - ")


def sign_up():
    if len(USERNAME) != 0 and len(PASSWORD) != 0:
        print("Creating Database...")
        time.sleep(1)
        database.toJSON(USERNAME, PASSWORD)


def log_in():
    if len(USERNAME) != 0 and len(PASSWORD) != 0:
        val = database.check_acc_exists(USERNAME, PASSWORD)
        if val == 1:
            pass
    else:
        print("Enter Username and Password")


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
    else:
        print("Enter Something Usefule dude!")


if __name__ == "__main__":
    main()
