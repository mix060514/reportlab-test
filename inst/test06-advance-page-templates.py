from reportlab.lib.pagesizes import letter
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, NextPageTemplate, PageBreak
from reportlab.lib.units import inch

doc = BaseDocTemplate("output06-advance-page-templates.pdf", pagesize=letter)

from reportlab.platypus import Frame, PageTemplate, FrameBreak

# Define frames for each template
frame1 = Frame(inch, 8*inch, 2*inch, 2*inch, id='normal', showBoundary=1)
frame2 = Frame(3*inch, 8*inch, 2*inch, 2*inch, id='normal', showBoundary=1)
frame3 = Frame(5*inch, 8*inch, 2*inch, 2*inch, id='normal', showBoundary=1)

frame4 = Frame(inch, 6*inch, 2*inch, 2*inch, id='normal', showBoundary=1)
frame5 = Frame(3*inch, 6*inch, 2*inch, 2*inch, id='normal', showBoundary=1)
frame6 = Frame(5*inch, 6*inch, 2*inch, 2*inch, id='normal', showBoundary=1)

frame7 = Frame(inch, 4*inch, 2*inch, 2*inch, id='normal', showBoundary=1)
frame8 = Frame(3*inch, 4*inch, 2*inch, 2*inch, id='normal', showBoundary=1)
frame9 = Frame(5*inch, 4*inch, 2*inch, 2*inch, id='normal', showBoundary=1)

frame10 = Frame(inch, 2*inch, 2*inch, 2*inch, id='normal', showBoundary=1)
frame11 = Frame(3*inch, 2*inch, 2*inch, 2*inch, id='normal', showBoundary=1)
frame12 = Frame(5*inch, 2*inch, 2*inch, 2*inch, id='normal', showBoundary=1)

# Create page templates using frames
first_template = PageTemplate(id="First", frames=[frame1, frame5, frame9, frame11])
second_template = PageTemplate(id="Second", frames=[frame5,frame2, frame6, frame4, frame8])
third_template = PageTemplate(id="Third", frames=[frame1, frame3, frame5, frame7, frame9])

doc.addPageTemplates([first_template, second_template, third_template])

from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()
normal_style = styles['Normal']

story = []

# First page content
story.append(Paragraph("flow01", normal_style))
story.append(FrameBreak())
story.append(Paragraph("flow02", normal_style))
story.append(FrameBreak())
story.append(Paragraph("flow03", normal_style))
story.append(FrameBreak())
story.append(Paragraph("flow04", normal_style))
story.append(NextPageTemplate("Second"))
story.append(PageBreak())

# Second page content
story.append(Paragraph("flow05", normal_style))
story.append(FrameBreak())
story.append(Paragraph("flow06", normal_style))
story.append(FrameBreak())
story.append(Paragraph("flow07", normal_style))
story.append(FrameBreak())
story.append(Paragraph("flow08", normal_style))
story.append(FrameBreak())
story.append(Paragraph("flow09", normal_style))
story.append(NextPageTemplate("Third"))
story.append(PageBreak())

# Third page content
story.append(Paragraph("flow10", normal_style))
story.append(FrameBreak())
story.append(Paragraph("flow11", normal_style))
story.append(FrameBreak())
story.append(Paragraph("flow12", styles['h1']))
story.append(FrameBreak())
story.append(Paragraph("flow13", normal_style))
story.append(FrameBreak())
story.append(Paragraph("flow14", normal_style))

doc.build(story)










