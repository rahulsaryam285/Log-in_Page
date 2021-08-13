import json
def Sign():
    with open("myjson.json","r") as obj:
        d=json.load(obj)
    print("Check your Bio Data or not?")
    user=input("Enter your Username :- ")
    Pass=input("Enter your Password :- ")
    flag = 0
    for x in d.values():
        for y in x.values():
            for z in y:
                if y.get(z) == user or y.get(z) == Pass:
                    print("Success")
                    flag +=1
                    
        if flag == 2:
            break
        else:
            print("Your username or password does not exist please try again ")
            break
            
        
    



  
            

    
