
from .. import parsers

from . import (
    StrOrPathLike,
    InteractiveOMC,
)


def bootstrap(
    omc_command: StrOrPathLike
):
    with InteractiveOMC.open(omc_command) as omc:
        component_record_decl = omc.execute(
            "getComponentsTest("
            "    OpenModelica.Scripting.getComponentsTest.Component"
            ")"
        )

    tree = parsers.omc_value_parser.parse(component_record_decl)
    print(tree)
