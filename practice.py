import twitter
import os
from decouple import config

# Initialize client
api_client = twitter.Api(
	consumer_key=config('CONSUMER_KEY'),
	consumer_secret=config('CONSUMER_SECRET'),
	access_token_key=config('ACCESS_TOKEN_KEY'),
	access_token_secret=config('ACCESS_TOKEN_SECRET')
)



# Checking credentials out
# print(api_client.VerifyCredentials())

# posting a twit
# result = api_client.GetFollowers()
# first_ten = result[:10]

# print(result[0])
# for f in first_ten:
# 	print(f)

image_path = os.path.abspath('image2.jpg')

result = api_client.PostUpdate(
	"Stunning and brave",
	media=image_path
)

print(result)



"""
# Checking credentials out
api_client.VerifyCredentials()

# posting a twit
result =  api_client.GetFollowers()

for followers in result[:10]:
    print(followers)
"""
a ="""
 Un hombre va al médico. Le cuenta que está deprimido. Le dice que la vida le parece dura y cruel. Dice que se siente muy solo en este mundo lleno de amenazas donde lo que nos espera es vago e incierto. El doctor le responde '
El tratamiento es sencillo. El gran payaso Pagliacci se encuentra esta noche en la ciudad. Vaya a verlo. Eso lo animará'. El hombre se echa a llorar. Y dice 'Pero, doctor... yo soy Pagliacci'. Es un buen chiste. Todo el mundo se ríe, suena un redoble y cae el telón. 
"""


#result = api_client.PostUpdate("")
#image_path = os.path.abspath("image.jpg")
#result = api_client.PostUpdate("Yeah, I love rick and morty", media=image_path)
