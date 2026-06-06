from PIL import Image, ImageDraw
import random

# Configuration for a 2x2 tilemap texture
TILE_SIZE = 32
COLS = 2
ROWS = 2
IMG_WIDTH = TILE_SIZE * COLS
IMG_HEIGHT = TILE_SIZE * ROWS

def generate_tilesheet():
    # Create a new image with an alpha channel
    img = Image.new("RGBA", (IMG_WIDTH, IMG_HEIGHT), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # --- Tile 0: Grass (Top-Left) ---
    # This is the default tile (index 0) that bevy_ecs_tilemap will use
    draw.rectangle([0, 0, 31, 31], fill=(34, 139, 34, 255))
    # Add some simple grass blade details
    for _ in range(15):
        x = random.randint(2, 29)
        y = random.randint(2, 29)
        draw.line([x, y, x, y - 2], fill=(50, 205, 50, 255), width=1)

    # --- Tile 1: Dirt (Top-Right) ---
    draw.rectangle([32, 0, 63, 31], fill=(139, 69, 19, 255))
    # Add pebble details
    for _ in range(10):
        x = random.randint(34, 61)
        y = random.randint(2, 29)
        draw.point((x, y), fill=(160, 82, 45, 255))

    # --- Tile 2: Water (Bottom-Left) ---
    draw.rectangle([0, 32, 31, 63], fill=(30, 144, 255, 255))
    # Add small wave lines
    draw.line([5, 42, 12, 42], fill=(0, 191, 255, 255), width=1)
    draw.line([18, 52, 26, 52], fill=(0, 191, 255, 255), width=1)

    # --- Tile 3: Stone (Bottom-Right) ---
    draw.rectangle([32, 32, 63, 63], fill=(128, 128, 128, 255))
    # Draw a simple brick/block outline
    draw.rectangle([34, 34, 61, 61], fill=(105, 105, 105, 255), outline=(169, 169, 169, 255))

    # Save the output
    filename = "../assets/tiles.png"
    img.save(filename)
    print(f"Successfully generated 2x2 tilemap '{filename}'")

if __name__ == "__main__":
    generate_tilesheet()
