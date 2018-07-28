#coding:utf-8
import reportlib

from reportlab.lib.styles import getSamleStyleSheet

from repoerlab.platypus import Paragraph,SimpleDocTemplate
from reportlab.lib import colors

Stype = getSampleStyleSheet()
bt = Stype['Normal']
bt.fontSize=14
bt.firstLineIndent = 32
bt.leading = 20

ct = Stype['Normal']
ct.fontSize = 12
ct.alignment = 1

ct.textColor = colors.red


t = Paragraph('hello',bt)
pdf = SimpleDocTemplate('ppff.pdf')
pdf.multiBuild([t])