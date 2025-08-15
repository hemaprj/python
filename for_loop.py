exp=[20,30,40,50,60]
total=sum(exp)
print(total)
total=0
for i in exp:
    total=total+i
print(total)
for i in range(1,11):
    print(i)
for i in range(len(exp)):
    print("Month: ", i+1, "Expense: ", exp[i])
    total=total+exp[i]

print("Total: ", total)

key="chair"
locations=["garage","bedroom","chair","kitchen"]
for i in locations:
    if i==key:
        print("Key is found in ", i)
        break
    else:
        print("Key is not found in ", i)
        
