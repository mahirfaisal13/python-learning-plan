clintlist = ["tomal", "jamal", "numan","rakib"]
print(clintlist)

clintlist2 = ["abul", "nitul", "pappu","jony"]
clintlist.extend(clintlist2)
print(clintlist)

clintlist3 = ["abul", "togol", "motol"]
clintlist.extend(clintlist3)
print(clintlist)

clintlist.append("hannan")
print(clintlist)

if "nitul" in clintlist:
    print("yes, nitul is here")
    
    clintlist[2] = "salam"
    print(clintlist)
    
    clintlist.remove("nitul")
    print(clintlist)
    
    del clintlist[1]
    print(clintlist)