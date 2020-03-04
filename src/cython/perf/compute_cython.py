import datetime
import multiprocessing
import colorama
from threading import Thread
from math_core import do_math


def main():
    do_math(1)
    processor_count = multiprocessing.cpu_count()
    print(f"Doing math on {processor_count} cores.")

    threads = []
    for n in range(1, processor_count + 1):
        threads.append(Thread(target=do_math,
                              args=(3_000_000 * (n - 1) / processor_count,
                                    3_000_000 * n / processor_count), daemon=True))

    [t.start() for t in threads]

    t0 = datetime.datetime.now()

    [t.join() for t in threads]

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + f"Done in: {dt.total_seconds():.2f}"
                                f" sec. (factor: {1.22/dt.total_seconds():.2f}x)", flush=True)


# def do_math(start=0, num=10):
#     pos = start
#     k_sq = 1000 * 1000
#     while pos < num:
#         pos += 1
#         math.sqrt((pos - k_sq)*(pos - k_sq))


if __name__ == '__main__':
    main()
