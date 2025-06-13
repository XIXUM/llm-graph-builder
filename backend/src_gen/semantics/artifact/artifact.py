"""Definition of meta model 'artifact'."""
from functools import partial
import pyecore.ecore as Ecore
from pyecore.ecore import *
from src_gen.semantics import INamable, IDataComponent, IIdentifiable, IContainable


name = 'artifact'
nsURI = 'http://www.xixum.org/semantics/artifact'
nsPrefix = 'artifact'

eClass = EPackage(name=name, nsURI=nsURI, nsPrefix=nsPrefix)

eClassifiers = {}
getEClassifier = partial(Ecore.getEClassifier, searchspace=eClassifiers)


@abstract
class ITextBodyEl(EObject, metaclass=MetaEClass):

    chunk = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, chunk=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if chunk is not None:
            self.chunk = chunk


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
class Styleable(EObject, metaclass=MetaEClass):

    css_style = EReference(ordered=True, unique=True, containment=False, derived=False, upper=-1)

    def __init__(self, *, css_style=None):
        # if kwargs:
        #    raise AttributeError('unexpected arguments: {}'.format(kwargs))

        super().__init__()

        if css_style:
            self.css_style.extend(css_style)


class CSS_Style(IPropertyable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class GridElement(Styleable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Artifact(INamable, IPropertyable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


@abstract
class Token(IDataComponent, Styleable):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class RowContainer(GridElement):

    row = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    cell = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, cell=None, row=None, **kwargs):

        super().__init__(**kwargs)

        if row is not None:
            self.row = row

        if cell:
            self.cell.extend(cell)


class Cell(GridElement):

    column = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    rowSpan = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    colSpan = EAttribute(eType=EInt, unique=True, derived=False, changeable=True)
    rowblockel = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, rowblockel=None, column=None, rowSpan=None, colSpan=None, **kwargs):

        super().__init__(**kwargs)

        if column is not None:
            self.column = column

        if rowSpan is not None:
            self.rowSpan = rowSpan

        if colSpan is not None:
            self.colSpan = colSpan

        if rowblockel:
            self.rowblockel.extend(rowblockel)


@abstract
class MetaElement(IPropertyable, IDataComponent):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Document(Artifact):

    kg_reference = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, kg_reference=None, **kwargs):

        super().__init__(**kwargs)

        if kg_reference is not None:
            self.kg_reference = kg_reference


class Sentence(IDataComponent, IContainable):

    token = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, token=None, **kwargs):

        super().__init__(**kwargs)

        if token:
            self.token.extend(token)


class Word(Token):

    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)
    word = EReference(ordered=True, unique=True, containment=False, derived=False)

    def __init__(self, *, value=None, word=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value

        if word is not None:
            self.word = word


class Number(Token):

    value = EReference(ordered=True, unique=True, containment=True, derived=False)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class NamedIdentity(Token):

    value = EAttribute(eType=EString, unique=True, derived=False, changeable=True)

    def __init__(self, *, value=None, **kwargs):

        super().__init__(**kwargs)

        if value is not None:
            self.value = value


class GridBlockEl(MetaElement):

    row = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, row=None, **kwargs):

        super().__init__(**kwargs)

        if row:
            self.row.extend(row)


class SelfClosingTag(MetaElement):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class NonVoidTag(MetaElement):

    rowblockel = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, rowblockel=None, **kwargs):

        super().__init__(**kwargs)

        if rowblockel:
            self.rowblockel.extend(rowblockel)


class ASCIIdocument(Document):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class Paragraph(ITextBodyEl, IIdentifiable, IDataComponent, Styleable):

    sentence = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, sentence=None, **kwargs):

        super().__init__(**kwargs)

        if sentence:
            self.sentence.extend(sentence)


class BinaryDocument(Document):

    def __init__(self, **kwargs):

        super().__init__(**kwargs)


class PlainText(ASCIIdocument):

    blockElement = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    rowblockel = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, blockElement=None, rowblockel=None, **kwargs):

        super().__init__(**kwargs)

        if blockElement:
            self.blockElement.extend(blockElement)

        if rowblockel:
            self.rowblockel.extend(rowblockel)


class XMLdocument(ASCIIdocument):

    metaelement = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, metaelement=None, **kwargs):

        super().__init__(**kwargs)

        if metaelement:
            self.metaelement.extend(metaelement)


class RowBlockEl(Styleable, NonVoidTag):

    gridblockel = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)
    paragraph = EReference(ordered=True, unique=True, containment=True, derived=False, upper=-1)

    def __init__(self, *, gridblockel=None, paragraph=None, **kwargs):

        super().__init__(**kwargs)

        if gridblockel:
            self.gridblockel.extend(gridblockel)

        if paragraph:
            self.paragraph.extend(paragraph)
