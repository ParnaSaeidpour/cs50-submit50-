
while True:

    fuel= input("Fraction: ")

    try:
        numerator,denomiantor = fuel.split("/")
        numerator_new = int(numerator)
        denomiantor_new= int(denomiantor)
        result= numerator_new/denomiantor_new

        if result <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
percent= int(result*100)

if percent <= 1:
    print("E")
elif percent >=99:
    print("F")
else:
    print(f"{percent}%")

