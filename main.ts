for (let i = 0; i < 2; i++) {
    basic.showIcon(IconNames.Heart)
    basic.forever(function on_forever() {
        basic.showLeds(`
    . # . # .
    # . # . #
    # . . . #
    . # . # .
    . . # . .
    `)
    })
}
basic.clearScreen()
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    radio.sendString("HI")
})
radio.onReceivedString(function on_received_string(receivedString: string) {
    basic.showString(receivedString)
})
