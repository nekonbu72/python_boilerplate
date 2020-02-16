from typing import List


def add(i: int) -> int:
    return i + 1


def hello(name: str) -> str:
    return f"Hello, {name}!"


def even(li: List[int]) -> List[int]:
    return [i for i in li if i % 2 == 0]
