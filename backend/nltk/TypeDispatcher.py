from pyecore.utils import dispatch


class TypeHandler:

    @dispatch(int)
    def handle(self, value):
        return f"Integer: {value}"

    @dispatch(float)
    def handle(self, value):
        return f"Float: {value}"

    @dispatch(str)
    def handle(self, value):
        return f"String: {value}"

    @dispatch(list)
    def handle(self, value):
        return f"List with {len(value)} elements: {value}"

    @dispatch(tuple)
    def handle(self, value):
        return f"Tuple with {len(value)} elements: {value}"

    @dispatch(dict)
    def handle(self, value):
        return f"Map with {len(value)} keys: {value}"

    @dispatch(object)
    def handle(self, value):
        return f"Unsupported type: {type(value).__name__}"


# Example Usage:
handler = TypeHandler()

values = [42, "hello", 3.14, [1, 2, 3], ("a", "b"), {"key": "value"}, {1, 2, 3}]
for value in values:
    print(handler.handle(value))
