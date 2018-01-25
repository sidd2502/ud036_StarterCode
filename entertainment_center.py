import fresh_tomatoes
import media

"""
Creating 3 objects of Movie in the module "media"
"""

ddlj = media.Movie(
	"Dilwale Dulhania Le Jayenge",
	"Raj and Simran meet on Eurail and fall for each other.",
	"https://www.youtube.com/watch?v=c25GKl5VNeY&vl=en",
	"https://upload.wikimedia.org/wikipedia/en/8/80/Dilwale_Dulhania_Le_Jayenge_poster.jpg"  # NOQA
	)

swades = media.Movie(
	"Swades",
	"Mohan, a project manager who is employed with NASA, travels to India.",
	"https://www.youtube.com/watch?v=qjc4a2Sg-B4",
	"https://upload.wikimedia.org/wikipedia/en/8/85/Swades_poster.jpg"
	)

cdi = media.Movie(
	"Chak De! India",
	"A former star, who is said to have betrayed country, begins coaching.",
	"https://www.youtube.com/watch?v=6a0-dSMWm5g",
	"http://www.gstatic.com/tv/thumb/movieposters/168383/p168383_p_v8_ae.jpg"
	)


"""
Creating a list of 3 movie objects
"""

allMovies = [ddlj, swades, cdi]

"""
Sending the movie list as input to fresh tomato
"""

fresh_tomatoes.open_movies_page(allMovies)