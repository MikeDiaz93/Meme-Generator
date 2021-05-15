from abc import ABC, abstractmethod

extensions = {
    "TEXT": ".txt",
    "CSV": ".csv",
    "PDF": ".pdf",
    "DOCX": ".docx"
}


class IngestorInterface(ABC):
    """
    A class that represents an Ingestor Interface.

    ...

    Methods
    -------
    verify
    parse
    """

    @classmethod
    def verify(cls, file_extension):
        """
        If the file extension is passed, then it is validated in
        the extensions values.

        Parameters
        ----------
        cls: self
        file_extension: str

        Returns
        -------
        boolean
        """
        return file_extension in extensions.values()

    @abstractmethod
    def parse(cls, path):
        """
        Let child classes do their own implementation.

        Parameters
        ----------
        cls: self
        path: str

        """
        pass
