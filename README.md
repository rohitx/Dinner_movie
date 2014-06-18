Dinner_movie
============
The project is “Dinner+Movie”. The idea is that we wish to go for a date or just with friends, have a delicious dinner and watch an “edge-of-our-seat” movie. So, how do we do this? We could search sites such as Yelp to find a good restaurant and Fandango to decide on a movie. At the end of 30 min. we would have a choice of restaurant and a movie. But that’s such a waste of time! 

My application (currently written purely in Python) makes this easier by combining the two. The user will be presented with a webpage, the front-end (currently I am working on it) with four choices: (1) Approximate dollar amount the user wishes to spend for dinner; (2) Type of Cuisine; (3) Type of movie (i.e. Comedy, Action, etc.) and (4) Distance. Next to these there are 5 sliders which tell me “How important their choices are?” These sliders are: (1) Dollar amount; (2) Type of Cuisine; (3) Rating of Restaurant; (4) Distance; (5) Type of movie. 

I have collected data of 370 restaurants in San Francisco using Yelp, and Google Places API, Movies playing in theaters using RottenTomatoes API,  Theaters around San Francisco using Google Places API, and distances from 4 locations to movie theaters and restaurants using MapQuest API. 

I create a metric for restaurants. I compute a score for each restaurant using initial conditions the user provides and use weights from the sliders. I sort the restaurants by their score and present to the user. When the user selects a restaurant, I use the zip code of that restaurant and find theaters that are close by. 
