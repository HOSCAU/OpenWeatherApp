class AlertSystem:
    def __init__(self, threshold_temp: float, consecutive_updates: int):
        self.threshold_temp = threshold_temp
        self.consecutive_updates = consecutive_updates
        self.alert_triggered = False
        self.update_count = 0

    def check_threshold(self, current_temp: float):
        if current_temp > self.threshold_temp:
            self.update_count += 1
            if self.update_count >= self.consecutive_updates:
                self.trigger_alert()
        else:
            self.update_count = 0

    def trigger_alert(self):
        if not self.alert_triggered:
            print("Alert: Temperature exceeded the threshold!")
            # Implement email or other notification systems
            self.alert_triggered = True
