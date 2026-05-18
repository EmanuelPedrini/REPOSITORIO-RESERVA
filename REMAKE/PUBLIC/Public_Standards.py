import random, time, os, json, copy
from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional

Conversions = {
    "Resistance_Conversion": lambda x: x/(x + 100),
    "Attribute_Conversion": 0.75,
    "Action_Max_Time": 1,
    "Delta": 0.1
}

Mathematic_Conventions = {
    "_PI": 3.1415,
    "_AREA": lambda x: (x**2),
    "_CUBIC_AREA": lambda x: (x**3),
}

def Clamp(Value, Max_Value):
    return max(0, min(Value, Max_Value))