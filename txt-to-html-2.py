def text_to_html(input_text):
    sections = input_text.strip().split('\n\n')

    html_output = ''
    for section in sections:
        lines = section.strip().split('\n')
        if lines[0].strip() == "Dimensions :":
            html_output += '<ul>\n'
            for line in lines:
                if line.strip() == "Dimensions :":
                    html_output += '<li><strong>{}</strong><br />\n'.format(line.strip())
                else:
                    html_output += '<li>{}</li>\n'.format(line.strip())
            html_output += '</ul>\n'
        else:
            html_output += '<p><strong><u>{}</u></strong></p>\n'.format(lines[0].strip())
            html_output += '<ul>\n'
            for line in lines[1:]:
                html_output += '<li>{}</li>\n'.format(line.strip())
            html_output += '</ul>\n'

    return html_output

input_text = """
Details and Style
Cropped Body Length
Fitted Shape
Round Neckline
Straight Hem
Cotton Elastane Blended Rib Fabric For Stretch And Comfort
Contains Bci Cotton
Contains 20% Regenerated Cotton From Pre-Consumer Waste
Dimensions :
Size: Bust Circumference x Front length
2XS - 70.0 x 41.5 cm
XS - 75.0 x 42.5 cm
S - 80.0 x 43.5 cm
M - 85.0 x 44.5 cm
L - 91.0 x 45.5 cm
XL - 97.0 x 46.5 cm
2XL - 104.0 x 47.5 cm
3XL - 111.0 x 48.5 cm
4XL - 118.0 x 49.5 cm
5XL - 125.0 x 50.5 cm

Composition and Care Instruction
Composition Main: 95% Cotton, 5% Cotton.
Care:
Cold handwash inside out
Do not bleach or wring
Do not tumble dry
Warm iron inside out
Do not iron trim or print
Do not dry clean
"""
html_output = text_to_html(input_text)
print(html_output)
