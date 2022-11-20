from os import curdir
from ShoeLexer import *
from ToLinkedList import *


class ShoeParser:
    def __init__(self, variables={}):
        self.variables = variables

    def to_linked_list(self, lexemes, tokens):
        linked_nodes = LinkedLexer.link()
        return linked_nodes

    def parse(self):
        linked_nodes = self.to_linked_list()
        variables = {}
        for i in range(len(linked_nodes)):
            cur = linked_nodes[i]
            cur = linked_nodes[i].token
            self.initial(cur)

    def initial(self, cur):
        self.start(cur)
        self.end(cur)

    def start(self, cur):
        if current.token == 29:
            current = cur.next
            self.stmt()
        else:
            print("Syntax Error: File must begin with 'start' ")

    def stmt(self, cur):
        self.stmt_type()

    def stmt_type(self, cur):
        if cur.token in range(6, 10):
            current = current.next
            self.as_stmt()
        elif cur.token == 5:
            current = current.next
            self.shoelace()
        elif cur.token == 3:
            current = current.next
            self.fits(cur)
        elif cur.token == 2 or cur.token == 18:
            current = current.next
            self.expr(cur)

    def as_stmt(self, cur):
        what_type = self.int_type(cur)
        cur = cur.next
        what_name = self.var_name(cur)
        if cur.next.token == 12:
            cur = cur.next.next
        else:
            print("SyntaxError: invalid assignment")
            quit
        what_value = self.expr(cur)
        self.variables[what_name] = [what_type, what_value]

    def int_type(self, cur):
        if cur.token == 6:
            return "sandal"
        if cur.token == 7:
            return "loafer"
        if cur.token == 8:
            return "cowboy"
        if cur.token == 9:
            return "wellington"

    def var_name(self, cur):
        if re.match("^[A-Za-z_]{5,7}", cur.lexeme):
            return cur.lexeme
        else:
            print("syntactic error! Variable name invalid")
            quit

    def expr(self, cur):
        """
        POMADS precedence ( O = Modulo)
        <expr> -> <var>
        <expr> -> ( <var> )
        <expr> -> <var> * <var>
        <expr> -> <var> + <var>
        <expr> -> <var> \ <var>
        <expr> -> <var> - <var>
        """
        value = 0
        variable_flag = 0
        if cur.token == 1:
            value = self.variables[cur.lexeme][1]
        if cur.token == 2:
            value = int(cur.lexeme)
        if cur.next == None:
            value = int(cur.lexeme)
        elif cur.token == 19:
            return
        elif cur.token == 18:
            cur = cur.next
            self.expr(cur)
        elif cur.next.token == 17:
            if cur.next.next.token == 2:
                value %= int(cur.next.next.lexeme)
        elif cur.next.token == 15:
            if cur.next.next.token == 2:
                value *= int(cur.next.next.lexeme)
        elif cur.next.token == 13:
            if cur.next.next.token == 2:
                value += int(cur.next.next.lexeme)
        elif cur.next.token == 16:
            if cur.next.next.token == 2:
                value /= int(cur.next.next.lexeme)
        elif cur.next.token == 14:
            if cur.next.next.token == 2:
                value -= int(cur.next.next.lexeme)
        else:
            print("syntactic error! Expression invalid")
            quit
        return value

    def fits(self, cur):
        cur = cur.next
        if cur.token != 18:
            print(
                "Syntax Error! Boolean statements in a fits statement should be enclosed in parantheses"
            )
            quit
        else:
            cur = cur.next
            boo = self.bool_expr()
            if boo == True & cur.next.token == 19 & cur.next.next.token == 10:
                cur = cur.next.next
                self.block_expr()

    def bool_expr(self, cur):
        pass

    def block_expr(self, cur):
        cur = cur.next
        self.expr()
