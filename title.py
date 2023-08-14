class Title:
    '''
    A class for titles.
    '''
    def __init__(self, name, publisher, genre, quantity):
        '''
        :param name: names of the books
        :param publisher: publisher of the books
        :param genre: genre of the books
        :param quantity: number of the books
        '''
        self.name = name
        self.publisher = publisher
        self.genre = genre
        self.quantity = quantity

    @property
    def quantity(self):
        return self.quantity

    @quantity.setter
    def quantity(self, value):
        self.quantity = value

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        self.name = value

    @property
    def genre(self):
        return self.genre

    @genre.setter
    def genre(self, value):
        self.genre = value

    @property
    def publisher(self):
        return self.publisher

    @publisher.setter
    def publisher(self, value):
        self.publisher = value




