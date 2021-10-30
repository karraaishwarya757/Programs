def usdtoINR(n):
   if n >= 1:
        return  n * 74.92

us = int(input("Enter amount in usd: "))

if us < 0:
    print("Enter a valid amount ")
else:
    print("The amount in INR is ", usdtoINR(us))
