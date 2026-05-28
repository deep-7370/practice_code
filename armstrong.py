n=16345
power=len(str(n))
num=n
result=0
while num>0:
    last_digit=num%10
    result+=last_digit**power
    num=num//10
if n==result:
    print("armstrong")
else:
    print("not armstrong")
