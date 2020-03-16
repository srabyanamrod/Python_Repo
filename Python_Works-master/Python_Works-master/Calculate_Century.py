def calculate_year(year):
    if(len(year) < 3): print("1")
    elif(int(year) >= 1 and int(year) <= 2005):
        if(year[-1] == '0' and year[-2] == '0'):
            print(year[0:2])
        else:
            print(int(year[0:2]) + 1)
    else:
        print("Wrong input")

year = input("Enter the year: ")
calculate_year(year)
