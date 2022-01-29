import spacy
nlp = spacy.load("en_core_web_sm")

# You can add helper functions and variables if needed



def tokenize_with_pos(input):
    tokens = nlp(input)
    tokens_output = []
    for token in tokens:
        tokens_output.append({"text": token.text, "start":token.idx, "end":token.idx + len(token), "pos": token.pos_})
    """
    This function should take a string as input , process it with the "en_core_web_sm"
    spacy pipeline and return a list of token representations. Tokens should be represented
    by dictionaries as follows: {"text": token text, "start": token start char index, "end": token char offset,
             "pos": human readable token POS tag}
    Complete the function body
    """
    return tokens_output


def get_named_entities(input):
    tokens = nlp(input)
    tokens_output = []
    for ent in tokens.ents:
        tokens_output.append({"text": ent.text, "start": ent.start_char, "end": ent.end_char, "ne_label": ent.label_})
    """
    This function should take a string as input , process it with the "en_core_web_sm"
    spacy pipeline and return a list of named entity representations. Entities should be represented
    by dictionaries as follows: {"text": entity text, "start": entity start char index, "entity": token char offset,
             "ne_label": human readable entity label}
    Complete the function body
    """
    return tokens_output

# print(tokenize_with_pos("Hello how are you, I am doing just fantastic"))
