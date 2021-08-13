import Log_in
import Sign_up
import forgate
print(" 1. Login \n 2. Singup \n 3. Forget Password")
a=int(input(" Are you new user :- Enter 1 :-\n Already you have account :- Enter 2 :- \n Forget password :- Enter 3 :- "))
if a == 1:
    Log_in.Log()
elif a == 2:
    Sign_up.Sign()
else:
    forgate.Pass()
print("Thanks for Visit My site")