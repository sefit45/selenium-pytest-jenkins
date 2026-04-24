import pytest
from pages.wikipedia_page import WikipediaPage

@pytest.mark.ui
@pytest.mark.smoke
def test_search_bitcoin(driver):
    wiki = WikipediaPage(driver)

    wiki.open()
    wiki.search_for("Bitcoin")

    assert wiki.get_main_heading() == "Bitcoin"
