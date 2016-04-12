# create an .exe file

import sys
import cx_Freeze

build_exe_options = {"packages": ["sys", "os", "re", "argparse"]}

ex = [cx_Freeze.Executable(
	"agrep.py")]

cx_Freeze.setup(name = "agrep",
	version = "1.2",
	description = "ASCII grep tool",
	options = {"build_exe": build_exe_options},
	executables = ex);