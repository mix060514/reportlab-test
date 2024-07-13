from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

doc = BaseDocTemplate("output04-frame-and-page-template.pdf", pagesize=letter)

frame1 = Frame(doc.leftMargin, doc.bottomMargin, doc.width/2-6, doc.height, id='col1', showBoundary=1)
frame2 = Frame(doc.leftMargin+doc.width/2+6, doc.bottomMargin, doc.width/2-6, doc.height, id='col2', showBoundary=1)

page_template = PageTemplate(id='TwoCol', frames=[frame1, frame2])

doc.addPageTemplates([page_template])

styles = getSampleStyleSheet()
story = []
for i in range(200):
    story.append(Paragraph(f"This is paragraph {i}", styles['Normal']))

doc.build(story)
