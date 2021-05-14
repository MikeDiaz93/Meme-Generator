extensions = {
    "TEXT": ".txt",
    "CSV": ".csv",
    "PDF": ".pdf",
    "DOCX": ".docx"
}


class IngestorInterface():
    """
    A class that represents an Ingestor Interface.

    ...

    Attributes
    ----------
    Nothing

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
        cls: str
        file_extension: str

        Returns
        -------
        boolean
        """
        return file_extension in extensions.values()

    @classmethod
    def parse(cls, path):
        """
        Let child classes do their own implementation.

        Parameters
        ----------
        cls: str
        path: str

        """
        pass
