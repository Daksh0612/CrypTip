from fastapi import APIRouter, Depends
from ..database import SessionLocal
from .. import models
from ..utils import address_utils, auth as auth_utils
import random
from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/seed_demo")
def seed_demo(db: Session = SessionLocal()):
    # create demo admin user
    from ..database import engine
    models.Base.metadata.create_all(bind=engine)
    s = db
    # create admin if not exists
    admin = s.query(models.User).filter(models.User.email=="admin@cryptip.local").first()
    if not admin:
        admin = models.User(name="Admin", email="admin@cryptip.local", password_hash=auth_utils.get_password_hash("admin123"), role="admin")
        s.add(admin)
    # add sample addresses
    sample_addrs = [
        ("0x" + "a"*40, "ETH"),
        ("0x" + "b"*40, "ETH"),
        ("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "BTC"),
        ("3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy", "BTC"),
    ]
    for a, c in sample_addrs:
        if not s.query(models.Address).filter(models.Address.address==a).first():
            metadata, risk_score, category = address_utils.analyze_address(a,c)
            aobj = models.Address(address=a, chain=c, category=category, risk_score=risk_score, metadata=metadata)
            s.add(aobj)
    s.commit()
    return {"seeded": True}