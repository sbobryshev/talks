from unittest.mock import MagicMock


class ExampleForTests:
    def method1(self) -> str:
        return "method1 called"


def test1_mock_existent_method() -> None:
    """Переопределение при помощи `MagicMock` существующего метода."""

    # Arrange
    example = ExampleForTests()
    example.method1 = MagicMock(return_value="method1 mocked")

    # Act
    result = example.method1(1, 2, 3, 4, key="value")

    # Assert
    assert result == "method1 mocked"
    example.method1.assert_called_once_with(1, 2, 3, key="value")
