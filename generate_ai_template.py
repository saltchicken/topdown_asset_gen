from PIL import Image, ImageDraw, ImageFont

# Increased resolution for AI image generator legibility
FRAME_WIDTH = 256
FRAME_HEIGHT = 256
COLS = 4 
ROWS = 4
IMG_WIDTH = FRAME_WIDTH * COLS
IMG_HEIGHT = FRAME_HEIGHT * ROWS

def generate_ai_templates():
    actions = ["idle", "walk"]
    directions = ["down", "left", "up", "right"]

    # Try to load a larger default font (requires Pillow >= 10.0)
    # If using an older version, it will fallback to the tiny default font.
    try:
        font = ImageFont.load_default(size=32)
    except TypeError:
        font = ImageFont.load_default()

    for action in actions:
        # Solid white background is generally better for AI grid references
        img = Image.new("RGB", (IMG_WIDTH, IMG_HEIGHT), "white")
        draw = ImageDraw.Draw(img)

        for row, direction in enumerate(directions):
            for col in range(COLS):
                x0 = col * FRAME_WIDTH
                y0 = row * FRAME_HEIGHT
                x1 = x0 + FRAME_WIDTH
                y1 = y0 + FRAME_HEIGHT

                # Draw the bounding box for the frame
                draw.rectangle([x0, y0, x1, y1], outline="black", width=4)

                # Define the text for this specific frame
                text = f"{action.upper()}\n{direction.upper()}\nFrame {col}"

                # Calculate text size to center it in the box
                bbox = draw.multiline_textbbox((0, 0), text, font=font)
                text_w = bbox[2] - bbox[0]
                text_h = bbox[3] - bbox[1]

                text_x = x0 + (FRAME_WIDTH - text_w) / 2
                text_y = y0 + (FRAME_HEIGHT - text_h) / 2

                # Draw the centered text
                draw.multiline_text(
                    (text_x, text_y), 
                    text, 
                    fill="black", 
                    font=font, 
                    align="center"
                )

        filename = f"../assets/ai_template_{action}.png"
        img.save(filename)
        print(f"Successfully generated AI template '{filename}'")

if __name__ == "__main__":
    generate_ai_templates()
