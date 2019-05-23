positive_count=0
nagative_count=0

i=1
for i in range (1,6):
    num=int(input("enter a num "))
    if(num>0):
        positive_count+=1
    else:
        nagative_count+=1

print(positive_count)
print(nagative_count)


