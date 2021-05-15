import os
import random
import sys

from meme import MemeEngine
from ingestors import Ingestor
from models import QuoteModel
from meme.meme_generator import generate_meme


if __name__ == "__main__":
    args = sys.argv
    obj = {}
    for i in range(len(args)):
        try:
            if args[i] == '--body':
                obj['body'] = args[i+1]
            if args[i] == '--path':
                obj['path'] = args[i+1]
            if args[i] == '--author':
                obj['author'] = args[i+1]
        except:
            pass
    print(generate_meme(obj["path"], obj["body"], obj["author"]))
