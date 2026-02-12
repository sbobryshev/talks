from unittest.mock import Mock, call
from typing import Protocol
import pytest


type PageNumber = int


class PagerProtocol(Protocol):
    def get(self, page_number: int) -> str: ...


class PagesContentFinder:
    def __init__(self, pager: PagerProtocol):
        self._pager = pager

    def find(self, target: str, max_pages: int) -> PageNumber:
        for page_number in range(1, max_pages + 1):
            page_content = self._pager.get(page_number)
            if target in page_content:
                return page_number
        raise Exception(f"Target={target} not found.")


def test4_1_side_effect_content() -> None:
    """Создаем `Mock` с SideEffect для возвращаемого значения."""

    # Arrange
    target = "example for side effect"
    pager_mock = Mock()
    pager_mock.get.side_effect = ("text1", f"text with {target}", "unreachable")
    # ----------------------------<< 1 >>, <<<<<<<<< 2 >>>>>>>>>, <<<< 3 >>>>>>
    finder = PagesContentFinder(pager_mock)

    # Act
    page_number = finder.find(target, max_pages=10)

    # Assert
    assert page_number == 2
    assert pager_mock.get.call_count == 2
    pager_mock.get.assert_has_calls([call(1), call(2)])


def test4_2_side_effect_content() -> None:
    """Создаем `Mock` с SideEffect для возвращаемого значения."""

    # Arrange
    target = "<<>>"
    pager_mock = Mock()
    pager_mock.get.side_effect = ("text1", "text2", target)
    finder = PagesContentFinder(pager_mock)

    # Act
    with pytest.raises(Exception) as exc_info:
        finder.find(target, max_pages=2)

    assert exc_info.match("Target=.* not found.")
    assert pager_mock.get.call_count == 2
    pager_mock.get.assert_has_calls([call(1), call(2)])
