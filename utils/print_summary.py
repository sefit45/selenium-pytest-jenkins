from report_summary import generate_test_summary


summary = generate_test_summary()

print("===== TEST EXECUTION SUMMARY =====")
print(f"Total Tests: {summary['total']}")
print(f"Passed: {summary['passed']}")
print(f"Failed: {summary['failed']}")
print(f"Broken: {summary['broken']}")
print(f"Skipped: {summary['skipped']}")
print(f"Success Rate: {summary['success_rate']}")
print("==================================")