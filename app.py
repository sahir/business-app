from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from utility.database import get_db,Business
from utility.models import BusinessModel, BusinessCreateModel

app = FastAPI(title="SoftBank Business APIs",
              docs_url="/api/docs",
              debug=True)

@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})


# CRUD operations
@app.post("/business/", response_model=BusinessModel)
async def create_business(business_data: BusinessCreateModel, db: Session = Depends(get_db)):
    try:
        business = Business(**business_data.dict())
        db.add(business)
        db.commit()
        db.refresh(business)
        return business
    except Exception as ex:
        raise HTTPException(status_code=500, detail=str(ex))


@app.get("/business/{business_id}")
async def read_business(business_id: int, db: Session = Depends(get_db)):
    business = db.query(Business).filter(Business.id == business_id).first()
    if not business:
        raise HTTPException(status_code=404, detail="Business not found")
    return business


@app.put("/business/{business_id}", response_model=BusinessModel)
async def update_business(
    business_id: int, business_data: BusinessCreateModel, db: Session = Depends(get_db)
):
    try:
        business = db.query(Business).filter(Business.id == business_id).first()
        if not business:
            raise HTTPException(status_code=404, detail="Business not found")

        for key, value in business_data.dict().items():
            if value is not None:
                setattr(business, key, value)

        db.commit()
        db.refresh(business)
        return business
    except Exception as ex:
        raise HTTPException(status_code=404, detail=str(ex))

@app.delete("/business/{business_id}", response_model=BusinessModel)
async def delete_business(business_id: int, db: Session = Depends(get_db)):
    try:
        business = db.query(Business).filter(Business.id == business_id).first()
        if not business:
            raise HTTPException(status_code=404, detail="Business not found")

        db.delete(business)
        db.commit()
        db.refresh(business)
        return business
    except Exception as ex:
        raise HTTPException(status_code=404, detail=str(ex))

@app.get("/business/", response_model=list[BusinessModel])
async def search_business(query: str = None, db: Session = Depends(get_db)):
    if query:
        search_query = f"%{query}%"
        businesses = db.query(Business).filter(
            (Business.name.ilike(search_query))
            | (Business.address.ilike(search_query))
            | (Business.owner_info.ilike(search_query))
        ).all()
    else:
        businesses = db.query(Business).all()
    return businesses