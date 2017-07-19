import webbrowser


class Movie():
    """ This creates a Movie class to have information about each one  """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """This function opens the webbrowser and goes to the URL passed in"""
        webbrowser.open(self.trailer_youtube_url)
