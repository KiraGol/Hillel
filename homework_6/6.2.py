from typing import Tuple, Union


def square(side_of_square: int) -> Tuple[int, int, Union[int, float]]:
    p = 4 * side_of_square
    s = side_of_square ** 2
    d = side_of_square * (2 ** 0.5)
    answer = (p, s, d)
    return answer


print(square(4))
