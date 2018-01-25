"""
Defining class Movie that creates instances of movie objects
"""


class Movie():

    """
....This Movie class creates instances of movies and their information
...."""

    def __init__(
        self,
        movieTitle,
        movieAbout,
        trailerYoutube,
        posterURL
    ):
        """
........Istance variables store info sent while creating objects
........"""

        self.title = movieTitle
        self.movieAbout = movieAbout
        self.trailer_youtube_url = trailerYoutube
        self.poster_image_url = posterURL
