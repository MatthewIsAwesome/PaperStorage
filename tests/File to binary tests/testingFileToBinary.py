## READING

import base64

with open('exampleZip.zip','rb') as imageFile:
    str = base64.b64encode(imageFile.read())

imageBytes = base64.decodebytes(str)
imageBinary = "".join(["{:08b}".format(x) for x in imageBytes])

# DEBUG: print(imageBinary)

## WRITING

with open("duplicatedZip.zip", "wb") as f:
	f.write(imageBytes)
