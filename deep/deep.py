result=input("what is the answer to the Great question of life, the universe and Everything?")

if result.strip()== "42":
    print("Yes")
elif result.lower().strip()== "forty-two":
    pint("yes")
elif result.lower().strip()== "Forty two":
    print("yes")
else:
    print("No")