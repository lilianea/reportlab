from reportlab.pdfbase import pdfmetrics
from reportlab.lib.units import cm, mm, inch
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas
from src.report import MyPrint
from io import BytesIO
import os
import numpy as np

print("REPORT GENERATION")
wd = os.getcwd()
pdfmetrics.registerFont(
    TTFont('Roboto', os.path.join(wd, 'font/Roboto-Thin.ttf')))
fileName = os.path.join(wd, 'report.pdf')
logo = os.path.join(wd, 'images/Exnaton_logo_block.jpg')
documentTitle = 'Monthly report'

buffer = BytesIO()

pdf = MyPrint(buffer, 'A4')

# pdf.setFont('Roboto', 36)
# pdf.drawInlineImage(logo, 400, 700, width=120, preserveAspectRatio=True)
data_x = [x for x in range(10)]
data_y = ['data ' + str(y) for y in range(10)]
pdf.add_table(data_x, data_y)
user = pdf.print_doc()
buffer.seek(0)

with open(fileName, 'wb') as f:
    f.write(buffer.read())
