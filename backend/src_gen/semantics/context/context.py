"""Definition of meta model 'context'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from semantics import INamable


name = 'context'
nsURI = 'http://www.xixum.org/semantics/context'
nsPrefix = 'context'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


@abstract
class IChronological(EObject, metaclass=MetaEClass):

    after = EReference(ordered=True, unique=True, containment=False, derived=False)
    before = EReference(ordered=True, unique=True, containment=False, derived=False)
    synchronous = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, after=None, before=None, synchronous=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if after is not None:
            self.after = after

        if before is not None:
            self.before = before

        if synchronous is not None:
            self.synchronous = synchronous


@abstract
class IRefferable(EObject, metaclass=MetaEClass):

    operation = EReference(ordered=True, unique=True, containment=False, derived=False)
    command = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, operation=None, command=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if operation is not None:
            self.operation = operation

        if command is not None:
            self.command = command


@abstract
class IContextEl(INamable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Prototype(IRefferable):

    abstract = EReference(ordered=True, unique=True, containment=False, derived=False)
    specification = EReference(ordered=True, unique=True,
                               containment=False, derived=False, upper=-1)
    entity = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, abstract=None, specification=None, entity=None, **kwargs):

        super().__init__(**kwargs)

        if abstract is not None:
            self.abstract = abstract

        if specification:
            self.specification.extend(specification)

        if entity is not None:
            self.entity = entity


class ContextRoot(IContextEl):

    entity = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    event = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    time = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    relation = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    prototype = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, entity=None, event=None, time=None, relation=None, prototype=None, **kwargs):

        super().__init__(**kwargs)

        if entity:
            self.entity.extend(entity)

        if event:
            self.event.extend(event)

        if time:
            self.time.extend(time)

        if relation:
            self.relation.extend(relation)

        if prototype:
            self.prototype.extend(prototype)


class Event(IContextEl):

    next = EReference(ordered=True, unique=True, containment=False, derived=False)
    previous = EReference(ordered=True, unique=True, containment=False, derived=False)
    state = EReference(ordered=True, unique=True, containment=False, derived=False)
    time = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, next=None, previous=None, state=None, time=None, **kwargs):

        super().__init__(**kwargs)

        if next is not None:
            self.next = next

        if previous is not None:
            self.previous = previous

        if state is not None:
            self.state = state

        if time is not None:
            self.time = time


class State(IContextEl):

    event = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, event=None, **kwargs):

        super().__init__(**kwargs)

        if event is not None:
            self.event = event


class Relation(IContextEl):

    active_entity = EReference(ordered=True, unique=True, containment=False, derived=False)
    passive_entity = EReference(ordered=True, unique=True, containment=False, derived=False)
    kg_relation = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, active_entity=None, passive_entity=None, kg_relation=None, **kwargs):

        super().__init__(**kwargs)

        if active_entity is not None:
            self.active_entity = active_entity

        if passive_entity is not None:
            self.passive_entity = passive_entity

        if kg_relation is not None:
            self.kg_relation = kg_relation


@abstract
class Entity(IContextEl, IRefferable):

    state = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    kg_entity = EReference(ordered=True, unique=True, containment=False, derived=False)
    prototype = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, state=None, kg_entity=None, prototype=None, **kwargs):

        super().__init__(**kwargs)

        if state:
            self.state.extend(state)

        if kg_entity is not None:
            self.kg_entity = kg_entity

        if prototype is not None:
            self.prototype = prototype


@abstract
class Time(IContextEl, IChronological):

    event = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, event=None, **kwargs):

        super().__init__(**kwargs)

        if event is not None:
            self.event = event


class AbsTime(Time):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class RelativeTime(Time):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PysicalE(Entity):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class VirtualE(Entity):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
