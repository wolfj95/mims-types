from vocabulary import starts_with_vowel_sound
from grammatical_types import (
    Noun, 
    PluralNoun,
    TransitiveVerb,
    IntransitiveVerb,
    PastTenseTransitiveVerb,
    PastTenseIntransitiveVerb,
    Adjective,
    Adverb, 
    NounPhrase,
    Determiner, 
    DeterminedNounPhrase,
    VerbPhrase, 
    Sentence
)

# NEEDED FOR LOVE POEM

def pluralize(noun):
    "Noun -> PluralNoun"
    assert type(noun) == Noun
    if noun.endswith("s") or noun.endswith("ch") or noun.endswith("sh"):
        return PluralNoun(noun + 'es')
    else:
        return PluralNoun(noun + 's')

# NEEDED FOR COUPLET

def noun_phrase(adjective, noun):
    "(Adjective, Noun) -> NounPhrase"
    raise NotImplemented("This function isn't done!")

def determine_noun_phrase(determiner, noun_phrase):
    "(Determiner, NounPhrase) -> Determined NounPhrase"
    raise NotImplemented("This function isn't done!")

def make_definite(noun_phrase):
    "NounPhrase -> DeterminedNounPhrase"
    raise NotImplemented("This function isn't done!")

def make_indefinite(noun_phrase):
    "NounPhrase -> DeterminedNounPhrase"
    raise NotImplemented("This function isn't done!")

# NEEDED FOR LIMERICK

def verb_phrase(adverb, verb_phrase):
    "(Adverb, VerbPhrase) -> VerbPhrase"
    raise NotImplemented("This function isn't done!")

def past_tense_transitive(verb):
    "TransitiveVerb -> PastTenseTransitiveVerb"
    raise NotImplemented("This function isn't done!")

def past_tense_intransitive(verb):
    "TransitiveVerb -> PastTenseTransitiveVerb"
    raise NotImplemented("This function isn't done!")

def verb_phrase_transitive(verb, noun_phrase):
    "(TransitiveVerb, NounPhrase) -> VerbPhrase"
    raise NotImplemented("This function isn't done!")

