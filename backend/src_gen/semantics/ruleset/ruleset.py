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
    command = EReference(ordered=True, unique=True, containment=False, derived=False)
    operation = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, type=None, command=None, operation=None, **kwargs):

        super().__init__(**kwargs)

        if type is not None:
            self.type = type

        if command is not None:
            self.command = command

        if operation is not None:
            self.operation = operation


class Predicate(IRuleEl):

    activeToken = EReference(ordered=True, unique=True, containment=False, derived=False)
    passiveToken = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, activeToken=None, passiveToken=None, **kwargs):

        super().__init__(**kwargs)

        if activeToken is not None:
            self.activeToken = activeToken

        if passiveToken is not None:
            self.passiveToken = passiveToken
