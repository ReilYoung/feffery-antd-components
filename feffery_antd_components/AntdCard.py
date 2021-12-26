# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdCard(Component):
    """An AntdCard component.


Keyword arguments:

- children (a list of or a singular dash component, string or number; optional):
    The content of the tab - will only be displayed if this tab is
    selected.

- id (string; optional)

- bodyStyle (dict; optional)

- border (boolean; optional)

- className (string; optional)

- coverImg (dict; optional)

    `coverImg` is a dict with keys:

    - alt (string; optional)

    - src (string; optional)

    - style (dict; optional)

- extraLink (dict; optional)

    `extraLink` is a dict with keys:

    - className (string; optional)

    - content (string; optional)

    - href (string; optional)

    - style (dict; optional)

    - target (string; optional)

- headStyle (dict; optional)

- hoverable (boolean; optional)

- loading_state (dict; optional)

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- size (a value equal to: 'default', 'small'; optional)

- style (dict; optional)

- title (string; optional)"""
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, extraLink=Component.UNDEFINED, coverImg=Component.UNDEFINED, bodyStyle=Component.UNDEFINED, headStyle=Component.UNDEFINED, border=Component.UNDEFINED, hoverable=Component.UNDEFINED, size=Component.UNDEFINED, title=Component.UNDEFINED, loading_state=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'bodyStyle', 'border', 'className', 'coverImg', 'extraLink', 'headStyle', 'hoverable', 'loading_state', 'size', 'style', 'title']
        self._type = 'AntdCard'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'bodyStyle', 'border', 'className', 'coverImg', 'extraLink', 'headStyle', 'hoverable', 'loading_state', 'size', 'style', 'title']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdCard, self).__init__(children=children, **args)