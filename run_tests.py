#!/usr/bin/env python3
"""
Simple test runner script for Deep-Live-Cam.
This makes it easy to run tests without needing to know pytest commands.
"""
import sys
import subprocess


def main():
    """Run the test suite."""
    print("=" * 70)
    print("Deep-Live-Cam Test Suite")
    print("=" * 70)
    print()
    
    # Check if pytest is installed
    try:
        import pytest
    except ImportError:
        print("ERROR: pytest is not installed.")
        print("Please install test dependencies with:")
        print("  pip install -r requirements-dev.txt")
        return 1
    
    # Run pytest with default arguments
    print("Running tests...")
    print()
    
    # Run pytest programmatically
    args = ["-v", "--tb=short", "tests/"]
    if len(sys.argv) > 1:
        # Allow passing custom arguments
        args = sys.argv[1:] + ["tests/"]
    
    return pytest.main(args)


if __name__ == "__main__":
    sys.exit(main())
