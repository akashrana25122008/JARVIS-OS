import psutil


class SystemMonitor:

    @staticmethod
    def cpu():
        return psutil.cpu_percent(interval=0.1)

    @staticmethod
    def ram():
        return psutil.virtual_memory().percent

    @staticmethod
    def battery():
        battery = psutil.sensors_battery()

        if battery is None:
            return "N/A"

        return battery.percent