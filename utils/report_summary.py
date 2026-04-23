import os
import json


def generate_test_summary():
    allure_results_path = "allure-results"

    total = 0
    passed = 0
    failed = 0
    broken = 0
    skipped = 0

    if not os.path.exists(allure_results_path):
        return {
            "total": 0,
            "passed": 0,
            "failed": 0,
            "broken": 0,
            "skipped": 0,
            "success_rate": "0%"
        }

    for file_name in os.listdir(allure_results_path):
        if file_name.endswith("-result.json"):
            file_path = os.path.join(allure_results_path, file_name)

            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

                total += 1
                status = data.get("status", "")

                if status == "passed":
                    passed += 1
                elif status == "failed":
                    failed += 1
                elif status == "broken":
                    broken += 1
                elif status == "skipped":
                    skipped += 1

    success_rate = f"{round((passed / total) * 100, 2)}%" if total > 0 else "0%"

    return {
        "total": total,
        "passed": passed,
        "failed": failed,
        "broken": broken,
        "skipped": skipped,
        "success_rate": success_rate
    }