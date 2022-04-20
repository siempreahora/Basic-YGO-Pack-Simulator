from time import sleep
import sys, os


def rpg_choices(*arg):
    """Takes an *arg list of inputs, asks for an integer input between 1 and the last arg input, and returns that integer."""
    tracker = []
    incre = 1
    for _ in arg:
        tracker.append(incre)
        incre += 1

    while True:
        print()
        incre = 0
        for x in tracker:
            print(f"[{x}] {arg[incre]}")
            incre += 1
        print()

        chosen_choice = input(f"(Input a number from [1]-[{len(tracker)}]): ")

        try:
            chosen_choice = int(chosen_choice)
        except ValueError:
            rpg_speak("(Invalid input, try again)")
            sleep(0.4)
        else:
            if chosen_choice in tracker:
                return chosen_choice
            else:
                rpg_speak("(Invalid input, try again)")
                sleep(0.4)


def rpg_speak(text_to_print, text_speed=0.035, peri_speed=0.4, voice=None):
    if voice != None:
        print(f"{voice}: ", end='')

    for letter in text_to_print:
        sys.stdout.write(letter)
        sys.stdout.flush()
        if letter == ".":
            sleep(peri_speed)
        elif letter in [",", "!", "?"]:
            sleep(0.35)
        else:
            sleep(text_speed)
    sleep(0.25)
    print()


def osClear():
    os.system('clear' if os.name == 'posix' else 'cls')





