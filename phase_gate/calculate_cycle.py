from datetime import datetime, timedelta
import unittest

def calculate_cycle(last_period_start, cycle_length, period_length):
    start_date = datetime.strptime(last_period_start, "%Y-%m-%d")
    next_period = start_date + timedelta(days=cycle_length)
    ovulation = start_date + timedelta(days=cycle_length // 2)
    fertile_start = ovulation - timedelta(days=2)
    fertile_end = ovulation + timedelta(days=2)
    safe_periods = [
        (start_date + timedelta(days=period_length), fertile_start - timedelta(days=1)),
        (fertile_end + timedelta(days=1), next_period - timedelta(days=1))
    ]
    return {
        "next_period_start": next_period.strftime("%Y-%m-%d"),
        "next_ovulation_date": ovulation.strftime("%Y-%m-%d"),
        "fertile_window": (fertile_start.strftime("%Y-%m-%d"), fertile_end.strftime("%Y-%m-%d")),
        "safe_periods": [(s.strftime("%Y-%m-%d"), e.strftime("%Y-%m-%d")) for s, e in safe_periods]
    }

