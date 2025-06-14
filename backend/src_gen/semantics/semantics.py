"""Definition of meta model 'semantics'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from pyecore.type import Boolean


name = 'semantics'
nsURI = 'http://www.xixum.org/semantics'
nsPrefix = 'semantics'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


@abstract
class INamable(EObject, metaclass=MetaEClass):

    name = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    index = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, name=None, index=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if name is not None:
            self.name = name

        if index is not None:
            self.index = index


@abstract
class IDataComponent(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class IIdentifiable(EObject, metaclass=MetaEClass):

    hasID = EAttribute(eType=Boolean, unique=True, derived=False, changeable=True)

    def __init__(self, *, hasID=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if hasID is not None:
            self.hasID = hasID


@abstract
class IAtomic(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class IAggregated(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class IPropertyable(EObject, metaclass=MetaEClass):

    property = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, property=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if property:
            self.property.extend(property)


@abstract
class IValueComponent(INamable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Pair(IAggregated):

    key = EReference(ordered=True, unique=True, containment=True, derived=False)
    value = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, key=None, value=None, **kwargs):

        super().__init__(**kwargs)

        if key is not None:
            self.key = key

        if value is not None:
            self.value = value


@abstract
class IIterable(IAggregated):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class IContainable(IAggregated):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class Property(IValueComponent):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class StringProperty(Property, IAggregated):

    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class IntProperty(Property, IAtomic):

    value = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class FloatProperty(Property, IAtomic):

    value = EAttribute(eType=EFloat, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class BoolProperty(Property, IAtomic):

    value = EAttribute(eType=Boolean, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class ListProperty(Property, IIterable):

    entry = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, entry=None, **kwargs):

        super().__init__(**kwargs)

        if entry:
            self.entry.extend(entry)


class MapProperty(Property, IIterable):

    entry = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, entry=None, **kwargs):

        super().__init__(**kwargs)

        if entry:
            self.entry.extend(entry)
