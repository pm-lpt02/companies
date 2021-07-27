import csv
from fastapi import HTTPException, status
from models.companies import Company
from sqlalchemy.orm import Session
from datetime import datetime


# needs to created to both upload csv and pull ids from other apis

def dataImport(filePath: str, db: Session):

    with open(filePath, 'r') as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            try:
