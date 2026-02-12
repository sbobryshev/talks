# Разборы: Программирование

Серия разборов возможностей модуля `unittest.mock` в Python.

## Содержание

| # | Тема | Ключевые концепции |
|---|------|--------------------|
| 1 | [Мок существующего метода](1_mock_existent_method.md) | `MagicMock`, `return_value`, `assert_called_once_with` |
| 2 | [Мок несуществующего метода](2_mock_non_existent_method.md) | `MagicMock`, вложенные атрибуты |
| 3 | [side_effect: Исключения](3_side_effect_exception.md) | `side_effect`, `ValueError`, `Protocol` |
| 4 | [side_effect: Возвращаемые значения](4_side_effect_content.md) | `side_effect` с tuple, `call_count`, `assert_has_calls` |
| 5 | [spec и autospec](5_spec.md) | `Mock(spec=...)`, `create_autospec` |

## Запуск тестов

```bash
uv run pytest tests-talk/ -v
```
