for (let i = 0; i < 4; i++) {
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
radio.onReceivedString(function on_received_string(receivedString: string) {
    
})
