"""
Test that core modules can be imported successfully.
This verifies that the basic installation is working.
"""
import pytest


def test_import_basic_modules():
    """Test that basic modules can be imported without heavy dependencies."""
    try:
        import modules.globals
        import modules.metadata
        import modules.utilities
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import basic modules: {e}")


def test_import_modules_with_insightface():
    """Test that modules requiring insightface can be imported."""
    pytest.importorskip("insightface", reason="insightface not installed")
    try:
        import modules.typing
        import modules.custom_types
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import modules: {e}")


def test_tkinter_fix_import():
    """Test that tkinter_fix can be imported."""
    pytest.importorskip("tkinter", reason="tkinter not installed")
    try:
        import tkinter_fix
        assert True
    except ImportError as e:
        pytest.fail(f"Failed to import tkinter_fix: {e}")
