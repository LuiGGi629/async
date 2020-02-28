from typing import List, Generator


# def fib(n: int) -> List[int]:
#     numbers = []
#     current, nxt = 0, 1
#     while len(numbers) < n:
#         current, nxt = nxt, current + nxt
#         numbers.append(current)
#
#     return numbers
#
#
# print(fib(10))


def fib() -> Generator[int, None, None]:
    current, nxt = 0, 1
    while True:
        current, nxt = nxt, current + nxt
        yield current


result = fib()

for n in result:
    print(n, end=', ')
    if n > 10000:
        break

print()
print('Done')
