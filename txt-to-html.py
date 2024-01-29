import pandas as pd 

file_Description = 'Product_desc.xlsx'
sheet_name = 'Sheet1'
Column_nm = 'DESC'

class text_toHTML:
    def __init__(self, file_desc,Sheet_name, Column_name):
        self.file = file_desc
        self.dataframe = pd.read_excel(file_desc, sheet_name=Sheet_name)
        self.Column_name = Column_name
    
    def read_desc(self):
        list_desc = self.dataframe[f'{self.Column_name}'].tolist()
        return list_desc
    
    def to_html(self,input_text):
        # Split the input text into paragraphs
        paragraphs = input_text.strip().split('\n\n')
        
        # Convert paragraphs to HTML format
        html_output = ''
        for paragraph in paragraphs:
            html_output += '<p>{}</p>\n'.format(paragraph.strip().replace('\n', '<br/>'))
        return html_output
    
    def Create(self):
        list_html_result = []
        list_paragraps = text_html.read_desc()
        for par in list_paragraps:
            new_par = text_html.to_html(par)
            list_html_result.append(new_par)
        
        return text_html.result(list_html_result)
    
    def result(self, lst_result):
        df = pd.DataFrame({
            'DESC' : lst_result
        })
        with pd.ExcelWriter(self.file, engine='openpyxl', mode='a') as Writer:
            df.to_excel(Writer,sheet_name='Desc_HTML', index=False)

text_html = text_toHTML(file_Description,sheet_name,Column_nm)
text_html.Create()




'''SPU : MSS1895-T38

Made from super-soft cashmere like fabric, this jumper is designed to stay cosy and comfortable wash after wash. Cut in a regular fit with a ribbed trim along the body and cuffs. Designed in a simple, versatile style to be paired with almost any outfit.

Item details: Neck to hem length for a size 12:61cm

Fit and style: 
Regular fit ,
Crew neck , 
Ribbed trim , 
Stay Soft feature for longer-lasting softness

Care and composition: 
Composition: 100% acrylic 
Care instructions: Machine washable even at 30º
Tumble dry , Keep away from fire and flames
"""

# Convert text to HTML

'''

