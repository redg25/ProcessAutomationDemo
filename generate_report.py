import time
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import utils


def generate_report(raw_image_report):
    """
    Generate a pdf report from the invoice recon image.
    :param raw_image_report: png of the invoice recon diagram
    :return: a pdf file of the formatted report
    """
    pdf_file = raw_image_report.replace('png','pdf')
    doc = SimpleDocTemplate(pdf_file, pagesize=letter,
                            rightMargin=72, leftMargin=72,
                            topMargin=72, bottomMargin=18)
    story=[]
    formatted_time = time.ctime()
    full_name = "Regis Corblin"
    address_parts = ["221B Baker Street", "London"]

    def get_image(path):
        """
        Resize an image to a 0.8 ratio
        :param path: path of the image to resize
        :return: A ReportLab image object
        """
        ratio = 0.8
        img = utils.ImageReader(path)
        iw, ih = img.getSize()
        width = iw * ratio
        aspect = ih / float(iw)
        return Image(path, width=width, height=(width * aspect))

    im = get_image(raw_image_report)
    #Set report style
    styles=getSampleStyleSheet()
    styles.add(ParagraphStyle(name='Justify', alignment=TA_JUSTIFY))
    #Create date time paragraphe
    ptext = formatted_time
    story.append(Paragraph(ptext, styles["Normal"]))
    story.append(Spacer(1, 12))
    # Create return address
    ptext = full_name
    story.append(Paragraph(ptext, styles["Normal"]))
    for part in address_parts:
        ptext = part.strip()
        story.append(Paragraph(ptext, styles["Normal"]))
    story.append(Spacer(1, 12))
    #Create report body text and image
    ptext = f'Dear {full_name.split()[0].strip()}:'
    story.append(Paragraph(ptext, styles["Normal"]))
    story.append(Spacer(1, 12))
    ptext = 'Please find the invoice reconciliation summary as of today'
    story.append(Paragraph(ptext, styles["Justify"]))
    story.append(Spacer(1, 12))
    story.append(im)
    story.append(Spacer(1, 12))
    ptext = 'Sincerely,'
    story.append(Paragraph(ptext, styles["Normal"]))
    story.append(Spacer(1, 48))
    doc.build(story)
    return pdf_file

