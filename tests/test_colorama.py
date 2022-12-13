import colorama

# for windows, and for IO redirection
import sys
from functools import partial
# stream = colorama.AnsiToWin32(sys.stdout).stream
wrapper = colorama.AnsiToWin32(sys.stdout)
stream = wrapper.stream
print = partial(print, file=stream)
print('strip ANSI sequences from our output: %s, convert ANSI sequences into win32 calls: %s'
      % (wrapper.strip, wrapper.convert))

bold = colorama.Style.BRIGHT
yellow = colorama.Fore.YELLOW
reset = colorama.Style.RESET_ALL
bg_red = colorama.Back.RED

print(repr(bold))
print(repr(yellow))
print(repr(reset))
print(repr(bg_red))

print(repr(bold+yellow))

print(bold+yellow+'hello'+reset)
print('\x1b[1m\x1b[33m'+'hello'+'\x1b[0m')
print('\x1b[1;33m'+'hello'+'\x1b[0m')
print('\x1b[1m'+'hello'+'\x1b[0m')
print('\x1b[33m'+'hello'+'\x1b[0m')


print('===== test esc functions ====')
# Returns escape codes from format codes
def esc1(*codes: int) -> str:
    # Example (bold + fg yellow + bg red): '\x1b[1;33;41m'
    return "\033[" + ";".join(str(code) for code in codes) + "m"


def esc2(*codes: int) -> str:
    # Also works! So you can simply add the codes together.
    # Example (bold + fg yellow + bg red): '\x1b[1m\x1b[33m\x1b[41m'
    return "".join("\033[" + str(code) + "m" for code in codes)

color1 = esc1(1, 33, 41)
color2 = esc2(1, 33, 41)
print(repr(color1))
print(repr(color2))
print('start '+color1+'hello'+reset+' end')
print('start '+color2+'hello'+reset+' end')

