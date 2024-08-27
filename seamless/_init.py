import os

from .context import Context
from .core import JS
from .core import Component
from .internal.constants import DISABLE_GLOBAL_CONTEXT_ENV
from .html import *
from .rendering import render
from .version import version as __version__

if not os.getenv(DISABLE_GLOBAL_CONTEXT_ENV):
    from .context.context import set_global_context

    set_global_context(Context.standard())
    del set_global_context
    
del DISABLE_GLOBAL_CONTEXT_ENV

__all__ = [
    "Component",
    "A",
    "Abbr",
    "Address",
    "Area",
    "Article",
    "Aside",
    "B",
    "Base",
    "BlockQuote",
    "Body",
    "Br",
    "Button",
    "Canvas",
    "Cite",
    "Code",
    "Col",
    "Div",
    "Em",
    "Embed",
    "Footer",
    "Form",
    "Fragment",
    "H1",
    "H2",
    "H3",
    "H4",
    "H5",
    "H6",
    "Head",
    "Header",
    "Hr",
    "Html",
    "I",
    "Img",
    "Input",
    "Label",
    "Li",
    "Link",
    "Main",
    "Meta",
    "Nav",
    "Ol",
    "Option",
    "P",
    "Param",
    "Pre",
    "Script",
    "Section",
    "Select",
    "Small",
    "Source",
    "Span",
    "Strong",
    "Style",
    "Sub",
    "Sup",
    "Table",
    "TBody",
    "Td",
    "TextArea",
    "Th",
    "THead",
    "Time",
    "Title",
    "Tr",
    "Track",
    "U",
    "Ul",
    "Wbr",
    "Context",
    "JS",
    "render",
    "__version__",
]