from ingestors.ingestor_interface import IngestorInterface
from models import QuoteModel


class TextIngestor(IngestorInterface):
    """
    A class that represents a Text ingestor.

    ...

    Attributes
    ----------
    IngestorInterface: str

    Methods
    -------
    parse
    """
    @classmethod
    def parse(cls, path):
        """
        Parameters
        ----------
        cls: str
        path: str

        Returns
        ------
        parse from the text file.
        """
        file = open(path, 'r', encoding='utf-8-sig')
        lines = file.readlines()
        file.close()

        return [QuoteModel(*quote.rstrip('\n').split(' - '))
                for quote in lines]
