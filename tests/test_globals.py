"""
Test the globals module configuration.
"""
import pytest
import modules.globals as globals


class TestGlobalsConfiguration:
    """Test global configuration values."""

    def test_file_types_defined(self):
        """Test that file_types is properly defined."""
        assert hasattr(globals, 'file_types')
        assert isinstance(globals.file_types, list)
        assert len(globals.file_types) > 0

    def test_file_types_structure(self):
        """Test file_types has correct structure."""
        for item in globals.file_types:
            assert isinstance(item, tuple)
            assert len(item) == 2
            assert isinstance(item[0], str)
            assert isinstance(item[1], tuple)

    def test_default_log_level(self):
        """Test that log_level has a default value."""
        assert hasattr(globals, 'log_level')
        assert isinstance(globals.log_level, str)

    def test_boolean_flags(self):
        """Test that boolean flags are properly initialized."""
        assert hasattr(globals, 'keep_fps')
        assert hasattr(globals, 'keep_audio')
        assert hasattr(globals, 'many_faces')
        assert hasattr(globals, 'map_faces')
        assert hasattr(globals, 'nsfw_filter')

    def test_paths_initialized(self):
        """Test that path variables are initialized."""
        assert hasattr(globals, 'source_path')
        assert hasattr(globals, 'target_path')
        assert hasattr(globals, 'output_path')

    def test_execution_providers_list(self):
        """Test that execution_providers is a list."""
        assert hasattr(globals, 'execution_providers')
        assert isinstance(globals.execution_providers, list)
