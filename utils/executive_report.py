import json
import os
from datetime import datetime

ALLURE_RESULTS_DIR = "allure-results"
REPORT_FILE = "executive_qa_dashboard.html"


def load_allure_results():
    total = 0
    passed = 0
    failed = 0
    broken = 0
    skipped = 0

    failed_tests = []

    if not os.path.exists(ALLURE_RESULTS_DIR):
        return total, passed, failed, broken, skipped, failed_tests

    for filename in os.listdir(ALLURE_RESULTS_DIR):
        if filename.endswith("-result.json"):
            total += 1
            file_path = os.path.join(ALLURE_RESULTS_DIR, filename)

            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)

            name = data.get("name", "Unknown Test")
            status = data.get("status", "unknown")

            if status == "passed":
                passed += 1
            elif status == "failed":
                failed += 1
                failed_tests.append(name)
            elif status == "broken":
                broken += 1
                failed_tests.append(name)
            elif status == "skipped":
                skipped += 1

    return total, passed, failed, broken, skipped, failed_tests


def calculate_pass_rate(total, passed):
    if total == 0:
        return 0
    return round((passed / total) * 100, 2)


def get_release_decision(failed, broken, pass_rate):
    if failed > 0 or broken > 0:
        return "NO-GO", "Critical failures detected. Release should be blocked.", "high"

    if pass_rate < 95:
        return "REVIEW", "Execution is mostly stable but requires validation.", "medium"

    return "GO", "System is stable and ready for release.", "low"


def build_failed_tests_table(failed_tests):
    if not failed_tests:
        return """
        <tr>
            <td colspan="2">No failed tests detected 🎉</td>
        </tr>
        """

    rows = ""
    for index, test in enumerate(failed_tests, start=1):
        rows += f"""
        <tr>
            <td>{index}</td>
            <td>{test}</td>
        </tr>
        """
    return rows


def generate_html(total, passed, failed, broken, skipped,
                  pass_rate, decision, recommendation,
                  risk_level, failed_tests):

    generated_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    failed_table = build_failed_tests_table(failed_tests)

    decision_class = {
        "high": "danger",
        "medium": "warning",
        "low": "success"
    }.get(risk_level, "success")

    html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Executive QA Intelligence Dashboard</title>

