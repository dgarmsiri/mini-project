def on_forever():
    basic.show_leds("""
    . # . # .
    # . # . #
    # . . . #
    . # . # .
    . . # . .
    """)
for i in range(4):
    basic.show_icon(IconNames.HEART)
    basic.forever(on_forever)

def on_received_string(receivedString):
    pass
radio.on_received_string(on_received_string)
