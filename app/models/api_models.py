from sqlalchemy import Column, Integer, String
from app.core.database import Base

class DadosEmbrapa(Base):
    __tablename__ = "dados_vitivinicultura"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    grupo = Column(Integer, index=True)
    subgrupo = Column(Integer, index=True)
    medida = Column(String)
    ano = Column(Integer)
    texto_tipo_dado = Column(String)
    texto_tipo_item = Column(String)
    texto_nome_item = Column(String)
    quantidade = Column(Integer)
    valor = Column(Integer)
    texto_moeda = Column(Integer)

class DadosUsuarios(Base):
    __tablename__ = "dados_usuarios"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, index=True)
    password = Column(String)
    