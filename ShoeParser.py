from os import curdir
from ShoeLexer import *
from ToLinkedList import *


class ShoeParser:
    def __init__(self, variables={}):
        self.variables = variables

    def to_lexer(self):
        # send to lexer with all test files
        files = [
            "test.txt",
            "test2.txt",
            "test_fail_syntax.txt",
            "test_fail_lexical.txt",
        ]
        for f in files:
            my_file = ShoeFileManager(f)
            self.to_linked_list()

    def to_linked_list(self):
        # convert to consolidated nodes
        LL = LinkedLexer(lexemes, tokens)
        linked_nodes = LL.link()
        return linked_nodes

    def parse(self):
        # main function for parsing
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
        if cur.token == 29:
            cur = cur.next
            self.stmt(cur)
            self.end(cur)
        else:
            print("Syntax Error: File must begin with 'start' ")

    def stmt(self, cur):
        self.stmt_type(cur)

    def stmt_type(self, cur):
        if cur.token in range(6, 10):
            current = current.next
            self.as_stmt(cur)
        elif cur.token == 5:
            current = current.next
            self.shoelace(cur)
        elif cur.token == 3:
            current = current.next
            self.fits(cur)
        elif cur.token == 2 or cur.token == 18:
            current = current.next
            self.expr(cur)

    def as_stmt(self, cur):
        # <as_stmt> -> <type> <var_name> = <expr>
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
        """<type> -> sandal
        <type> -> loafer
        <type> -> cowboy
        <type> -> wellington"""
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
            variable_flag = 1
            v_to_update = self.variables[cur.lexeme]
            value = int(self.variables[cur.lexeme][1])
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

        if variable_flag == 1:
            self.variables[1] = value
            return
        return value

    def fits(self, cur):
        # <if_stmt> -> fits ( <bool_expr> ) <block_stmt>
        cur = cur.next
        if cur.token != 18:
            print(
                "Syntax Error! Boolean statements in a fits statement should be enclosed in parantheses"
            )
            quit
        else:
            cur = cur.next
            boo = self.bool_expr(cur)
            if boo == True & cur.next.token == 19 & cur.next.next.token == 10:
                cur = cur.next.next
                self.block_expr(cur)

    def bool_expr(self, cur):
        # <bool_expr> -> <var_name> == int_lit
        flag = False
        if cur.token != 1:
            print("Syntax error: A boolean expression must start with a variable.")
            quit
        else:
            value = int(self.variables[cur.lexeme][1])
            if cur.next.next != 2:
                print(
                    "Syntax error: A boolean expression can only be compared with a literal."
                )
                quit
            compare_val = int(cur.next.next.lexeme)
            cur = cur.next
            if cur.token == 20 & (value < compare_val):
                flag = True
            elif cur.token == 21 & (value > compare_val):
                flag = True
            elif cur.token == 22 & (value <= compare_val):
                flag = True
            elif cur.token == 23 & (value >= compare_val):
                flag = True
            elif cur.token == 24 & (value == compare_val):
                flag = True
            elif cur.token == 25 & (value != compare_val):
                flag = True
        return flag

    def shoelace(self, cur):
        # <loop> ->  shoelace ( <bool_expr> ) <block_stmt>
        cur = cur.next
        if cur.token != 18:
            print(
                "Syntax Error! Boolean statements in a fits statement should be enclosed in parantheses"
            )
            quit
        else:
            cur = cur.next
            boo = self.bool_expr(cur)
            if boo == True & cur.next.token == 19 & cur.next.next.token == 10:
                cur = cur.next.next
                self.block_expr(cur)

    def lace_loop(self, cur):

        cur = cur.next
        boo = self.bool_expr(cur)
        if boo == True:
            cur = cur.next.next
            self.block_expr(cur)
            self.lace_loop(cur)
        else:
            return

    def block_expr(self, cur):
        # <block_stmt> -> { <stmt> }
        cur = cur.next
        self.expr(cur)

    def end(self, cur):
        if cur.token != 30:
            print("SyntaxError, file must end with end statement")


parser = ShoeParser()
parser.to_lexer()
