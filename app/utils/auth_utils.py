from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.models.api_models import DadosUsuarios

def get_usuarios_data(db: Session):
    return db.query(DadosUsuarios).all()

def get_usuario_by_username(db: Session, username: str):
    return db.query(DadosUsuarios).filter(
        DadosUsuarios.username == username
    ).first()

def valida_senha(db: Session, username: str, password: str):

    user = get_usuario_by_username(db, username)
    if user:
        credentials = db.query(DadosUsuarios).filter(
            DadosUsuarios.username == username
        ).first()

        if credentials.password == password:
            return True
    return False

def create_user_account(db: Session, username: str, password: str):
    try:
        novo_usuario = DadosUsuarios(
                username=username,
                password=password)
        db.add(novo_usuario)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        raise Exception(f"Error creating user: {str(e)}")
