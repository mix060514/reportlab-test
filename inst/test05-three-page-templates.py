from reportlab.lib.pagesizes import letter
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, NextPageTemplate, PageBreak
from reportlab.lib.units import inch

def create_page_template(id, content_draw_func):
    frame = Frame(inch, inch, 6*inch, 9*inch, id='normal')
    template = PageTemplate(id=id, frames=[frame], onPage=content_draw_func)
    return template

def first_page(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold', 16)
    canvas.drawCentredString(4*inch, 10*inch, "First Page Template")
    canvas.restoreState()

def second_page(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold', 77)
    canvas.drawCentredString(4*inch, 10*inch, "Second Page Template")
    canvas.restoreState()

def third_page(canvas, doc):
    canvas.saveState()
    canvas.setFont('Times-Bold', 6)
    canvas.drawCentredString(4*inch, 10*inch, "Third Page Template")
    canvas.restoreState()

doc = BaseDocTemplate("output05-three-page-templates.pdf", pagesize=letter)

first_template = create_page_template("First", first_page)
second_template = create_page_template("Second", second_page)
third_template = create_page_template("Third", third_page)

doc.addPageTemplates([first_template, second_template, third_template])

from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()
normal_style = styles['Normal']

story = []

# First page content
story.append(Paragraph("This is the first page content", normal_style))
story.append(NextPageTemplate("Second"))
story.append(PageBreak())

# Second page content
story.append(Paragraph("This is the second page content", normal_style))
story.append(NextPageTemplate("Third"))
story.append(PageBreak())

# Third page content
story.append(Paragraph("This is the third page content", normal_style))

doc.build(story)










