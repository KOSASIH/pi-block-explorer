from typing import List, Dict
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Block:
    height: int
    hash: str
    previous_hash: str
    timestamp: datetime
    transactions: List['Transaction']

    def to_dict(self) -> Dict:
        return {
            'height': self.height,
            'hash': self.hash,
            'previous_hash': self.previous_hash,
            'timestamp': self.timestamp.isoformat(),
            'transactions': [tx.to_dict() for tx in self.transactions]
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Block':
        return cls(
            height=data['height'],
            hash=data['hash'],
            previous_hash=data['previous_hash'],
            timestamp=datetime.fromisoformat(data['timestamp']),
            transactions=[Transaction.from_dict(tx) for tx in data['transactions']]
        )
