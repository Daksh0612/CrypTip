from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from typing import List
from .. import schemas, database, models
from ..deps import get_db, get_current_user
from sqlalchemy.orm import Session
import csv, io, json
from ..utils import address_utils

router = APIRouter()

@router.post("/add", response_model=schemas.AddressOut)
def add_address(payload: schemas.AddressCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    # Validate format
    if not address_utils.validate_address(payload.address, payload.chain):
        raise HTTPException(status_code=400, detail="Invalid address format for chain")
    # analyze (demo)
    metadata, risk_score, category = address_utils.analyze_address(payload.address, payload.chain)
    addr = models.Address(address=payload.address, chain=payload.chain.upper(), category=payload.category or category, risk_score=risk_score, tags=payload.tags, metadata=metadata)
    db.add(addr)
    db.commit()
    db.refresh(addr)
    return addr

@router.get("/list", response_model=List[schemas.AddressOut])
def list_addresses(db: Session = Depends(get_db), user=Depends(get_current_user)):
    addrs = db.query(models.Address).order_by(models.Address.date_added.desc()).all()
    return addrs

@router.get("/{addr_id}", response_model=schemas.AddressOut)
def get_address(addr_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    addr = db.query(models.Address).filter(models.Address.id == addr_id).first()
    if not addr:
        raise HTTPException(status_code=404, detail="Not found")
    return addr

@router.delete("/{addr_id}")
def delete_address(addr_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):
    addr = db.query(models.Address).filter(models.Address.id == addr_id).first()
    if not addr:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(addr)
    db.commit()
    return {"message":"deleted"}

@router.post("/upload-csv")
def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db), user=Depends(get_current_user)):
    content = file.file.read().decode('utf-8')
    reader = csv.DictReader(io.StringIO(content))
    added = []
    for row in reader:
        addr = row.get("address") or row.get("wallet") or row.get("addr")
        chain = row.get("chain") or row.get("currency") or "ETH"
        if not addr: continue
        if not address_utils.validate_address(addr, chain): continue
        metadata, risk_score, category = address_utils.analyze_address(addr, chain)
        model = models.Address(address=addr, chain=chain.upper(), category=category, risk_score=risk_score, tags=row.get("tags",""), metadata=metadata)
        db.add(model)
        added.append(addr)
    db.commit()
    return {"added": added, "count": len(added)}