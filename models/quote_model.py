class QuoteModel():
    """
    A class that represents a Quote model.

    ...

    Attributes
    ----------
    Nothing

    Methods
    -------
    """

    def __init__(self, body='', author=''):
        """
        Constructs all the necessary attributes for the object.

        Parameters
        ----------
            body : str
                quote body
            author : str
                author's name
        """
        self.body = body
        self.author = author

    def __str__(self):
        """
        Returns the string version of the object.

        Parameters
        ----------
        Nothing
        """
        return f'{self.body} - {self.author}'

    def __repr__(self):
        """
        Returns a printable representation of the object.

        Parameters
        ----------
        Nothing
        """
        return f'{self.body} - {self.author}'
