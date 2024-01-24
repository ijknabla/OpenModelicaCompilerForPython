from __future__ import annotations as _

from omc4py.modelica import package
from omc4py.openmodelica import TypeName
from omc4py.protocol import T_Calling

from . import Annotations as annotations


class Annotations(package[T_Calling]):
    __omc_class__ = TypeName("OpenModelica.AutoCompletion.Annotations")
    Documentation = annotations.Documentation
    experiment = annotations.experiment
    Dialog = annotations.Dialog
    Selector = annotations.Selector
    uses = annotations.uses
    Access = annotations.Access
    Protection = annotations.Protection
    Authorization = annotations.Authorization
    License = annotations.License
    inverse = annotations.inverse
    choices = annotations.choices
    derivative = annotations.derivative
    _OpenModelica_commandLineOptions = (
        annotations._OpenModelica_commandLineOptions
    )
    _OpenModelica_simulationFlags = annotations._OpenModelica_simulationFlags
