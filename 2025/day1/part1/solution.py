def main():
    total = 0
    curr = 50

    def rotateRight(times):
        nonlocal curr
        nonlocal total
        actual = times % 100
        curr += actual
        curr = curr % 100
        if curr == 0:
            total += 1

    def rotateLeft(times):
        nonlocal curr
        nonlocal total
        actual = times % 100
        if actual > curr:
            curr = 100 - actual + curr
        else:
            curr -= actual

        if curr == 0:
            total += 1

    with open("input.txt", "r") as file:
        line = file.readline()
        while line:
            dir = line[0]
            num = int(line[1:])

            if dir == "R":
                rotateRight(num)
            else:
                rotateLeft(num)

            line = file.readline()  # Read next line

    print(total)


main()
