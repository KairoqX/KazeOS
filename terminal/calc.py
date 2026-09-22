def calc():
    while True:
        x = int(input("first no: "))
        y = (input("+, -, *, /: "))
        z = int(input("second no: "))

        if y == "+":
            print(x + z)
        elif y == "-":
            print(x - z)
        elif y == "*":
            print(x * z)
        elif y == "/":
            print(x//z)
        elif x or z == 0 and y == "/":
            print("0")
            
        else:
            print("invalide")

