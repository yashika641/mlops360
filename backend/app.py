# app.py

from fastapi import FastAPI
from routes import upload_route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="AutoMLOps Backend")

# CORS for Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production: use specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(upload_route.router)
