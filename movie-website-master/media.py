import webbrowser


class movie():
    """Class used for storing movie"""
    def __init__(self,mtitle,mstoryline,posterimg,trailery):
        """For storing data in objects creaated in entertainment_center.py
        (constructor method)"""
        self.title=mtitle
        """title of movie being stored in self.title for given object"""
        self.storyline=mstoryline
        """storyline of movie being stored in self.storyline for given object"""
        self.poster_image_url=posterimg
        """poster url of movie being stored in self.poster_image_url for given object"""
        self.trailer_youtube_url=trailery
        """trailer URL of movie being stored in self.youtube_url for given object"""
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
