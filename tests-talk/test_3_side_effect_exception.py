from typing import Protocol
from random import randint
from unittest.mock import Mock


class FetcherProtocol(Protocol):
    def fetch(self, organization_id: int) -> list[str]: ...


class APIClient:
    def __init__(self, fetcher: FetcherProtocol):
        self._fetcher = fetcher

    def get_clients(self, organization_id: int) -> list[str]:
        try:
            return self._fetcher.fetch(organization_id)
        except ValueError:
            return []


def test3_side_effect_exception() -> None:
    """Создаем `Mock` c SideEffect для проверки различных сценариев."""

    # Arrange
    organization_id = randint(1, 100)
    fetcher_mock = Mock()
    fetcher_mock.fetch.side_effect = ValueError()
    api_client = APIClient(fetcher=fetcher_mock)

    # Act
    clients = api_client.get_clients(organization_id)

    # Assert
    assert clients == []
    fetcher_mock.fetch.assert_called_once_with(organization_id)
