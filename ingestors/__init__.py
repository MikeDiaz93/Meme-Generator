import os

from ingestors.ingestor_interface import IngestorInterface, extensions
from ingestors.csv_ingestor import CsvIngestor
from ingestors.docx_ingestor import DocxIngestor
from ingestors.pdf_ingestor import PdfIngestor
from ingestors.text_ingestor import TextIngestor


class Ingestor(IngestorInterface):
    """
    A class that represents an Ingestor.

    ...

    Attributes
    ----------
    IngestorInterface : str

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
        A parsed text, docx, pdf or csv.   
        """
        file_name, file_extension = os.path.splitext(path)
        if not cls.verify(file_extension):
            raise ValueError('Unsupported file extension')
        if file_extension == extensions.get('TEXT'):
            return TextIngestor.parse(path)
        if file_extension == extensions.get('DOCX'):
            return DocxIngestor.parse(path)
        if file_extension == extensions.get('PDF'):
            return PdfIngestor.parse(path)
        if file_extension == extensions.get('CSV'):
            return CsvIngestor.parse(path)
