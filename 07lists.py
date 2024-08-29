lucky_numbers = [44, 18, 135, 16, 243, 42]
friends = ["Ali", "Muthu","Ah Hock", "Aminah", "Roshini", "Mei Ling"]

print(friends[3]) #print only 1 value, index starts from 0
print(friends[1:-2]) #print range of value. starting from index you choose on the left, and the right side index will not be included

#if you would like to modify the value
friends[-2] = "Jayaletchumi"
print(friends)


print(friends[-1])
#theres a few function that we can use with lists and those functions allow us to like modify the list and get information

#extend - take a list, append another list inside it

friends.extend(lucky_numbers)
print(friends)

#to add invidiual value to the end of the list
friends.append("Creed")
print(friends)

#if you want to add value in the middle of the list (first parameter is index, then name of the element you want to add )
friends.insert(1,"Abu")
print(friends)

#to remove element
friends.remove("Aminah")
print(friends)

#to get rid of every single element
#friends.clear()
#print(friends)

#to remove last element in the list, use pop function
friends.pop()
print(friends)

#to check if certain value/amount is in the list
print(friends.index("Mei Ling"))


#to count the frequency of an element in the list

friends = ["Ali", "Muthu", "Ah Hock", "Ah Hock", "Ah Hock", "Aminah", "Roshini", "Mei Ling"]
print(friends.count("Ah Hock"))


#to sort in alphaebatical order (but only applies to same data types)
#friends.sort()
#lucky_numbers.sort()
print(friends)
print(lucky_numbers)

#to reverse the order of the list
lucky_numbers.reverse()
print(lucky_numbers)