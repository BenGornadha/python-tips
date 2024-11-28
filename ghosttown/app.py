from fastapi import FastAPI, HTTPException, Path, Request, APIRouter
from pydantic import BaseModel
from typing import Dict
import openai

app = FastAPI()

ghost_town = APIRouter(prefix="")

ghost_town.include_router(update_batch_date_router)
