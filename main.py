import os
from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI
app = FastAPI()

# Supabase Config
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Create Supabase Client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# Pydantic Model for User
class User(BaseModel):
    name: str
    email: str

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with Supabase!"}

# Create User
@app.post("/users")
def create_user(user: User):
    response = supabase.table("user").insert(user.dict()).execute()
    if response.data:
        return {"message": "User created", "data": response.data}
    raise HTTPException(status_code=400, detail="Error creating user")

# Read All Users
@app.get("/users")
async def get_users():
    try:
        response = supabase.table("user").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Read Single User by ID
@app.get("/users/{user_id}")
def get_user(user_id: int):
    response = supabase.table("user").select("*").eq("id", user_id).execute()
    if response.data:
        return response.data[0]
    raise HTTPException(status_code=404, detail="User not found")

# Update User by ID
@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    response = supabase.table("user").update(user.dict()).eq("id", user_id).execute()
    if response.data:
        return {"message": "User updated", "data": response.data}
    raise HTTPException(status_code=400, detail="Error updating user")

# Delete User by ID
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    response = supabase.table("user").delete().eq("id", user_id).execute()
    if response.data:
        return {"message": "User deleted"}
    raise HTTPException(status_code=400, detail="Error deleting user")
