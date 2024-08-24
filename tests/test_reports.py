import pytest

from src.read_excel import read_excel
from src.reports import spending_by_category

result_read = read_excel("../data/operations.xlsx")
result_spend = spending_by_category(result_read, "Переводы", date="31.12.2021")


@pytest.fixture
def fix_reports():
    return result_spend


def test_report(fix_reports):
    assert spending_by_category(result_read, "Переводы", date="31.12.2021") == fix_reports
    assert result_spend[0] == fix_reports[0]


def test_reports():
    assert spending_by_category(result_read, "Переводы") == []
    assert spending_by_category(result_read, "Красота") == []
    assert spending_by_category(result_read, "sdfsf") == []
