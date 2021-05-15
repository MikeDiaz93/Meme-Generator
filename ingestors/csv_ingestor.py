import pandas as pd
from abc import abstractmethod

from ingestors.ingestor_interface import IngestorInterface
from models import QuoteModel


class CsvIngestor(IngestorInterface):
    """
    A class that represents a Csv ingestor.

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
        -------
        A parse from the csv file.
        """
        csv = pd.read_csv(path)

        return [QuoteModel(**row) for index, row in csv.iterrows()]
