"""Definition of meta model 'knowledgegraph'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *


name = 'knowledgegraph'
nsURI = ''
nsPrefix = ''

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class KGroot(EObject, metaclass=MetaEClass):

    document = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    relation = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    entity = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, document=None, relation=None, entity=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if document:
            self.document.extend(document)

        if relation:
            self.relation.extend(relation)

        if entity:
            self.entity.extend(entity)


class KGrelation(EObject, metaclass=MetaEClass):

    target_node = EReference(ordered=True, unique=True, containment=False, derived=False)
    source_node = EReference(ordered=True, unique=True, containment=False, derived=False)
    context_ref = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, target_node=None, source_node=None, context_ref=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if target_node is not None:
            self.target_node = target_node

        if source_node is not None:
            self.source_node = source_node

        if context_ref is not None:
            self.context_ref = context_ref


@abstract
class INode(EObject, metaclass=MetaEClass):

    in_relation = EReference(ordered=True, unique=True, containment=False, derived=False)
    out_relation = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, in_relation=None, out_relation=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if in_relation is not None:
            self.in_relation = in_relation

        if out_relation is not None:
            self.out_relation = out_relation


class KGdocument(INode):

    chunk = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    context_ref = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, chunk=None, context_ref=None, **kwargs):

        super().__init__(**kwargs)

        if chunk:
            self.chunk.extend(chunk)

        if context_ref is not None:
            self.context_ref = context_ref


class KGchunk(INode):

    context_ref = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, context_ref=None, **kwargs):

        super().__init__(**kwargs)

        if context_ref is not None:
            self.context_ref = context_ref


class KGentity(INode):

    context_ref = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, context_ref=None, **kwargs):

        super().__init__(**kwargs)

        if context_ref is not None:
            self.context_ref = context_ref
