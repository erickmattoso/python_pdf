# Python libraries
from fpdf import FPDF
from datetime import date

class PDF(FPDF):
  # def header(self):
  #     header_loc=static_img_loc+'header.png'
  #     self.image(header_loc, 0, 0, 300,10)
  #     self.ln(10)

  # Page footer
  def footer(self):
      # Position at 1.5 cm from bottom
      self.set_y(-17)
      self.set_font('Arial', 'B', 8)
      self.set_text_color(0,75,126)
      self.cell(0, 20, 'Página ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

def create_title(day, pdf):
  pdf.set_font('Arial', '', 24)  
  pdf.ln(60)
  pdf.write(5, f"Covidário Report")
  pdf.ln(10)
  pdf.set_font('Arial', '', 16)
  pdf.write(4, f'{day}')
  pdf.ln(5)

def create_analytics_report(day,filename="../report/Report.pdf"):
  pdf = PDF('P','mm',(WIDTH, HEIGHT))
  pdf.alias_nb_pages()

  ''' First Page '''
  pdf.add_page()
  pdf.image("../resources/letterhead_cropped.png", 0, 0, WIDTH)
  create_title(day, pdf)
  pdf.image("../resources/usa_cases.png", 5, 90, WIDTH-20)
  pdf.image("../resources/cases.png", 5, 200, WIDTH/2-10)
  pdf.image("../resources/deaths.png", WIDTH/2, 200, WIDTH/2-10)

  ''' Second Page '''
  pdf.add_page()
  pdf.image("../resources/cases_day.png", 5, 20, WIDTH/2-10)
  pdf.image("../resources/deaths_day.png", WIDTH/2, 20, WIDTH/2-10)
  pdf.image("../resources/cases2.png", 5, 110, WIDTH/2-10)
  pdf.image("../resources/deaths2.png", WIDTH/2, 110, WIDTH/2-10)
  pdf.image("../resources/cases3.png", 5, 200, WIDTH/2-10)
  pdf.image("../resources/deaths3.png", WIDTH/2, 200, WIDTH/2-10)

  ''' Third Page '''
  pdf.add_page()
  pdf.image("../resources/global_cases.png", 5, 20, WIDTH-20)
  pdf.image("../resources/cases4.png", 5, 130, WIDTH/2-10)
  pdf.image("../resources/deaths4.png", WIDTH/2, 130, WIDTH/2-10)

  ''' Fourt Page '''
  pdf.add_page()
  pdf.image("../resources/cases_day.png",        5, 20, WIDTH/2-10)
  pdf.image("../resources/deaths_day.png", WIDTH/2, 20, WIDTH/2-10)
  pdf.image("../resources/cases2.png",           5,110, WIDTH/2-10)
  pdf.image("../resources/deaths2.png",   WIDTH/2, 110, WIDTH/2-10)
  pdf.image("../resources/cases3.png",          5, 200, WIDTH/2-10)
  pdf.image("../resources/deaths3.png",   WIDTH/2, 200, WIDTH/2-10)

  ''' END '''
  pdf.output(filename, 'F')

if __name__ == '__main__':
  static_img_loc = "../resources/"
  WIDTH = 210 
  HEIGHT = 297
  day = (date.today())
  create_analytics_report(day)