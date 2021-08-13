import json
def Log():
    flag_1= 0
    chance = 3
    for x in range(3):
        print("You have "+str(chance)+" chance\nyour username you use gmail.com format")
        b=input("Enter your good username :-")
        if b.islower() and "1" in b or "2" in b or "3" in b or "4" in b or "5" in b or "6" in b or "7" in b or "8" in b or "9" in b or "0" in b :
            if "@" in b and "." in b:
                print("Successfuly username")
                flag_1 +=1
                break
            else:
                print("Invalid username")           
        else:
            print("Invalid username")
        chance -=1
    if flag_1 == 1:
        chance = 3
        for x in range(3):
            print("You have "+str(chance)+" You use strong password format")
            c=input("Enter your best password :- ")
            if len(c)>=8 and len(c)<=16:
                if c.capitalize():
                    if "@" in c:
                        print("Successfuly password")
                        old_dict = {}
                        print("Bio DATA")
                        fname=input("Enter First name :- ")
                        lname=input("Enter last name :- ")
                        record=[b,c,fname,lname]
                        list1=["User","Pass","First_name","Last_name"]
                        for x in range(len(list1)):
                            old_dict[list1[x]]=record[x]
                        try:
                            with open("myjson.json","r") as obj:
                                b=json.load(obj)
                            for x in b["Info"]:
                                value=int(x)
                            b["Info"][str(value+1)]=old_dict
                            with open("myjson.json","w") as obj1:
                                json.dump(b,obj1,indent=4)
                            print("Your data successufly submited")
                        except:
                            a=1
                            old={}
                            old[str(1)]=old_dict
                            main={}
                            main["Info"]=old
                            with open("myjson.json","w") as c:
                                json.dump(main,c,indent=4)
                            print("Your data successufly submited")
                        break               
                    else:
                        print("Invalid password")                
                else:
                    print("Invalid")                
            else:
                print("Check your password length")
            chance -=1
    else:
        print("Please Create Your username and Password")



