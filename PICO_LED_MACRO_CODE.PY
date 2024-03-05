import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.consts import UnicodeMode
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.LED import LED

keyboard = KMKKeyboard()
layers = Layers()
encoder_handler = EncoderHandler()
keyboard.modules = [layers, encoder_handler]

keyboard.col_pins = (board.GP5, board.GP4, board.GP3) #Columns
keyboard.row_pins = (board.GP0, board.GP1, board.GP2) #Rows

encoder_handler.pins = ((board.GP19, board.GP21, board.GP20, False),)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

leds = LED(led_pin=[board.GP15])
KMKKeyboard.extensions.append(leds)

# Keymap - Simple 9-key layout
keyboard.keymap = [
    [
        KC.N1, KC.N2, KC.N3,
        KC.N4, KC.N5, KC.N6,
        KC.N7, KC.N8, KC.N9
    ]
]

# Encoder mapping - map F13, F14, F15 to the encoder
encoder_handler.map = [((KC.F14, KC.F15, KC.F13),)]

if __name__ == '__main__':
    print("Starting script...")
    try:
        keyboard.go()
    except Exception as e:
        print(f"An error occurred: {str(e)}")

