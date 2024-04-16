from __future__ import annotations as _

from omc4py.modelica import package
from omc4py.openmodelica import TypeName
from omc4py.protocol import T_Calling


class ReleaseNotes(package[T_Calling]):
    __omc_class__ = TypeName("OpenModelica.UsersGuide.ReleaseNotes")
