import webbrowser
class Book():
    """saves info about books"""
    #class variable
    VALID_RATINGS=[1,2,3,4,5]
    def __init__(self, title, description, author ,image_url):
        self.title=title
        self.description=description
        self.image_url=image_url
        self.author=author
    def show_timage(self):
        webbrowser.open(self.image_url)