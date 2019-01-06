import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread('..\\..\\samples\\test8by8.png')
img = img.tolist()
print(img)
plt.imshow(img)
plt.show()
for row in img:
    for pixel in row:
        blackvalues = 0
        for value in pixel:
            if value == 1:
                blackvalues += 1
