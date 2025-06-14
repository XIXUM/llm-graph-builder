from pyecore.resources import global_registry
from .semantics import getEClassifier, eClassifiers
from .semantics import name, nsURI, nsPrefix, eClass
from .semantics import INamable, IDataComponent, Property, IValueComponent, StringProperty, IntProperty, FloatProperty, BoolProperty, ListProperty, MapProperty, Pair, IIdentifiable, IAtomic, IAggregated, IIterable, IContainable, IPropertyable


from .artifact import Token, NonVoidTag, Document, ITextBodyEl, Styleable, RowBlockEl, Number, Paragraph, Word, Cell, MetaElement, Artifact, GridBlockEl, Sentence, XMLdocument, RowContainer, CSS_Style, PlainText
from .infrastructure import Environment, PathEl, ISubDir, Domain, Device, ILocation
from .context import Relation, State, Time, Event, IRefferable, Entity, IChronological, Class, ContextRoot
from .dictionary import DictionaryRoot, Word, WordClass, Stem
from .ruleset import RuleRoot, Predicate, Token
from .knowledgegraph import KGroot, INode, Relation, Entity, Chunk, Document
from . import semantics
from . import artifact

from . import infrastructure

from . import context

from . import dictionary

from . import ruleset

from . import knowledgegraph


__all__ = ['INamable', 'IDataComponent', 'Property', 'IValueComponent', 'StringProperty', 'IntProperty', 'FloatProperty', 'BoolProperty',
           'ListProperty', 'MapProperty', 'Pair', 'IIdentifiable', 'IAtomic', 'IAggregated', 'IIterable', 'IContainable', 'IPropertyable']

eSubpackages = [artifact, infrastructure, context, dictionary, ruleset, knowledgegraph]
eSuperPackage = None
semantics.eSubpackages = eSubpackages
semantics.eSuperPackage = eSuperPackage

Paragraph.sentence.eType = Sentence
Sentence.token.eType = Token
Word.word.eType = Word
Number.value.eType = IAtomic
PlainText.blockElement.eType = ITextBodyEl
PlainText.rowblockel.eType = RowBlockEl
XMLdocument.metaelement.eType = MetaElement
GridBlockEl.row.eType = RowContainer
RowBlockEl.gridblockel.eType = GridBlockEl
RowBlockEl.paragraph.eType = Paragraph
RowContainer.cell.eType = Cell
Cell.rowblockel.eType = NonVoidTag
Styleable.css_style.eType = CSS_Style
NonVoidTag.rowblockel.eType = RowBlockEl
Device.subdir.eType = ISubDir
PathEl.isubdir.eType = ISubDir
PathEl.artifact.eType = Artifact
Domain.subdir.eType = ISubDir
Environment.location.eType = ILocation
ContextRoot.entity.eType = Entity
ContextRoot.event.eType = Event
ContextRoot.time.eType = Time
ContextRoot.relation.eType = Relation
ContextRoot.class_.eType = Class
Entity.state.eType = State
IChronological.synchronous.eType = IChronological
DictionaryRoot.word.eType = Word
DictionaryRoot.wordclass.eType = WordClass
Word.ofType.eType = WordClass
Word.baseform.eType = Word
Word.stem.eType = Stem
RuleRoot.token.eType = Token
RuleRoot.command.eType = Predicate
Document.chunk.eType = Chunk
Chunk.entity.eType = Entity
KGroot.document.eType = Document
KGroot.relation.eType = Relation
ListProperty.entry.eType = Property
MapProperty.entry.eType = Pair
Pair.key.eType = Property
Pair.value.eType = Property
IPropertyable.property.eType = Property
Document.kg_reference.eType = Document
ITextBodyEl.chunk.eType = Chunk
Entity.kg_entity.eType = Entity
Entity.class_.eType = Class
Event.next.eType = Event
Event.previous.eType = Event
Event.previous.eOpposite = Event.next
Event.state.eType = State
Event.time.eType = Time
State.event.eType = Event
State.event.eOpposite = Event.state
Time.event.eType = Event
Time.event.eOpposite = Event.time
Relation.active_entity.eType = IRefferable
Relation.passive_entity.eType = IRefferable
Relation.kg_relation.eType = Relation
IChronological.after.eType = IChronological
IChronological.before.eType = IChronological
IChronological.before.eOpposite = IChronological.after
Class.abstract.eType = Class
Class.extension.eType = Class
Class.extension.eOpposite = Class.abstract
Class.entity.eType = Entity
Class.entity.eOpposite = Entity.class_
IRefferable.operation.eType = Relation
IRefferable.operation.eOpposite = Relation.passive_entity
IRefferable.command.eType = Relation
IRefferable.command.eOpposite = Relation.active_entity
Token.command.eType = Predicate
Token.operation.eType = Predicate
Predicate.activeToken.eType = Token
Predicate.activeToken.eOpposite = Token.command
Predicate.passiveToken.eType = Token
Predicate.passiveToken.eOpposite = Token.operation
Document.context_ref.eType = Document
Document.context_ref.eOpposite = Document.kg_reference
Chunk.context_ref.eType = ITextBodyEl
Chunk.context_ref.eOpposite = ITextBodyEl.chunk
Entity.context_ref.eType = Entity
Entity.context_ref.eOpposite = Entity.kg_entity
Relation.target_node.eType = INode
Relation.source_node.eType = INode
Relation.context_ref.eType = Relation
Relation.context_ref.eOpposite = Relation.kg_relation
INode.in_relation.eType = Relation
INode.in_relation.eOpposite = Relation.target_node
INode.out_relation.eType = Relation
INode.out_relation.eOpposite = Relation.source_node

otherClassifiers = []

for classif in otherClassifiers:
    eClassifiers[classif.name] = classif
    classif.ePackage = eClass

for classif in eClassifiers.values():
    eClass.eClassifiers.append(classif.eClass)

for subpack in eSubpackages:
    eClass.eSubpackages.append(subpack.eClass)

register_packages = [semantics] + eSubpackages
for pack in register_packages:
    global_registry[pack.nsURI] = pack
