import re

# Main execution block
if __name__ == "__main__":
    with open('./assets/input-5.txt', 'r') as f:
        num_fresh = 0
        ingredient_ranges = []
        for line in f:
            # Parse our input line.
            line = line.strip("\n")
            if matches := re.match(r'^(\d+)-(\d+)$', line):
                ingredient_ranges.append([int(matches.group(1)), int(matches.group(2))])
            elif matches := re.match(r'^(\d+)$', line):
                ingredient_id = int(matches.group(1))
                for ingredient_range in ingredient_ranges:
                    if (ingredient_id >= ingredient_range[0]) and (ingredient_id <= ingredient_range[1]):
                        num_fresh += 1
                        break
        print('Num fresh:', num_fresh)
