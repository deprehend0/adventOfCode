from utils.file_utils import read_input

def get_distance(left: int, right: int) -> int:
    return abs(left - right)



def to_int_lists(lines) -> tuple[list[int], list[int]]:
    left_int_list = []
    right_int_list = []
    for line in lines:
        left, right = line.split("   ")
        left_int_list.append(int(left))
        right_int_list.append(int(right))

    return left_int_list, right_int_list


def calculate_total_distance(left_list, right_list) -> int:
    total_distance = 0
    combined_lists = zip(left_list, right_list)
    for left, right in combined_lists:
        # print(get_distance(left, right))
        total_distance += get_distance(left, right)

    return total_distance


if __name__ == "__main__":
    lines = read_input()
    left_list, right_list = to_int_lists(lines)

    # Order lists smallest first
    left_list.sort()
    print(left_list)
    right_list.sort()
    print(right_list)

    # Get itemwise differences
    total_distance = calculate_total_distance(left_list, right_list)
    print(total_distance)