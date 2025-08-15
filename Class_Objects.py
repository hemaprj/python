class employee:
    def __init__(self, id, name):
        self.id=id
        self.name=name

    def display(self):
        print(self.id,self.name)


emp=employee(1,"coder")
emp.display()

del emp.id

try:
    print(emp.id)
except Exception as e:
    print("Error is ", e)

del emp
print(emp.name)