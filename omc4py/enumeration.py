from .modelica import enumeration, external


@external(".OpenModelica.AutoCompletion.Annotations.Access")
class Access__v_1_14(enumeration):
    """```modelica
    type Access = enumeration(hide, icon, documentation, diagram, nonPackageText, nonPackageDuplicate, packageText, packageDuplicate);
    ```"""

    hide = 1
    icon = 2
    documentation = 3
    diagram = 4
    nonPackageText = 5
    nonPackageDuplicate = 6
    packageText = 7
    packageDuplicate = 8


@external(".OpenModelica.Scripting.DiffFormat")
class DiffFormat__v_1_13(enumeration):
    """```modelica
    type DiffFormat = enumeration(plain "no deletions, no markup", color "terminal escape sequences", xml "XML tags");
    ```"""

    plain = 1
    color = 2
    xml = 3


@external(".OpenModelica.Scripting.ErrorKind")
class ErrorKind__v_1_13(enumeration):
    """```modelica
    type ErrorKind = enumeration(syntax "syntax errors", grammar "grammatical errors", translation "instantiation errors: up to flat modelica", symbolic "symbolic manipulation error, simcodegen, up to executable file", runtime "simulation/function runtime error", scripting "runtime scripting /interpretation error");
    ```"""

    syntax = 1
    grammar = 2
    translation = 3
    symbolic = 4
    runtime = 5
    scripting = 6


@external(".OpenModelica.Scripting.ErrorLevel")
class ErrorLevel__v_1_13(enumeration):
    """```modelica
    type ErrorLevel = enumeration(notification, warning, error);
    ```"""

    notification = 1
    warning = 2
    error = 3


@external(".OpenModelica.Scripting.ErrorLevel")
class ErrorLevel__v_1_15(enumeration):
    """```modelica
    type ErrorLevel = enumeration(internal, notification, warning, error);
    ```"""

    internal = 1
    notification = 2
    warning = 3
    error = 4


@external(".OpenModelica.Scripting.ExportKind")
class ExportKind__v_1_13(enumeration):
    """```modelica
    type ExportKind = enumeration(Absyn "Normal Absyn", SCode "Normal SCode", MetaModelicaInterface "A restricted MetaModelica package interface (protected parts are stripped)", Internal "True unparsing of the Absyn");
    ```"""

    Absyn = 1
    SCode = 2
    MetaModelicaInterface = 3
    Internal = 4


@external(".OpenModelica.Scripting.Internal.FileType")
class FileType__v_1_13(enumeration):
    """```modelica
    type FileType = enumeration(NoFile, RegularFile, Directory, SpecialFile);
    ```"""

    NoFile = 1
    RegularFile = 2
    Directory = 3
    SpecialFile = 4


@external(".OpenModelica.Scripting.LinearSystemSolver")
class LinearSystemSolver__v_1_13(enumeration):
    """```modelica
    type LinearSystemSolver = enumeration(dgesv, lpsolve55);
    ```"""

    dgesv = 1
    lpsolve55 = 2


@external(".OpenModelica.Scripting.StandardStream")
class StandardStream__v_1_13(enumeration):
    """```modelica
    type StandardStream = enumeration(stdin, stdout, stderr);
    ```"""

    stdin = 1
    stdout = 2
    stderr = 3


@external(".OpenModelica.Scripting.oms_causality")
class oms_causality__v_1_14(enumeration):
    """```modelica
    type oms_causality = enumeration(oms_causality_input, oms_causality_output, oms_causality_parameter, oms_causality_bidir, oms_causality_undefined);
    ```"""

    oms_causality_input = 1
    oms_causality_output = 2
    oms_causality_parameter = 3
    oms_causality_bidir = 4
    oms_causality_undefined = 5


@external(".OpenModelica.Scripting.oms_fault_type")
class oms_fault_type__v_1_15(enumeration):
    """```modelica
    type oms_fault_type = enumeration(oms_fault_type_bias, oms_fault_type_gain, oms_fault_type_const);
    ```"""

    oms_fault_type_bias = 1
    oms_fault_type_gain = 2
    oms_fault_type_const = 3


@external(".OpenModelica.Scripting.oms_signal_type")
class oms_signal_type__v_1_14(enumeration):
    """```modelica
    type oms_signal_type = enumeration(oms_signal_type_real, oms_signal_type_integer, oms_signal_type_boolean, oms_signal_type_string, oms_signal_type_enum, oms_signal_type_bus);
    ```"""

    oms_signal_type_real = 1
    oms_signal_type_integer = 2
    oms_signal_type_boolean = 3
    oms_signal_type_string = 4
    oms_signal_type_enum = 5
    oms_signal_type_bus = 6


@external(".OpenModelica.Scripting.oms_solver")
class oms_solver__v_1_14(enumeration):
    """```modelica
    type oms_solver = enumeration(oms_solver_none, oms_solver_sc_min, oms_solver_sc_explicit_euler, oms_solver_sc_cvode, oms_solver_sc_max, oms_solver_wc_min, oms_solver_wc_ma, oms_solver_wc_mav, oms_solver_wc_assc, oms_solver_wc_mav2, oms_solver_wc_max);
    ```"""

    oms_solver_none = 1
    oms_solver_sc_min = 2
    oms_solver_sc_explicit_euler = 3
    oms_solver_sc_cvode = 4
    oms_solver_sc_max = 5
    oms_solver_wc_min = 6
    oms_solver_wc_ma = 7
    oms_solver_wc_mav = 8
    oms_solver_wc_assc = 9
    oms_solver_wc_mav2 = 10
    oms_solver_wc_max = 11


@external(".OpenModelica.Scripting.oms_system")
class oms_system__v_1_14(enumeration):
    """```modelica
    type oms_system = enumeration(oms_system_none, oms_system_tlm, oms_system_wc, oms_system_sc);
    ```"""

    oms_system_none = 1
    oms_system_tlm = 2
    oms_system_wc = 3
    oms_system_sc = 4


@external(".OpenModelica.Scripting.oms_tlm_domain")
class oms_tlm_domain__v_1_14(enumeration):
    """```modelica
    type oms_tlm_domain = enumeration(oms_tlm_domain_input, oms_tlm_domain_output, oms_tlm_domain_mechanical, oms_tlm_domain_rotational, oms_tlm_domain_hydraulic, oms_tlm_domain_electric);
    ```"""

    oms_tlm_domain_input = 1
    oms_tlm_domain_output = 2
    oms_tlm_domain_mechanical = 3
    oms_tlm_domain_rotational = 4
    oms_tlm_domain_hydraulic = 5
    oms_tlm_domain_electric = 6


@external(".OpenModelica.Scripting.oms_tlm_interpolation")
class oms_tlm_interpolation__v_1_14(enumeration):
    """```modelica
    type oms_tlm_interpolation = enumeration(oms_tlm_no_interpolation, oms_tlm_coarse_grained, oms_tlm_fine_grained);
    ```"""

    oms_tlm_no_interpolation = 1
    oms_tlm_coarse_grained = 2
    oms_tlm_fine_grained = 3
