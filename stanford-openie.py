"""
Java needs to be installed first
Then install with: pip install stanford_openie
"""

from openie import StanfordOpenIE

#list of properties is available here:
#https://stanfordnlp.github.io/CoreNLP/openie.html
properties = {
    'openie.affinity_probability_cap': 2 / 3,
    'resolve_coref': True
}

with StanfordOpenIE(properties=properties) as client:
    #preparation of corpus (40 sentences)
    corpus = []
    with open('corpus.txt', encoding='utf8') as r:
        for line in r:
            corpus.append(line)

    #output file
    f = open("triples.txt", "w", encoding='utf8')

    for n, line in enumerate(corpus, start=1):
        #writing the sentence
        f.write("#" + str(n) + ": " + line + "\n")

        #annotation
        triples_corpus = client.annotate(line)
        for triple in triples_corpus:
            f.write(triple["subject"] + " <TAB> " + triple["relation"] + " <TAB> " + triple["object"] + "\n")
        f.write('\n')