# Pytest configuration and shared fixtures.
# Tests that need the `arxiv` package use allow_module_level=True skip in the test module
# when arxiv is not installed, so collection succeeds and those tests are skipped.
