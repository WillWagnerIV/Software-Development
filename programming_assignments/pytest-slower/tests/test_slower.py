"""Testing the pytest-nice plugin."""

import pytest

@pytest.mark.yippee
def test_pass_fail(testdir):

    # create a temporary pytest test module
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2
    """)

    # run pytest
    result = testdir.runpytest()

    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines([
        '*.F*'
    ])  # . for Pass, F for Fail

    # make sure that that we get a '1' exit code for the testsuite
    assert result.ret == 1

@pytest.fixture()
def sample_test(testdir):
    testdir.makepyfile("""
        def test_pass():
            assert 1 == 1

        def test_fail():
            assert 1 == 2
    """)
    return testdir


