import re
from ShoeLexer import *


class Node:
    def __init__(self, token, lexeme):
        self.token = token
        self.lexeme = lexeme
        self.next = None


class LinkedList:
    """Form Linked List from Nodes"""

    def __init__(self, tokens, lexemes):
        self.head = Node(tokens[0], lexemes[0])
        current = self.head
        for l in range(1, (len(lexemes))):
            if len(lexemes[l]) != 0:
                current.next = Node(token=tokens[l], lexeme=lexemes[l])
                current = current.next


class LinkedLexer:
    def __init__(self, tokens, lexemes):
        self.tokens = tokens
        self.lexemes = lexemes

    def link(self):
        """Converts list to linked list"""
        Tokenizer = ShoeTokenizer(word_matrix)
        tokens, lexemes, _ = Tokenizer.tokenize()
        linked_lines = []

        for i in range(len(tokens)):
            if len(tokens[i]) != 0:
                linked = LinkedList(tokens=tokens[i], lexemes=lexemes[i])
            linked_lines.append(linked)

        return linked_lines


tokens, lexemes, lex_count = Tokenizer.tokenize()
LL = LinkedLexer(tokens, lexemes)
linked_lines = LL.link()
for L in linked_lines:
    current = L.head
    while current is not None:
        print(current.lexeme)

        current = current.next
