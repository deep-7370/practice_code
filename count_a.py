ss=str(input("enter string value : "))
lot=int(input("enter a lot val "))
max_val=0
count=0
for i in range(len(ss)):
    if i%lot==0:
        max_val=max(max_val,count)
        count=0
    if ss[i]=="a":
        count+=1
if count>max_val:
    max_val=count
print(max_val)