class Gadget:
    def __init__(self, color, g_type):
        self.color = color
        self.g_type = g_type
    
    def is_white(self):
        return self.color == 'White'

    def is_charger(self):
        return self.g_type == 'Charger'

    def __str__(self):
        return f"{self.color} {self.g_type}"

class Human:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

def yell(human):
    if isinstance(human, Human):
        if human.name == 'Tarik':
            print(f"Aaaaaaaaaaaa Tarik")
        else:
            print(f"Helloooooooo {human.name}")

def constellation():
    day = int(input("Input birthday: "))
    month = input("Input month of birth (e.g. march, july etc): ")
    if month == 'december': # 1
        if day < 22: # 2
            astro_sign = 'Sagittarius'
        else:
            'capricorn'
    elif month == 'january': # 3
        astro_sign = 'Capricorn' if (day < 20) else 'aquarius' # 4
    elif month == 'february': # 5
        astro_sign = 'Aquarius' if (day < 19) else 'pisces' # 6
    elif month == 'march': # 7
        astro_sign = 'Pisces' if (day < 21) else 'aries' # 8
    elif month == 'april': # 9
        astro_sign = 'Aries' if (day < 20) else 'taurus' # 10
    elif month == 'may': # 11
        astro_sign = 'Taurus' if (day < 21) else 'gemini' # 12
    elif month == 'june': # 13
        astro_sign = 'Gemini' if (day < 21) else 'cancer' # 14
    elif month == 'july': # 15
        astro_sign = 'Cancer' if (day < 23) else 'leo' # 16
    elif month == 'august': # 17
        astro_sign = 'Leo' if (day < 23) else 'virgo' # 18
    elif month == 'september': # 19
        astro_sign = 'Virgo' if (day < 23) else 'libra' # 20
    elif month == 'october': # 21
        astro_sign = 'Libra' if (day < 23) else 'scorpio' # 22
    elif month == 'november': # 23
        astro_sign = 'scorpio' if (day < 22) else 'sagittarius' # 24
    print("Your Astrological sign is :",astro_sign)
    # Cyclomatic Complexity 25

def main():
    oussama = Human('Oussama')
    mouse = Gadget('Black', 'Mouse')
    yell(oussama)
    print(mouse)

    tarik = Human('Tarik')
    charger = Gadget('White', 'Charger')
    yell(tarik)
    print(charger)

if __name__ == "__main__":
    main()