"""
DDD - Value Object 예제
"""

from dataclasses import dataclass

@dataclass(frozen=True)  # 불변 객체
class Money:
    amount: int
    currency: str
