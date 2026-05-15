from PUBLIC.Public_Enums import _DAMAGE_TYPE
from dataclasses import dataclass

@dataclass
class DAMAGE:
    Amount: int
    Type: _DAMAGE_TYPE
    Source: object

@dataclass
class REQUEST:
    pass
