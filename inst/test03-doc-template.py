from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter 

def create_pdf():
    doc = SimpleDocTemplate("output03-doc-template.pdf", pagesize=letter)
    styles = getSampleStyleSheet()
    
    story = []
    story.append(Paragraph("Welcome to ReportLab!", styles['Title']))
    story.append(Spacer(1, 12))
    story.append(Paragraph("This is a paragraph in the document.", styles['Normal']))
    
    doc.build(story)

create_pdf()
