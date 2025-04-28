

def convert(ops,value ):
    if ops =="km":
        return f"Metre{value*1000}"
    elif ops =="metre":
        return f"KM {value / 1000}"
    else:
        return "Error"
print("hello\n")

ops = input(" metre or km ? : ")
value = int(input("enter value"))

print(convert(ops, value))

print("\noodbye")
