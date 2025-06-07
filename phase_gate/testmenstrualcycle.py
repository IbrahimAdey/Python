class TestMenstrualCycle(unittest.TestCase):
    def test_cycle(self):
        result = calculate_cycle("2025-06-01", 28, 5)
        self.assertEqual(result["next_period_start"], "2025-06-29")
        self.assertEqual(result["next_ovulation_date"], "2025-06-15")
        self.assertEqual(result["fertile_window"], ("2025-06-13", "2025-06-17"))
        self.assertEqual(result["safe_periods"], [("2025-06-06", "2025-06-12"), ("2025-06-18", "2025-06-28")])

if __name__ == "__main__":
    unittest.main()