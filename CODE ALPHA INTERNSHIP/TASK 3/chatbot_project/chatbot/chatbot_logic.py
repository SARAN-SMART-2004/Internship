
import random
import spacy

nlp = spacy.load("en_core_web_sm")

responses = {
    "greet": ["Hello!", "Hi there!", "Hey!", "Hi!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["I'm not sure how to respond to that.", "Can you rephrase?", "I don't understand."]
}

def get_intent(text):
    doc = nlp(text.lower())
    for token in doc:
        if token.lemma_ == "hello" or token.lemma_ == "hi":
            return "greet"
        elif token.lemma_ == "bye" or token.lemma_ == "goodbye":
            return "bye"
    return "default"

def get_response(intent):
    return random.choice(responses[intent])
