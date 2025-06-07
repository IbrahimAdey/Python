from datetime import datetime, timedelta

class MenstrualCycle:
    def __init__(self, last_period_start, cycle_length, period_length):
        self.last_period_start = datetime.strptime(last_period_start, "%Y-%m-%d")
        self.cycle_length = cycle_length
        self.period_length = period_length

    def calculate_next_period(self):
        return self.last_period_start + timedelta(days=self.cycle_length)

    def calculate_ovulation(self):
        return self.last_period_start + timedelta(days=self.cycle_length // 2)

    def calculate_fertile_window(self):
        ovulation = self.calculate_ovulation()
        return (ovulation - timedelta(days=2), ovulation + timedelta(days=2))

    def calculate_safe_periods(self):
        fertile_start, fertile_end = self.calculate_fertile_window()
        safe1_start = self.last_period_start + timedelta(days=self.period_length)
        safe1_end = fertile_start - timedelta(days=1)
        safe2_start = fertile_end + timedelta(days=1)
        safe2_end = self.calculate_next_period() - timedelta(days=1)
        return [(safe1_start, safe1_end), (safe2_start, safe2_end)]

    def get_cycle_info(self):
        next_period = self.calculate_next_period()
        ovulation = self.calculate_ovulation()
        fertile_start, fertile_end = self.calculate_fertile_window()
        safe_periods = self.calculate_safe_periods()
        return (
            f"Next Period Start: {next_period.strftime('%Y-%m-%d')}\n"
            f"Ovulation Date: {ovulation.strftime('%Y-%m-%d')}\n"
            f"Fertile Window: {fertile_start.strftime('%Y-%m-%d')} to {fertile_end.strftime('%Y-%m-%d')}\n"
            f"Safe Periods:\n"
            f"  1. {safe_periods[0][0].strftime('%Y-%m-%d')} to {safe_periods[0][1].strftime('%Y-%m-%d')}\n"
            f"  2. {safe_periods[1][0].strftime('%Y-%m-%d')} to {safe_periods[1][1].strftime('%Y-%m-%d')}"
        )

def main():
    last_period_start = input("Enter the start date of your last period (yyyy-mm-dd): ")
    cycle_length = int(input("Enter your cycle length : "))
    period_length = int(input("Enter your period length : "))

    cycle = MenstrualCycle(last_period_start, cycle_length, period_length)
    print("\n=== Your Menstrual Cycle Info ===")
    print(cycle.get_cycle_info())

if __name__ == "__main__":
    main()