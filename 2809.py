from datetime import date
from datetime import timedelta


def captain(lst, date):
    file = open('captain_notes.txt', 'a')
    for i in lst:
        file.write(str(date) + '\n')
        date += timedelta(days=1)
        file.write(i)
    file.close()


list = ["- first day on the boat.\n", "- second day is a little bit harder.\n",
        "- the third is going to be freezy.\n", "- I don't like the idea to go on that trip.\n"]
date_1 = date(1789, 2, 28)

captain(list, date_1)
