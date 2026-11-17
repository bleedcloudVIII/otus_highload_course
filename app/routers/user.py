from fastapi import APIRouter, Depends, HTTPException
from psycopg2.extensions import connection as PgConnection
from passlib.hash import bcrypt

from app.db import get_connection
from app.schemas.user import UserRegister, UserOut

router = APIRouter(prefix="/user", tags=["user"])


@router.post("/register", response_model=dict)
def register_user(user: UserRegister, conn: PgConnection = Depends(get_connection)):
    password_hash = bcrypt.hash(user.password)

    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO users (first_name, second_name, birthdate, biography, city, password)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id
            """,
            (
                user.first_name,
                user.second_name,
                user.birthdate,
                user.biography,
                user.city,
                password_hash
            ),
        )
        new_id = cur.fetchone()[0]
        conn.commit()

    return {"user_id": new_id}


@router.get("/get/{user_id}", response_model=UserOut)
def get_user(user_id: int, conn: PgConnection = Depends(get_connection)):
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT id, first_name, second_name, birthdate, biography, city
            FROM users
            WHERE id = %s
            """,
            (user_id,),
        )
        row = cur.fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    return UserOut(
        id=row[0],
        first_name=row[1],
        second_name=row[2],
        birthdate=row[3],
        biography=row[4],
        city=row[5]
    )
