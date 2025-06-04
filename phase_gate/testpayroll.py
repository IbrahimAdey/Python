import unittest
import payroll

class TestPayroll(unittest.TestCase):

    def setUp(self):
        payroll.tasks.clear()

    def test_add_task(self):
        payroll.add_task("name")
        self.assertEqual(len(payroll.tasks), 1)
        self.assertEqual(payroll.tasks[0]["description"], "name")
        self.assertFalse(payroll.tasks[0]["completed"])

    def test_view_tasks_output(self):
        payroll.add_task("ibrahim")
        expected_output = "[ ] ibrahim"
        printed = payroll.view_tasks()

    def test_view_tasks_output(self):
        payroll.add_task("hourly_rate")
        expected_output = "[ ] hourly_rate"
        printed = payroll.view_tasks() 

if __name__ == "__main__":
    unittest.main()

