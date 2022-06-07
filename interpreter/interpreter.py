from ast import Expression


expression = input("Expression: ")

x, y, z = expression.split(" ")

x_new=float(x)
z_new=float(z)

if y=="+":
    result = x_new + z_new
if y=="-":
    result = x_new - z_new
if y=="*":
    result =x_new * z_new
if y=="/":
    result =x_new / z_new
print(round(result,1))