from docx import Document
from abc import abstractmethod

from ingestors.ingestor_interface import IngestorInterface
from models import QuoteModel


class DocxIngestor(IngestorInterface):
    """
    A class that represents a Docx ingestor.

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
        A quote parsed from the docx.
        """
        document = Document(path)
        quotes = []
        for paragraph in document.paragraphs:
            paragraph.text and quotes.append(
                QuoteModel(*paragraph.text.split(' - ')))

        return quotes
