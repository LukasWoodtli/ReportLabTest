#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      LUW
#
# Created:     25.05.2012
# Copyright:   (c) LUW 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.units import cm
from reportlab.lib.pagesizes import A4

c = canvas.Canvas("hello.pdf", pagesize=A4)
width, height = A4

# move the origin up and to the left
c.translate(width/2, height/2)
# define a large font
c.setFont("Helvetica", 80)
# choose some colors
c.setStrokeColorRGB(0,0,0)
c.setFillColorRGB(0,0,0)

radius = 3
# draw a circle
c.circle(0,0,radius*cm, stroke=1)
c.circle(0,0,1, stroke=1)

# draw ticks
y1 = (radius-0.1)*cm
y2 = (radius+0.1)*cm
num_tics = 12
angle = 360 / num_tics
for i in range(num_tics):
    c.saveState()
    c.rotate(i * angle)
    c.line(0, y1,0,y2)
    c.restoreState()



c.showPage()
c.save()