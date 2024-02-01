import nltk
def pcfg_parse(sentence, pcfg_grammar):
    tokens = nltk.word_tokenize(sentence)
    parser = nltk.EarleyChartParser(pcfg_grammar)
    parse_tree = None
    for tree in parser.parse(tokens):
        parse_tree = tree
        break  
    return parse_tree
pcfg_grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> Det N [0.5] | N [0.5]
    VP -> V NP [0.7] | VP PP [0.3]
    PP -> P NP [1.0]
    Det -> 'the' [0.8] | 'a' [0.2]
    N -> 'cat' [0.4] | 'dog' [0.6]
    V -> 'chased' [0.9] | 'caught' [0.1]
    P -> 'in' [0.6] | 'on' [0.4]
""")
example_sentence = "the cat chased a dog"
parse_tree = pcfg_parse(example_sentence, pcfg_grammar)
if parse_tree:
    parse_tree.pretty_print()
else:
    print("No parse tree found for the given sentence.")
