from typing import Any

from fastapi import APIRouter, HTTPException, Query

from app.api.deps import CurrentUser, SessionDep
from utils.scrape_judicial_processes import scrape_judicial_processes

router = APIRouter()


@router.get("/{id}")
def read_document(
    session: SessionDep,
    current_user: CurrentUser,
    id: int,
    entity_type: str,
) -> Any:
    """
    Get item by ID_document.
    """
    id_document = id
    if not id_document:
        raise HTTPException(status_code=404, detail="Item not found")
    if not current_user.is_superuser:
        raise HTTPException(status_code=400, detail="Not enough permissions")
    try:
        return scrape_judicial_processes(id_document, entity_type)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
