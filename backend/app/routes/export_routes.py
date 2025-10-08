from fastapi import APIRouter, Depends, Response
from ..deps import get_db, get_current_user
from .. import models
from sqlalchemy.orm import Session
import csv, io, json

router = APIRouter()

@router.get("/csv")
def export_csv(db: Session = Depends(get_db), user=Depends(get_current_user)):
    addrs = db.query(models.Address).all()
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["id","address","chain","category","risk_score","tags","date_added"])
    for a in addrs:
        writer.writerow([a.id,a.address,a.chain,a.category,a.risk_score,a.tags,a.date_added])
    return Response(content=output.getvalue(), media_type="text/csv")