import pyfiglet, random
from rich.console import Console

console = Console()
variavel = random.randint(2, 5)

def texto_grande(texto, cor="green", fonte="small"):
    ascii_art = pyfiglet.figlet_format(texto, font=fonte)
    console.print(ascii_art, style=cor)

# Fontes disponíveis: 'standard', 'slant', 'big', 'banner', 'block', etc.
texto_grande(f"{variavel}", cor="bold green", fonte="standard")

