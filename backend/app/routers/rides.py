from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import Ride
from app.schemas import RideCreate, RideOut

#### pendiente 