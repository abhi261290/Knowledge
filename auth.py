from fastapi import Header, HTTPException
from app.settings import settings

def verify_token(x_api_key: str = Header(...)):
    if x_api_key != settings.AUTH_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")
