import time
import threading


def main():
    threads = [
        threading.Thread(target=greeter, args=("Szczepan", 10), daemon=True),
        threading.Thread(target=greeter, args=("Ilona", 5), daemon=True),
        threading.Thread(target=greeter, args=("Ewa", 2), daemon=True),
        threading.Thread(target=greeter, args=("Marek", 11), daemon=True),
    ]

    [t.start() for t in threads]

    print()
    print("This is other work.")
    print(41*41)
    print()

    [t.join(timeout=1) for t in threads]

    print("Done.")


def greeter(name: str, times: int):
    for n in range(0, times):
        print(f"{n}. Elo {name}")
        time.sleep(1)


if __name__ == '__main__':
    main()
