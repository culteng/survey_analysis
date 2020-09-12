# generate pdf report from analysis outputs

# python imports
import sys
from fpdf import FPDF 


class PDF(FPDF):
    def header(self):
        # Logo
        self.image('./imgs/logo_strickland.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Name of School Diversity Survey Results', 0, 0, 'C')
        # Line break
        self.ln(20)
    
    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', 'I', 8)
        # Page number
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


def main(args):
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    # insert lines of text
    pdf.cell(0, 5, 'The ethnicity demographics show a fairly even distribution of participants in the survey', 0, 1)
    
    # insert chart
    pdf.image('./imgs/foo.png', x=50, w=80)
    # insert lines of text
    pdf.cell(0, 10, 'Unfortunately, this distribution does not match the school\'s population', 0, 1)
    
    # insert chart
    pdf.image('./imgs/foo2.png', x=50, w=80)
        
    pdf.output('diversity_survey_results.pdf', 'F')


if __name__ == '__main__':
    main(sys.argv[1:])




