from app.utils import embrapa_utils as eu
        
def get_value(opt, sub_opt, year):
    
    html = eu.get_html(opt, sub_opt, year)
    table = html.find('table', class_='tb_base tb_dados')
    
    if opt in [2,3,4]:
        return eu.get_data_without_value(table,opt,sub_opt,year)
    else: 
        return eu.get_data_with_value(table,opt,sub_opt,year)

def get_description(opt, sub_opt, year):
    
    html = eu.get_html(opt,sub_opt,year)
    
    p = html.find('p', class_="text_center")
    
    if p.contents[0] is None:
        return "No content"
    
    description = p.contents[0].strip()
    
    return description