n=121000
num=n
num2=0
while num>0:
    last_digit=num%10
    num2=num2*10+last_digit
    num=num//10
if n==num2:
    print("palindrome")
else:
    print("notpalindrome")
