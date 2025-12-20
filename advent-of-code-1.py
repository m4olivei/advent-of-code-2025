import re
from math import floor

# Main execution block
if __name__ == "__main__":
    currentPosition = 50
    numZeros = 0
    with open('./assets/input-1.txt', 'r') as f:
        for line in f:
            # Parse our input line.
            line = line.strip("\n")
            m = re.match(r"^([RL])(\d+)", line)
            direction, distance = m.groups()
            distance = int(distance)

            # A full rotation of the dial by definition passes zero once per
            # rotation.
            fullRotations = floor(distance / 100)
            numZeros += fullRotations

            # After full rotations, we have the remainder left to go.
            distance = distance % 100
            # Left will move out current position in the negative direction.
            if direction == "L":
                distance = distance * -1
            newPosition = currentPosition + distance
            # If we land right on zero, we count it as a new zero. Exclude the
            # case where we're starting at zero. Full rotations will have
            # already counted. Moves of 0 shouldn't count.
            if newPosition == 0 and currentPosition != 0:
                numZeros += 1
            elif newPosition < 0:
                # If we're moving from a current position of 0, we don't count
                # a new zero.
                if currentPosition != 0:
                    numZeros += 1
                newPosition = 100 + newPosition
            elif newPosition > 99:
                # If we're moving from a current position of 0, we don't count
                # a new zero.
                if currentPosition != 0:
                    numZeros += 1
                newPosition = newPosition - 100
            currentPosition = newPosition
            print('The dial is rotated', line, 'to point at', newPosition, 'Num zeros', numZeros)
    print('Num zeros:', numZeros)