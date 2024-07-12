from PIL import Image
from collections import deque
import time

def floodfill(img, x, y, new_color):
    # Convert image to RGB mode if not already
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Dimensions of the image
    w, h = img.size
    
    # Get the old color of the starting pixel
    old_color = img.getpixel((x, y))
    
    # If old_color is already new_color, return early
    if old_color == new_color:
        return img
    
    # Deque for BFS and set for visited pixels
    queue = deque([(x, y)])
    visited = set([(x, y)])
    
    # Perform flood fill
    while queue:
        cx, cy = queue.popleft()
        
        # Update pixel color to new_color
        img.putpixel((cx, cy), new_color)
        
        # Check neighboring pixels
        for nx, ny in [(cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)]:
            # Check if neighboring pixel is within bounds and hasn't been visited
            if 0 <= nx < w and 0 <= ny < h and (nx, ny) not in visited:
                # Get the current pixel color
                current_color = img.getpixel((nx, ny))
                
                # Add neighboring pixel to the queue if its color matches old_color
                if current_color == old_color:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
    
    return img

try:
    # Load the image
    img = Image.open("/home/joel/Downloads/IV SEM/3. DAA/20M/prg/test1.png")
    
    # Record start time
    start_time = time.perf_counter()
    
    # Perform flood fill with red color at (300, 100)
    modified_img = floodfill(img, 215, 218, (255, 0, 255))
    
    # Record end time
    end_time = time.perf_counter()
    
    # Print execution time
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    
    # Show the modified image
    if modified_img:
        modified_img.show()
        
        # Optionally save the modified image
        # modified_img.save("output.png")
    
except FileNotFoundError:
    print("Image file not found.")
except Exception as e:
    print(f"An error occurred: {e}")

