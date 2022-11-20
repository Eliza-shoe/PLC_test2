
# PLC_test2
## This language, in honor of my last name, shall be shoe-based.

## Question A

### Variable names
1: Regex: ^[A-Z|a-z][A-Z|a-z|_]{5,7}\

### Digits
2: [0-9]*\
  #### In Parser
  sandal: 0*[0-16]\
  loafer: 0*[0-255]\
  cowboy: 0*[0-4294967295]\
  wellington: [0-9]* (it's too big, sue me)\


### Special Words
5: Regex: shoelace (loop)\
3: Regex: fits? (if)\
4: Regex: wearit? (else)\
6: Regex: sandal (1 byte int)\
7: Regex: loafer (2 byte int)\
8: Regex: cowboy (4 byte int)\
9: Regex: wellington (8 byte int)\

### Symbols 
"{": 10,  # right curly brace, used for differentiation\
"}": 11,  # left curly brace, used for differentiation\
"=": 12,  # variable declaration | equals\
"+": 13,  # addition\
"-": 14,  # subtraction\
"*": 15,  # multiplication\
"/": 16,  # division\
"%": 17,  # modulo\
"(": 18,  # right parenthesis, for precedence setting\
")": 19,  # left parenthesis, for precedence setting\
"<": 20,  # less than\
">": 21,  # greater than\
"<=": 22,  # less than or equal to\
">=": 23,  # greater than or equal to\
"==": 24,  # is equal to\
"!=": 25,  # is not equal to\
"'": 26,  # quotation\
";": 28,  # semicolon, used to denote end of like\
"illegal": 99\

## Question 2

### Precedence 

POMADS

Paranthesis\
mOdulo\
Multiplication\
Addition\
Division\
Subtraction\

S --> S - S\
S --> S / S\
S --> S + S\
S --> S * S\
S --> digit\
S --> (S)\

## Rules

### Lexical: 
Variable names must follow the pattern: ^[A-Z|a-z][A-Z|a-z|_]{5,7}
Digits must follow patten: [0-9]*

#### Syntactic 
<start> -> start; <stmt> end;/
<stmt> -> <stmt_type>/
<stmt_type> -> <as_stmt> ;/
<stmt_type> -> <block_stmt> ;/
<as_stmt> -> <type> <var_name> = <expr>/
<type> -> sandal/
<type> -> loafer/
<type> -> cowboy/
<type> -> wellington/
<var> -> int_lit/
<expr> -> <var>/
<expr> -> <var> * <var>/
<expr> -> <var> + <var>/
<expr> -> <var> \ <var>/
<expr> -> <var> - <var>/
<var_name> -> char var_char var_char var_char var_char/
<var_name> -> char var_char var_char var_char var_char var_char/
<var_name> -> char var_char var_char var_char var_char var_char/

var_char -> _/
var_char -> char/

char -> cap_char/
char -> lower_char/

cap_char -> A/

lower_char -> a/

int_lit-> 0/
int_lit-> 1/
int_lit-> 2/
int_lit-> 3/
int_lit-> 4/
int_lit-> 5/
int_lit-> 6/
int_lit-> 7/
int_lit-> 8/
int_lit-> 9/

<block_stmt> -> { <stmt> }/


