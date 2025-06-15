from semantics import StringProperty, IntProperty, FloatProperty, ListProperty, MapProperty, BoolProperty, IAggregated, \
    IContainable

property_factory = {
    "string": StringProperty,
    "integer": IntProperty,
    "float": FloatProperty,
    "list": ListProperty,
    "map": MapProperty,
    "boolean": BoolProperty,
    # Synonyms:
    "int": IntProperty,
    "bool": BoolProperty,
    "str": StringProperty,
    "dict": MapProperty,
    "aggregate": ListProperty,
    "collection": ListProperty
}

typed_property_factory = {
    str: StringProperty,
    int: IntProperty,
    float: FloatProperty,
    list: ListProperty,
    dict: MapProperty,
    bool: BoolProperty,
    tuple: ListProperty,
    range: ListProperty,
    # not supported yet:
    # bypes, bytearray, memoryview
    # complex
    # set
    # contextmanager
    # annotation types
    # further special types, see:
    # https://docs.python.org/3/library/stdtypes.html#other-built-in-types
}


def manual_create_property(datatype: str, name: str, value=None):
    prop = property_factory[datatype.lower()]()
    prop.name = name
    if isinstance(prop, IContainable):
        #only append if not null
        if value:
            prop.value.append(value)
    else:
        prop.value = value

    return prop

def create_property(name: str, value=None):
    if not value:
        raise ValueError(f"Value name {name} is empty or null.")
    prop = typed_property_factory[type(value)]()
    prop.name = name
    if isinstance(prop, IContainable):
        #only append if not null
        if value:
            prop.value.append(value)
    else:
        prop.value = value

    return prop


