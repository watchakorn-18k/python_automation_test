import pytest
from py.xml import html


@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(1, html.th("Group"))
    cells.insert(3, html.th("Description"))


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    custom_group = getattr(report, "custom_group", "")
    custom_description = getattr(report, "custom_description", "")
    cells.insert(1, html.td(custom_group))
    cells.insert(3, html.td(custom_description))


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    outcome._result.custom_group = item.parent.name.replace("Test", "")
    outcome._result.custom_description = item.function.__doc__
