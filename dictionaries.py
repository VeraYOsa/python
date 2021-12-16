release_year_dict = {"Thriller": "1982", "Back in Black": "1980", \
                    "The Dark Side of the Moon": "1973", "The Bodyguard": "1992", \
                    "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976", \
                    "Saturday Night Fever": "1977", "Rumours": "1977"}
release_year_dict


#get the keys and value
release_year_dict.keys()
release_year_dict.values()

#add an item
release_year_dict['Graduation'] = '2007'
release_year_dict


# Delete entries by key

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict


# Verify the key is in the dictionary

'The Bodyguard' in release_year_dict



# You will need this dictionary for the following questions:

# The Albums Back in Black, The Bodyguard and Thriller have the following music recording sales in millions 50, 50 and 65 respectively:

# a) Create a dictionary album_sales_dict where the keys are the album name and the sales in millions are the values.

# _sales_dict
# Write your code below and press Shift+Enter to execute
album_sales_dict = {"Back in Black":50, "the Bodyguard":50 , "Thriller":65}



# b) Use the dictionary to find the total sales of Thriller:

# Write your code below and press Shift+Enter to execute
album_sales_dict["Thriller"]

# c) Find the names of the albums from the dictionary using the method keys():

# Write your code below and press Shift+Enter to execute
album_sales_dict.keys()

# d) Find the values of the recording sales from the dictionary using the method values:

# Write your code below and press Shift+Enter to execute

album_sales_dict.values()
