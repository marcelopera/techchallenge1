from sqlalchemy.orm import Session
from app.models.api_models import DadosEmbrapa

def get_embrapa_data(db: Session, opt: int, sub_opt: int, year: int):
    return db.query(DadosEmbrapa).filter(
        DadosEmbrapa.grupo == str(opt),
        DadosEmbrapa.subgrupo == str(sub_opt),
        DadosEmbrapa.ano == year
    ).all()


def get_html(opt, sub_opt, year):
    
    import requests
    from bs4 import BeautifulSoup
    
    try:
        url = f"http://vitibrasil.cnpuv.embrapa.br/index.php?ano={year}&opcao=opt_0{opt}&subopcao=subopt_0{sub_opt}"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
    
        return soup
    
    except Exception as e:
        print(e)
        
def get_data_without_value(table,opt,sub_opt,year):
        
    json_data = {
        "metadados": {
            "grupo": "",
            "subgrupo": "",
            "ano": "",
            "tipo": "",
            "medida": ""          
        },
        "dados": []
    }

    if table:   
        thead = table.find('thead')
        if thead:
            headers = thead.find_all('th')
            if len(headers) >= 2:
                json_data["metadados"]["grupo"] = opt
                json_data["metadados"]["subgrupo"] = sub_opt
                json_data["metadados"]["ano"] = year
                json_data["metadados"]["tipo"] = headers[0].text.strip()
                json_data["metadados"]["medida"] = headers[1].text.strip()
        
        rows = table.find('tbody').find_all('tr')
        tipo_atual = ""
        valor_atual = 0
        tem_subitens = False
        
        for i, row in enumerate(rows):
            if row.find('td', class_='tb_item'):
                if tipo_atual and not tem_subitens:
                    item = {
                        "produto": "",
                        "tipo": tipo_atual,
                        "quantidade": valor_atual,
                    }
                    json_data["dados"].append(item)
                
                cells = row.find_all('td', class_='tb_item')
                tipo_atual = cells[0].text.strip()
                valor_atual = clean_number(cells[1].text)
                tem_subitens = False
                                
                if i == len(rows) - 1:
                    item = {
                        "produto": "",
                        "tipo": tipo_atual,
                        "quantidade": valor_atual,
                    }
                    json_data["dados"].append(item)
                
            elif row.find('td', class_='tb_subitem'):
                tem_subitens = True
                cells = row.find_all('td', class_='tb_subitem')
                if len(cells) >= 2:
                    item = {
                        "produto": cells[0].text.strip(),
                        "tipo": tipo_atual,
                        "quantidade": clean_number(cells[1].text),
                    }
                    json_data["dados"].append(item)
        return json_data

def get_data_with_value(table,opt,sub_opt,year):
    
    json_data = {
        "metadados": {
            "grupo": "",
            "subgrupo": "",
            "ano": "",
            "tipo": "",
            "medida": "",
            "valor": ""
        },
        "dados": []
    }

    if table:   
        thead = table.find('thead')
        if thead:
            headers = thead.find_all('th')
            json_data["metadados"]["grupo"] = opt
            json_data["metadados"]["subgrupo"] = sub_opt
            json_data["metadados"]["ano"] = year
            json_data["metadados"]["tipo"] = headers[0].text.strip()
            json_data["metadados"]["medida"] = headers[1].text.strip()
            json_data["metadados"]["valor"] = headers[2].text.strip()
        
        rows = table.find('tbody').find_all('tr')        
        tipo_atual = ""
        quantidade_atual = 0
        tem_subitens = False
        valor_atual = 0
        
        for i, row in enumerate(rows):
            if row.find('td'):
                if tipo_atual and not tem_subitens:
                    item = {
                        "produto": "",
                        "tipo": tipo_atual,
                        "quantidade": quantidade_atual,
                        "valor": valor_atual
                    }
                    json_data["dados"].append(item)
                
                cells = row.find_all('td')
                tipo_atual = cells[0].text.strip()
                quantidade_atual = clean_number(cells[1].text)
                valor_atual = clean_number(cells[2].text)
                tem_subitens = False
                
                if i == len(rows) - 1:
                    item = {
                        "produto": "",
                        "tipo": tipo_atual,
                        "quantidade": quantidade_atual,
                        "valor": valor_atual
                    }
                    json_data["dados"].append(item)

            
            elif row.find('td'):
                tem_subitens = True
                cells = row.find_all('td')
                item = {
                    "produto": cells[0].text.strip(),
                    "tipo": tipo_atual,
                    "quantidade": clean_number(cells[1].text),
                    "valor": clean_number(cells[2].text),
                }
                json_data["dados"].append(item)

        return json_data

def clean_number(text):
    try:
        return int(text.replace('.', '').strip())
    except:
        return None