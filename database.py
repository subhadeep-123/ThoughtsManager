import pymongo
from pprint import pprint
CLIENT = pymongo.MongoClient('localhost', 27017)
FLAG = 0

db = CLIENT['Thoughts-Manager']
col = db['SomeThoughts']


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
    result = col.insert_one(data).inserted_id
    print("Data Inserted")


def check_acc_exists(uname, psswd):
    for account in col.find():
        if account['username'] == uname:
            if account['password'] == psswd:
                print("Welcome")
                FLAG = 1
            else:
                print("Password did not match")
        else:
            print("Username did not match")
    return FLAG


def read(uname, psswd):
    query = {"username": uname, "password": psswd}
    pprint(col.find_one(query))


def update(uname, psswd, key, new_val):
    for account in col.find():
        if account['username'] == uname and account['password'] == psswd:
            pprint(account)
        else:
            print("No Record Found")


def delete():
    pass
