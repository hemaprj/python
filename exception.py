x=input("Enter a number: ")
y=input("Enter a number: ")
try:
    z=int(x)/int(y)
except Exception as e:
    print("Error is ", e)
    z=None
print("Result is ", z)
