# PaperStorage\encode\export.py
# Plots and stores the data to a picture stored in outpath

from PIL import Image

class exporter(object):
    def __init__(self):
        # Boilerplate code i'm sure isn't important... super(exporter, self).__init__()
        self.outpath = None

    def _makeTable(self, binaryString, width=400, height=574):
        return exampleresult # DEBUG


        img = Image.new('RGB', (width, height), (0, 0, 255))

        table = [[[]]*height]
        print()
        counter = 0
        rowcounter = counter
        for bit in binaryString:
            counter += 1
            rowcounter += 1
            if rowcounter > width:
                height += 1
                rowcounter = 0
            table[height].append(bit)
        # TODO: Make this work
        print(table) # DEBUG
        return [table, width, height]



    def makeBinary(self, path):
        self.path = path
        # TODO: Turn into binary

    def makeImg(self, binaryString):
        self.binaryString = binaryString
        image = self._makeTable(binaryString)
        width = image[1]
        height = image[2]
        # TODO: Make this work
        for x in range(1, width-1):
            print(x)
            for y in range(1, height-1):
                img.putpixel((x, y), tuple(image[0][x][y]))
        img.show() # DEBUG
        # TODO: Save it

    def sendImg(path, email):
        pass
        # TODO: send image located at file path to email address... somehow.
