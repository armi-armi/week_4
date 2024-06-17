
import random

def main():
    num_picks = int(input("How many quick picks? "))
    for _ in range(num_picks):
        quick_pick = generate_quick_pick()
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))

def generate_quick_pick():
    return random.sample(range(1, 46), 6)

if __name__ == "__main__":
    main()
