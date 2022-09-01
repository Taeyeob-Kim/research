A = int(input('Bank Balance :')) ##Bank_balance
B = int(input('period (day) : ')) ##Deposit period (days)

if 60 > B >= 30 :
    print(A + A * 0.008)
elif 90 > B >= 60 :
    print (A + A * 0.01)
elif 120 > B >= 90 :
    print (A + A * 0.0185)
elif 150 > B >= 120 :
    print (A + A * 0.019)
elif 180 > B >= 150 :
    print (A + A * 0.0225)
elif 210 > B >= 180 :
    print (A + A * 0.031)
elif 240 > B >= 210 :
    print (A + A * 0.0315)
elif 270> B >= 240 :
    print (A + A * 0.032)
elif 365 > B >= 270 :
    print (A + A * 0.033)
elif 548 > B >= 365 :
    print (A + A * 0.04)
elif 730 > B >= 548 :
    print (A + A * 0.0405)
elif B >= 730 :
    print (A + A * 0.041)
    
    ## Simple code to caculate rate of Bank deposit (ANZ)
