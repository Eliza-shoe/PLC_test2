import re


class ShoeFileManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def get_word_matrix(self):
        word_matrix = []

        lines = []
        with open(self.filepath, "r") as f:
            contents = f.read()

        lines = contents.split(";")

        for i in range(len(lines)):
            word_list = []
            words = lines[i].split(" ")
            words = [item.strip() for item in words]
            words = [j for j in words if j]
            word_matrix.append(words)

        return word_matrix


class ShoeTokenizer:
    def __init__(self, word_matrix):
        self.word_matrix = word_matrix

    def define_tokens(self):
        """Defines tokens"""
        variable = re.compile("^[A-Za-z_]{5,7}")
        special_words = re.compile(
            "fits|wearit|shoelace|sandal|loafer|cowboy|wellington|start|end"
        )
        charmap = {
            # variables 1, digits 2
            "variable": 1,
            "digit": 2,
            "fits": 3,  # if
            "shoelace": 5,  # loop
            "sandal": 6,  # 1 byte int
            "loafer": 7,  # 2 byte int
            "cowboy": 8,  # 4 byte int
            "wellington": 9,  # 8 byte int
            "{": 10,  # right curly brace, used for differentiation
            "}": 11,  # left curly brace, used for differentiation
            "=": 12,  # variable declaration | equals
            "+": 13,  # addition
            "-": 14,  # subtraction
            "*": 15,  # multiplication
            "/": 16,  # division
            "%": 17,  # modulo
            "(": 18,  # right parenthesis, for precedence setting
            ")": 19,  # left parenthesis, for precedence setting
            "<": 20,  # less than
            ">": 21,  # greater than
            "<=": 22,  # less than or equal to
            ">=": 23,  # greater than or equal to
            "==": 24,  # is equal to
            "!=": 25,  # is not equal to
            "'": 26,  # quotation
            ";": 28,  # semicolon, used to denote end of like
            "start": 29,
            "end": 30,
            "illegal": 99,
        }
        return variable, special_words, charmap

    def tokenize(self):
        """Input is contents of given text file,
        output is list of integers encoding tokens"""
        variable, special_words, charmap = self.define_tokens()
        token_list = []
        lexemes = []
        lex_count = []
        lines = []

        for line in self.word_matrix:
            cur_count = 0
            cur_tokens = []
            cur_lexemes = []
            for word in line:

                if re.match(special_words, word):  # check if lexeme is special word
                    cur_tokens.append(charmap[word])
                    cur_count += 1
                    cur_lexemes.append(word)

                elif re.match(variable, word):  # check if lexeme could be varaible
                    cur_tokens.append(charmap["variable"])
                    cur_count += 1
                    cur_lexemes.append(word)

                elif word.isnumeric():
                    cur_tokens.append(charmap["digit"])
                    cur_count += 1
                    cur_lexemes.append(word)

                elif word in charmap.keys():
                    cur_tokens.append(charmap[word])
                    cur_count += 1
                    cur_lexemes.append(word)
                else:
                    token_list.append(charmap["illegal"])
                    print("Lexical Error: invalid symbol detected")
                    print(f"Symbol is {word}")
                    return 1, token_list, lexemes, lex_count
            token_list.append(cur_tokens)
            lexemes.append(cur_lexemes)
            lex_count.append(cur_count)

        return token_list, lexemes, lex_count


class ShoeSyntaxAnalyzer:
    def __init__(self, tokens, lexemes):
        self.tokens = tokens
        self.lexemes = lexemes

    def syntax_analyzer(self):
        pass


my_file = ShoeFileManager("test.txt")
word_matrix = my_file.get_word_matrix()
print(word_matrix)
Tokenizer = ShoeTokenizer(word_matrix)
tokens, lexemes, lex_count = Tokenizer.tokenize()
