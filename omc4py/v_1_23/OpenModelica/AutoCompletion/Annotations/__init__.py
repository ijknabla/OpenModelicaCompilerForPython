from __future__ import annotations as _

from dataclasses import dataclass
from typing import List, Union

from omc4py.modelica import enumeration, record
from omc4py.openmodelica import TypeName


@dataclass(frozen=True)
class Documentation(record):
    """
    .. code-block:: modelica

        record Documentation "Defines the documentation."
          String info "The textual description of the class.";
          String revisions "A list of revisions and other annotations defined by a tool.";
        end Documentation;"""

    __omc_class__ = TypeName(
        "OpenModelica.AutoCompletion.Annotations.Documentation"
    )
    info: str
    revisions: str


@dataclass(frozen=True)
class experiment(record):
    """
    .. code-block:: modelica

        record experiment "Define default experiment parameters."
          Real StartTime(unit = "s") = 0 "Default start time of simulation.";
          Real StopTime(unit = "s") = 1 "Default stop time of simulation.";
          Real Interval(unit = "s", min = 0) = 0.002 "Resolution for the result grid.";
          Real Tolerance(min = 0) = 1e-6 "Default relative integration tolerance.";
        end experiment;"""

    __omc_class__ = TypeName(
        "OpenModelica.AutoCompletion.Annotations.experiment"
    )
    StartTime: Union[float, None]
    StopTime: Union[float, None]
    Interval: Union[float, None]
    Tolerance: Union[float, None]


@dataclass(frozen=True)
class Dialog(record):
    """
    .. code-block:: modelica

        record Dialog
          parameter String tab = "General";
          parameter String group = "Parameters";
          parameter Boolean enable = true;
          parameter Boolean showStartAttribute = false;
          parameter Boolean colorSelector = false;
          parameter Selector loadSelector;
          parameter Selector saveSelector;
          parameter String groupImage = "";
          parameter Boolean connectorSizing = false;
        end Dialog;"""

    __omc_class__ = TypeName("OpenModelica.AutoCompletion.Annotations.Dialog")
    tab: Union[str, None]
    group: Union[str, None]
    enable: Union[bool, None]
    showStartAttribute: Union[bool, None]
    colorSelector: Union[bool, None]
    loadSelector: Selector
    saveSelector: Selector
    groupImage: Union[str, None]
    connectorSizing: Union[bool, None]


@dataclass(frozen=True)
class Selector(record):
    """
    .. code-block:: modelica

        record Selector
          parameter String filter = "";
          parameter String caption = "";
        end Selector;"""

    __omc_class__ = TypeName(
        "OpenModelica.AutoCompletion.Annotations.Selector"
    )
    filter: Union[str, None]
    caption: Union[str, None]


@dataclass(frozen=True)
class uses(record):
    """
    .. code-block:: modelica

        record uses "A list of dependent classes."
        end uses;"""

    __omc_class__ = TypeName("OpenModelica.AutoCompletion.Annotations.uses")


class Access(enumeration):
    """
    .. code-block:: modelica

        type Access = enumeration(hide, icon, documentation, diagram, nonPackageText, nonPackageDuplicate, packageText, packageDuplicate);
    """

    __omc_class__ = TypeName("OpenModelica.AutoCompletion.Annotations.Access")
    hide = 1
    icon = 2
    documentation = 3
    diagram = 4
    nonPackageText = 5
    nonPackageDuplicate = 6
    packageText = 7
    packageDuplicate = 8


@dataclass(frozen=True)
class Protection(record):
    """
    .. code-block:: modelica

        record Protection "Protection of class"
          Access access "Defines what parts of a class are visible.";
          String features[:] = fill("", 0) "Required license features";

          record License
            String libraryKey;
            String licenseFile = "" "Optional, default mapping if empty";
          end License;
        end Protection;"""

    __omc_class__ = TypeName(
        "OpenModelica.AutoCompletion.Annotations.Protection"
    )
    access: Access
    features: Union[List[str], None]


@dataclass(frozen=True)
class Authorization(record):
    """
    .. code-block:: modelica

        record Authorization
          String licensor = "" "Optional string to show information about the licensor";
          String libraryKey "Matching the key in the class. Must be encrypted and not visible";
          License license[:] "Definition of the license options and of the access rights";
        end Authorization;"""

    __omc_class__ = TypeName(
        "OpenModelica.AutoCompletion.Annotations.Authorization"
    )
    licensor: Union[str, None]
    libraryKey: str
    license: List[License]


@dataclass(frozen=True)
class License(record):
    """
    .. code-block:: modelica

        record License
          String licensee = "" "Optional string to show information about the licensee";
          String id[:] "Unique machine identifications, e.g. MAC addresses";
          String features[:] = fill("", 0) "Activated library license features";
          String startDate = "" "Optional start date in UTCformat YYYY-MM-DD";
          String expirationDate = "" "Optional expiration date in UTCformat YYYY-MM-DD";
          String operations[:] = fill("", 0) "Library usage conditions";
        end License;"""

    __omc_class__ = TypeName("OpenModelica.AutoCompletion.Annotations.License")
    licensee: Union[str, None]
    id: List[str]
    features: Union[List[str], None]
    startDate: Union[str, None]
    expirationDate: Union[str, None]
    operations: Union[List[str], None]


@dataclass(frozen=True)
class inverse(record):
    """
    .. code-block:: modelica

        record inverse
        end inverse;"""

    __omc_class__ = TypeName("OpenModelica.AutoCompletion.Annotations.inverse")


@dataclass(frozen=True)
class choices(record):
    """
    .. code-block:: modelica

        record choices "Defines a suitable redeclaration or modifications of the element."
          Boolean checkBox = true "Display a checkbox to input the values false or true in the graphical user interface.";
          String choice[:] = fill("", 0) "the choices as an array of strings";
        end choices;"""

    __omc_class__ = TypeName("OpenModelica.AutoCompletion.Annotations.choices")
    checkBox: Union[bool, None]
    choice: Union[List[str], None]


@dataclass(frozen=True)
class derivative(record):
    """
    .. code-block:: modelica

        record derivative
          Integer order = 1;
          String noDerivative;
          String zeroDerivative;
        end derivative;"""

    __omc_class__ = TypeName(
        "OpenModelica.AutoCompletion.Annotations.derivative"
    )
    order: Union[int, None]
    noDerivative: str
    zeroDerivative: str


@dataclass(frozen=True)
class _OpenModelica_commandLineOptions(record):
    """
    .. code-block:: modelica

        record __OpenModelica_commandLineOptions
        end __OpenModelica_commandLineOptions;"""

    __omc_class__ = TypeName(
        "OpenModelica.AutoCompletion.Annotations.__OpenModelica_commandLineOptions"
    )


@dataclass(frozen=True)
class _OpenModelica_simulationFlags(record):
    """
    .. code-block:: modelica

        record __OpenModelica_simulationFlags
        end __OpenModelica_simulationFlags;"""

    __omc_class__ = TypeName(
        "OpenModelica.AutoCompletion.Annotations.__OpenModelica_simulationFlags"
    )
