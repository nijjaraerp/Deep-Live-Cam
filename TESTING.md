# Testing Guide for Deep-Live-Cam

This guide explains how to test the Deep-Live-Cam application after cloning the repository.

## Quick Start

After cloning the repository, follow these steps to verify your installation:

### 1. Install Test Dependencies

```bash
pip install -r requirements-dev.txt
```

This installs pytest and related testing tools.

### 2. Install Basic Runtime Dependencies

For basic tests to pass, you need these minimal dependencies:

```bash
pip install numpy opencv-python tqdm
```

### 3. Run Tests

The easiest way:

```bash
python run_tests.py
```

Or use pytest directly:

```bash
pytest
```

## Test Structure

The test suite is organized as follows:

```
tests/
├── __init__.py
├── test_imports.py      # Tests for module imports
├── test_utilities.py    # Tests for utility functions
└── test_globals.py      # Tests for global configuration
```

## What Gets Tested

### Basic Tests (Always Run)
- **Module Imports**: Verifies that basic modules can be imported
- **File Type Detection**: Tests image and video file type detection
- **Path Operations**: Tests temporary directory paths and output path normalization
- **Configuration**: Tests that global configuration variables are properly initialized

### Optional Tests (Skipped Without Dependencies)
- **InsightFace Integration**: Tests that require the insightface library
- **Tkinter UI**: Tests that require tkinter for GUI functionality

## Test Output

When you run tests, you'll see output like this:

```
======================================================================
Deep-Live-Cam Test Suite
======================================================================

Running tests...

tests/test_globals.py::TestGlobalsConfiguration::test_file_types_defined PASSED
tests/test_imports.py::test_import_basic_modules PASSED
tests/test_imports.py::test_import_modules_with_insightface SKIPPED (insightface not installed)
...

16 passed, 2 skipped in 0.13s
```

- **PASSED**: Test succeeded ✓
- **SKIPPED**: Test skipped due to missing optional dependencies (normal)
- **FAILED**: Test failed - indicates a problem that needs fixing

## Running Specific Tests

```bash
# Run only import tests
pytest tests/test_imports.py

# Run only utility tests
pytest tests/test_utilities.py

# Run tests with verbose output
pytest -v

# Run tests and show coverage
pytest --cov=modules --cov-report=html
```

## Continuous Integration

This repository includes a GitHub Actions workflow that automatically runs tests on:
- Multiple operating systems (Ubuntu, Windows, macOS)
- Multiple Python versions (3.10, 3.11)
- Every push and pull request to main/premain branches

You can see the test results in the "Actions" tab of the GitHub repository.

## Troubleshooting

### Import Errors

If you get import errors for cv2, numpy, or tqdm:

```bash
pip install numpy opencv-python tqdm
```

### All Tests Skipped

If all optional tests are skipped, that's normal! It means you have a minimal installation. The core functionality tests should still pass.

### Test Failures

If tests fail:
1. Make sure you're in the repository root directory
2. Verify you installed the dependencies correctly
3. Check that your Python version is 3.10 or newer
4. Try updating pip: `pip install --upgrade pip`

## Adding New Tests

When contributing to the project, please add tests for new features:

1. Create test files in the `tests/` directory
2. Follow the existing naming convention: `test_*.py`
3. Use pytest fixtures and assertions
4. Run tests locally before submitting a pull request

Example test:

```python
def test_my_new_feature():
    """Test description."""
    from modules.my_module import my_function
    result = my_function()
    assert result == expected_value
```

## Manual Testing

The test suite covers automated unit tests. For complete testing, also refer to the manual testing checklist in `CONTRIBUTING.md`, which includes:

- Realtime face swap functionality
- Camera listing
- FPS performance
- GPU stability
- Application responsiveness

Both automated and manual testing help ensure the quality of Deep-Live-Cam.
