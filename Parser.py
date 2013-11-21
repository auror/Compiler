NT=['N_START','N_main','N_otherFunctions','N_otherFunctions1','N_dataType','N_parameterslist','N_parameterslist1',
'N_end','N_declaration','N_variable','N_variableList','N_statement','N_statement2','N_statement1','N_statement3','N_returnStatement','N_arithmetic', 'N_arithmetic1','N_relational','N_iterative','N_conditional','N_else','N_functionCall','N_functionCall1','N_arglist','N_arglist1','N_assignment','			N_assignment1','N_literal','N_arithmeticOp','N_arithmeticOp1','N_relationalOp']

T=['TK_L','TK_G','TK_LE','TK_GE','TK_NEQ','TK_EQQ','TK_MOD','TK_MINUS','TK_PLUS','TK_MUL','TK_DIV','TK_STRINGLIT','TK_DOUBLELIT','TK_CHARLIT','TK_INTLIT', 'TK_EQT','TK_COMMA','TK_IDENTIFIER','TK_RBRAC','TK_LBRAC','TK_COLON','TK_ELSE','TK_IF','TK_SEM','TK_FOR','TK_WHILE','TK_RETURN','TK_SQR','TK_VALUE','TK_SQL', 'TK_ENDPROGRAM','TK_ENDLOOP','TK_VOID','TK_STRING','TK_DOUBLE','TK_INT','TK_CHAR','TK_MAIN']


#sym=list(enumerate(ls1,start=-1))

#dic_grammar={1:[N_main,N_otherFunctions].reverse(),2:[TK_MAIN,TKCOLON,N_statement,N_end].reverse(),3:[N_dataType,TK_IDENTIFIER,TK_LBRAC,N_otherFunctions].reverse(),4:[N_parameterslist,TK_RBRAC,TK_COLON,N_statement,N_end].reverse(),5:[+RBRAC,+COLON,N_statement,N_end].reverse(),6:[TK_CHAR],7:[TK_INT],8:[TK_DOUBLE],9:[TK_STRING],10:[TK_VOID],11:TK_IDENTIFIER,N_variable,N_parameterslist'],
f = open('Rules.txt', 'r')
ls = [line.strip('\n').split(' ') for line in f.readlines()]

p=[[-1]*38 for _ in xrange(31)]
p[0][37]=1
p[1][37]=2
p[2][32]=3
p[2][33]=3
p[2][34]=3
p[2][35]=3
p[2][36]=3
p[3][17]=4
p[3][18]=5
p[4][32]=10
p[4][33]=9
p[4][34]=8
p[4][35]=7
p[4][36]=6
p[5][17]=11
p[6][16]=12
p[6][18]=13
p[7][30]=15
p[7][31]=14
p[8][20]=16
p[9][20]=17
p[10][16]=19
p[10][18]=19
p[10][23]=19
p[10][29]=18
p[11][0]=21
p[11][1]=21
p[11][2]=21
p[11][3]=21
p[11][4]=21
p[11][5]=21
p[11][6]=21
p[11][7]=21
p[11][8]=21
p[11][9]=21
p[11][10]=21
p[11][17]=26
p[11][22]=25
p[11][24]=22
p[11][25]=22
p[11][26]=23
p[11][30]=24
p[11][31]=24
p[12][11]=28
p[12][12]=28
p[12][13]=28
p[12][14]=28
p[12][15]=28
p[12][19]=27
p[12][20]=29
p[13][23]=30
p[14][0]=31
p[14][1]=31
p[14][2]=31
p[14][3]=31
p[14][4]=31
p[14][5]=31
p[14][6]=31
p[14][7]=31
p[14][8]=31
p[14][9]=31
p[14][10]=31
p[14][17]=31
p[14][22]=31
p[14][24]=31
p[14][25]=31
p[14][26]=31
p[14][30]=31
p[14][31]=31
p[14][23]=32
p[15][26]=33
p[16][6]=34
p[16][7]=34
p[16][8]=34
p[16][9]=34
p[16][10]=34
p[17][6]=35
p[17][7]=35
p[17][8]=35
p[17][9]=35
p[17][10]=35
p[17][17]=36
p[18][0]=37
p[18][1]=37
p[18][2]=37
p[18][3]=37
p[18][4]=37
p[18][5]=37
p[19][24]=39
p[19][25]=38
p[20][22]=40
p[21][21]=41
p[21][23]=42
p[22][19]=43
p[23][17]=44
p[23][18]=45
p[24][17]=46
p[25][16]=47
p[25][18]=48
p[26][11]=50
p[26][12]=50
p[26][13]=50
p[26][14]=50
p[26][15]=49
p[27][6]=51
p[27][7]=51
p[27][8]=51
p[27][9]=51
p[27][10]=51
p[27][19]=52
p[28][11]=56
p[28][12]=55
p[28][13]=54
p[28][14]=53
p[29][6]=61
p[29][7]=60
p[29][8]=59
p[29][9]=58
p[29][10]=57
p[30][0]=67
p[30][1]=66
p[30][2]=65
p[30][3]=64
p[30][4]=63
p[30][5]=62

def parser(tokens):
	stack=['$']
	stack.append(tokens[0])
	i=0
	k=''
	while (1):
		if(stack[len(stack)-1]=='$' and len(tokens)==0):
			print 'parsing successful'
			break
		elif(stack[len(stack)-1]!='$' and len(tokens)==0):
			print 'error'
			break
		elif(stack[len(stack)-1] in T):
			if(p[i][T.index(stack[len(stack)-1])]>=1 and p[i][T.index(stack[len(stack)-1])]<=67):
				stack.pop()
				tokens.pop()
			else:
				print 'error'
				break
		elif(stack[len(stack)-1] in NT):
			j=NT.index(stack.pop()) 
			ls[p[i][j]-1].reverse()
			for a in range(len(ls[p[i][j]-1])-1):
				stack.append(ls[p[i][j]-1][a])
			ls[p[i][j]-1].reverse()
			k=ls[p[i][j]-1][0]
			i=NT.index(k)

f = open('Tokens.txt','r')
tokens = f.read()
tokens = tokens.split(' ')
f.close()
parser(tokens)
