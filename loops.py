nums = [1, 2, 3, 4, 5]
for num in nums:
    if num == 3:
     print("Found")
     break
    print(num)

a=[1,2,3,4,5,]
b=[1,2,3,4,5,]
b=a
print (id(a))
print (id(b))
print(a==b)

condition = 10
if condition:
    print('this is true')
else:
    print('this is false')     