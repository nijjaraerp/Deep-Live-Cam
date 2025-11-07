"""
Test utility functions.
"""
import os
import tempfile
import pytest
from modules.utilities import (
    has_image_extension,
    is_image,
    is_video,
    get_temp_directory_path,
    normalize_output_path,
)


class TestFileExtensions:
    """Test file extension and type detection."""

    def test_has_image_extension_png(self):
        """Test PNG image extension detection."""
        assert has_image_extension("test.png") is True
        assert has_image_extension("test.PNG") is True

    def test_has_image_extension_jpg(self):
        """Test JPG/JPEG image extension detection."""
        assert has_image_extension("test.jpg") is True
        assert has_image_extension("test.jpeg") is True
        assert has_image_extension("test.JPEG") is True

    def test_has_image_extension_invalid(self):
        """Test invalid image extensions."""
        assert has_image_extension("test.mp4") is False
        assert has_image_extension("test.txt") is False
        assert has_image_extension("test") is False

    def test_is_image_nonexistent(self):
        """Test is_image with non-existent file."""
        assert is_image("nonexistent.png") is False

    def test_is_video_nonexistent(self):
        """Test is_video with non-existent file."""
        assert is_video("nonexistent.mp4") is False


class TestPathOperations:
    """Test path manipulation functions."""

    def test_get_temp_directory_path(self):
        """Test temp directory path generation."""
        target_path = "/path/to/video.mp4"
        temp_path = get_temp_directory_path(target_path)
        assert "temp" in temp_path
        assert "video" in temp_path

    def test_normalize_output_path_with_directory(self):
        """Test output path normalization with directory."""
        source_path = "source.png"
        target_path = "target.mp4"
        output_path = "/output/dir"
        
        # Create a temporary directory for testing
        with tempfile.TemporaryDirectory() as tmpdir:
            result = normalize_output_path(source_path, target_path, tmpdir)
            assert result.startswith(tmpdir)
            assert "source-target" in result
            assert result.endswith(".mp4")

    def test_normalize_output_path_with_file(self):
        """Test output path normalization with file."""
        source_path = "source.png"
        target_path = "target.mp4"
        output_path = "/output/result.mp4"
        
        result = normalize_output_path(source_path, target_path, output_path)
        assert result == output_path

    def test_normalize_output_path_missing_params(self):
        """Test output path normalization with missing parameters."""
        result = normalize_output_path(None, None, "/output/result.mp4")
        assert result == "/output/result.mp4"
