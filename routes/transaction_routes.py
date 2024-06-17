from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from pydantic import BaseModel
from app.transaction import Transaction

router = APIRouter()

class TransactionRequest(BaseModel):
    sender: str
    recipient: str
    amount: float

class TransactionResponse(BaseModel):
    transaction: Transaction

@router.get("/transactions/{id}")
async def get_transaction(id: str):
    # Implement logic to fetch transaction by ID
    transaction = Transaction(id=id, block_height=100, timestamp=datetime.now(), sender=" sender@example.com", recipient="recipient@example.com", amount=10.0)
    return JSONResponse(content=TransactionResponse(transaction=transaction).dict(), media_type="application/json")

@router.post("/transactions")
async def create_transaction(request: Request, transaction_request: TransactionRequest):
    # Implement logic to create a new transaction
    transaction = Transaction(id="tx123456", block_height=100, timestamp=datetime.now(), sender=transaction_request.sender, recipient=transaction_request.recipient, amount=transaction_request.amount)
    return JSONResponse(content=TransactionResponse(transaction=transaction).dict(), media_type="application/json", status_code=201)
