# Definindo a classe Color que armazena o valor das componentes de cor
class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    # Retorna a cor em formato hexadecimal
    def to_hex(self):
        return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

    # Retorna a cor em formato RGB
    def to_rgb(self):
        return f"rgb({self.r}, {self.g}, {self.b})"

# Função para converter a cor em hexadecimal para RGB


def hex_to_rgb(hex_color):
    if hex_color.startswith("#"):  # Remove o caractere '#' se existir
        hex_color = hex_color[1:]

    if len(hex_color) == 3:  # Formato #rgb
        # Repete cada caractere (ex: "a" -> "aa")
        r = int(hex_color[0] * 2, 16)
        g = int(hex_color[1] * 2, 16)
        b = int(hex_color[2] * 2, 16)
    elif len(hex_color) == 6:  # Formato #rrggbb
        r = int(hex_color[0:2], 16)
        g = int(hex_color[2:4], 16)
        b = int(hex_color[4:6], 16)
    else:
        raise ValueError("[2;31mInvalid HEX color format[0m")

    # Retorna uma instância da classe Color com as componentes de cor em RGB
    return Color(r, g, b)

# Função para converter a cor em RGB para hexadecimal


def rgb_to_hex(rgb_color):
    r, g, b = rgb_color
    return Color(r, g, b).to_hex()


# Obtém a cor em formato hexadecimal a partir do usuário e a converte para RGB
hex_color = input(
    "Digite uma cor em [2;37m[2;34mHEX[0m[2;37m[0m (ex: #ffffff): ")
rgb_color = hex_to_rgb(hex_color)

# Imprime a cor em formato RGB
print(
    f"A cor {hex_color} em [2;37m[2;36mRGB[0m[2;37m[0m é {rgb_color.to_rgb()}")

# Obtém a cor em formato RGB a partir do usuário e a converte para hexadecimal
rgb_color = input("Digite uma cor em RGB (ex: 255, 255, 255): ").split(",")
rgb_color = tuple(map(int, rgb_color))
hex_color = rgb_to_hex(rgb_color)

# Imprime a cor em formato hexadecimal
print(f"A cor {rgb_color} em HEX é {hex_color}")
