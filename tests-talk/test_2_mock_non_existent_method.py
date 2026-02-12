from unittest.mock import MagicMock


class ExampleForTests:
    def method1(self) -> str:
        return "method1 called"


def test2_mock_non_existent_method_with_nested_function() -> None:
    """Переопределение при помощи `MagicMock` несуществующего метода."""

    # Arrange
    example = ExampleForTests()
    example.method2 = MagicMock()
    example.method2.nested_function.return_value = 15

    # Act
    result = example.method2.nested_function()

    # Assert
    assert result == 15
    example.method2.nested_function.assert_called_once()
