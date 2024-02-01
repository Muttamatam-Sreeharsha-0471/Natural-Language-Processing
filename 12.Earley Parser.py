class EarleyParser:
    def __init__(self, grammar):
        self.grammar = grammar
    def parse(self, input_string):
        self.chart = [[] for _ in range(len(input_string) + 1)]
        self.chart[0].append(('start', '', 0))
        for i in range(len(input_string) + 1):
            for state in self.chart[i]:
                self.predictor(state, i)
                if i < len(input_string):
                    self.scanner(state, input_string[i], i)
                else:
                    self.completer(state, i)
        if ('start', self.grammar['start'], 0) in self.chart[len(input_string)]:
            print(f'Parsing failed for input: {input_string}')
        else:
            print(f'Parsing successfull for input: {input_string}')
    def predictor(self, state, index):
        if state[1] in self.grammar:
            for production in self.grammar[state[1]]:
                self.chart[index].append((state[1], production, index))
    def scanner(self, state, token, index):
        if state[1] == '' or state[1][0] != token:
            return
        self.chart[index + 1].append((state[0], state[1][1:], state[2]))
    def completer(self, state, index):
        for st in self.chart[state[2]]:
            if st[1] == '' or st[1][0] != state[0]:
                continue
            self.chart[index].append((st[0], st[1][1:], st[2]))
# Example usage
grammar = {
    'start': 'Expression',
    'Expression': ['Term + Expression', 'Term'],
    'Term': ['Factor * Term', 'Factor'],
    'Factor': ['( Expression )', 'number']
}

parser = EarleyParser(grammar)

# Test the parser
parser.parse('3* (2+1)') # Parsing successful for input: 3* (2+1)
parser.parse('2+1*3') # Parsing successful for input: 2+1*3
parser.parse('2+ (1*3)') # Parsing successful for input: 2+ (1*3)
