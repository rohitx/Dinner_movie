#------------------------------------
# INPUT FROM THE USER 
#------------------------------------
# This program finds a restaurant for a user-specified conditions. 
# The program takes user-specified inputs such as : 
	# Category: Indian, Chinese, Thai, ...
	# Location of the user via zipcode 
# The user is then presented with "How important are the following conditions?"
# statement and requests use to input percentage values for the following conditions:
	# Distance 
	# Prices
	# Restaurant Ratings
#------------------------------------
# MAIN CALCULATIONS  
#------------------------------------	
# The program takes the zipcode and finds the appropriate column in the restaurant database. 
# If the distance is very important, it sorts by shortest distance from the zipcode. If not, 
# the program does not sort the distance column. 
# The program then computes a Z-factor for prices and ratings 
# The program then computes the z-score for each restaurant 
# The program then sorts in descending order of z-score
#------------------------------------
# OUTPUT 
#------------------------------------
# The program presents the user with 5 restaurants with their addresses and phone numbers. 
#------------------------------------
# DEPENDANCIES 
#------------------------------------
# makes use of restaurant_database_distances.csv 
# makes use of Pandas and Numpy packages 

#----------------------------------------------------------------
# IMPORT STATEMENTS 
#---------------------------------------------------------------- 
import numpy as np
import pandas as pd

#----------------------------------------------------------------
# READ FILE IN PANDAS 
#---------------------------------------------------------------- 
restaurants_file = 'data_prep/restaurant_database_distances.csv'
df_restaurants = pd.read_csv(restaurants_file)
# Change the dtypes of the DataFrame: 
df_restaurants[["rating", "price"]] = df_restaurants[["rating", "price"]].astype(float)

#----------------------------------------------------------------
# GET USER INPUT ON CATEGORY
#---------------------------------------------------------------- 

# GET ZIPCODE 
print "Zipcode choices: 94114, 94501, 94607, 94707"
input_zipcode = raw_input("Please Enter your zipcode: ")
user_zip = str(input_zipcode)

# GET CUISINE CHOICE: 
print "Here are the following categories:"
print "Indian(1), Chinese(2), Japanese(3), Korean(4), Italian(5), American(6), Mexican(7), Seafood(8)"
input_cat = raw_input("Enter your choice (1-8): ")
cat = int(input_cat) - 1
cuisine = df_restaurants["Category"].unique()
user_cat = cuisine[cat]

# GET PERCENTAGES 
print "How important are the following factors? Enter between (1-100): " 
count = 0
while count < 1:
	input_price  = int(raw_input("Price: "))
	rating_range = 100 - input_price
	if rating_range == 0:
		input_rating   = 0
		input_distance = 0
		break

	print "Enter between {input_price:2d} and {rating_range:2d}".format(rating_range=rating_range, input_price=input_price)
	input_rating   = int(raw_input("Rating: "))
	if (input_price - input_rating) == 0:
		input_distance = 0
		break
	else:
		input_distance = (100 - input_price - input_rating)
		count = 1

weights = [input_price, input_rating, input_distance]

#----------------------------------------------------------------
# JUST GET DATA CORRESPONDING TO THE CATEGORY IN PANDAS 
#---------------------------------------------------------------- 
df_cuisine = df_restaurants[(df_restaurants['Category'] == user_cat)]
ind = len(df_cuisine.index)+1
index_user = [i for i in range(1, ind, 1)]
user_columns = ["restaurant_name", "Category", "Address", "Phone_number", "rating", "price", "noise_level"]

df_userselected = pd.DataFrame(index = index_user, columns = user_columns)

df_userselected["restaurant_name"] = df_cuisine["restaurant_name"].values 
df_userselected["Category"] = df_cuisine["Category"].values
df_userselected["Address"] = df_cuisine["Address"].values
df_userselected["Phone_number"] = df_cuisine["Phone_number"].values
df_userselected["rating"] = df_cuisine["rating"].values
df_userselected["price"] = df_cuisine["price"].values
df_userselected["noise_level"] = df_cuisine["noise_level"].values
df_userselected["Distance"] = df_cuisine["Distance_from_"+user_zip].values
print df_userselected.head()

#----------------------------------------------------------------
# DO STATISTICS ON THE DATA 
#----------------------------------------------------------------

# Get mean values for prices and rating for all of the restaurants
fsafsa
 



