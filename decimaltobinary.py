def DecimalToBinary(num):
    s=""
    while(num>0):
        r=num%2
        s=str(r)+s
        num=num//2
    return(s)
print(DecimalToBinary(10))