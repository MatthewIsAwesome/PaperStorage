# PaperStorage\encode\export.py
# Plots and stores the data to a picture stored in outpath

from PIL import Image

class exporter(object):

    # VARIABLES
    outpath = None


    # METHODS
    def __init__(self, arg):
        super(exporter, self).__init__()
        self.arg = arg

    def _makeTable(binaryString, width=400, height=574):

        img = Image.new('RGB', (width, height), (0, 0, 255))

        table = [[[]]*10]
        print()
        counter = 0
        rowcounter = counter
        for bit in binaryString:
            counter += 1
            rowcounter += 1
            if rowcounter > width:
                height += 1
                rowcounter = 0

        # TODO: Make this work
        return



    def encode(path):
        pass
        # TODO: Turn into binary

    def makeImg(binaryString):
        image = super()._makeTable(binaryString)
        # TODO: Make this work
        for x in range(1, width-1):
            print(x)
            for y in range(1, height-1):
                img.putpixel((x, y), tuple(image[x][y]))
        img.show() # DEBUG
        # TODO: Save it

    def sendImg(path, email):
        pass
        # TODO: send image located at file path to email address... somehow.
