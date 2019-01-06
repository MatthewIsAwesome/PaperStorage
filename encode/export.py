# PaperStorage\encode\export.py
# Plots and stores the data to a picture stored in outpath

from PIL import Image
import base64

class exporter(object):
    def __init__(self, outpath):
        # GLOBALS
        self.imagedimensions = (400, 574)
        self.outOfData = False
        self.binaryStringCount = 0
        self.page = 0
        self.outpath = outpath
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

    def makeTable(self, binaryString, width=self.imagedimensions[0], height=self.imagedimensions[1]):
        self.binaryString = binaryString
        table = tuple()

        # DEBUG: print(table) # DEBUG
        # binaryStringCount = 0
        for y in range(height):
            row = tuple()
            for x in range(width):
                try:
                    # DEBUG: print(binaryString[binaryStringCount])
                    # DEBUG: print(row) # DEBUG
                    row += tuple(binaryString[self.binaryStringCount])
                except IndexError:
                    row += tuple("0")
                    self.outOfData = True
                finally:
                    self.binaryStringCount += 1
                    # DEBUG: print(row) # DEBUG
            # DEBUG: print(row) # DEBUG
            table += (row,) # DON'T REMOVE THESE BRACKETS and comma
            # DEBUG: print(table) # DEBUG
        # TODO: Make this work
        # DEBUG: print(table) # DEBUG
        return [table, width, height]



    def makeBinary(self, path):
        self.path = path
        # NOTE: I do not completely understnad this bit. Credit goes to https://stackoverflow.com/users/6380921/nouman-riaz-khan
        with open(path, 'rb') as imageFile:
            str = base64.b64encode(imageFile.read())

        imageBytes = base64.decodebytes(str)
        imageBinary = "".join(["{:08b}".format(x) for x in imageBytes])

        return imageBinary

    def makeImg(self, binaryString):
        self.binaryString = binaryString
        table = self.makeTable(binaryString) # DEBUG in place thus TODO: Change the values to the correct paper size
        width = table[1]
        height = table[2]
        img = Image.new('RGB', (width, height), (0, 0, 255))
        # DEBUG: print("width: "+str(width)) # DEBUG
        # DEBUG: print("height: "+str(height)) # DEBUG
        for y in range(height):
            for x in range(width):
                # DEBUG: print(str(y)+", "+str(x)) # DEBUG
                if table[0][y][x] == "1":
                    img.putpixel((x, y), self.black)
                elif table[0][y][x] == "0":
                    img.putpixel((x, y), self.white)
                else:
                    # DEBUG: print(table[0][y][x])
                    # DEBUG: print(table[0])
                    raise ValueError("Illegal value in binaryString: "+table[0][y][x])
                # print(str(x)+", "+str(y)) # DEBUG
        # img.show() # DEBUG
        img.save(self.outpath+"out_"+str(self.page)+".png")
        self.page += 1

    def sendImg(path, email):
        pass
        # TODO: send image located at file path to email address... somehow.
