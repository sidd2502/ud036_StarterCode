# Defining class Movie that creates instances of movie objects

class Movie ():
	"""This Movie class creates instances of movies and their information"""
	def __init__(self, title, movieAbout, trailer_youtube_url, poster_image_url):
		self.title = title
		self.movieAbout = movieAbout
		self.trailer_youtube_url = trailer_youtube_url
		self.poster_image_url = poster_image_url
