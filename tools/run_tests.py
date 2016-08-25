""" run_tests.py """
import sys
import os
import yaml

from . import base


class Config(object):
    """
    Load the vBuild configuration from vbuild.yaml
    """

    def __init__(self, base_dir):
        self.base_dir = base_dir
        yaml_path = os.path.join(base_dir, 'vbuild.yaml')
        with open(yaml_path, 'r') as vbuild_config:
            self.config = yaml.load(vbuild_config)

    @property
    def code_directories(self):
        """
        A list of code directories the project depends upon
        """
        return self.config.get('code-directories', [])

    @property
    def libraries(self):
        """
        A list of code directories the project depends upon
        """
        return self.config.get('libraries', [])

    @property
    def environment_variables(self):
        """
        A list of environment variables the project depends upon
        """
        return self.config.get('env_variables', [])

    @staticmethod
    def _insert_path(path):
        """
        Add path to sys.path
        """
        if os.path.exists(path):
            if path not in sys.path:
                sys.path.insert(1, path)

    def prepare_code_directories(self):
        """
        Add code directories to sys.path
        """
        fixed_paths = []
        for code_directory in self.code_directories:
            path = os.path.abspath(os.path.join(self.base_dir, code_directory))
            self._insert_path(path)
            fixed_paths.append(path)
        return fixed_paths

    def prepare_libraries(self):
        """
        Add libraries to sys.path
        """
        fixed_paths = []
        appengine_path = base.get_google_appengine_path()
        self._insert_path(appengine_path)
        fixed_paths.append(appengine_path)

        for library in self.libraries:

            format_string = "{0}"
            format_args = [library['name']]

            if 'version' in library:
                format_string += "-{1}"
                format_args.append(library['version'])

            library_name = format_string.format(*format_args)

            path = os.path.join(appengine_path, "lib", library_name)
            self._insert_path(path)
            fixed_paths.append(path)

        return fixed_paths

    def prepare_environment_variables(self):
        """
        Add environment variables to os.environ
        """
        for env_variable in self.environment_variables:
            for k, v in env_variable.iteritems():
                os.environ[k] = v

    def setup_python_path(self):
        """
        Add code directories to sys.path and configure any required environment variables
        """
        self.prepare_environment_variables()
        fixed_paths = self.prepare_libraries()
        fixed_paths += self.prepare_code_directories()
        return fixed_paths
