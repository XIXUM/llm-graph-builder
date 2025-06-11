"""Definition of meta model 'infrastructure'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from src_gen.semantics.semantics import INamable


name = 'infrastructure'
nsURI = 'http://www.xixum.org/semantics/infrastructure'
nsPrefix = 'infrastructure'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


class Environment(EObject, metaclass=MetaEClass):

    location = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, location=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if location:
            self.location.extend(location)


@abstract
class ILocation(EObject, metaclass=MetaEClass):

    def __init__(self):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()


@abstract
class IInfrastructureEl(INamable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class ILocalLocation(ILocation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class IWebLocation(ILocation):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Domain(ILocation, IWebLocation):

    subdir = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, subdir=None, **kwargs):

        super().__init__(**kwargs)

        if subdir:
            self.subdir.extend(subdir)


@abstract
class ISubDir(IInfrastructureEl):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PathEl(ISubDir):

    isubdir = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    artifact = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, isubdir=None, artifact=None, **kwargs):

        super().__init__(**kwargs)

        if isubdir:
            self.isubdir.extend(isubdir)

        if artifact:
            self.artifact.extend(artifact)


class Device(IInfrastructureEl, ILocalLocation):

    subdir = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, subdir=None, **kwargs):

        super().__init__(**kwargs)

        if subdir:
            self.subdir.extend(subdir)
