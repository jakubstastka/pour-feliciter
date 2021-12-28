import datetime
import random


def wish_happy_new_year(wisher=None):
    this_year = datetime.date.today().year
    next_year = this_year + 1

    if (
            datetime.date(year=this_year, month=12, day=1)
            < datetime.date.today()
            < datetime.date(year=this_year, month=12, day=31)
    ):

        messages = [
            f"Happy New Year {next_year}!",
            f"Pour Felicitér {next_year}!",
            f"Best Wishes for {next_year}!",
            f"gl&hf in {next_year}!",
            f"Happy another revolution around "
            f"the sun designated as {next_year}!"
        ]

        suffix = f" From {wisher}" if wisher else ""

        return random.choice(messages) + suffix

    else:
        return "Too early for that, no?"


if __name__ == '__main__':
    wish_happy_new_year("Jakub Stastka")
