import barcode
from barcode import Code128
from barcode.writer import ImageWriter
from io import BytesIO

# Read the contents of the text file
text_file_path = '../extracted_text.txt'  # Adjust the path as needed
with open(text_file_path, 'r') as file:
    text_content = file.read().strip()

# Generate and save a Code 128 barcode image with the text content in PNG format
code128 = Code128(text_content, writer=ImageWriter())
png_filename = code128.save('images/barcode_with_text.png')
print(f"Saved PNG barcode image with text as: {png_filename}")

# Create a BytesIO buffer and write the barcode image to it
png_buffer = BytesIO()
code128.write(png_buffer)

# Generate a Code 128 barcode image with the text content in SVG format
svg_filename = barcode.generate('Code128', text_content, output='images/barcode_with_text_svg')
print(f"Generated SVG barcode image with text as: {svg_filename}")

# Create a BytesIO buffer for SVG output
svg_buffer = BytesIO()
barcode.generate('Code128', text_content, writer=ImageWriter(), output=svg_buffer)

"""
# Save the barcode images from BytesIO buffers to files
with open("images/png_file_with_text.png", "wb") as f_png:
    f_png.write(png_buffer.getvalue())

with open("images/svg_file_with_text.svg", "wb") as f_svg:
    f_svg.write(svg_buffer.getvalue())
"""

print("Saved PNG and SVG barcode images with text to files.")
