from PIL import Image, ImageDraw

# Configuration for a 4x4 grid (4 frames per animation, 4 directions)
FRAME_WIDTH = 32
FRAME_HEIGHT = 32
COLS = 4 
ROWS = 4
IMG_WIDTH = FRAME_WIDTH * COLS
IMG_HEIGHT = FRAME_HEIGHT * ROWS

COLORS = {
    "down": (220, 50, 50, 255),    # Red
    "left": (50, 50, 220, 255),    # Blue
    "up": (50, 220, 50, 255),      # Green
    "right": (220, 220, 50, 255),  # Yellow
}

def generate_spritesheet():
    # Define our separate sheets and their walk state
    actions = [
        ("idle", False),
        ("walk", True)
    ]
    
    directions = ["down", "left", "up", "right"]

    for action_name, is_walk in actions:
        img = Image.new("RGBA", (IMG_WIDTH, IMG_HEIGHT), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        for row, direction in enumerate(directions):
            color = COLORS[direction]

            for col in range(COLS):
                x = col * FRAME_WIDTH
                y = row * FRAME_HEIGHT
                anim_step = col # Cycle through 0, 1, 2, 3

                # Breathing animation logic
                breath_offset = 0
                if not is_walk:
                    if anim_step == 1: breath_offset = -1 # Expand
                    elif anim_step == 3: breath_offset = 1  # Contract
                
                # Walking animation logic
                walk_offset = 0
                if is_walk:
                    if anim_step == 1: walk_offset = -4
                    elif anim_step == 3: walk_offset = 4

                # Draw the body
                padding = 6 + breath_offset
                draw.ellipse(
                    [x + padding, y + padding, x + FRAME_WIDTH - padding, y + FRAME_HEIGHT - padding],
                    fill=color
                )

                # Draw the indicator
                indicator_color = (255, 255, 255, 255)
                if direction == "down":
                    draw.rectangle([x + 12, y + 18 + walk_offset, x + 20, y + 24 + walk_offset], fill=indicator_color)
                elif direction == "up":
                    draw.rectangle([x + 12, y + 8 + walk_offset, x + 20, y + 14 + walk_offset], fill=indicator_color)
                elif direction == "left":
                    draw.rectangle([x + 8 + walk_offset, y + 12, x + 14 + walk_offset, y + 20], fill=indicator_color)
                elif direction == "right":
                    draw.rectangle([x + 18 + walk_offset, y + 12, x + 24 + walk_offset, y + 20], fill=indicator_color)

        filename = f"player_{action_name}.png"
        img.save(filename)
        print(f"Successfully generated 4x4 '{filename}'")

if __name__ == "__main__":
    generate_spritesheet()
