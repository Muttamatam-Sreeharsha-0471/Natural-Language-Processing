class SimpleParser:
    def __init__ (self, grammar):
        self.grammar = grammar
    def parse (self, input_string):
        self.input = input_string
        self.index = 0
        self.result = True
        if self.expression ():
            if self.index == len (self.input):
                print (f'Parsing successful for input: {input_string}')
                return
        print (f'Parsing failed for input: {input_string}')
    def expression (self):
        return self.term () and self.expression_tail ()
    def expression_tail (self):
        current_index = self.index
        if self.match ('+'):
            return self.term () and self.expression_tail ()
        self.index = current_index
        return True
    def term (self):
        return self.factor () and self.term_tail ()
    def term_tail (self):
        current_index = self.index
        if self.match ('*'):
            return self.factor () and self.term_tail ()
        self.index = current_index
        return True
    def factor (self):
        if self.match ('('):
            if self.expression () and self.match (')'):
                return True
            return False
        return self.match ('number')
    def match (self, expected):
        if self.index < len (self.input) and (expected == self.input [self.index] or expected == 'number' and self.input [self.index].isdigit ()):
            self.index += 1
            return True
        return False

grammar = {
    'start': 'Expression',
}

parser = SimpleParser (grammar)

parser.parse ('3* (2+1)') 
parser.parse ('2+1*3') 
parser.parse ('2+ (1*1)') 
