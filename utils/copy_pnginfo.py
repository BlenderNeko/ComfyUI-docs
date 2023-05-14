import sys
from PIL.PngImagePlugin import PngInfo
from PIL import Image
image = Image.open(sys.argv[1])
image1 = Image.open(sys.argv[2])

metadata = PngInfo()
for x in image1.info.keys():
  metadata.add_text(x, image1.info[x])
image.save(sys.argv[3], pnginfo=metadata)