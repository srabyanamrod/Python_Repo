name = "Murat"
surname = "Celiktepe"
age = 21

def quiz(name, surname, *args, shoes_number = 42):
    print("Name: ",name)
    print("Surname: ", surname)
    print("Age: ",float(args[0]))
    print(type(shoes_number))

quiz(name, surname, age)
