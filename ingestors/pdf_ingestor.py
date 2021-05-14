import os
import subprocess

from ingestors.ingestor_interface import IngestorInterface
from ingestors.text_ingestor import TextIngestor


class PdfIngestor(IngestorInterface):
    """
    A class that represents a Pdf ingestor.

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
        -------
        A quote  parsed from the pdf file.
        """
        text_file = 'pdf_to_text.txt'
        # if you're working with linux change ./pdftotext to pdftotext
        subprocess.call(['./pdftotext', '-layout', '-nopgbrk',
                         f'{path}', f'{text_file}'])
        quotes = TextIngestor.parse(text_file)
        os.remove(text_file)

        return quotes
