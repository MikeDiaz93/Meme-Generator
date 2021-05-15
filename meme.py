import os
import random
import sys

from meme import MemeEngine
from ingestors import Ingestor
from models import QuoteModel
from meme.meme_generator import generate_meme

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='create a meme')
    parser.add_argument('--path', type=str, default=None,
                        help='path to an image file')
    parser.add_argument('--body', type=str, default=None,
                        help='quote body to add to the image')
    parser.add_argument('--author', type=str, default=None,
                        help='quote author to add to the image')
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
