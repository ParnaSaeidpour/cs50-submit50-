result=input("Greeting: ")
new_result = result.lower().strip()

if "hello" in new_result:
    print("$0 ")
elif "h"==new_result[0]:
    print("$20")

else:
    print("$100")