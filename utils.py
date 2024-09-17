from typing import TypeAlias


Shape: TypeAlias = int


def count_frets(shape: Shape) -> int:
    """Return the number of bits equal to 1"""
    return bin(shape).count('1')
