from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse  

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
    return {"message": "Welcome to the Neurobot Buddy API!"}    

@app.get("/health")
def health_check(): 
    return {"status": "healthy"}   

@app.get("/favicon.ico")
def favicon():
    return FileResponse("favicon.ico")