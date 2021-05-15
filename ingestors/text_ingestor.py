from ingestors.ingestor_interface import IngestorInterface
from models import QuoteModel
from abc import abstractmethod


class TextIngestor(IngestorInterface):
    """
    A class that represents a Text ingestor.

    ...

    Methods
    -------
    parse
    """

    @classmethod
    def parse(cls, path):
        """
        Parameters
        ----------
        cls: self
        path: str

        Returns
        ------
        Parse from the text file.
        """
        file = open(path, 'r', encoding='utf-8-sig')
        lines = file.readlines()
        file.close()

        return [QuoteModel(*quote.rstrip('\n').split(' - '))
                for quote in lines]
