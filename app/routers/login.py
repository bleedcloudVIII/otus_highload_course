from fastapi import APIRouter, Depends, HTTPException
from psycopg2.extensions import connection as PgConnection
from passlib.hash import bcrypt

from app.db import get_connection
from app.schemas.login import LoginRequest, LoginResponse
from app.auth import create_access_token

router = APIRouter(tags=["login"])


@router.post("/login", response_model=LoginResponse)
def login(data: LoginRequest, conn: PgConnection = Depends(get_connection)):
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id, password FROM users WHERE id = %s",
            (data.id,),
        )
        row = cur.fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    user_id, password = row

    if not bcrypt.verify(data.password, password):
        raise HTTPException(status_code=401, detail="Неправильные данные для логина")

    token = create_access_token(user_id)
    return LoginResponse(token=token)
