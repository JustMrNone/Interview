class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # (x, y)
        coordinates = [0, 0]

        move_map = {
            'U': (0, 1),  # Up increases y
            'D': (0, -1), # Down decreases y
            'L': (-1, 0), # Left decreases x
            'R': (1, 0)   # Right increases x
        }

        # Update the coordinates based on the moves
        for move in moves:
            dx, dy = move_map[move]
            coordinates[0] += dx
            coordinates[1] += dy

        # Check if the robot is back at the origin
        return coordinates == [0, 0]