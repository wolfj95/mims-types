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
# LOVE POEMS

def pluralize(noun):
    "Noun -> PluralNoun"
    assert type(noun) == Noun
    if noun.endswith("s") or noun.endswith("ch") or noun.endswith("sh"):
        return PluralNoun(noun + 'es')
    else:
        return PluralNoun(noun + 's')

# COUPLETS

def noun_phrase(adjective, noun_phrase):
    "(Adjective, NounPhrase) -> NounPhrase"
    #YOUR CODE GOES HERE
    
    raise NotImplemented("This function isn't done!") # Get rid of this after writing the function

def determine_noun_phrase(determiner, noun_phrase):
    "(Determiner, NounPhrase) -> DeterminedNounPhrase"
    #YOUR CODE GOES HERE
    
    raise NotImplemented("This function isn't done!")

def make_definite(noun_phrase):
    "NounPhrase -> DeterminedNounPhrase"
    #YOUR CODE GOES HERE
    
    raise NotImplemented("This function isn't done!")

def make_indefinite(noun_phrase):
    "NounPhrase -> DeterminedNounPhrase"
    #YOUR CODE GOES HERE
    
    raise NotImplemented("This function isn't done!")

# LIMERICKS

def verb_phrase(adverb, verb_phrase):
    "(Adverb, VerbPhrase) -> VerbPhrase"
    #YOUR CODE GOES HERE
    
    raise NotImplemented("This function isn't done!")

def past_tense_transitive(verb):
    "TransitiveVerb -> PastTenseTransitiveVerb"
    #YOUR CODE GOES HERE

    raise NotImplemented("This function isn't done!")

def past_tense_intransitive(verb):
    "TransitiveVerb -> PastTenseTransitiveVerb"
    #YOUR CODE GOES HERE

    raise NotImplemented("This function isn't done!")

def verb_phrase_transitive(verb, noun_phrase):
    "(TransitiveVerb, NounPhrase) -> VerbPhrase"
    #YOUR CODE GOES HERE

    raise NotImplemented("This function isn't done!")

