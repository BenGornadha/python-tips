import dataclasses
from typing import Any


class Letter:
    next: Any


@dataclasses.dataclass(frozen=True)
class S(Letter):
    next: Any = None


@dataclasses.dataclass(frozen=True)
class A(Letter):
    next = S()


@dataclasses.dataclass(frozen=True)
class M(Letter):
    next = A()


@dataclasses.dataclass(frozen=True)
class X(Letter):
    next = M()


@dataclasses.dataclass(frozen=True)
class NoLetter(Letter):
    next: Any = None
