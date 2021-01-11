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
 if 
