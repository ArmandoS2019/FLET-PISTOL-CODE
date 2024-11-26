from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


class PdfReport:
    
    def __init__(self):
        pass
      
    def generate_pdf_report(self, pdf_path):
        # Document setup
        doc = SimpleDocTemplate(pdf_path, pagesize=letter)
        elements = []  # List to hold PDF elements
        styles = getSampleStyleSheet()

        # Title
        title = Paragraph('<font size=24 color="#27AE60"><b>Invoice</b></font>', styles['Title'])
        elements.append(title)

        # Invoice and date information
        elements.append(Spacer(1, 20))
        header_data = [
            ['WeasyPrint', '', 'Invoice number: <b>12345</b>'],
            ['26 rue Emile Decorps', '', 'Date: <b>March 31, 2018</b>'],
            ['69100 Villeurbanne', '', ''],
            ['France', '', 'Our awesome developers'],
            ['', '', 'From all around the world'],
            ['', '', 'Earth'],
        ]
        header_table = Table(header_data, colWidths=[200, 50, 250])
        header_table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'Helvetica'),
            ('FONT', (2, 0), (2, -1), 'Helvetica-Bold'),
            ('ALIGN', (2, 0), (2, -1), 'RIGHT'),
            ('LINEBELOW', (0, -1), (-1, -1), 0.25, colors.lightgrey),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ]))
        elements.append(header_table)

        # Add some spacing
        elements.append(Spacer(1, 20))

        # Table data
        data = [
            ['DESCRIPTION', 'PRICE', 'QUANTITY', 'SUBTOTAL'],
            ['Website design', '€34.20', '100', '€3,420.00'],
            ['Website development', '€45.50', '100', '€4,550.00'],
            ['Website integration', '€25.75', '100', '€2,575.00'],
            ['Website integration', '€25.75', '100', '€2,575.00'],
            ['Website integration', '€25.75', '100', '€2,575.00'],
            ['Website integration', '€25.75', '100', '€2,575.00'],
        ]

        # Create a table
        table = Table(data, colWidths=[250, 100, 100, 100])
        table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONT', (0, 1), (-1, -1), 'Helvetica'),
            ('ALIGN', (1, 1), (-1, -1), 'CENTER'),
            ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#F4F4F4")),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('TEXTCOLOR', (-1, 1), (-1, -1), colors.HexColor("#27AE60")),  # Green for subtotals
            ('LINEBELOW', (0, 0), (-1, 0), 1, colors.HexColor("#DADADA")),
            ('LINEBELOW', (0, 1), (-1, -1), 0.25, colors.lightgrey),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
        ]))
        elements.append(table)

        # Add a thank you note
        elements.append(Spacer(1, 30))
        thank_you = Paragraph('<font size=12 color="#27AE60"><b>♥ Thank you!</b></font>', styles['BodyText'])
        elements.append(thank_you)

        # Footer with contact information
        footer_data = [
            ['contact@weasyprint.org', '', 'weasyprint.org']
        ]
        footer_table = Table(footer_data, colWidths=[250, 50, 250])
        footer_table.setStyle(TableStyle([
            ('FONT', (0, 0), (-1, -1), 'Helvetica'),
            ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor("#95A5A6")),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ]))
        elements.append(footer_table)

        # Build the PDF
        doc.build(elements)
        print(f"PDF generated: {pdf_path}")