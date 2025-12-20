# Main execution block
if __name__ == "__main__":
    joltage = 0
    with open('./assets/input-3.txt', 'r') as f:
        for line in f:
            # Parse our input line.
            line = line.strip("\n")
            batteries = list(map(int ,line))
            firstBattery = max(batteries[:-1])
            firstBatteryIndex = batteries.index(firstBattery)
            secondBattery = max(batteries[firstBatteryIndex + 1:])
            bankJoltage = int(str(firstBattery) + str(secondBattery))
            joltage += bankJoltage
    print('Total joltage: ', joltage)