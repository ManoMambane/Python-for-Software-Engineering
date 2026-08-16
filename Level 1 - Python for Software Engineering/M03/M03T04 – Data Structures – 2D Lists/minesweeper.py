def count_adjacent_mines(grid, row, col):
    """
    Helper function to count mines (#) around a specific grid cell (row, col).
    Checks all 8 adjacent directions (N, S, E, W, NW, NE, SW, SE).
    """
    rows = len(grid)
    cols = len(grid[0])
    mine_count = 0

    # Offsets for all 8 neighboring positions
    directions = [
        (-1, -1), (-1, 0), (-1, 1), # NW, N, NE
        (0, -1),           (0, 1),  # W,     E
        (1, -1),  (1, 0),  (1, 1)   # SW, S, SE
    ]

    for r_offset, c_offset in directions:
        adj_row = row + r_offset
        adj_col = col + c_offset

        # Ensure adjacent indices stay within valid grid bounds
        if 0 <= adj_row < rows and 0 <= adj_col < cols:
            if grid[adj_row][adj_col] == "#":
                mine_count += 1

    return mine_count


def minesweeper(grid):
    """
    Processes a grid of '#' and '-' and returns a grid where each '-'
    is replaced by the count of adjacent mines.
    """
    rows = len(grid)
    cols = len(grid[0])

    # Create a new grid structure to store the results
    result_grid = []

    for r in range(rows):
        new_row = []
        for c in range(cols):
            # Keep mines as '#'
            if grid[r][c] == "#":
                new_row.append("#")
            # Calculate adjacent mines for mine-free spots '-'
            else:
                mines = count_adjacent_mines(grid, r, c)
                new_row.append(str(mines))
        result_grid.append(new_row)

    return result_grid


# Example usage / testing
if __name__ == "__main__":
    test_grid = [
        ["-", "-", "-", "#", "#"],
        ["-", "#", "-", "-", "-"],
        ["-", "-", "#", "-", "-"],
        ["-", "#", "#", "-", "-"],
        ["-", "-", "-", "-", "-"]
    ]

    result = minesweeper(test_grid)
    for row in result:
        print(row)