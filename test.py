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
print weights