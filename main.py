def on_forever():
    basic.show_leds("""
    . # . # .
    # . # . #
    # . . . #
    . # . # .
    . . # . .
    """)
for i in range(2):
    basic.show_icon(IconNames.HEART)
    basic.forever(on_forever)
    
basic.clear_screen()

def on_button_pressed_a():
    radio.send_string("HI")    
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_received_string(receivedString):
    basic.show_string(receivedString)
radio.on_received_string(on_received_string)
