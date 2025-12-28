def find_adjacent(rows, row, col):
    num_adjacent = 0
    for delta_x in range(-1, 2):
        for delta_y in range(-1, 2):
            if delta_x == 0 and delta_y == 0:
                continue
            check_x = row + delta_x
            check_y = col + delta_y
            if check_x < 0 or check_y < 0:
                continue
            if check_x >= len(rows[0]) or check_y >= len(rows):
                continue
            if rows[check_x][check_y] == '@':
                num_adjacent += 1
    return num_adjacent

# Main execution block
if __name__ == "__main__":
    with open('./assets/input-4.txt', 'r') as f:
        rows = []
        for line in f:
            # Parse our input line.
            line = line.strip("\n")
            columns = list(map(str, line))
            rows.append(columns)
        num_accessible_paper = 0
        for index_row, row in enumerate(rows):
            for index_column, column in enumerate(row):
                if rows[index_row][index_column] != '@':
                    continue
                num_adjacent = find_adjacent(rows, index_row, index_column)
                if num_adjacent < 4:
                    num_accessible_paper += 1
    print('Num accessible paper:', num_accessible_paper)