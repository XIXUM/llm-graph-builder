"""Definition of meta model 'infrastructure'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from semantics import INamable


name = 'infrastructure'
nsURI = 'http://www.xixum.org/semantics/infrastructure'
nsPrefix = 'infrastructure'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


@abstract
class IInfrastructureEl(INamable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Environment(INamable):

    location = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, location=None, **kwargs):

        super().__init__(**kwargs)

        if location:
            self.location.extend(location)


@abstract
class ILocation(INamable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class ISubDir(IInfrastructureEl):

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


class Domain(IWebLocation, IInfrastructureEl):

    subdir = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, subdir=None, **kwargs):

        super().__init__(**kwargs)

        if subdir:
            self.subdir.extend(subdir)
