import spacy
nlp = spacy.load("en_core_web_sm")
with open('example.txt') as f:

    raw_content = f.read()

    #POS file creation. First, cleaning up file.

    content = raw_content.replace('\n', '').split('.')
    content = [sentence.strip() for sentence in content]
    content = content[:-1]
    content[3] = content[3] + content[4]
    del content[4]

    with open('pos.txt', 'w') as f:
        for sentence in content:
            tokens = nlp(sentence)
            for token in tokens:
                f.write(token.text + '\t' + token.pos_ + '\n')
            f.write('\n')
    f.close()

    #Entity file creation.

    tokens = nlp(raw_content)

    with open('entities.txt', 'w') as f:
        for ent in tokens.ents:
            f.write(ent.text + '\t' + str(ent.start_char) + '\t' +  str(ent.end_char) + '\t' +  ent.label_ + '\n')
    f.close()