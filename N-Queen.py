global N

N = 4;

global board
board = [[0 for i in range(N)] for j in range(N)];

global placement
placement = [-1 for i in range(N)]

def check(row, col):
	for prow in range(0,row):
		pcol = placement[prow];
        
		if(pcol == col or abs(prow - row) == abs(pcol - col)):
			return 0;
	return 1;

def nQueen(n):
	if(n==N):
		for i in range(0,N):
			for j in range(0,N):
				print(board[i][j], end = " ")
			print("")
		print("")
		return

	for i in range(0,N):
		if(check(n,i)):
			placement[n]=i
			board[n][i]=1
			nQueen(n+1)
			board[n][i] = 0
			placement[n]=-1
	return

nQueen(0)
