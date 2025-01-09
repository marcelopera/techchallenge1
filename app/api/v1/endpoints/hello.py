from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.api import deps
from app.schemas.token import Hello
from app.core.security import require_jwt

router = APIRouter()

@router.get("/", response_class=JSONResponse, dependencies=[require_jwt])
def say_hello(): 

    message = Hello(content="{\"data\":\"helloWorld\"}")
    
    return message.get_content()