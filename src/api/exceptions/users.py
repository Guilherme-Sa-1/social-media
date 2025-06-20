from pydantic import BaseModel
from fastapi import FastAPI, HTTPException


def login_wrong_exception():
    raise HTTPException(status_code=404, detail="E-mail/senha incorretos")

def email_already_registered_exception():
    raise HTTPException(status_code=409, detail="E-mail já está em uso")