import os
import json
import asyncio
from app.core.embrapa import get_value, get_description
from app.core.database import SessionLocal
from app.models.api_models import DadosEmbrapa

async def cache_embrapa_data():
    # Years range to fetch
    years = range(1970, 2024)  # Adjust years as needed
    # Options and sub-options available
    options = range(2, 7)  # 1 to 4
    sub_options = range(1, 6)  # 1 to 3
    
    cached_data = []
    
    for year in years:
        for opt in options:
            for sub_opt in sub_options:
                try:
                    data = get_value(opt, sub_opt, year)
                    description = get_description(opt, sub_opt, year)
                    if data and "dados" in data:
                        for item in data["dados"]:
                            cached_item = {
                                "grupo": data["metadados"]["grupo"],
                                "subgrupo": data["metadados"]["subgrupo"],
                                "ano": year,
                                "medida": data["metadados"]["medida"],
                                "texto_tipo_dado": data["metadados"]["tipo"],
                                "texto_tipo_item": item["tipo"],
                                "texto_nome_item": item["produto"],
                                "quantidade": item["quantidade"],
                                "descricao": description
                            }
                            if "valor" in data["metadados"]:
                                cached_item["valor"] = item["valor"]
                                cached_item["texto_moeda"] = data["metadados"]["valor"]
                            cached_data.append(cached_item)
                    
                except Exception as e:
                    print(f"Error fetching data for year {year}, opt {opt}, sub_opt {sub_opt}: {e}")
    
    # Save to file
    if not os.path.exists("data"):
        os.mkdir("data")
    with open("data/embrapa_cache.json", "w", encoding="utf-8") as f:
        json.dump(cached_data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    asyncio.run(cache_embrapa_data())