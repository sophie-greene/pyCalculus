# google programming style guide
import webbrowser
class Movie():
    def __init__(self, title, story_line, poster_image, trailer_youtube):
        self.title=title
        self.story_line=story_line
        self.poster_image_url=poster_image
        self.trailer_youtube_url=trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
    
