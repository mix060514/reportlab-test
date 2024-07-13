from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter 

def create_pdf():
    c = canvas.Canvas("output02-shape-and-image.pdf", pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(100, 750, "Welcome to ReportLab!")
    
    # Add a line
    c.line(100, 735, 500, 735)
    
    # Add a rectangle
    c.rect(100, 700, 400, 100, fill=0)
    
    # Add an image (make sure you have the image file)
    c.drawImage("ref/logo.png", 100, 600, width=100, height=100)
    
    c.save()

create_pdf()
