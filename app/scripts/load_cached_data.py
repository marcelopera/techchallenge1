import json
from app.core.database import SessionLocal
from app.models.api_models import DadosEmbrapa

def load_cached_data():
    db = SessionLocal()
    try:
        # Clear existing data
        db.query(DadosEmbrapa).delete()
        
        # Read cached data
        with open("data/embrapa_cache.json", "r", encoding="utf-8") as f:
            cached_data = json.load(f)
        
        # Insert into database
        for item in cached_data:
            db_item = DadosEmbrapa(
                grupo=item.get("grupo"),
                subgrupo=item.get("subgrupo"),
                medida=item.get("medida"),
                ano=item.get("ano"),
                texto_tipo_dado=item.get("texto_tipo_dado"),
                texto_tipo_item=item.get("texto_tipo_item"),
                texto_nome_item=item.get("texto_nome_item"),
                quantidade=item.get("quantidade"),
                valor=item.get("valor"),
                texto_moeda=item.get("texto_moeda")
            )
            db.add(db_item)
                
        db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    load_cached_data()