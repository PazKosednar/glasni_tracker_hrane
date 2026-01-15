import speech_recognition as sr

seznam_zivil = {
    "toast": {
        "kcal": 61,
        "beljakovine": 2.3,
        "ogljikovi_hidrati": 11.4,
        "maščobe": 1.0
    },
    "jajca": {
        "kcal": 77,
        "beljakovine": 6.3,
        "ogljikovi_hidrati": 0.6,
        "maščobe": 5.3
    },
    "banana": {
        "kcal": 105,
        "beljakovine": 1.3,
        "ogljikovi_hidrati": 27,
        "maščobe": 0.4
    }
}


def main():

    while True:
        input("⏎ ENTER za začetek poslušanja...")

        spoken_text = poslusaj()
        kolicina, hrana = spoken_text.split(" ")

        if spoken_text is None:
            print("Nič ni bilo prepoznano")
            continue

        print("Uporabnik je rekel:", spoken_text.capitalize())

        zivilo = seznam_zivil.get(hrana)

        faktor = 1
        if kolicina == "dvakrat":
            faktor = 2

        if hrana in seznam_zivil:
            print("=" * 35)
            print(f"{spoken_text.capitalize()} dodan/a v jedilnik.")
            print(f"{zivilo['kcal'] * faktor} kalorij")
            print(f"{zivilo['beljakovine'] * faktor} beljakovin")
            print(
                f"{zivilo['ogljikovi_hidrati'] * faktor} ogljikovih hidratov")
            print(f"{zivilo['maščobe'] * faktor} maščob")
            print("=" * 35)

        elif "izhod" in spoken_text.lower():
            print(f"Adijo")
            break

        else:
            print("Ni v seznamu živil!")

        print()


def poslusaj(language="sl-SI"):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Kalibriram šum...")
        r.adjust_for_ambient_noise(source, duration=1)
        print("Govori...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio, language=language)
        return text
    except:
        return None


if __name__ == "__main__":
    main()
