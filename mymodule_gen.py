
import sys

from pybindgen import FileCodeSink
from pybindgen.gccxmlparser import ModuleParser

def generate():
    module_parser = ModuleParser('mymodule', '::')
    module_parser.parse(["my-module.h"], includes=['"my-module.h"'], pygen_sink=FileCodeSink(sys.stdout))

if __name__ == '__main__':
    generate()
