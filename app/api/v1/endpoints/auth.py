from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi import status
from app.core.security import create_access_token, Token

router = APIRouter()

@router.post("/login", response_model=Token)
async def login(username: str, password: str):
    if username == "admin" and password == "admin":
        access_token = create_access_token(
            data={"sub": username}
        )
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciais incorretas",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
@router.post("/sign-in", response_class=JSONResponse)
async def create_account(username: str, password: str):
    # TODO: criar lógica de cadastramento
    return None