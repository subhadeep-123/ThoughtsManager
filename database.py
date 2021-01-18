import pymongo

CLIENT = pymongo.MongoClient('localhost', 27017)
FLAG = 0


def create_database():
    db = CLIENT['Thoughts-Manager']
    collection = db['SomeThoughts']
    return collection


def toJSON(uname, psswd):
    name = input("Enter Your Name - ")
    age = int(input("Enter Your Age - "))
    email = input("Enter Your Email - ")
    content = input("Write Here Anything You want - \n")
    data = {
        "username": uname,
        "password": psswd,
        "name": name,
        "age": age,
        "email": email,
        "content": content
    }
    return insert_data(data)


def insert_data(data):
    col = create_database()
    result = col.insert_one(data).inserted_id
    print("Data Inserted")


def check_acc_exists(uname, psswd):
    col = create_database()
    for account in create_database().find():
        if account['username'] == uname:
            if account['password'] == psswd:
                print("Welcome")
                FLAG = 1
            else:
                print("Password did not match")
        else:
            print("Username did not match")
    return FLAG


def read():
    pass


def update():
    pass


def delete():
    pass


if __name__ == "__main__":
    create_database()
