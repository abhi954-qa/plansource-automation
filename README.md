# plansource-automation

This project demonstrates end-to-end QA automation for the [PlanSource Benefits Admin Portal](https://partner-dev-benefits.plansource.com), using:

- Selenium (UI testing)
- Requests (API validation)
- Pytest (test runner)
- Page Object Model (POM) design pattern
- Logging & Reporting

1.Clone the repository

(bash)
git clone https://github.com/abhi954-qa/plansource-automation.git
cd plansource-automation

2.Create virtual environment (recommended)

python -m venv venv
venv\Scripts\activate    

3.Install dependencies
pip install -r requirements.txt

4.How to Run Tests

pytest tests/test_create_employee.py

pytest tests/test_enroll_benefits.py


5.Logs and Reports
    Logs: test_run.log
    
to generate report:
    pytest --html=report.html
            OR
    pytest tests/test_create_employee.py --html=reports/plan_source_report.html --self-contained-html

6.Troubleshooting
TimeoutException → Increase wait time or review element locators

500 API errors → Check session ID and headers. Fetch session ID from Chrome.

7.Upload to Github

git init
git remote add origin https://github.com/<yourusername>/<repository_name>.git
git add .
git commit -m "Initial commit"
git push -u origin main
