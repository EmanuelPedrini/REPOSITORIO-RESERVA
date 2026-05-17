from PUBLIC.Public_Standards import *
from PUBLIC.Public_Enums import _EQUIPMENT_SLOTS
@dataclass
class _ITEM:
    ID: str
    Name: str
    Slot: _EQUIPMENT_SLOTS
    Bonuses: list
    
    