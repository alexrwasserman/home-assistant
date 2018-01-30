class Assistant(object):
    def __init__(self):
        object.__init__(self)

    def turn_lights_on(cls):
        print("Assistant turned the lights on")

    def turn_lights_off(cls):
        print("Assistant turned the lights off")

    def set_alarm(cls, args):
        print("Assistant set an alarm for " + args[0])
