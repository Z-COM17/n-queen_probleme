class ChessBoard:

    def __init__(self, board_dimentions=1):
        self.board_dimentions = board_dimentions
        self.board = []
        
        for _ in range(self.board_dimentions):
            self.board.append(['*' for _ in range(self.board_dimentions)])

    def __str__(self):
        result = ''
        
        for line in self.board:
            prnt = ''
            for i in line:
                prnt += str(i) + '  '
            result += prnt + '\n'
        
        return str(result) 
    
class Pieces(ChessBoard):
    num_pieces = 0
    def __init__(self, piece):
        super().__init__(int(input('Enter the board dimentions: ')))    
        self.piece = piece
        self.moves = '+'
        self.posicion = self.find_empty_position()

    def __str__(self):
        return super().__str__() + f'\n{Pieces.num_pieces}'

    def find_empty_position(self):
        for x in range(len(self.board)):
            for y in range(self.board_dimentions):
                if self.board[x][y] == '*':
                    return x, y
          
    def add_piece(self, x=0, y=0):
        if x == 0 and y == 0:
            x, y = self.posicion
        if  self.piece == 'rook':
            self.board[x] = [self.moves for _ in range(self.board_dimentions)]
            for i in range(self.board_dimentions):
                self.board[i][y] = self.moves
            

        elif self.piece == 'horse':
            knight_moves = [(2, 1), (1, 2), (-1, 2), (-2, 1),(-2, -1), (-1, -2), (1, -2), (2, -1)]
            for dx, dy in knight_moves:
                if 0 <= x + dx < self.board_dimentions and 0 <= y + dy < self.board_dimentions:
                    self.board[x + dx][y + dy] = self.moves
                
        elif self.piece == 'pawn':
            if x + 1 < self.board_dimentions and y + 1 < self.board_dimentions:
                self.board[x+1][y+1] = self.moves
            if x + 1 < self.board_dimentions and 0 <= y - 1:
                self.board[x+1][y-1] = self.moves
        
        elif self.piece == 'bishop':
            bishop_moves = [(1, 1), (-1, 1),(-1, -1), (1, -1)]
            for dx, dy in bishop_moves:
                for i in range(1, self.board_dimentions+1):
                    if 0 <= x + dx*i < self.board_dimentions and 0 <= y + dy*i < self.board_dimentions:
                        self.board[x + dx*i][y + dy*i] = self.moves

        elif self.piece == 'queen':
            bishop_moves = [(1, 1), (-1, 1),(-1, -1), (1, -1)]
            for dx, dy in bishop_moves:
                for i in range(1, self.board_dimentions+1):
                    if 0 <= x + dx*i < self.board_dimentions and 0 <= y + dy*i < self.board_dimentions:
                        self.board[x + dx*i][y + dy*i] = self.moves
            self.board[x] = [self.moves for _ in range(self.board_dimentions)]
            for i in range(self.board_dimentions):
                self.board[i][y] = self.moves

        elif self.piece == 'knight':
            king_moves = [(1, 1), (1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, -1)]
            
            for dx, dy in king_moves:
                if 0 <= x + dx < self.board_dimentions and 0 <= y + dy < self.board_dimentions:
                    self.board[x + dx][y + dy] = self.moves
        else:
            return None



        self.board[x][y] = '0'
        self.posicion = self.find_empty_position()
        Pieces.num_pieces += 1


    def add_max(self):
        while self.find_empty_position():
            self.add_piece()

    def max_posible(self):
        best_pieces_num = 0
        best_board = None
    
        for a in range(self.board_dimentions):
            for b in range(self.board_dimentions):
                self.board = [['*' for _ in range(self.board_dimentions)] for _ in range(self.board_dimentions)]
                Pieces.num_pieces = 0
                self.add_piece(a, b)
                if not self.add_piece:
                    return None
                self.add_max()
                if Pieces.num_pieces >= best_pieces_num:
                    best_board = self.board
                    best_pieces_num = Pieces.num_pieces
                    result = ''
        
                    for line in self.board:
                        prnt = ''
                        for i in line:
                            prnt += str(i) + '  '
                        result += prnt + '\n'
                    
                    print(str(result) + f'\n{Pieces.num_pieces}')
                    
        self.board = best_board
        Pieces.num_pieces = best_pieces_num


while True:
    experiment = Pieces(input('Enter the piece: '))
    experiment.max_posible()

    print(experiment)
    if input('Do you want to continue? (y/n): ') == 'n':
        break