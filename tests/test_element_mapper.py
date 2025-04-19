# === FILE: tests/test_element_mapper.py ===

"""
Unit tests for core/web/html/element_mapper.py
"""

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.web.html.element_mapper import extract_code_blocks_by_innertext
from unittest.mock import MagicMock

def test_extract_code_blocks_by_innertext_single_block():
    mock_element = MagicMock()
    mock_element.get_attribute.return_value = "print('Hello, world!')"
    result = extract_code_blocks_by_innertext([mock_element])
    assert result == ["print('Hello, world!')"]

def test_extract_code_blocks_by_innertext_ignores_empty():
    mock_element = MagicMock()
    mock_element.get_attribute.return_value = "   "
    result = extract_code_blocks_by_innertext([mock_element])
    assert result == []

def test_extract_code_blocks_by_innertext_multiple_blocks():
    el1 = MagicMock(); el1.get_attribute.return_value = "def foo(): pass"
    el2 = MagicMock(); el2.get_attribute.return_value = "x = 42"
    result = extract_code_blocks_by_innertext([el1, el2])
    assert result == ["def foo(): pass", "x = 42"]

