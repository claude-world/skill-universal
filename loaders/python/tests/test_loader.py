"""
Tests for Python Loader wrapper
"""

from skill_universal import SkillLoader, SkillConfig


def test_import():
    """Test that we can import from the wrapper"""
    loader = SkillLoader()
    assert loader is not None
