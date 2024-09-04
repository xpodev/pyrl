from typing_extensions import Unpack
from pydom.element import Element

from ..types.html import HTMLIFrameElement
from ..types import ChildType


class IFrame(Element):
    def __init__(self, *children: ChildType, **kwargs: Unpack[HTMLIFrameElement]): ...
