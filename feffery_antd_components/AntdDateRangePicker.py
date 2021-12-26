# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class AntdDateRangePicker(Component):
    """An AntdDateRangePicker component.


Keyword arguments:

- id (string; optional)

- bordered (boolean; optional)

- className (string; optional)

- defaultPickerValue (string; optional)

- defaultValue (list of strings; optional)

- disabled (list of booleans; optional)

- format (string; optional)

- loading_state (dict; optional):
    Object that holds the loading state object coming from
    dash-renderer.

    `loading_state` is a dict with keys:

    - component_name (string; optional):
        Holds the name of the component that is loading.

    - is_loading (boolean; optional):
        Determines if the component is loading or not.

    - prop_name (string; optional):
        Holds which property is loading.

- locale (a value equal to: 'zh-cn', 'en-us'; default 'zh-cn')

- persisted_props (list of a value equal to: 'value's; default ['value']):
    Properties whose user interactions will persist after refreshing
    the  component or the page. Since only `value` is allowed this
    prop can  normally be ignored.

- persistence (boolean | string | number; optional):
    Used to allow user interactions in this component to be persisted
    when  the component - or the page - is refreshed. If `persisted`
    is truthy and  hasn't changed from its previous value, a `value`
    that the user has  changed while using the app will keep that
    change, as long as  the new `value` also matches what was given
    originally.  Used in conjunction with `persistence_type`.

- persistence_type (a value equal to: 'local', 'session', 'memory'; default 'local'):
    Where persisted user changes will be stored:  memory: only kept in
    memory, reset on page refresh.  local: window.localStorage, data
    is kept after the browser quit.  session: window.sessionStorage,
    data is cleared once the browser quit.

- picker (a value equal to: 'date', 'week', 'month', 'quarter', 'year'; optional)

- placeholder (list of strings; optional)

- showTime (boolean; default False)

- size (a value equal to: 'small', 'middle', 'large'; optional)

- style (dict; optional)

- value (list of strings; optional)"""
    @_explicitize_args
    def __init__(self, id=Component.UNDEFINED, className=Component.UNDEFINED, style=Component.UNDEFINED, locale=Component.UNDEFINED, picker=Component.UNDEFINED, format=Component.UNDEFINED, showTime=Component.UNDEFINED, placeholder=Component.UNDEFINED, disabled=Component.UNDEFINED, value=Component.UNDEFINED, defaultValue=Component.UNDEFINED, bordered=Component.UNDEFINED, size=Component.UNDEFINED, defaultPickerValue=Component.UNDEFINED, loading_state=Component.UNDEFINED, persistence=Component.UNDEFINED, persisted_props=Component.UNDEFINED, persistence_type=Component.UNDEFINED, **kwargs):
        self._prop_names = ['id', 'bordered', 'className', 'defaultPickerValue', 'defaultValue', 'disabled', 'format', 'loading_state', 'locale', 'persisted_props', 'persistence', 'persistence_type', 'picker', 'placeholder', 'showTime', 'size', 'style', 'value']
        self._type = 'AntdDateRangePicker'
        self._namespace = 'feffery_antd_components'
        self._valid_wildcard_attributes =            []
        self.available_properties = ['id', 'bordered', 'className', 'defaultPickerValue', 'defaultValue', 'disabled', 'format', 'loading_state', 'locale', 'persisted_props', 'persistence', 'persistence_type', 'picker', 'placeholder', 'showTime', 'size', 'style', 'value']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}
        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(AntdDateRangePicker, self).__init__(**args)