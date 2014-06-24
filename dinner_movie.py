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
import glob 
import os

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
	input_distance = (100 - (input_price + input_rating))
	count = 1

weights = [input_price, input_rating, input_distance]

print weights

#----------------------------------------------------------------
# GET DATA CORRESPONDING TO THE CATEGORY IN PANDAS 
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
#print df_userselected.head()

#----------------------------------------------------------------
# DO STATISTICS ON THE DATA 
#----------------------------------------------------------------

# Get mean and STDEV of prices and rating for all of the restaurants in the database: 
mu_price  = df_restaurants["price"].mean()
mu_rating = df_restaurants["rating"].mean()
std_price = df_restaurants["rating"].std()
std_rating = df_restaurants["rating"].std()

# For distance, use the user-specified zipcode distance: 
mu_distance = df_userselected["Distance"].mean()
std_distance = df_userselected["Distance"].std()

# Compute the Z-value for each restaurant: 
zprice    = (df_userselected["price"]    - mu_price) / std_price
zrating   = -(df_userselected["rating"]   - mu_rating) / std_rating
zdistance = (df_userselected["Distance"] - mu_distance) / std_distance

# Compute the Z-score for price, rating, and distance. This involves the weights:  
price_score    = (zprice * input_price)
rating_score   = (zrating * input_rating)
distance_score = (zdistance * input_distance) 

# Calculate the total score for each restaurant 

price_score    = (zprice    * input_price)
rating_score   = (zrating   * input_rating)
distance_score = (zdistance * input_distance)

zscore = (price_score + rating_score + distance_score)

#----------------------------------------------------------------
# ORGANIZE DATA AND POST TO SCREEN 
#----------------------------------------------------------------

# Put all of this information into the database for displaying: 

df_userselected["zscore"] = zscore
#print df_userselected.head()

# Sort restaurants by ascending order of Zscore: 

best = df_userselected.sort(["zscore"], ascending=[True])

#----------------------------------------------------------------
# GET USER CHOICE OF RESTAURANT 
#----------------------------------------------------------------

# Print out the top 5 restaurants along with their address and phone #: 
for i in range(0,5):
	rest_sr_no = str(i+1)
	this_best_rest = best.iloc[i].head(8)
	this_rest_name   = this_best_rest[0]
	this_rest_add    = this_best_rest[2]
	this_rest_rating = this_best_rest[4]
	this_rest_price  = this_best_rest[5]
	this_rest_dist   = this_best_rest[7]
	if (this_rest_price == 2 or this_rest_price == 2.5):
		this_rest_price = "$$"
	elif (this_rest_price == 3 or this_rest_price == 3.5):
		this_rest_price == "$$$"
	elif (this_rest_price < 2):
		this_rest_price == "$"
	else:
		this_rest_price == "$$$$"
	this_rest_noise  = this_best_rest[6] 
	print "({num:2s}) Restaurant Name: {rest:5s} \n Price: {price:3s} \n Rating: {rating:.1f} \n Distance: {dist:.2f}\n".format(rest = this_rest_name, price = this_rest_price, rating = this_rest_rating, dist = this_rest_dist, num=rest_sr_no)

input_restaurant = raw_input("Please select restaurant of your choice: ")
user_restaurant  = int(input_restaurant) - 1

user_rest = best.iloc[user_restaurant].head(8)
user_rest_name = user_rest[0]
user_rest_add  = user_rest[2]
user_rest_phone = user_rest[3]
print "Your restaurant of choice: "
print "Restaurant Name: {name:5s}\n Address: {address:5s}\n Phone # {phone:5s} " .format(name = user_rest_name, address=user_rest_add, phone=user_rest_phone)

#----------------------------------------------------------------
#  GET CHOICE OF MOVIE 
#----------------------------------------------------------------
# Read in the latest movies playing in theatres: 
#current_movies = glob.glob('data_prep/current_movies*.csv')
#current_movies = max(glob.iglob('data_prep/current_movies*.csv'), key=os.path.getctime)
#file_movie = current_movies[0]
#header_names_movie = ["movie_name", "parent_rating", "rotten_scores", "public_scores", "genre1", "genre2"]
#df_movies = pd.read_csv(file_movie, names = header_names_movie, )
#print df_movies 

# Output to JSON: 
#print best.head(3).to_json(orient="records")













