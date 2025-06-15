from semantics import StringProperty, IntProperty, FloatProperty, ListProperty, MapProperty, BoolProperty, IAggregated, \
    IContainable, Pair, Property

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


def manual_create_property(datatype: str, name, value=None):
    prop = property_factory[datatype.lower()]()
    prop.name = name
    if isinstance(name, int):
        prop.index = name
    return switch(prop, value)


def handle_atomic(value, prop: (IntProperty, FloatProperty, StringProperty)):
    if isinstance(value, (int,float,str)):
        prop.value = value
        return prop
    else:
        raise TypeError(f"Unsupported type: {type(value).__name__}")


def handle_aggregated(value, prop: ListProperty):
    if isinstance(value, (list,tuple)):
        for i, v in enumerate(value):
            create_property(i, v)
    else:
        raise TypeError(f"Unsupported type: {type(value).__name__}")


def handle_map(value, prop: MapProperty):
    if isinstance(value, dict):
        for i, (k, v) in enumerate(value.items()):
            key = create_property(i, k)
            value = create_property(i, v)
            pair = Pair()
            pair.key = key
            pair.value = value
            value.e
    else:
        raise TypeError(f"Unsupported type: {type(value).__name__}")

def switch(prop, value):
    """Switch-like function to handle atomic, aggregated, and map types."""
    # Create a "case" dictionary based on type
    switch_cases = {
        int: handle_atomic,
        float: handle_atomic,
        str: handle_atomic,
        list: handle_aggregated,
        tuple: handle_aggregated,
        dict: handle_map
    }

    # Find the handler function for the specific type
    dataType = type(value)
    if dataType in switch_cases:
        handler = switch_cases.get(type(value))
    else:
        raise TypeError(f"Unsupported type: {type(value).__name__}")

    # Call the handler function and return its result
    return handler(value, prop)

def create_property(name: str, value: object) -> Property:
    if not value:
        raise ValueError(f"Value name {name} is empty or null.")
    prop = typed_property_factory[type(value)]()
    prop.name = name
    if isinstance(prop, IContainable):
        #only append if not null
        if value:
            expand_aggregated_value(prop, value)
    else:
        prop.value = value

    return prop


