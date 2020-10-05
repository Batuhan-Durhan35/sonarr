distance_to_object = 0
basic.show_icon(IconNames.YES)
basic.pause(500)
# Created by: Batuhan Durhan
# Created at: 2 october 2020

def on_forever():
    global distance_to_object
    distance_to_object = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.CENTIMETERS)
    basic.show_number(distance_to_object)
basic.forever(on_forever)
