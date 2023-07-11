# -*clang- Python -*-

import os
import platform
import re
import subprocess
import sys

import lit.formats
import lit.util

# Configuration file for the 'lit' test runner.

# name: The name of this test suite.
config.name = 'Enzyme-JaX'

# testFormat: The test format to use to interpret tests.
#
# For now we require '&&' between commands, until they get globally killed and
# the test runner updated.
execute_external = platform.system() != 'Windows'
config.test_format = lit.formats.ShTest(execute_external)

# suffixes: A list of file extensions to treat as test files.
config.suffixes = ['.pyt']

# test_source_root: The root path where tests are located.
config.test_source_root = os.path.dirname(__file__)

# test_exec_root: The root path where tests should be run.
config.test_exec_root = os.path.dirname(__file__)

#ToolSubst('%lli', FindTool('lli'), post='.', extra_args=lli_args),

# Tweak the PATH to include the tools dir and the scripts dir.
base_paths = [os.path.join(os.path.dirname(__file__), '..', '..', 'bazel-bin', 'external', 'llvm-project', 'llvm'), config.environment['PATH']]
path = os.path.pathsep.join(base_paths) # + config.extra_paths)
config.environment['PATH'] = path

config.substitutions.append(('python', sys.executable))
