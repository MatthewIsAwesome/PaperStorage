# PaperStorage\encode\export.py
# Plots and stores the data to a picture stored in outpath

from PIL import Image

class exporter(object):
    def __init__(self):
        self.outpath = None
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)

    def makeTable(self, binaryString, width=400, height=574):
        table = tuple()
        
        print(table) # DEBUG
        binaryStringCount = 0
        for y in range(height):
            for x in range(width):
                try:
                    print(binaryString[binaryStringCount])
                    table[y].append(binaryString[binaryStringCount])
                except IndexError:
                    table[y].append("0")
                finally:
                    binaryStringCount += 1
        # TODO: Make this work
        print(table) # DEBUG
        return [table, width, height]



    def makeBinary(self, path):
        self.path = path
        # TODO: Turn into binary

    def makeImg(self, binaryString):
        self.binaryString = binaryString
        table = self.makeTable(binaryString, 10, 10) # TODO: Change the values to the correct paper size
        width = table[1]
        height = table[2]
        img = Image.new('RGB', (width, height), (0, 0, 255))
        print("width: "+str(width)) # DEBUG
        print("height: "+str(height)) # DEBUG
        for y in range(height):
            for x in range(width):
                # DEBUG: print(str(y)+", "+str(x)) # DEBUG
                if table[0][y][x] == "1":
                    img.putpixel((x, y), self.black)
                elif table[0][y][x] == "0":
                    img.putpixel((x, y), self.white)
                else:
                    print(table[0][y][x])
                    print(table[0])
                    raise ValueError("Illegal value in binaryString: "+table[0][y][x])
                #print(str(x)+", "+str(y)) # DEBUG
        img.show() # DEBUG
        # TODO: Save it

    def sendImg(path, email):
        pass
        # TODO: send image located at file path to email address... somehow.
