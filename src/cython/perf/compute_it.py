import datetime
import math
import colorama


def main():
    do_math(1)

    t0 = datetime.datetime.now()

    do_math(num=3_000_000)

    dt = datetime.datetime.now() - t0
    print(colorama.Fore.WHITE + f"App exiting, total time: {dt.total_seconds():.2f} sec.", flush=True)


def do_math(start=0, num=10):
    pos = start
    k_sq = 1000 * 1000
    while pos < num:
        pos += 1
        math.sqrt((pos - k_sq)*(pos - k_sq))


if __name__ == '__main__':
    main()
