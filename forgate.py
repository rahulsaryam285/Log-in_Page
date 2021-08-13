import json
def Pass():
    with open("myjson.json","r") as obj:
        d=json.load(obj)
    user=input("Enter your Username :- ")
    flag = 0
    for x in d.values():
        for y in x.values():
            for z in y:
                if y.get(z) == user:
                    store = y
                    new=input("Enter new password :- ")
                    new1=input("Enter confirm your password :- ")
                    store["Pass"] = new
                    flag +=1
                    break
        if flag == 1:
            break
        else:
            print("Your username does not exist please try again ")
            break
    with open("myjson.json","w") as obj1:
        json.dump(d,obj1,indent=4)




    
