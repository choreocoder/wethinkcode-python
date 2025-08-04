import sys
import pyfiglet
import random

# Check the number of command-line arguments
if len(sys.argv) > 3:
    sys.exit("Too many arguments")
elif len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Arguments must be either 0 or 2")

# Get list of available fonts
available_fonts = pyfiglet.FigletFont.getFonts()

# Decide on the font
if len(sys.argv) == 3:
    if sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage. Use -f or --font")
    if sys.argv[2] not in available_fonts:
        sys.exit("Invalid font name")
    font = sys.argv[2]
else:
    font = random.choice(available_fonts)

# Prompt for text and render
text = input("Enter text: ")
figlet = pyfiglet.Figlet(font=font)
print(figlet.renderText(text))










