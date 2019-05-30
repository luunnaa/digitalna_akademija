def funkcija_godina(ime,god_rodjenja):
    now = datetime.datetime.now()
    ova_godina = now.year

    godine = ova_godina-god_rodjenja
    print(godine)

    print("Zdravo " + ime + " ti imas " + str(godine) + " godina!")

import datetime

funkcija_godina("Luna", 1998)
