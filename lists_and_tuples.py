# Create a list
L = ["Michael Jackson", 10.1, 1982]
L

# Print the elements on each index
print('the same element using negative and positive indexing:\n Postive:',L[0],
'\n Negative:' , L[-3]  )
print('the same element using negative and positive indexing:\n Postive:',L[1],
'\n Negative:' , L[-2]  )
print('the same element using negative and positive indexing:\n Postive:',L[2],
'\n Negative:' , L[-1]  )


# List slicing
L[3:5]

# Use extend to add elements to list
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L

# Use append to add elements to list
L = [ "Michael Jackson", 10.2]
L.append(['pop', 10])
L

# Use extend to add elements to list
L = [ "Michael Jackson", 10.2]
L.extend(['pop', 10])
L

# Use append to add elements to list
L.append(['a','b'])
L

A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# Change the element based on the index
A = ["disco", 10, 1.2]
print('Before change:', A)
A[0] = 'hard rock'
print('After change:', A)

# Split the string, default is by space

'hard rock'.split()

# Split the string by comma

'A,B,C,D'.split(',')

# Copy (copy by reference) the list A

A = ["hard rock", 10, 1.2]
B = A
print('A:', A)
print('B:', B)

# Examine the copy by reference

print('B[0]:', B[0])
A[0] = "banana"
print('B[0]:', B[0])

# Clone (clone by value) the list A

B = A[:]



# Write your code below and press Shift+Enter to execute
a_list = [1, "hello", [1,2,3], True]
a_list


#Find the value stored at index 1 of a_list.

list[1]
# Write your code below and press Shift+Enter to execute
a_list[1]

# Write your code below and press Shift+Enter to execute
a_list[1:4]


# Write your code below and press Shift+Enter to execute
A = [1, 'a']
B = [2, 1, 'd']
A+B
