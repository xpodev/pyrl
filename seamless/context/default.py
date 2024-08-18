from typing import TYPE_CHECKING

from ..extra.components import init_components
from ..extra.events import init_events

from ..extra.transformers.class_transformer import class_transformer
from ..extra.transformers.dash_transformer import dash_transformer
from ..extra.transformers.js_transformer import init_transformer, js_transformer
from ..extra.transformers.html_events_transformer import html_events_transformer
from ..extra.transformers.simple_transformer import simple_transformer

if TYPE_CHECKING:
    from . import Context


def add_standard_features(ctx: "Context"):
    ctx.add_feature(init_components)
    ctx.add_feature(init_events, claim_time=30)

    ctx.add_prop_transformer(*class_transformer())
    ctx.add_prop_transformer(*simple_transformer())
    ctx.add_prop_transformer(*html_events_transformer())
    ctx.add_prop_transformer(*dash_transformer())
    ctx.add_prop_transformer(*init_transformer())
    ctx.add_prop_transformer(*js_transformer())