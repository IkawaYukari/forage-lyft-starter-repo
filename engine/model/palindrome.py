from datetime import datetime

from engine.sternman_engine import SternmanEngine
from battery.nubbin_battery import NubbinBattery


class Palindrome(SternmanEngine, NubbinBattery):
    def needs_service(self):
        if self.battery_should_be_serviced() or self.engine_should_be_serviced():
            return True
        else:
            return False
