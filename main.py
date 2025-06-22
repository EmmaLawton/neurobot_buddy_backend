from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import os
from dotenv import load_dotenv 

app = FastAPI(title="Neurobot Buddy API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def read_root():
    return {"message": "Welcome to the Neurobot Buddy APP API!"}    

@app.get("/health")
def health_check(): 
    return {"status": "healthy"}   

@app.get("/favicon.ico")
def favicon():
    return FileResponse("favicon.ico")

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="My Awesome App API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
#Get datbase URL from environment
database_url = os.environ.get("DATABASE_URL", "No database configured")


@app.get("/")
def read_root():
    return {
        "message": "Hello from FastAPI on Render!", 
        "status": "working",
        "service": "Render"
    }

@app.get("/health")
def health_check():
    return {
        "status": "healthy", 
        "service": "Render",
        "database": "connected" if database_url != "No database configured" else "not configured",
    }

@app.get("/database-info")
def database_info():
    return {
        "database_configured": database_url != "No database configured",
        "database_type": "PostgreSQL" if database_url != "No database configured" else "None"
    }

@app.get("/favicon.ico")
def favicon():
    return {"status": "no favicon"}

#@app.get("/test")
#def test_endpoint():
 #   return {
  #      "test": "API is working perfectly!", 
   #     "timestamp": "2025-06-22",
    #    "platform": "Back4App"
    #}