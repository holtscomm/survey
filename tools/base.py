"""
Common utilities used within the build process.
"""
import os
import fnmatch
from collections import OrderedDict
import yaml


class PathContext(object):
    """PathContext manager for changing the current working directory"""
    def __init__(self, new_path):
        self.new_path = new_path

    def __enter__(self):
        self.saved_path = os.getcwd()
        os.chdir(self.new_path)

    def __exit__(self, etype, value, traceback):
        os.chdir(self.saved_path)


def get_google_appengine_path():
    """
    return path of google appengine
    """
    path = None
    possible_paths = [
        os.path.join('/', 'usr', 'local', 'google_appengine'),
        os.path.join('/', 'usr', 'local', 'google-cloud-sdk', 'platform', 'google_appengine'),
        os.path.join('C:', 'Program Files (x86)', 'Google', 'google_appengine'),
        os.path.join('C:', 'Program Files', 'Google', 'google_appengine'),
        os.path.join(os.path.expanduser("~"), 'google-cloud-sdk', 'platform', 'google_appengine'),
        os.path.join('/', 'google-cloud-sdk', 'platform', 'google_appengine'),
    ]
    sdk_root = os.environ.get('GAE_SDK_ROOT')
    if sdk_root:
        possible_paths.append(os.path.join(sdk_root, "google_appengine"))
    for possible in possible_paths:
        possible = os.path.realpath(possible)
        if os.path.exists(possible):
            path = possible
    if not path:
        raise ValueError("Cannot find Google appengine path")
    return path


def get_module_configuration(environment, base_dir):
    """
    Load the configuration for the specified environment.
    """
    yaml_path = os.path.join(base_dir, 'vbuild.yaml')
    with open(yaml_path, 'r') as vbuild_config:
        config = yaml.load(vbuild_config)
    return config.get(environment)


def find_files(directory, include_pattern, exclude_patterns=None):
    """
    Return a list of files within a directory matching the specified pattern.
    """
    if exclude_patterns is None:
        exclude_patterns = []
    if not isinstance(exclude_patterns, list):
        exclude_patterns = [exclude_patterns]

    matches = []
    for root, _, file_names in os.walk(directory):
        for filename in fnmatch.filter(file_names, include_pattern):
            match = True
            include_file = os.path.join(root, filename)
            for exclude_pattern in exclude_patterns:
                if fnmatch.fnmatch(include_file, exclude_pattern):
                    match = False
            if match:
                matches.append(include_file)
    return matches


def ordered_load(stream, Loader=None, object_pairs_hook=OrderedDict):
    """
    Maintain the order of a yaml files keys when loading.
    """
    if Loader is None:
        Loader = yaml.Loader

    class OrderedLoader(Loader):
        pass

    def construct_mapping(loader, node):
        loader.flatten_mapping(node)
        return object_pairs_hook(loader.construct_pairs(node))

    OrderedLoader.add_constructor(
        yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
        construct_mapping)
    return yaml.load(stream, OrderedLoader)


def ordered_dump(data, stream=None, Dumper=None, **kwds):
    """
    Maintain the order of a yaml files keys when dumping.
    """
    if Dumper is None:
        Dumper = yaml.Dumper

    class OrderedDumper(Dumper):
        pass

    def _dict_representer(dumper, data):
        return dumper.represent_mapping(
            yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
            data.items())

    OrderedDumper.add_representer(OrderedDict, _dict_representer)
    return yaml.dump(data, stream, OrderedDumper, **kwds)
