
from PIL import Image, ImageSequence
from PIL import GifImagePlugin

 

imageObject = Image.open("./sample_animated.gif")
print(imageObject.is_animated)
print(imageObject.n_frames)



#for frame in range(0,imageObject.n_frames):
#    imageObject.seek(frame)
#    imageObject.show()


frames = []
for frame in ImageSequence.Iterator(imageObject):
  frames.append( frame.resize((100, 100) ) )

for frame in frames:
    frame.show()
