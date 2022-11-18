import re

# Eliza Schuh
# PLC Exam 2
# This language, in honor of my last name, shall be shoe-based.


class ShoeNode:
    """I'm essentially writing my lexer like a linked list"""

    def __init__(self, data):
        self.data = data
        self.next = None


class ShoeFile:
    def __init__(self, filepath):
        # constructor
        self.filepath = filepath
        self.words = 0

    def read_file_to_words(self):
        """Should take in txt file and count lexemes"""
        word_list = []
        with open(self.filepath, "r") as f:
            contents = f.read()
        words = contents.split(" ")
        words = [i for i in words if i]  # remove empty strings
        special_char = re.compile("[@_!#$%^&*()<>?/\|};{~:.]")

        for word in words:

            if special_char.search(word) != None:

                splitsies = special_char.split(word)

                splitsies = [j for j in splitsies if j]

                for spl in splitsies:
                    word_list.append(spl)

                specials = re.findall(special_char, word)

                for s in specials:
                    word_list.append(s)

            else:
                word_list.append(word)
        word_list = [item.strip() for item in word_list]
        word_list = [i for i in word_list if i]
        return word_list


class ShoeLexer:
    def __init__(self, word_list):
        self.word_list = word_list

    def define_tokens(self):
        """Defines tokens"""
        variable = re.compile("^[A-Z|a-z][A-Z|a-z|_]{5,7}")
        special_words = re.compile(
            "fits\?|wearit\?|shoelace|sandal|loafer|cowboy|wellington"
        )
        charmap = {
            # variables 1, digits 2
            "variable": 1,
            "digit": 2,
            "fits?": 3,  # if
            "wearit?": 4,  # else
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
            "illegal": 99,
        }
        return variable, special_words, charmap

    def tokenize(self):
        """Input is contents of given text file,
        output is list of integers encoding tokens"""
        variable, digit, special_words, charmap = self.define_tokens()
        token_list = []
        lexemes = []
        lex_count = 0

        for word in self.word_list:
            if re.match(special_words, word):  # check if lexeme is special word
                token_list.append(charmap[word])
                lex_count += 1
                lexemes.append(word)

            elif re.match(variable, word):  # check if lexeme could be varaible
                token_list.append(charmap["variable"])
                lex_count += 1
                lexemes.append(word)

            elif word.isnumeric():
                token_list.append(charmap["digit"])
                lex_count += 1
                lexemes.append(word)
            elif word in charmap.keys():
                token_list.append(charmap[word])
                lex_count += 1
                lexemes.append(word)
            else:
                token_list.append(charmap["illegal"])
                print("Lexical Error: invalid symbol detected")
                quit

        return token_list, lexemes, lex_count

    def check_syntax():
        return


my_file = ShoeFile("test.txt")
word_list = my_file.read_file_to_words()
print(word_list)
Lexer = ShoeLexer(word_list)
print(Lexer.tokenize())
