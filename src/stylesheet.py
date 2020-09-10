from reportlab.lib.styles import StyleSheet1, ParagraphStyle, ListStyle
from reportlab.platypus.tables import TableStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT, TA_JUSTIFY
from reportlab.lib.units import mm, cm, inch
from reportlab.lib.colors import HexColor, black, blue, turquoise, red, green, white
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import os

wd = os.getcwd()
pdfmetrics.registerFont(
    TTFont('Roboto', os.path.join(wd, 'font/Roboto-Thin.ttf')))
pdfmetrics.registerFont(
    TTFont('RobotoM', os.path.join(wd, 'font/Roboto-Medium.ttf')))
pdfmetrics.registerFont(
    TTFont('RobotoB', os.path.join(wd, 'font/Roboto-Bold.ttf')))
pdfmetrics.registerFont(
    TTFont('RobotoI', os.path.join(wd, 'font/Roboto-ThinItalic.ttf')))
pdfmetrics.registerFont(
    TTFont('RobotoBI', os.path.join(wd, 'font/Roboto-BoldItalic.ttf')))
pdfmetrics.registerFont(
    TTFont('RobotoR', os.path.join(wd, 'font/Roboto-Regular.ttf')))
pdfmetrics.registerFont(
    TTFont('RobotoL', os.path.join(wd, 'font/Roboto-Light.ttf')))
pdfmetrics.registerFont(
    TTFont('RobotoSlabL', os.path.join(wd, 'font/RobotoSlab-Light.ttf')))
pdfmetrics.registerFont(
    TTFont('RobotoSlabT', os.path.join(wd, 'font/RobotoSlab-Thin.ttf')))



_baseFontName = 'Roboto'
_baseFontNameB = 'RobotoB'
_baseFontNameL = 'RobotoL'
_baseFontNameI = 'RobotoI'
_baseFontNameBI = 'RobotoBI',
_baseFontNameR = 'RobotoR'
_baseFontNameM = 'RobotoM'

exnaton = HexColor('#2bb3a0')

stylesheet = StyleSheet1()

stylesheet.add(ParagraphStyle(name='Normal',
                              alignment=TA_JUSTIFY,
                              fontName=_baseFontName,
                              fontSize=11,
                              leading=1.15*11,
                              spaceAfter=4)
               )
stylesheet.add(ParagraphStyle(name='NormalM',
                              alignment=TA_JUSTIFY,
                              fontName=_baseFontNameM,
                              fontSize=11,
                              leading=1.15*11,
                              spaceAfter=4)
               )
stylesheet.add(ParagraphStyle(name='NormalT',
                              alignment=TA_JUSTIFY,
                              fontName=_baseFontName,
                              fontSize=11,
                              leading=1.15*11,
                              spaceAfter=4)
               )
stylesheet.add(ParagraphStyle(name='BodyText',
                              parent=stylesheet['Normal'],
                              spaceBefore=6)
               )

stylesheet.add(ParagraphStyle(name='Italic',
                              parent=stylesheet['BodyText'],
                              fontName=_baseFontNameI)
               )

stylesheet.add(ParagraphStyle(name='Title1',
                              alignment=TA_CENTER,
                              fontName=_baseFontName,
                              fontSize=24,
                              leading=1.5*24,
                              spaceAfter=14*mm))

stylesheet.add(ParagraphStyle(name='Subtitle1',
                              alignment=TA_CENTER,
                              fontName=_baseFontName,
                              fontSize=18))

stylesheet.add(ParagraphStyle(name='Header1',
                              alignment=TA_LEFT,
                              fontName=_baseFontName,
                              fontSize=18,
                              leading=11*mm,
                              spaceAfter=11*mm))

stylesheet.add(ParagraphStyle(name='Index',
                              alignment=TA_LEFT,
                              fontName=_baseFontName,
                              fontSize=11,
                              leading=1.15*11))

stylesheet.add(ParagraphStyle(name='right',
                              parent=stylesheet['Normal'],
                              fontName='Roboto',
                              fontSize=12,
                              alignment=TA_RIGHT))

stylesheet.add(ParagraphStyle(name='Heading1',
                              parent=stylesheet['Normal'],
                              fontName=_baseFontNameL,
                              fontSize=20,
                              leading=1.15*20,
                              spaceAfter=20),
               alias='h1')

