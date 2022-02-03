from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from schemas.item_resp import ItemsResp
from datasources.epic_free_game import get_epic_free_game
from utils import get_db

router = APIRouter(prefix="/api", tags=["epic"])


@router.get("/epic", response_model=ItemsResp)
async def epic_free_game(start: int = 0, db: Session = Depends(get_db)):
    if start != 0:
        return ItemsResp(status="fail", items=[])
    items = get_epic_free_game(db)
    return ItemsResp(status="success", items=items)
