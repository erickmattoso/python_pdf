from fpdf import FPDF
from datetime import date
import pandas as pd


class PDF(FPDF):
  def header(self):
    self.image(resources+'header.png', 0, 0, 300,10)
    self.ln(10)


  def footer(self):
    self.image(resources+'footer.PNG', 0,190,282,20.5)
    self.set_y(-7)
    self.set_font('Arial', '', 8)
    self.set_text_color(0,75,126)
    self.cell(0, 0, 'Página ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')


def create_analytics_report(day,filename="../report/PPT.pdf"):
  pdf = PDF('L','mm','A4')
  pdf.alias_nb_pages()


  ''' First Page '''
  pdf.add_page()
  # Imagens
  pdf.image(resources+'logo.PNG',w=300)
  pdf.image(resources+'divider_line.PNG',w=300)
  ## Título
  pdf.ln(h = 10)
  pdf.set_text_color(0,75,126)
  pdf.set_font('Arial', 'B', 30)
  pdf.cell(0,0,"Relatório Mensal", 0, 0, 'C')
  ## Sub-Título
  pdf.ln(h = 20)
  pdf.set_text_color(192,80,77)
  pdf.set_font('Arial', 'B', 16)
  pdf.cell(0,0,f'{month}',0,0,'C')


  ''' Second Page '''
  pdf.add_page()
  ## Título
  pdf.ln(60)
  pdf.set_font('Arial', 'B', 24)  
  pdf.write(5, f"Agradecimentos")
  ## Data
  pdf.ln(10)
  pdf.set_font('Arial', '', 16)
  pdf.write(4, f'{day}')


  ''' Third Page '''
  pdf.add_page()

  ## Block 0 - Header
  pdf.set_text_color(221,23,23)
  pdf.set_font('Arial', 'B', 30)
  pdf.cell(32.5, 10,'Título')
  pdf.set_font('Arial', '', 28)
  pdf.set_text_color(0,75,126)
  pdf.write(10, f"Sub-Título")
  pdf.ln(12)
  pdf.image(resources+'divider_line.PNG',w=300)

  ## Block 1 - title
  pdf.ln(h = 0)
  pdf.set_font('Arial', 'U', 15)
  pdf.cell(30,5,'Distribution:',align='C')
  ybefore = pdf.get_y()

  ## Block 1 - image
  pdf.ln(h = 5)
  pdf.image(resources+'age_Dist.png',w=pdf.w/2.5, h=pdf.h/2.5)

  ## Block 2 - title
  pdf.ln(h = 5)
  pdf.set_font('Arial', 'U', 15)
  pdf.cell(40,5,'Statistical Tests:',align='L')
  
  ## Block 2 - table
  pdf.ln(h = 10)
  values=pd.read_csv(resources+'pres_stats_tab.csv')
  pdf.set_font('Arial', 'B', 10)
  pdf.set_fill_color(0,75,126)
  pdf.set_text_color(255,255,255)
  
  cell_width=[65,25,25]
  pdf.cell(cell_width[0],5,'  ',1,0,align='L',fill=True)
  pdf.cell(cell_width[1],5,values.columns[1],1,0,align='L',fill=True)
  pdf.cell(cell_width[2],5,values.columns[2],1,0,align='L',fill=True)
  pdf.ln(h = 5)
  pdf.set_font('Arial', '', 10)
  pdf.set_text_color(0,0,0)
  pdf.cell(cell_width[0],5,values.loc[0,'Name'],1,0,align='L')
  pdf.cell(cell_width[1],5,str(round(values.loc[0,'Value'],3)) if(values.loc[0,'Value']!='') else values.loc[0,'Value'] ,1,0,align='L')
  pdf.cell(cell_width[2],5,str(round(values.loc[0,'p Value'],3)) if(values.loc[0,'p Value']!='') else values.loc[0,'p Value'] ,1,0,align='L')
  pdf.ln(h = 5)
  pdf.set_font('Arial', '', 10)
  pdf.set_text_color(0,0,0)
  pdf.cell(cell_width[0],5,values.loc[1,'Name'],1,0,align='L')
  pdf.cell(cell_width[1],5,str(round(values.loc[1,'Value'],3)) if(values.loc[1,'Value']!='') else values.loc[1,'Value'],1,0,align='L')
  pdf.cell(cell_width[2],5,str(round(values.loc[1,'p Value'],3)) if(values.loc[1,'p Value']!='') else values.loc[1,'p Value'],1,0,align='L')
  pdf.ln(h = 5)
  pdf.set_font('Arial', '', 10)
  pdf.set_text_color(0,0,0)
  pdf.cell(cell_width[0],5,values.loc[2,'Name'],1,0,align='L')
  pdf.cell(cell_width[1],5,str(round(values.loc[2,'Value'],3)) if(values.loc[2,'Value']!='') else values.loc[2,'Value'],1,0,align='L')
  pdf.cell(cell_width[2],5,str(round(values.loc[2,'p Value'],3)) if(values.loc[2,'p Value']!='') else values.loc[2,'p Value'],1,0,align='L')
  
  ## Block 3 - title
  effective_page_width = pdf.w - 2*pdf.l_margin
  posicao_titulo = effective_page_width/1.93 + pdf.r_margin # ((276.9975833333333/1.93)+ 10.001249999999999) == 153.5233139032815
  
  ## Block 3 - title
  pdf.ln(h = 0)
  pdf.set_xy(posicao_titulo, ybefore)
  pdf.set_text_color(0,75,126)
  pdf.set_font('Arial', 'U', 15)
  pdf.cell(30,5,'Segments with Distinctly Different Outcomes:',align='L')

  ## Block 3 - image
  pdf.ln(h = 5)
  pdf.image(resources+"age_IV_based_BP.png",x=150,y=50,w=pdf.w/2.5, h=pdf.h/2.5)

  # Block 4 - Title
  pdf.ln(h = 89)
  pdf.set_x(posicao_titulo)
  pdf.set_font('Arial', 'U', 15)
  pdf.cell(30,5,'Inference:',align='L')
 
  ## Block 4 - content
  txt_data = pd.read_csv(resources+'age_inference.txt', header=None,sep='\t')
  pdf.ln(h = 5)
  pdf.set_x(2.5 + posicao_titulo)
  pdf.set_text_color(0,0,0)
  pdf.set_font('Arial', '', 12)
  # # # # # pdf.cell(0,10,txt_data.loc[2,0],0,0,align='L')

  ''' END '''
  pdf.output(filename, 'F')


if __name__ == '__main__':
  resources = "../resources/"
  day = date.today()
  month = day.strftime('%m-%d-%Y')
  create_analytics_report(day)
  # WIDTH = 190.5
  # HEIGHT = 338.67