import fresh_tomatoes
import media

# Creating 3 objects of Movie in the module "media"

ddlj = media.Movie("Dilwale Dulhania Le Jayenge",
				   "Raj and Simran meet on Eurail and unknowingly fall for each other. Raj is shattered to learn that she is already engaged. He follows Simran to India in order to win her and her strict father's heart.",
				   "https://www.youtube.com/watch?v=c25GKl5VNeY&vl=en",
				   "https://upload.wikimedia.org/wikipedia/en/8/80/Dilwale_Dulhania_Le_Jayenge_poster.jpg")

swades = media.Movie("Swades",
				   "Mohan, a project manager who is employed with NASA, travels to India to take his nanny along with him. Little does he know that this journey will change his life forever.",
				   "https://www.youtube.com/watch?v=qjc4a2Sg-B4",
				   "https://upload.wikimedia.org/wikipedia/en/8/85/Swades_poster.jpg")

cdi = media.Movie("Chak De! India",
				   "Kabir Khan, a former hockey star, tainted as someone who betrayed his country, begins coaching the Indian women's national hockey team to prove his loyalty to the nation.",
				   "https://www.youtube.com/watch?v=6a0-dSMWm5g",
				   "http://www.gstatic.com/tv/thumb/movieposters/168383/p168383_p_v8_ae.jpg")

# Creating a list of 3 movie objects

allMovies = [ddlj, swades, cdi]

# Sending the movie list as input to the fresh tomatoe module's function called open_movies_page

fresh_tomatoes.open_movies_page(allMovies)