from reportlab.pdfgen import canvas

print("REPORT GENERATION")

fileName ='/Users/lilianeableitner/Desktop/Exnaton-Code/reportlab/report.pdf'
logo = '/Users/lilianeableitner/Desktop/Exnaton-Code/reportlab/images/Exnaton_logo_block.jpg'
documentTitle= 'Monthly report'

#Helper function
def drawMyRuler(pdf):
    pdf.drawString(100, 810, 'x100')
    pdf.drawString(200, 810, 'x200')
    pdf.drawString(300, 810, 'x300')
    pdf.drawString(400, 810, 'x400')
    pdf.drawString(500, 810, 'x500')
    pdf.drawString(10, 100, 'y100')
    pdf.drawString(10, 200, 'y200')
    pdf.drawString(10, 300, 'y300')
    pdf.drawString(10, 400, 'y400')
    pdf.drawString(10, 500, 'y500')
    pdf.drawString(10, 600, 'y600')
    pdf.drawString(10, 700, 'y700')
    pdf.drawString(10, 800, 'y800')
  


pdf = canvas.Canvas(fileName)
pdf.setTitle(documentTitle)
drawMyRuler(pdf)



from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

pdfmetrics.registerFont(
    TTFont ('Roboto', '/Users/lilianeableitner/Desktop/Exnaton-Code/reportlab/font/Roboto-Thin.ttf')
)
pdf.setFont('Roboto', 36)
pdf.drawCentredString(300,770,documentTitle)
pdf.line(30, 710, 550, 710)

pdf.drawInlineImage(logo, 100, 400)

pdf.save()