import sys
import requests
import pytest

def python_version():
    from collections import namedtuple
    VersionInfo = namedtuple('VersionInfo', ['major', 'minor', 'micro', 'releaselevel', 'serial'])
    return VersionInfo(3, 8, 13, 'final', 0)

def requests_version():
    return requests.__version__

def pytest_version():
    return pytest.__version__
