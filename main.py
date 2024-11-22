from sqlalchemy.ext.asyncio.session import async_sessionmaker
from starlette.responses import JSONResponse
import uvicorn
from fastapi import FastAPI, Request, Depends
from sqlalchemy.ext.asyncio import AsyncSession
import models
from sqlalchemy import select, and_
import hashlib

app = FastAPI()
# bro did NOT cook anything

Session = async_sessionmaker(bind=models.engine)
session = Session()

@app.post("/login")
async def login(request: Request, db: AsyncSession = Depends(models.get_db)) -> JSONResponse:
    try:
        data = await request.json()
        print(data)
        async with db.begin():
            # print("1")
            query = await db.execute(select(models.User).
            where(
                and_(
                    models.User.email == data["email"],
                    models.User.password == await hash_password(data["password"])
                )
            )
            )
            print(query)

            user_data = query.scalar()
            user_id = user_data.user_id

        if user_data is None:
            return JSONResponse(content={"Error": "User not found"}, status_code=404)

        # user_id = user_data["user_id"]
        # print("\n\n\n\n\n", user_id)

        return JSONResponse(content={"Success": "User logged in successfully", "user_id": user_id}, status_code=200)

    except Exception as e:
        print(e)
        return JSONResponse(content={"Error": f"Unexpected Error {e}"}, status_code=500)


@app.get("/send_email")

async def hash_password(password):
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256(password_bytes)
    return hash_object.hexdigest()

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="127.0.0.1", port=8000)
