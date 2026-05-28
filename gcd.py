# gcd is also known as hcf 
def gcd(num1 , num2):
    Min=min(num1,num2)
    while(min):
        if num1%Min==0 and num2%Min==0:
            break
        Min-=1
    return Min

print(gcd(12,16))