<style>
    * {{
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }}

    body {{
        font-family: Arial, sans-serif;
        background: #0f172a;
        color: white;
        padding: 30px;
    }}

    .container {{
        max-width: 1400px;
        margin: auto;
    }}

    .header {{
        background: linear-gradient(135deg, #111827, #2563eb);
        border-radius: 20px;
        padding: 40px;
        margin-bottom: 30px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    }}

    .header h1 {{
        font-size: 42px;
        margin-bottom: 10px;
    }}

    .header p {{
        color: #d1d5db;
        font-size: 16px;
    }}

    .cards {{
        display: grid;
        grid-template-columns: repeat(5, 1fr);
        gap: 20px;
        margin-bottom: 30px;
    }}

    .card {{
        background: #1e293b;
        border-radius: 18px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }}

    .card h2 {{
        font-size: 38px;
        margin-bottom: 10px;
    }}

    .card p {{
        color: #cbd5e1;
    }}

    .green {{
        color: #22c55e;
    }}

    .red {{
        color: #ef4444;
    }}

    .orange {{
        color: #f97316;
    }}

    .yellow {{
        color: #eab308;
    }}

    .blue {{
        color: #3b82f6;
    }}

    .section {{
        background: #1e293b;
        border-radius: 20px;
        padding: 35px;
        margin-bottom: 30px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }}

    .section h2 {{
        margin-bottom: 20px;
        font-size: 28px;
    }}

    .progress-container {{
        background: #334155;
        border-radius: 999px;
        height: 30px;
        overflow: hidden;
        margin-top: 20px;
    }}

    .progress-bar {{
        height: 100%;
        width: {pass_rate}%;
        background: linear-gradient(90deg, #22c55e, #3b82f6);
    }}

    .decision {{
        font-size: 42px;
        font-weight: bold;
        margin-bottom: 15px;
    }}

    .success {{
        color: #22c55e;
    }}

    .warning {{
        color: #facc15;
    }}

    .danger {{
        color: #ef4444;
    }}

    table {{
        width: 100%;
        border-collapse: collapse;
        margin-top: 20px;
    }}

    table th {{
        background: #334155;
        padding: 16px;
        text-align: left;
    }}

    table td {{
        padding: 16px;
        border-bottom: 1px solid #334155;
    }}

    .footer {{
        text-align: center;
        margin-top: 40px;
        color: #94a3b8;
        font-size: 14px;
    }}

    .badge {{
        display: inline-block;
        background: #2563eb;
        padding: 8px 16px;
        border-radius: 999px;
        margin-top: 10px;
        font-size: 14px;
    }}
</style>
</head>
<body>

<div class="container">

    <div class="header">
        <h1>Executive QA Intelligence Dashboard</h1>
        <p>Enterprise-grade release dashboard generated from Allure results</p>
        <p>Generated at: {generated_at}</p>
        <div class="badge">
            Selenium + Pytest + Docker + Jenkins + GitHub Actions + Allure
        </div>
    </div>

    <div class="cards">
        <div class="card">
            <h2>{total}</h2>
            <p>Total Tests</p>
        </div>

        <div class="card">
            <h2 class="green">{passed}</h2>
            <p>Passed</p>
        </div>

        <div class="card">
            <h2 class="red">{failed}</h2>
            <p>Failed</p>
        </div>

        <div class="card">
            <h2 class="orange">{broken}</h2>
            <p>Broken</p>
        </div>

        <div class="card">
            <h2 class="yellow">{skipped}</h2>
            <p>Skipped</p>
        </div>
    </div>

    <div class="section">
        <h2>Pass Rate</h2>
        <h1 class="blue">{pass_rate}%</h1>

        <div class="progress-container">
            <div class="progress-bar"></div>
        </div>
    </div>

    <div class="section">
        <h2>Release Decision</h2>

        <div class="decision {decision_class}">
            {decision}
        </div>

        <p>{recommendation}</p>
    </div>

    <div class="section">
        <h2>Top Risk Areas</h2>

        <p>
        • Authentication flows<br>
        • Login critical business path<br>
        • API token validation<br>
        • Negative authentication scenarios<br>
        • E2E browser execution stability
        </p>
    </div>

    <div class="section">
        <h2>Failed / Broken Tests</h2>

        <table>
            <thead>
                <tr>
                    <th>#</th>
                    <th>Test Name</th>
                </tr>
            </thead>
            <tbody>
                {failed_table}
            </tbody>
        </table>
    </div>

    <div class="section">
        <h2>Executive Summary</h2>

        <p>
        This dashboard provides management-level release intelligence based on
        automated test execution results.
        It enables fast GO / NO-GO decisions, highlights business-critical risks,
        and provides visibility into overall system quality and release readiness.
        </p>
    </div>

    <div class="footer">
        Executive QA Dashboard V2 | Built for Senior QA / QA Architect / Test Manager level
    </div>

</div>

</body>
</html>
"""
    return html


def main():
    total, passed, failed, broken, skipped, failed_tests = load_allure_results()

    pass_rate = calculate_pass_rate(total, passed)

    decision, recommendation, risk_level = get_release_decision(
        failed,
        broken,
        pass_rate
    )

    html = generate_html(
        total,
        passed,
        failed,
        broken,
        skipped,
        pass_rate,
        decision,
        recommendation,
        risk_level,
        failed_tests
    )

    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        file.write(html)

    print(f"Executive QA Dashboard V2 generated: {REPORT_FILE}")


if __name__ == "__main__":
    main()