def max_joltage_digit(battery_bank, digits_remaining, from_index):
    end_index = -digits_remaining + 1
    subsection = battery_bank[from_index:] if end_index == 0 else battery_bank[from_index:end_index]
    return max(subsection)

# Main execution block
if __name__ == "__main__":
    joltage = 0
    joltage_digits = 12
    with open('./assets/input-3.txt', 'r') as f:
        for line in f:
            # Parse our input line.
            line = line.strip("\n")
            batteries = list(map(int, line))
            bank_joltage = []
            from_index = 0
            for i in range(joltage_digits):
                max_digit = max_joltage_digit(batteries, joltage_digits - i, from_index)
                from_index = batteries.index(max_digit, from_index) + 1
                bank_joltage.append(max_digit)
            joltage += int(''.join(str(n) for n in bank_joltage))

    print('Total joltage: ', joltage)

