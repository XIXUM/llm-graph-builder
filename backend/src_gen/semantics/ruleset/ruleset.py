"""Definition of meta model 'ruleset'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from semantics import INamable


name = 'ruleset'
nsURI = 'http://www.xixum.org/semantics/ruleset'
nsPrefix = 'ruleset'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


@abstract
class IRuleEl(INamable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class RuleRoot(IRuleEl):

    token = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    command = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, token=None, command=None, **kwargs):

        super().__init__(**kwargs)

        if token:
            self.token.extend(token)

        if command:
            self.command.extend(command)


class Token(IRuleEl):

    type = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, type=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type


class Command(IRuleEl):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
