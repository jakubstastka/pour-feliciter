import datetime
import random


def main():
    this_year = datetime.date.today().year
    next_year = datetime.date.today().year + 1

    if (
            datetime.date(year=this_year, month=12, day=1)
            < datetime.date.today()
            < datetime.date(year=this_year, month=12, day=31)
    ):

        messages = [
            f"Happy New Year {next_year}!",
            f"Pour Felicitér {next_year}!",
            f"Best Wishes for {next_year}!",
            f"gl hf in {next_year}!",
            f"Happy another revolution around the sun designated as {next_year}!"
        ]

        print(random.choice(messages))

    else:
        print("Too early for that, no?")


if __name__ == '__main__':
    main()
