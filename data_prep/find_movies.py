import urllib, json, yaml
from datetime import datetime
from time import sleep


url = "http://api.rottentomatoes.com/api/public/v1.0/lists/movies/in_theaters.json?apikey=gtpf26gfz747nzajm26uz9hp"
response = urllib.urlopen(url)
data = json.loads(response.read())

def convert(input):
    if isinstance(input, dict):
        return {convert(key): convert(value) for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [convert(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

data_clean = convert(data)
movies = data_clean["movies"]

movie_titles = []
mpaa_rating = []
runtime = []
ratings = []
movie_id = []
for movie in movies:
	movie_titles.append(movie["title"])
	mpaa_rating.append(movie["mpaa_rating"])
	runtime.append(movie["runtime"])
	ratings.append(movie["ratings"])
	movie_id.append(movie["id"])
#---------------------------------------------
# GET RATINGS BY CRITQUES & AUDIENCE 
#---------------------------------------------
rating_critics  = []
rating_audience = []
for rating in ratings: 
	rating_critics.append(rating["critics_score"])
	rating_audience.append(rating["audience_score"])

#print movie_titles
#print rating_critics	

#---------------------------------------------
# GET GENRE FOR EACH MOVIE 
#---------------------------------------------
movie_genre = []
movie_ids = ['771317257']
movie_synopsis = []
for ids in movie_id:
	print "Sleeping for 3 sec..."
	sleep(3)
	url_id = "http://api.rottentomatoes.com/api/public/v1.0/movies/"+ids+".json?apikey=gtpf26gfz747nzajm26uz9hp"
	response = urllib.urlopen(url_id)
	data_id = json.loads(response.read())
	moviegenre_clean = convert(data_id)
	movie_genre.append(moviegenre_clean["genres"])
	movie_synopsis.append(moviegenre_clean["synopsis"])

#---------------------------------------------
# CREATE CSV FILE FOR MOVIES PLAYING IN THEATERS 
#---------------------------------------------
date_today = ((datetime.now().isoformat()).split('T'))[0] 
filename = open("current_movies_"+date_today+".csv", "w")
for i in range(len(rating_critics)):
	this_title = movie_titles[i]
	this_mpaa  = mpaa_rating[i]
	this_runtime = runtime[i]
	this_crating = rating_critics[i]
	this_genre   = movie_genre[i]
	this_synopsis = movie_synopsis[i]
	print this_genre
	if len(this_genre) < 2:
		this_genre1 = this_genre[0]
		filename.write("{this_title:5s}, {this_mpaa:5s}, {this_runtime:5d}, {this_crating:5d}, {this_genre1:5s} \n".format(this_title=this_title, this_mpaa=this_mpaa, this_runtime=this_runtime, this_crating=this_crating, this_genre1=this_genre1))
	elif len(this_genre) == 2:
		this_genre1 = this_genre[0]
		this_genre2 = this_genre[1]
		filename.write("{this_title:5s}, {this_mpaa:5s}, {this_runtime:5d}, {this_crating:5d}, {this_genre1:5s}, {this_genre2:5s}\n".format(this_title=this_title, this_mpaa=this_mpaa, this_runtime=this_runtime, this_crating=this_crating, this_genre1=this_genre1, this_genre2=this_genre2))
	else:
		print "Too many genre categories in ", this_title
		this_genre1 = this_genre[1]
		this_genre2 = this_genre[2]
		filename.write("{this_title:5s}, {this_mpaa:5s}, {this_runtime:5d}, {this_crating:5d}, {this_genre1:5s}, {this_genre2:5s}\n".format(this_title=this_title, this_mpaa=this_mpaa, this_runtime=this_runtime, this_crating=this_crating, this_genre1=this_genre1, this_genre2=this_genre2))

filename.close()	 	



