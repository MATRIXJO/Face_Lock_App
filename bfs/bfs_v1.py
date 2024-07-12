from PIL import Image, ImageDraw
from queue import Queue
import time

def floodfill(img, x, y, new_color):
  w = img.width
  h = img.height
  old_color = img.getpixel((x, y))
  visited = set()
  queue = Queue()
  queue.put((x, y))
  while not queue.empty():
    x, y = queue.get()
    if (x, y) in visited or x < 0 or x >= w or y < 0 or y >= h or img.getpixel((x, y)) != old_color:
      continue
    visited.add((x, y))
    img.putpixel((x, y), new_color)
    queue.put((x + 1, y))
    queue.put((x - 1, y))
    queue.put((x, y + 1))
    queue.put((x, y - 1))

img=Image.open("/home/joel/Downloads/IV SEM/3. DAA/20M/prg/test1.png")
img=img.convert("RGB")
red=(0,0,255)

start_time=time.time()
floodfill(img,500,300,red)
end_time=time.time()

img.show()
print(f"Time taken: {end_time - start_time:.4f} seconds")
