import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import utils


def generate_report(raw_image_report):
    pdf_file = raw_image_report.replace('png','pdf')
    doc = SimpleDocTemplate(pdf_file,pagesize=letter,
                            rightMargin=72,leftMargin=72,
                            topMargin=72,bottomMargin=18)
    Story=[]


    formatted_time = time.ctime()
    full_name = "Regis Corblin"
    address_parts = ["221B Baker Street", "London"]

    def get_image(path):
        ratio = 0.8
        img = utils.ImageReader(path)
        iw, ih = img.getSize()
        width = iw * ratio
        aspect = ih / float(iw)
        return Image(path, width=width, height=(width * aspect))

    im = get_image(raw_image_report)

    #im = Image(report, 2*inch, 2*inch)


    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    ptext = '%s' % formatted_time

    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    # Create return address
    ptext = '%s' % full_name
    Story.append(Paragraph(ptext, styles["Normal"]))
    for part in address_parts:
        ptext = '%s' % part.strip()
        Story.append(Paragraph(ptext, styles["Normal"]))

    Story.append(Spacer(1, 12))
    ptext = 'Dear %s:' % full_name.split()[0].strip()
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 12))

    ptext = 'Please find the invoice reconciliation summary as of today'
    Story.append(Paragraph(ptext, styles["Justify"]))
    Story.append(Spacer(1, 12))
    Story.append(im)

    Story.append(Spacer(1, 12))
    ptext = 'Sincerely,'
    Story.append(Paragraph(ptext, styles["Normal"]))
    Story.append(Spacer(1, 48))

    doc.build(Story)
    return pdf_file