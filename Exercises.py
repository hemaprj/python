def calc_area(base, height):
    return (1/2)*base*height

print("Area is ",calc_area(10,15))

d={"China":143, "India":136,"USA":32,"Pakistan":21}
print(d)
action =input("What do you want to do? Print, Add, Remove or Query: ")

if action == "Print":
    for k,v in d.items():
        print(k, "==>",v)
elif action == "Add":
    NewCountry=input("What country do you want to add? ")
    if NewCountry in d:
        print("Country already exists!")
    else:
        NewPopulation=input("Please enter population for this country: ")
        d[NewCountry]=NewPopulation
        print(d)
elif action == "Remove":
    RemoveCountry=input("Please enter country you want to remove: ")
    if RemoveCountry in d:
        del d[RemoveCountry]
        print(d)
    else:
        print("Country does not exist!")
elif action == "Query":
    q=input("Which country you want to query: ")
    if q in d:
        print(d[q])
    else:
        print("Country does not exist!")


dict1={"Stock":"Prices","info":[600,630,620],"ril":[1430,1490,1567],"mtl":[234,180,160]}
print(dict1)

oper= input("Please enter Operation: ")
if oper=="print":
    for k,v in dict1.items():
        if v=="Prices":
            print("")
        else:
            m=round(sum(v)/len(v),2)
            print(k,"==>",v,"==> avg: " ,m)

if oper=="add":
    s=input("Please enter Stock: ")
    p=input("Please enter Prices: ")
    if s in dict1:
        dict1[s]=+p
    else:
        dict1[s]=p

print(dict1)


print(__name__)

'calling function'
import area
area.circle_calc()



