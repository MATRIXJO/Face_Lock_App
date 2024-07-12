from PIL import Image
from collections import deque
import time

def bfs(img, x, y, old_color, new_color):
    queue = deque([(x, y)])
    w, h = img.size
    
    while queue:
        cx, cy = queue.popleft()
        
        if cx < 0 or cx >= w or cy < 0 or cy >= h or img.getpixel((cx, cy)) != old_color:
            continue
        
        img.putpixel((cx, cy), new_color)
        
        queue.append((cx + 1, cy))
        queue.append((cx - 1, cy))
        queue.append((cx, cy + 1))
        queue.append((cx, cy - 1))

def floodfill(img, x, y, new_color):
    old_color = img.getpixel((x, y))
    
    if old_color == new_color:
        return
    
    bfs(img, x, y, old_color, new_color)

try:
    img = Image.open("/home/joel/Downloads/IV SEM/3. DAA/20M/prg/test1.png")
    img = img.convert("RGB")
    
    red = (255, 0, 255)
    start_time = time.time()
    
    floodfill(img, 500, 300, red)
    
    end_time = time.time()
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    
    img.show()
    # Optionally save the modified image
    # img.save("output.png")
    
except IOError:
    print("Unable to open image file")
