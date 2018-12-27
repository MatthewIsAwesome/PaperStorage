# PaperStorage\encode\export.py
# Plots and stores the data to a picture stored in outpath

from PIL import Image

class exporter(object):
    def __init__(self):
        self.outpath = None
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

    def _makeTable(self, binaryString, width=400, height=574):
        exampleresult = [[["101101111000"], ["101101111111"]], 12, 2]
        return exampleresult # DEBUG

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
        table = self._makeTable(binaryString)
        width = table[1]
        height = table[2]
        img = Image.new('RGB', (width, height), (0, 0, 255))
        print(width)
        print(height)
        for y in range(height):
            # print(x)
            for x in range(width):
                if table[0][y][x] == "1":
                    img.putpixel((x, y), black)
                elif table[0][y][x] == "0":
                    img.putpixel((x, y), white)
                else:
                    raise ValueError("Illegal value in binaryString: "+table[0][y][x])
                print(str(x)+", "+str(y)) # DEBUG
        img.show() # DEBUG
        # TODO: Save it

    def sendImg(path, email):
        pass
        # TODO: send image located at file path to email address... somehow.
