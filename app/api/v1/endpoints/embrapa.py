from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import JSONResponse, PlainTextResponse
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.embrapa import get_description
from app.utils.embrapa_utils import get_embrapa_data
from app.utils.embrapa_validation import ValidationError, valida_entrada
from app.core.security import require_jwt

router = APIRouter(
    prefix="/embrapa",
    tags=["Dados Vitivinicultura"],
    responses={404: {"description": "Não encontrado"}}
)

@router.get(
    "/query",
    response_class=JSONResponse,
    dependencies=[require_jwt],
    summary="Consultar dados da vitivinicultura",
    description="Endpoint para consultar dados da vitivinicultura por grupo, subgrupo e ano",
    responses={
        200: {
            "description": "Dados encontrados com sucesso",
            "content": {
                "application/json": {
                    "example": {
                        "dados": [{
                            "grupo": 1,
                            "subgrupo": 1,
                            "medida": "Hectares",
                            "ano": 2020,
                            "texto_tipo_dado": "Produção",
                            "texto_tipo_item": "Área",
                            "texto_nome_item": "Uva",
                            "quantidade": 1000,
                            "valor": 50000,
                            "texto_moeda": "R$"
                        }]
                    }
                }
            }
        },
        400: {
            "description": "Parâmetros inválidos",
            "content": {
                "application/json": {
                    "example": {"detail": "Ano inválido"}
                }
            }
        },
        401: {
            "description": "Não autorizado",
            "content": {
                "application/json": {
                    "example": {"detail": "Token inválido ou expirado"}
                }
            }
        }
    }
)
async def getData(
    opt: int = Query(..., title="Grupo", description="Código do grupo de dados"),
    sub_opt: int = Query(..., title="Subgrupo", description="Código do subgrupo de dados"),
    year: int = Query(..., title="Ano", description="Ano de referência dos dados"),
    db: Session = Depends(get_db)
    ):
    """
    obs. Dados carregados em cache para evitar indisponibilidade, porém dados limitados a 2023
    Consulta dados da vitivinicultura com os seguintes parâmetros:
    
    - **opt**: Código do grupo (2-6)
    - **sub_opt**: Código do subgrupo (1-5 dependendo do grupo)
    - **year**: Ano de referência (1970-2023)
    """
    try:
        valida_entrada(opt,sub_opt,year)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))

    data = get_embrapa_data(db, opt, sub_opt, year)    
    return {"dados":
        [
            {
                "grupo": item.grupo,
                "subgrupo": item.subgrupo,
                "medida": item.medida,
                "ano": item.ano,
                "texto_tipo_dado": item.texto_tipo_dado,
                "texto_tipo_item": item.texto_tipo_item,
                "texto_nome_item": item.texto_nome_item,
                "quantidade": item.quantidade,
                "valor": item.valor,
                "texto_moeda": item.texto_moeda
            } for item in data
        ] if data else []
    }

@router.get(
    "/description", 
    response_class=PlainTextResponse,
    dependencies=[require_jwt],
    summary="Consultar descrição dos dados da vitivinicultura",
    description="Endpoint para consultar a descrição detalhada dos dados disponíveis na API da Embrapa",
    responses={
        200: {
            "description": "Descrição encontrada com sucesso",
            "content": {
                "text/plain": {
                    "example": "Produção de vinhos, sucos e derivados  [2020]"
                }
            }
        },
        400: {
            "description": "Parâmetros inválidos",
            "content": {
                "application/json": {
                    "example": {"detail": "Grupo, subgrupo ou ano inválidos"}
                }
            }
        },
        401: {
            "description": "Não autorizado",
            "content": {
                "application/json": {
                    "example": {"detail": "Token inválido ou expirado"}
                }
            }
        },
        503: {
            "description": "Serviço indisponível",
            "content": {
                "application/json": {
                    "example": {"detail": "Serviço da Embrapa temporariamente indisponível"}
                }
            }
        }
    }
)
async def getDescription(
    opt: int = Query(..., title="Grupo", description="Código do grupo de dados"),
    sub_opt: int = Query(..., title="Subgrupo", description="Código do subgrupo de dados"),
    year: int = Query(..., title="Ano", description="Ano de referência dos dados")
    ):
    """
    obs. Consulta o site da embrapa diretamente, pode haver indisponibilidade
    Consulta a descrição do que cada combinação de parâmetros é com os seguintes parâmetros:
    
    - **opt**: Código do grupo (2-6)
    - **sub_opt**: Código do subgrupo (1-5 dependendo do grupo)
    - **year**: Ano de referência (1970-2023)
    """

    try:
        valida_entrada(opt,sub_opt,year)
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    
    return get_description(opt, sub_opt, year)

