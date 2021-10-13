from enum import Enum
from typing import Optional

from pyppeteer import browser

class ElementType(Enum):
    INPUT = 1
    CHECKBOX = 2
    BUTTON = 3

class ElementAction(Enum):
    CLICK = 1
    HOVER = 2

class Element:
    def __init__(self, element_id: str, element_type: ElementType, element_input: Optional[str], element_action: Optional[ElementAction]):
        id: str = element_id
        element_type: ElementType = element_type
        element_input: Optional[str] = element_input
        element_action: Optional[ElementAction] = element_action

    def execute(browser: browser.Browser):
        pass
