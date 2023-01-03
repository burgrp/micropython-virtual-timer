from machine import Timer

default_scheduler = None

class VirtualTimerScheduler:
    counter = 0
    period = 0
    timers = list()

    def __init__(self, hw_timer, period):

        def callback(timer):
            for timer in self.timers:
                if self.counter % timer.period == 0:
                    timer.callback(timer)

            self.counter += 1

        self.period = period
        hw_timer.init(mode=Timer.PERIODIC, period=period, callback=callback)

    def add(self, timer):
        self.timers.append(timer)

    def remove(self, timer):
        self.timers.remove(timer)

class VirtualTimer:

    period = 0
    scheduler = None
    callback = None

    def init(self, mode=Timer.PERIODIC, period=-1, callback=None, scheduler=None):

        if scheduler == None:
            global default_scheduler
            if default_scheduler == None:
                default_scheduler = VirtualTimerScheduler(Timer(0), 100)

            scheduler = default_scheduler

        self.scheduler = scheduler

        self.period = period / scheduler.period
        self.callback = callback

        self.scheduler.add(self)


    def deinit(self):
        self.scheduler.remove(self)
