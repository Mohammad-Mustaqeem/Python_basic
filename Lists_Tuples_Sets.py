Name = ["Maaz", "Noman", "Hassan", "Zain", "Aman", "Affan", "Sameer"] 
print(Name)
print(len(Name))  # Length
print(Name[2])     # Accessing  specific element in list 
print(Name[-1])    # Accesssing from reverse list(last element)
print(Name[0:5])   # Specific part of list
print(Name[:2])
print(Name[1:]) 

# Modifying the list 
Name.append("Zaeem")  # inserts an element at the last postion in list 
print(Name)
Name.insert(2, "Shaibaz")
print(Name)
Name.insert(-1, "Shazz")
print(Name)
Last_Name = ["Aazmi", "Momin", "Inamdar"]
# Name.append(Last_Name)   It print 2 list as a list (Same case in insert)
# print(Name)
Name.extend(Last_Name)
print(Name)  # Joins to Lists 
Name.remove("Shaibaz")  # removes an element 
print(Name)
Name.pop()  # deletes the last element 
print(Name)
poppedelement = Name.pop()  # prints the popped element 
print(poppedelement)
Name.reverse()  # reverses the list 
print(Name)
Name.sort()
print(Name)
Name.sort(reverse=True)
print(Name)

# meow 

nums = [2, 3, 212, 9350, 7]
print(nums)
sorted_nums = sorted(nums)
print(sorted_nums)
print(max(nums))
print(min(nums))
print(sum(nums))

