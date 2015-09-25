"""Module to identify all unit tests that need to run and return a TestSuite object to be run"""

import logging
import os
import re
import sys
import teamcity
import unittest

from teamcity.unittestpy import TeamcityTestRunner

pt = os.getcwd()
root_dir = pt
loglevel = int(os.environ.get('UNITTEST_LOGLEVEL', logging.CRITICAL))
loglevel_disable = int(os.environ.get('UNITTEST_LOGLEVEL_DISABLE', logging.CRITICAL))
logging.getLogger().setLevel(loglevel)  # DEBUG, LOG, WARN, ERROR(?) are too chatty
logging.disable(loglevel_disable)

TEST_MODULES = [
    'test'
]

COVERAGE_OMIT_PATHS = [
    'test/*', 'src/lib/*','src/app/views/*', 'tools/*', 'src/remote_scripts/*', '/usr/local/google_appengine/*' , 'C:\Program Files (x86)\Google\google_appengine/*',
    '/Applications/GoogleAppEngineLauncher.app/Contents/Resources/GoogleAppEngine-default.bundle/Contents/Resources/google_appengine/*'
]

COVERAGE_INCLUDE_PATHS = [
    'src/*', 'src/domain/*', 'src/handlers/*', 'src/models/*'
]


def set_sys_path():
    """
    Set system path to be sure src, lib, webapp2_lib directories are included in sys.path
    """
    current_path = os.path.abspath(os.path.dirname(__file__))
    src_path = os.path.join(current_path, 'src')
    test_path = os.path.join(current_path, 'test')
    test_lib_path = os.path.join(test_path, 'lib')
    lib_path = os.path.join(src_path, 'lib')
    tools_path = os.path.join(current_path, "tools")
    tools_lib_path = os.path.join(tools_path, "lib")

    # Add lib as primary libraries directory, with fallback to lib/dist
    # and optionally to lib/dist.zip, loaded using zipimport.
    sys.path[0:0] = [
        src_path,
        lib_path,
        os.path.join(lib_path, 'webapp2_lib'),
        test_lib_path,
        tools_path,
        tools_lib_path
    ]


def convert_module_path(module):
    """Helper method to convert a module in dot notation to
    a proper file path"""
    path_bits = module.split(".")
    return os.path.sep.join(path_bits)


def suite():
    """Iterate across all of the modules in TEST_MODULES, find all of the
    tests within and return a TestSuite which will run them all"""
    try:
        test_suite = unittest.TestSuite()

        TEST_RE = r"^.*_tests?\.py$"

        # Search through every file inside this package.
        for module in TEST_MODULES:
            test_dir = os.path.join(root_dir, convert_module_path(module))

            try: 
                for filename in os.listdir(test_dir):
                    
                    if os.path.isdir(os.path.join(test_dir, filename)) and not filename.startswith("."):
                        TEST_MODULES.append(module + "." + filename)
                        continue

                    if not re.match(TEST_RE, filename):
                        continue

                    # Import the test file and find all TestClass clases inside it.
                    module_name = '%s.%s' % (module, filename[:-3])
                    test_module = __import__(module_name, {}, {}, filename[:-3])
                    test_suite.addTest(unittest.TestLoader().loadTestsFromModule(test_module))
            except OSError:
                pass  # Ignore directories that are not found

        return test_suite

    except Exception as e:
        logging.critical("Error loading tests. %s" % e.message, exc_info=1)
        raise SystemExit("Error loading tests. %s" % e.message)

if __name__ == "__main__":

    coverage_report_dir = os.environ.get('CODE_COVERAGE_DIR')
    
    if coverage_report_dir:
        from coverage import coverage
        cov = coverage(timid=True, include=COVERAGE_INCLUDE_PATHS, omit=COVERAGE_OMIT_PATHS)
        cov.start() # need to do this as early as possible to "catch" the import statements

    if len(sys.argv) > 1:
        # tests specified
        test_suite = unittest.TestLoader().loadTestsFromNames(sys.argv[1:])
    else:
        test_suite = suite()
    if teamcity.underTeamcity():
        result = TeamcityTestRunner().run(test_suite)
    else:
        result = unittest.TextTestRunner(verbosity=int(os.environ.get('UNITTEST_VERBOSITY', 1))).run(test_suite)

    if coverage_report_dir:
        cov.stop()
        cov.html_report(directory=coverage_report_dir)
        cov.erase()

    if result.failures or result.errors:
        exit(1)
