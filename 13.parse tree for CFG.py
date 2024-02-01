import nltk
def generate_parse_tree(sentence, grammar):
    tokens = nltk.word_tokenize(sentence)
    parser = nltk.ChartParser(grammar)
    parse_tree = None
    for tree in parser.parse(tokens):
        parse_tree = tree
        break 
    return parse_tree
example_grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'cat' | 'dog'
    V -> 'chased' | 'caught'
""")
example_sentence = "the cat chased a dog"
parse_tree = generate_parse_tree(example_sentence, example_grammar)
if parse_tree:
    parse_tree.pretty_print()
else:
    print("No parse tree found for the given sentence.")
