d={"tom":555,"sam":666,"rob":222}
d["samir"]=888
print(d)
print(d["rob"])
for k,v in d.items():
    print("key",k,"value",v)
del d["tom"]
print(d)

