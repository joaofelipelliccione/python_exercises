"""
Desenvolva uma classe que simule uma TV.
"""


class Tv:
    def __init__(self, tamanho):
        self.__tamanho = tamanho
        self.__volume = 50
        self.__canal = 1
        self.__status = "Desligada"

    def get_tamanho(self):
        return f"Tv de {self.__tamanho} polegadas."

    def get_volume(self):
        return f"O volume atual é {self.__volume}."

    def set_volume(self, volume):
        if 0 <= volume <= 99:
            self.__volume = volume
            return f"Volume alterado para {volume}."
        else:
            return "Volume não pode ser menor que 0 ou maior que 99."

    def get_canal(self):
        return f"O canal atual é {self.__canal}."

    def set_canal(self, canal):
        if 1 <= canal <= 99:
            self.__canal = canal
            return f"Canal alterado para {canal}."
        else:
            return "Canal não pode ser menor que 1 ou maior que 99."

    def get_status(self):
        return f"A Tv está {self.__status}."

    def press_power_btn(self):
        if self.__status == "Desligada":
            self.__status = "Ligada"
            return "Tv acaba de ser ligada."
        else:
            return "Tv desligando em 3...2...1..."


samsung_OLED = Tv(50)
print(samsung_OLED.get_tamanho())
print(samsung_OLED.get_volume())
print(samsung_OLED.set_volume(80))
print(samsung_OLED.set_volume(-5))
print(samsung_OLED.get_canal())
print(samsung_OLED.set_canal(25))
print(samsung_OLED.set_canal(200))
print(samsung_OLED.get_status())
print(samsung_OLED.press_power_btn())
print(samsung_OLED.get_status())
