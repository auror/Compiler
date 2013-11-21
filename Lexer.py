import sys
import re

def lex(characters):
	
	token_exprs = [
		(r'[ \n\t]+',              None),
		(r'\=',                    'TK_EQT'),
		(r'\(',                    'TK_LBRAC'),
		(r'\)',                    'TK_RBRAC'),
		(r'\[',                    'TK_SQL'),
		(r'\]',                    'TK_SQR'),
		(r';',                     'TK_SEM'),
		(r'\+',                    'TK_PLUS'),
		(r'-',                     'TK_MINUS'),
		(r'\*',                    'TK_MUL'),
		(r'/',                     'TK_DIV'),
		(r'<',                     'TK_L'),
		(r'<=',                    'TK_LE'),
		(r'>',                     'TK_G'),
		(r'>=',                    'TK_GE'),
		#(r'=',                     'TK_EQT'),
		(r'=/=',                   'TK_NEQ'),
		(r'\:',                    'TK_COLON'),
		(r'\,',                    'TK_COMMA'),
		(r'\$MAIN',				   'TK_MAIN'),
		(r'char',                  'TK_CHAR'),
		(r'int',                   'TK_INT'),
		(r'double',                'TK_DOUBLE'),
		(r'string',                'TK_STRING'),
		(r'void',                  'TK_VOID'),
		(r'for',                   'TK_FOR'),
		(r'while',                 'TK_WHILE'),
		(r'return',                'TK_RETURN'),
		(r'EndLoop',               'TK_ENDLOOP'),
		(r'EndProgram',            'TK_END'),
		(r'[0-9]+',                'TK_INTV'),
		(r'[0-9]+\.?[0-9]+',        'TK_DOUBLEV'),
		(r'\"[A-Za-z0-9_]*\"',	   'TK_STRINGV'),
		(r'\'[A-Za-z0-9_]\'',	   'TK_CHARV'),
		(r'[A-Za-z][A-Za-z0-9_]*', 'TK_IDENTIFIER'),
]
	pos = 0
	tokens = []
	while pos < len(characters):
		match = None
		for token_expr in token_exprs:
			pattern, tag = token_expr
			regex = re.compile(pattern)
			match = regex.match(characters, pos)
			if match:
				text = match.group(0)
				if tag:
					token = tag
					tokens.append(token)
				break
		if not match:
			sys.stderr.write('Illegal character: %s\n' % characters[pos])
			sys.exit(1)
		else:
			pos = match.end(0)
	return tokens

f = open('Code.txt','r')
c = f.read()
f.close()
f = open('Tokens.txt','w')
f.write(' '.join(x for x in lex(c)))
f.close()
    
    
