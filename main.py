from reportlab.lib.units import cm, mm, inch
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from src.report import MyPrint
from io import BytesIO
import os
import numpy as np
from src.stylesheet import stylesheet as style

print("REPORT GENERATION")
wd = os.getcwd()
fileName = os.path.join(wd, 'report.pdf')
logo = os.path.join(wd, 'images/Exnaton_logo_block.jpg')
documentTitle = 'Monthly report'

buffer = BytesIO()

pdf = MyPrint(buffer, 'A4')

# pdf.setFont('Roboto', 36)
# pdf.drawInlineImage(logo, 400, 700, width=120, preserveAspectRatio=True)
data = (['Zeitraum', 'Lastspitze', 'Datum', 'Uhrzeit', 'Wochentag', 'Während\nBoilerzeiten?', 'Boiler-\nfreigabe'],
        ['04-2020', '3305.1', '01.04.20', '01:00:00', 'Mittwoch', 'Ja', '4200'])
pdf.add_figure('/Users/severin/Desktop/reportlab/images/Exnaton_logo_block.jpg', "")
pdf.add_table(data, colWidths=2.22*cm)
pdf.add_paragraph("Der typische Wochenverlauf", style=style['Heading3'])
pdf.add_figure('/Users/severin/Desktop/reportlab/images/Exnaton_logo_block.jpg', "")
pdf.add_paragraph("Beschreibung: Abgebildet ist der typische Wochenverlauf in 15-minütigen Messperioden.\
 Ein Tag umfasst 96 Perioden. Die Woche startet mit Montag. \
  In grün die tatsächlich gemessene Leistung des WEWs. \
   In türkis die Leistung des Kraftwerks Berschnerbach und in grau der errechnete Bruttoverbrauch von Walenstadt. \
    Die roten Flächen zeigen an, in welchen Zeiträumen Boiler geschaltet wurden. \
     Die rote Linie zeigt die maximale Boilerfreigabe in diesem Zeitraum an an. Die schwarze Linie enthält den bisherigen Powercap.",
      style=style['Normal'])
pdf.add_list("Ergebnis: Handlungsbedarf für den Monat April vorhanden",
["Zwei ungewöhnliche Tage (April 14, April 27), Messfehler?, Wintereinbruch?",
"Die Monatslastspitze wurde durch die Boiler verursacht; die nächtlichen Lastspitzen\
kommen nah an die morgendliche Lastspitze hin und sollten beobachtet werden",
"Bisheriges Powercap bei Boilern deutlich zu hoch"], style=style['NormalT'], bullet='-')
pdf.add_newpage()
pdf.add_paragraph("Detailanalayse auf Wochenbasis", style=style['Heading2'])
pdf.add_paragraph("Typischer Tagesverlauf nach Wochentag", style=style['Heading3'])
pdf.add_figure('/Users/severin/Desktop/reportlab/images/Exnaton_logo_block.jpg', "")
pdf.add_paragraph("Lastspitzen pro Woche", style=style['Heading3'])
data2 = (['Kalender-\nwoche', 'Lastspitze', 'Datum', 'Uhrzeit', 'Wochentag', 'Während\nBoilerzeiten?', 'Boiler-\nfreigabe'],
        ['14', '3305.1','01.04.20','01:00:00','Mittwoch','Ja', '4200'],
        ['15', '163.2', '06.04.20', '08:15:00', 'Montag', 'Nein','0'],
        ['16', '2822.7', '14.04.20', '10:15:00', 'Dienstag', 'Nein', '0'],
        ['17','2541.9', '26.04.20', '21:30:00', 'Sonntag', 'Ja', '3200'],
        ['18', '2532.3', '27.04.20', '07:00:00', 'Montag', 'Nein', '0'])
pdf.add_table(data2, colWidths=2.22*cm)
pdf.add_paragraph("Lastspitzen pro Woche", style=style['Heading3'])
data2 = (['Kalender-\nwoche', 'Lastspitze', 'Datum', 'Uhrzeit', 'Wochentag', 'Während\nBoilerzeiten?', 'Boiler-\nfreigabe'],
        ['14', '3305.1','01.04.20','01:00:00','Mittwoch','Ja', '4200'],
        ['15', '163.2', '06.04.20', '08:15:00', 'Montag', 'Nein','0'],
        ['16', '2822.7', '14.04.20', '10:15:00', 'Dienstag', 'Nein', '0'],
        ['17','2541.9', '26.04.20', '21:30:00', 'Sonntag', 'Ja', '3200'],
        ['18', '2532.3', '27.04.20', '07:00:00', 'Montag', 'Nein', '0'])
pdf.add_table(data2, colWidths=2.22*cm)
pdf.add_list("Ergebnisse:",
["Bei der Lastspitze von KW 17 haben wir keine Handlungsmöglichkeit.\
 Die Boiler waren warm, die Spitze wurde durch Konsumentenverhalten verursacht.",
"Nachmittags sehen wir klare Lastminima unabhängig vom Wochentag -> ein Teil der\
 Boiler sollte hier gestartet werden, sofern deren Last unter der morgendlichen\
 Lastspitze bleiben kann",
"Freigabe kann unabhängig vom Wochentag sein, da Unterschiede überschaubar"], style=style['NormalT'], bullet='-')

user = pdf.print_doc()
buffer.seek(0)

with open(fileName, 'wb') as f:
    f.write(buffer.read())
