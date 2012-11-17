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
from reportlab.lib.pagesizes import landscape

pagesz = landscape(A4)
c = canvas.Canvas("hello.pdf", pagesize=pagesz)
width, height = pagesz

# move the origin up and to the left
c.translate(width/2, height/2)
# define a large font
c.setFont("Helvetica", 80)
# choose some colors
c.setStrokeColorRGB(0,0,0)
c.setFillColorRGB(0,0,0)

radius = 4
# draw a circle
def draw_circle_with_center(canvas, radius):
  stroke_thickness = 0.07 # cm

  canvas.setFillColorRGB(0,0,0)
  canvas.circle(0,0,radius*cm, stroke=1, fill=1)

  canvas.setFillColorRGB(1,1,1)
  canvas.circle(0,0,(radius-stroke_thickness)*cm, stroke=1, fill=1)

  canvas.setFillColorRGB(0,0,0)
  canvas.circle(0,0,0.1*cm, stroke=1, fill=1)

  # draw ticks
  y1 = (radius-0.1-stroke_thickness)*cm
  y2 = (radius+0.1)*cm
  num_tics = 12
  angle = 360 / num_tics
  for i in range(num_tics):
      c.saveState()
      c.rotate(i * angle)
      c.line(0, y1, 0, y2)
      c.restoreState()

def draw_lines(x, y, no_lines, len, distance):
  for i in range(no_lines):
    c.line(x, y+i*distance, x+len, y+i*distance)


draw_circle_with_center(c, radius)

c.saveState()
c.translate(width/2, height/2)
draw_lines(-1*cm, -1*cm, 10, -10*cm, -0.7*cm)
c.restoreState()

c.saveState()
c.translate(width/2, -height/2)
draw_lines(-1*cm, 1*cm, 10, -10*cm, 0.7*cm)
c.restoreState()

c.saveState()
c.translate(-width/2, height/2)
draw_lines(1*cm, -1*cm, 10, 10*cm, -0.7*cm)
c.restoreState()

c.saveState()
c.translate(-width/2, -height/2)
draw_lines(1*cm, 1*cm, 10, 10*cm, 0.7*cm)
c.restoreState()


c.showPage()
c.save()
