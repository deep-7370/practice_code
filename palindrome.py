# first method this is for string value
def palindrome1(num):
    temp=num
    rev=num[::-1]
    if temp==rev:
        return "palindrome"
    else:
        return "not a palindrome palindrome"

print(palindrome1("dees"))

#___________________________________________
#second method this is for numeric value 
def palindrome2(num):
    temp=num
    rev=0
    while(num):
        last_digit=num%10
        rev=rev*10+last_digit
        num=num//10
    if rev==temp:
        return "palindrome"
    else:
        return "not a palindrome"

print(palindrome2(123321))

#_________________________________________
#third method this is for string value
def palindrome3(num):
    first=0
    last=len(num)-1
    while(last>first):
        if (num[first]!=num[last]):
            return "not a palindrome"
        first+=1
        last-=1
    return "palindrome"

print(palindrome3(123321))

