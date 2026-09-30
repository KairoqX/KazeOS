def calc(a):
    args = a.split(" ")
    try:
        x = int(args[1])
        y = (args[2])
        z = int(args[3])

        if y == "+":
            print(x + z)
        elif z == 0 and y == "/":
            print("0")
        elif x == 0 and y == "/":
            print("0")
        elif y == "-":
            print(x - z)
        elif y == "*":
            print(x * z)
        elif y == "/":
            print(x/z)

            
        else:
            print("invalide")
    except Exception:
        print("some error occure or likely use didn't used spaces (calc 2 + 3)")
