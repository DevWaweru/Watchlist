class Movie:
    '''
    Movie class to define movie objects
    '''
    def __init__(self,identity,title,overview,image,vote_average,vote_count):
        self.identity = identity
        self.title = title
        self.overview = overview
        self.image = 'https://image.tmdb.org/t/p/w500/'+image
        self.vote_average = vote_average
        self.vote_count = vote_count