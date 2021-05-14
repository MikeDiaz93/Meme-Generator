import os
import random

from PIL import Image, ImageFont, ImageDraw


class MemeEngine():
    """
    A class that represents a Meme engine.

    ...

    Attributes
    ----------
    Nothing

    Methods
    -------
    make_meme
    """

    def __init__(self, output_dir):
        """
        Constructs all the necessary attributes for the object.

        Parameters
        ----------
        output_dir : str
            path dir
        """
        self.output_dir = output_dir
        self.count = 1

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

    def make_meme(self, img_path, text, author, width=500):
        """
        If the image path, text, author and specific width
        is passed then it creates the outfile wheres the
        meme path.

        Parameters
        ----------
        img_path : str
           image path
        text: str
            text
        author: str
            author name
        width: int
            width of 500

        Returns
        -------
        outfile : str
            path file
        """
        img = Image.open(img_path)
        outfile = os.path.join(self.output_dir, f'temp_{self.count}.jpg')
        self.count += 1

        real_width, real_height = img.size
        height = int(real_height * real_width / real_width)
        img.thumbnail((width, height))

        font1 = ImageFont.truetype('./_data/fonts/Roboto-Bold.ttf', 22)
        font2 = ImageFont.truetype('./_data/fonts/Roboto-Medium.ttf', 18)

        text_position = random.choice(range(30, height - 50))
        fill = (0, 0, 0)
        stroke_fill = (255, 255, 255)
        draw = ImageDraw.Draw(img)
        draw.text((30, text_position), text, fill, font1,
                  stroke_width=1, stroke_fill=stroke_fill)
        draw.text((40, text_position + 25),
                  f'- {author}', fill, font2, stroke_width=1,
                  stroke_fill=stroke_fill)

        img.save(outfile, 'JPEG')

        return outfile
