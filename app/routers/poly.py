from fastapi import APIRouter, HTTPException
from typing import List
import requests
import json

from app.utilities.schema_models import PolyAsset, PolyList

with open("config.json") as config_file:
    data = json.load(config_file)

router = APIRouter(
    prefix="/poly",
    tags=["Poly"]
    )

@router.get("/assets", response_model=PolyList)
async def get_poly_assets_list():
    r = requests.get(f'https://poly.googleapis.com/v1/assets?key={data["poly_api_key"]}')
    print(r.status_code)
    if (r.status_code == 200):
        return r.json()
    else:
        raise HTTPException(status_code=404, detail="Item not found")

@router.get("/assets/{asset}", response_model=PolyAsset)
async def get_poly_asset(asset : str):
    r = requests.get(f'https://poly.googleapis.com/v1/assets/{asset}?key={data["poly_api_key"]}')
    print(r.status_code)
    if (r.status_code == 200):
        return r.json()
    else:
        raise HTTPException(status_code=404, detail="Item not found")
