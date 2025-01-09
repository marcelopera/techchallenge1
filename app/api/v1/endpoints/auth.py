from fastapi import APIRouter, HTTPException, Request, Depends
from fastapi import status
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.core.security import create_access_token, Token, require_jwt
from app.core.database import get_db
from app.utils.auth_utils import get_usuario_by_username, valida_senha, create_user_account

router = APIRouter(
    prefix="/auth",
    tags=["Autenticação"],
    responses={404: {"description": "Not found"}},
)

@router.post(
    "/login",
    response_model=Token,
    summary="Autenticar usuário",
    description="Endpoint para autenticar usuário e gerar token JWT",
    responses={
        200: {
            "description": "Login realizado com sucesso",
            "content": {
                "application/json": {
                    "example": {"access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...", "token_type": "bearer"}
                }
            }
        },
        401: {
            "description": "Credenciais inválidas",
            "content": {
                "application/json": {
                    "example": {"detail": "Credenciais incorretas"}
                }
            }
        }
    }
)
async def login(username: str, password: str, db: Session = Depends(get_db)):
    """
    Realiza autenticação do usuário:
    
    - **username**: Nome de usuário cadastrado
    - **password**: Senha do usuário
    """
    if valida_senha(db, username, password):
        access_token = create_access_token(data={"sub": username})
        return {"access_token": access_token, "token_type": "bearer"}
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Usuário ou senha incorretos",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
@router.post(
    "/sign-in",
    status_code=status.HTTP_201_CREATED,
    summary="Criar nova conta",
    description="Endpoint para criar uma nova conta de usuário",
    responses={
        201: {
            "description": "Conta criada com sucesso"
        },
        409: {
            "description": "Nome de usuário já existe",
            "content": {
                "application/json": {
                    "example": {"detail": "Username already exists"}
                }
            }
        },
        500: {
            "description": "Erro interno do servidor",
            "content": {
                "application/json": {
                    "example": {"detail": "Failed to create user account"}
                }
            }
        }
    }
)
async def create_account(username: str, password: str, db: Session = Depends(get_db)):
    """
    Cria uma nova conta de usuário:
    
    - **username**: Nome de usuário desejado (único)
    - **password**: Senha para a conta
    """
    existing_user = get_usuario_by_username(db, username)
    
    if existing_user is None:
        try:
            create_user_account(db, username, password)
        except:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Failed to create user account",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return status.HTTP_201_CREATED
    
    raise HTTPException(
        status_code=status.HTTP_409_CONFLICT,
        detail="Username already exists",
        headers={"WWW-Authenticate": "Bearer"},
    )