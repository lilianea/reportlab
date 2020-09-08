from io import BytesIO
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Frame, PageTemplate, Spacer, PageBreak, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT, TA_LEFT
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm, cm

STYLES = getSampleStyleSheet()
STYLES.add(ParagraphStyle(name='Title1', alignment=TA_CENTER,
                          fontName='Roboto', fontSize=24, leading=11*mm, spaceAfter=14*mm))
STYLES.add(ParagraphStyle(name='Subtitle1', alignment=TA_CENTER,
                          fontName='Roboto', fontSize=18))
STYLES.add(ParagraphStyle(name='Header1', alignment=TA_LEFT,
                          fontName='Roboto', fontSize=18, leading=11*mm, spaceAfter=11*mm))
STYLES.add(ParagraphStyle(name='Index', alignment=TA_LEFT,
                          fontName='Roboto', fontSize=12))
STYLES.add(ParagraphStyle(name='right', parent=STYLES['Normal'], fontName='Roboto',
                          fontSize=12, alignment=TA_RIGHT))

# TODO: how to create own pagelayout


class MyDocTemplate(SimpleDocTemplate):
    def __init__(self, filename, **kw):
        self.allowSplitting = 0
        SimpleDocTemplate.__init__(self, filename, **kw)


class MyPrint:

    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize
        self.story = []

    @staticmethod
    def _title_page(canvas, doc):
        # Save the state of our canvas so we can draw on it
        canvas.saveState()
        styles = getSampleStyleSheet()

        # Header
        header = Image("/Users/severin/Desktop/reportlab/images/Exnaton_logo_block.png",
                       width=5*cm, height=0.7*cm)
        w, h = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.width + doc.rightMargin - w,
                      doc.pagesize[1] - 2*cm)
        # Release the canvas
        canvas.restoreState()

    @staticmethod
    def _other_pages(canvas, doc):
        # Save the state of our canvas so we can draw on it
        canvas.saveState()

        # Header
        header = Image("/Users/severin/Desktop/reportlab/images/Exnaton_logo_block.png",
                       width=5*cm, height=0.7*cm)
        w, h = header.wrap(doc.width, doc.topMargin)
        header.drawOn(canvas, doc.width + doc.rightMargin - w,
                      doc.pagesize[1] - 2*cm)
        # Footer
        footer = Paragraph(str(canvas._pageNumber), STYLES['right'])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, h + 40)
        # Release the canvas
        canvas.restoreState()

    # TODO: Title page with variables, maybe create function to create a title_page with logo
    # TODO: how to position the Title and Index so they always fit on the page?

    def print_doc(self):
        buffer = self.buffer
        doc = MyDocTemplate(buffer,
                            rightMargin=1.5*cm,
                            leftMargin=1.5*cm,
                            topMargin=3.5*cm,
                            bottomMargin=3.5*cm,
                            pagesize=self.pagesize)

        # Our container for 'Flowable' objects
        mainStory = []
        titlePage = []
        # A large collection of style sheets pre-made for us

        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        title = Paragraph("<div>Exemplarische<br/>Datenanalyse für WEW</div>",
                          style=STYLES["Title1"])
        subtitle = Paragraph("Lastschaltplan unter Einheitstarif ab 2021",
                             style=STYLES["Subtitle1"])
        titlePage.append(Spacer(width=self.pagesize[0], height=5*cm))
        titlePage.append(title)
        titlePage.append(subtitle)
        titlePage.append(Spacer(width=self.pagesize[0], height=11.9*cm))
        titlePage.append(Paragraph(
            "Version: 1.0<br/>Stand: 21.08.2020<br/>Ansprechpartner:Liliane Ableitner, Exnaton AG", style=STYLES['Index']))
        titlePage.append(PageBreak())
        titlePage.append(Paragraph("Analyse für April 2020",
                                   style=STYLES['Header1']))
        mainStory.extend(titlePage)
        mainStory.extend(self.story)

        doc.build(mainStory, onFirstPage=self._title_page,
                  onLaterPages=self._other_pages)
    # TODO: create template functions for adding flowables like tables, header, paragraphs and images into the document

    def add_table(self, data_x, data_y, **kwargs):

        self.story.append(Table((data_x, data_y), **kwargs))
