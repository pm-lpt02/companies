from schemas import companiesSchema
from models.companies import Company
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from datetime import datetime


def get_all(db: Session):
    companies = db.query(Company).all()
    return companies


def create(request: companiesSchema.CompanyCreate, db: Session):
    new_company = Company(name=request.name, symbol_id=request.symbol_id)
    new_company.created_at = datetime.utcnow()
    db.add(new_company)
    db.commit()
    db.refresh(new_company)
    return new_company


def show(id: int, db: Session):
    company = db.query(Company).filter(Company.Id == id)
    if not company.first():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Company with id: {id} is not available"
        )
    return company


def update(id: int, request: companiesSchema.CompanyUpdate, db: Session):
    company = db.query(Company).filter(Company.Id == id).first()

    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Company with id: {id} not found"
        )

    company.updated_at = datetime.utcnow()
    company.update(request)
    db.commit()
    return company


def delete(id: int, db: Session):
    company = db.query(Company).filter(Company.Id == id)

    if not company:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Company with id: {id} not found"
        )

    company.delete(synchronize_session=False)
    db.commit()
    return 'done'



