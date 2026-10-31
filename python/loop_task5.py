# 1st is tarha se bhi even odd dekh sakte hain
i=0
while i<=100:
    print("even number",i)
    i+=2
    
i=1
while i>=100:
    print("odd number",i) 
    i+=2  
    
for i in range(1, 101):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")