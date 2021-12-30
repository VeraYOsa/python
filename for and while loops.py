# For loop example
dates = [1982,1980,1973]
N = len(dates)

for i in range(N):
    print(dates[i])     

# Same example but replacing dates[i] with year
for year in dates:  
    print(year)   

# Use for loop to change the elements in list

squares = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before square ", i, 'is',  squares[i])
    squares[i] = 'white'
    print("After square ", i, 'is',  squares[i])

#change some but not all of the elements
for i in range(0, 4):
    squares[i] = 'white'
squares


# While Loop Example
dates = [1982, 1980, 1973, 2000]
i = 0
year = dates[0]

while(year != 1973):    
    print(year)
    i = i + 1
    year = dates[i]

print("It took ", i ,"repetitions to get out of loop.")
    

#Write a for loop the prints out all the element between -5 and 5 using the range function.

for i in range(-4,5):
    print(i)
    
#Print the elements of the following list: Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop'] Make sure you follow Python conventions.

Genres=[ 'rock', 'R&B', 'Soundtrack', 'R&B', 'soul', 'pop']
N= len(Genres)
for i in range(N):
    print (Genres[i])
    
    #alternative
for genres in Genres:
    print(genres)


#Write a for loop that prints out the following list: squares=['red', 'yellow', 'green', 'purple', 'blue']

squares=['red', 'yellow', 'green', 'purple', 'blue']
for square in squares:
    print(square)


#Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings. 
#If the score is less than 6, exit the loop. 
#The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]


PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i=0
while (PlayListRatings[i]>6) and len(PlayListRatings)>i:
    print(PlayListRatings[i])
    i=i+1


#Write a while loop to copy the strings 'orange' of the list squares to the list new_squares. 
#Stop and exit the loop if the value on the list is not 'orange':
squares = ['purple', 'blue ', 'orange','orange']
new_squares=[]
i=0

while (i<len(squares) and squares[i]=='orange'):
    new_squares.append(squares[i])
    i=i+1

new_squares
