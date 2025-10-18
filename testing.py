from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

user_db = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 25},
    3: {"name": "Charlie", "age": 35}
}


class User(BaseModel):
    name: str
    age: int

# --- CORRECTION APPLIED HERE ---
@app.put("/user/{user_id}")
def user_update(user_id: int, user: User):
    if user_id in user_db:
        # Use user.model_dump() for Pydantic V2 or user.dict() for Pydantic V1
        user_db[user_id] = user.model_dump()
        return {"message": "User updated successfully", "user": user_db[user_id]}
    else:
        return {"message": "User not found"}