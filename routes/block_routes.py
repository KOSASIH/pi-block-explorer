from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from pydantic import BaseModel
from app.block import Block

router = APIRouter()

class BlockRequest(BaseModel):
    height: int

class BlockResponse(BaseModel):
    block: Block

@router.get("/blocks/{height}")
async def get_block(height: int):
    # Implement logic to fetch block from database or API
    block = Block(height=height, hash="0x123456", previous_hash="0x789012", timestamp=datetime.now(), transactions=[])
    return JSONResponse(content=BlockResponse(block=block).dict(), media_type="application/json")

@router.get("/blocks/latest")
async def get_latest_block():
    # Implement logic to fetch latest block from database or API
    block = Block(height=100, hash="0x123456", previous_hash="0x789012", timestamp=datetime.now(), transactions=[])
    return JSONResponse(content=BlockResponse(block=block).dict(), media_type="application/json")

@router.post("/blocks")
async def create_block(request: Request, block_request: BlockRequest):
    # Implement logic to create a new block
    block = Block(height=block_request.height, hash="0x123456", previous_hash="0x789012", timestamp=datetime.now(), transactions=[])
    return JSONResponse(content=BlockResponse(block=block).dict(), media_type="application/json", status_code=201)
