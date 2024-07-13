from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter 

def create_pdf():
    c = canvas.Canvas("output01-helloworld.pdf", pagesize=letter)
    c.drawString(100, 750, "Welcome to ReportLab!")
    c.save()

create_pdf()
