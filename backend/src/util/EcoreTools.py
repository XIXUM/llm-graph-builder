from semantics import StringProperty, IntProperty, FloatProperty, ListProperty, MapProperty, BoolProperty, IAggregated

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


def create_property(datatype: str, name: str, value=None):
    prop = property_factory[datatype.lower()]()
    prop.name = name
    if isinstance(prop, IAggregated):
        #only append if not null
        if value:
            prop.value.append(value)
    else:
        prop.value = value

    return prop

