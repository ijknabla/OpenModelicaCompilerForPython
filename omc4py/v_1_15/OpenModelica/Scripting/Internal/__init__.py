from __future__ import annotations as _

from omc4py.modelica import package
from omc4py.openmodelica import TypeName
from omc4py.protocol import T_Calling

from . import Time as time


class Time(package[T_Calling]):
    __omc_class__ = TypeName("OpenModelica.Scripting.Internal.Time")
    readableTime = time.readableTime
    timerTick = time.timerTick
    timerTock = time.timerTock
    timerClear = time.timerClear
