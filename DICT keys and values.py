d={"Eno":"pqr","Ename":456}
print(d)
print(d["Ename"])
print(d.get("Eno"))
d["Ename"]="xyz"
print(d)
d["age"]=18
print(d)
for key in d:
    print(key)
for value in d.value():
    print(values)
for key,value in d.items():
    print(key,":",value)
    
d.pop("Eno")
print(d)
d.popitem()
print(d)
d.clear()
print(d)
