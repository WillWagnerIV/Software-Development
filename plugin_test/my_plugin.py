@pytest.fixture (autouse = True)
def greetings():
    user_name = input ('Enter Name: ')
    print("Hello " + user_name +  ".  Thanks for using this awesome plugin.")

