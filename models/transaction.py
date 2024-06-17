from typing import List, Dict
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Transaction:
    id: str
    block_height: int
    timestamp: datetime
    sender: str
    recipient: str
    amount: float

    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'block_height': self.block_height,
            'timestamp': self.timestamp.isoformat(),
            'ender': self.sender,
            'ecipient': self.recipient,
            'amount': self.amount
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Transaction':
        return cls(
            id=data['id'],
            block_height=data['block_height'],
            timestamp=datetime.fromisoformat(data['timestamp']),
            sender=data['sender'],
            recipient=data['recipient'],
            amount=data['amount']
        )
