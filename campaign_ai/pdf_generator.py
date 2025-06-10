from typing import List, Dict
from fpdf import FPDF


class CatalogPDF(FPDF):
    def header(self):
        if hasattr(self, 'title_text'):
            self.set_font('Helvetica', 'B', 16)
            self.cell(0, 10, self.title_text, ln=True, align='C')
            self.ln(5)


def generate_catalog(products: List[Dict], output_path: str, title: str) -> None:
    pdf = CatalogPDF()
    pdf.title_text = title
    pdf.add_page()
    pdf.set_font('Helvetica', '', 12)

    for product in products:
        pdf.multi_cell(0, 10, f"{product.get('title')} - {product.get('price')}\n{product.get('description','')}\n")
        pdf.ln(2)

    pdf.output(output_path)
