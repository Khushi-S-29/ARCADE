import os

class Piece:
    def __init__(self, name, color, value, position=None, texture=None, texture_rect=None):
        self.name = name
        self.color = color
        value_sign = 1 if color == 'white' else -1
        self.value = value * value_sign
        self.moves = []
        self.moved = False
        self.texture = texture
        self.set_texture()
        self.texture_rect = texture_rect
        self.position = position  

    def set_texture(self, size=80):
        self.texture = os.path.join(
            rf'C:\Users\ADMIN\OneDrive\Documents\GAMES\CHESS\assets\images\imgs-{size}px/{self.color}_{self.name}.png')

    def add_move(self, move):
        self.moves.append(move)

    def clear_moves(self):
        self.moves = []

    def valid_moves(self):
        if self.position is None:
            raise ValueError("Piece position is not set.")
        row, col = self.position
        return []  


class Pawn(Piece):
    def __init__(self, color, position=None):
        self.dir = -1 if color == 'white' else 1
        self.en_passant = False
        super().__init__('pawn', color, 1.0, position)

    def valid_moves(self):
        """Calculate valid moves for the pawn."""
        if self.position is None:
            return []
        valid_moves = []
        row, col = self.position

        if 0 <= row + self.dir < 8:
            valid_moves.append((row + self.dir, col))

        if (self.dir == -1 and row == 6) or (self.dir == 1 and row == 1):
            if 0 <= row + 2 * self.dir < 8:
                valid_moves.append((row + 2 * self.dir, col))

        return valid_moves


class Knight(Piece):
    def __init__(self, color, position=None):
        super().__init__('knight', color, 3.0, position)

    def valid_moves(self):
        """Calculate valid moves for the knight."""
        if self.position is None:
            return []
        valid_moves = []
        row, col = self.position
        knight_moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]

        for r, c in knight_moves:
            if 0 <= r < 8 and 0 <= c < 8:
                valid_moves.append((r, c))

        return valid_moves


class Bishop(Piece):
    def __init__(self, color, position=None):
        super().__init__('bishop', color, 3.001, position)

    def valid_moves(self):
        """Calculate valid moves for the bishop."""
        if self.position is None:
            return []
        valid_moves = []
        row, col = self.position

        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                valid_moves.append((r, c))
                r += dr
                c += dc

        return valid_moves


class Rook(Piece):
    def __init__(self, color, position=None):
        super().__init__('rook', color, 5.0, position)

    def valid_moves(self):
        """Calculate valid moves for the rook."""
        if self.position is None:
            return []
        valid_moves = []
        row, col = self.position

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                valid_moves.append((r, c))
                r += dr
                c += dc

        return valid_moves


class Queen(Piece):
    def __init__(self, color, position=None):
        super().__init__('queen', color, 9.0, position)

    def valid_moves(self):
        """Calculate valid moves for the queen."""
        if self.position is None:
            return []
        valid_moves = []
        row, col = self.position

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            while 0 <= r < 8 and 0 <= c < 8:
                valid_moves.append((r, c))
                r += dr
                c += dc

        return valid_moves


class King(Piece):
    def __init__(self, color, position=None):
        self.left_rook = None
        self.right_rook = None
        super().__init__('king', color, 10000.0, position)

    def valid_moves(self):
        if self.position is None:
            return []
        valid_moves = []
        row, col = self.position

        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 8 and 0 <= c < 8:
                valid_moves.append((r, c))

        return valid_moves