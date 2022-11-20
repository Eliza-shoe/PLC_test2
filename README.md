
# PLC_test2
# Shoe Lang
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

## Test Files
 test_fail_syntax.txt has 5 syntax errors. The beginning and end of the program do not start with "start" and "end" so the syntax analyzer does not analyze it correctly in the start() or end() functions of ShoeParser(). In the statement 'shoelace ( Eliza <= HiWorld ) { Eliza = Eliza + 2 } ;', HiWorld has not been assigned value, so this cannot be resolved. In the next line, a variable cannot be assigned value using a fits statement. The last statement does not end in a semicolon. / 

   test_fail_lexical.txt has 5 lexical errors. The variable name Hi0World does not conform to the pattern "^[A-Za-z_]{5,7}" since it includes a digit, so the lexical analyzer does not encode it correctly as a variable. In "Loafer Eliza;", Loafer is capitalized and thus is also not encoded correctly. In the statement "shoelace ( Eliza =< 10 ) { Eliza = Eliza + 2 } ;", "=<" is not a valid operator. In "Hi0World = 2 ^ 3;" there is no ^ symbol in Shoe Lang. hello_world in "sandal hello_world;" also does not conform to "^[A-Za-z_]{5,7}" since it is too long. 

 
  

