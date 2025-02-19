import os
from fastapi import FastAPI, HTTPException
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

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with Supabase!"}

# Example: Fetch Data from a Supabase Table
@app.get("/users")
async def get_users():
    try:
        response = supabase.table("user").select("*").execute()
        return response.data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Example: Insert Data into Supabase
@app.post("/users")
def create_user(name: str, email: str):
    response = supabase.table("user").insert({"name": name, "email": email}).execute()
    if response.data:
        return {"message": "User created", "data": response.data}
    raise HTTPException(status_code=400, detail="Error creating user")

