"""Definition of meta model 'dictionary'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from semantics import INamable


name = 'dictionary'
nsURI = 'http://www.xixum.org/semantics/dictionary'
nsPrefix = 'dictionary'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


@abstract
class IDictionaryEl(INamable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class DictionaryRoot(IDictionaryEl):

    word = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    wordclass = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, word=None, wordclass=None, **kwargs):

        super().__init__(**kwargs)

        if word:
            self.word.extend(word)

        if wordclass:
            self.wordclass.extend(wordclass)


class Word(IDictionaryEl):

    ofType = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)
    baseform = EReference(ordered=True, unique=True, containment=False, derived=False)
    stem = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, ofType=None, baseform=None, stem=None, **kwargs):

        super().__init__(**kwargs)

        if ofType:
            self.ofType.extend(ofType)

        if baseform is not None:
            self.baseform = baseform

        if stem:
            self.stem.extend(stem)


class WordClass(IDictionaryEl):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Stem(IDictionaryEl):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)
