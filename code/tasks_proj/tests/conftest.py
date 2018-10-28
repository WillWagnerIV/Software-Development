def pytest_report_teststatus(report):
    """Turn failures into opportunities."""
    if report.when == 'call' and report.failed:
        return (report.outcome, 'O' , 'OPPORTUNITY for improvement' )