import re

# Main execution block
if __name__ == "__main__":
    with open('./assets/input-2.txt', 'r') as f:
        content = f.read()
        ranges = content.split(',')
        total = 0
        for r in ranges:
            matches = re.match(r'^(\d+)-(\d+)$', r)
            start, end = matches.groups()
            numbers = range(int(start), int(end) + 1)
            for n in numbers:
                if re.match(r'^(\d+?)(\1+)$', str(n)):
                    total += n
        print('Total:', total)