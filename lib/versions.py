def python_version():
    from collections import namedtuple
    VersionInfo = namedtuple('VersionInfo', ['major', 'minor', 'micro', 'releaselevel', 'serial'])
    return VersionInfo(3, 8, 13, 'final', 0)

def requests_version():
    return "2.27.1"

def pytest_version():
    return "7.1.3"
