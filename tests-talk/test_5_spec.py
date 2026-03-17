from unittest.mock import Mock, create_autospec
from typing import Protocol


class FetcherProtocol(Protocol):
    def fetch(self, item_id: int) -> str: ...


def test5_1_without_spec_attribute() -> None:
    # Arrange
    fetcher_mock_without_spec = Mock()
    fetcher_mock_without_spec.fetch.return_value = "item-1"

    # Act
    item = fetcher_mock_without_spec.fetch()

    # Assert
    assert item == fetcher_mock_without_spec.fetch.return_value


def test5_2_spec_attribute() -> None:
    # Arrange
    fetcher_mock_with_spec = Mock(spec=FetcherProtocol)
    fetcher_mock_with_spec.fetch.return_value = "item-1"

    # Act
    item = fetcher_mock_with_spec.fetch()

    # Assert
    assert item is fetcher_mock_with_spec.fetch.return_value


def test5_3_autospec() -> None:
    # Arrange
    fetcher_mock_autospec = create_autospec(FetcherProtocol)
    fetcher_mock_autospec.fetch.return_value = "item-1"

    # Act
    item = fetcher_mock_autospec.fetch()

    # Assert
    assert item is fetcher_mock_autospec.fetch.return_value
