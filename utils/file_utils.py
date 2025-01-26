def read_input() -> list[str]:
    lines: list[str] = []
    with open("input.txt") as file:
        input_lines = file.readlines()
        for line in input_lines:
            lines.append(line)

    return lines