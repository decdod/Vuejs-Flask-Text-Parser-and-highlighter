<template>
    <div class="inline-block-child">
        <div class="task">
        <pre>
        <h3 class="head">nlp_exercise.py</h3>
        <code class="code">
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
            </code>
        </pre>
        </div>
    </div>
</template>

<style>

.inline-block-child {
  display: inline-flex;
  text-align: center;

}

.code {
  background-color: #eee;
  border: 1px solid #999;
  display: block;
  padding: 20px;
}

.task {
  padding-left:0;
  text-align: left;

}

.head{
  text-align: center;
  display: inline;
}

</style>
