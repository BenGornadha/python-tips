from fastapi import FastAPI, HTTPException, Path, Request
from pydantic import BaseModel
from typing import Dict
import openai