stylesheet.add(ParagraphStyle(name='Title',
                              parent=stylesheet['Normal'],
                              fontName=_baseFontNameB,
                              fontSize=18,
                              leading=22,
                              alignment=TA_CENTER,
                              spaceAfter=6),
               alias='title')

stylesheet.add(ParagraphStyle(name='Heading2',
                              parent=stylesheet['Normal'],
                              fontName=_baseFontNameL,
                              fontSize=16,
                              leading=1.15*16,
                              spaceBefore=20,
                              spaceAfter=12),
               alias='h2')

stylesheet.add(ParagraphStyle(name='Heading3',
                              parent=stylesheet['Normal'],
                              fontName=_baseFontNameL,
                              fontSize=14,
                              leading=1.15*14,
                              spaceBefore=24,
                              spaceAfter=10),
               alias='h3')

stylesheet.add(ParagraphStyle(name='Heading4',
                              parent=stylesheet['Normal'],
                              fontName=_baseFontNameBI,
                              fontSize=10,
                              leading=12,
                              spaceBefore=10,
                              spaceAfter=4),
               alias='h4')

stylesheet.add(ParagraphStyle(name='Heading5',
                              parent=stylesheet['Normal'],
                              fontName=_baseFontNameB,
                              fontSize=9,
                              leading=10.8,
                              spaceBefore=8,
                              spaceAfter=4),
               alias='h5')

stylesheet.add(ParagraphStyle(name='Heading6',
                              parent=stylesheet['Normal'],
                              fontName=_baseFontNameB,
                              fontSize=7,
                              leading=8.4,
                              spaceBefore=6,
                              spaceAfter=2),
               alias='h6')

stylesheet.add(ParagraphStyle(name='Bullet',
                              parent=stylesheet['Normal'],
                              firstLineIndent=0,
                              spaceBefore=3),
               alias='bu')

stylesheet.add(ParagraphStyle(name='Definition',
                              parent=stylesheet['Normal'],
                              firstLineIndent=0,
                              leftIndent=36,
                              bulletIndent=0,
                              spaceBefore=6,
                              bulletFontName=_baseFontNameBI),
               alias='df')

stylesheet.add(ParagraphStyle(name='Code',
                              parent=stylesheet['Normal'],
                              fontName='Courier',
                              fontSize=8,
                              leading=8.8,
                              firstLineIndent=0,
                              leftIndent=36,
                              hyphenationLang=''))

stylesheet.add(ListStyle(name='UnorderedList',
                         parent=None,
                         leftIndent=18,
                         rightIndent=0,
                         bulletAlign='left',
                         bulletType='1',
                         bulletColor=black,
                         bulletFontName='Helvetica',
                         bulletFontSize=12,
                         bulletOffsetY=0,
                         bulletDedent='auto',
                         bulletDir='ltr',
                         bulletFormat=None,
                         # start='circle square blackstar sparkle disc diamond'.split(),
                         start=None,
                         ),
               alias='ul')

stylesheet.add(ListStyle(name='OrderedList',
                         fontName='Roboto',
                         fontSize=11,
                         textColor=black,
                         parent=None,
                         leftIndent=18,
                         rightIndent=0,
                         bulletAlign='left',
                         bulletType='1',
                         bulletColor=black,
                         bulletFontName='Helvetica',
                         bulletFontSize=12,
                         bulletOffsetY=0,
                         bulletDedent='auto',
                         bulletDir='ltr',
                         bulletFormat=None,
                         # start='1 a A i I'.split(),
                         start=None,
                         ),
               alias='ol')


MyTable = TableStyle((
[
 ('FONT', (0,0), (-1,0), 'RobotoSlabL', 10, 6*mm),
 ('FONT', (0,1), (-1,-1), 'RobotoSlabT', 10, 6*mm),
 ('BACKGROUND', (0,0), (-1,0), exnaton),
 ('TEXTCOLOR', (0,0), (-1,0), white),
 ('TEXTCOLOR', (0,1), (-1,-1), black),
 ('LINEABOVE', (0,1), (-1,-1), 0.25, exnaton),
 # ('LINEBELOW', (0,-1), (-1,-1), 1, exnaton),
 ('GRID', (0,0), (-1,-1), 1, exnaton),
 ('ALIGN', (0,0), (-1,-1), 'CENTRE')]
))
