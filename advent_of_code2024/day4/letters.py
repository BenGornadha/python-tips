import dataclasses
from typing import Any


class Letter:
    next: Any

    def __bool__(self):
        return isinstance(self,X) or isinstance(self,M)  or isinstance(self,A)  or isinstance(self,S)


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

