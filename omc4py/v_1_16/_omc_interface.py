
from omc4py.classes import (
    AbstractOMCSession,
    Boolean,
    Component,
    Integer,
    ModelicaEnumeration,
    ModelicaFunction,
    ModelicaPackage,
    ModelicaRecord,
    Real,
    String,
    TypeName,
    VariableName,
    alias,
    element,
    enum,
    external,
    modelica_name,
)

from omc4py.parser import parse_OMCValue__v_1_13 as parse_OMCValue

from omc4py.session import OMCSessionBase__v_1_13 as OMCSessionBase


@modelica_name('OpenModelica')
class OpenModelica(
    ModelicaPackage,
):
    @modelica_name('OpenModelica.Scripting')
    class Scripting(
        ModelicaPackage,
    ):
        @modelica_name('OpenModelica.Scripting.CheckSettingsResult')
        class CheckSettingsResult(
            ModelicaRecord,
        ):
            """
```modelica
record CheckSettingsResult
  String OPENMODELICAHOME, OPENMODELICALIBRARY, OMC_PATH, SYSTEM_PATH, OMDEV_PATH;
  Boolean OMC_FOUND;
  String MODELICAUSERCFLAGS, WORKING_DIRECTORY;
  Boolean CREATE_FILE_WORKS, REMOVE_FILE_WORKS;
  String OS, SYSTEM_INFO, SENDDATALIBS, C_COMPILER, C_COMPILER_VERSION;
  Boolean C_COMPILER_RESPONDING, HAVE_CORBA;
  String CONFIGURE_CMDLINE;
  annotation(
    preferredView = "text");
end CheckSettingsResult;
```
            """
            @element
            def OPENMODELICAHOME(cls):
                return Component(String)

            @element
            def OPENMODELICALIBRARY(cls):
                return Component(String)

            @element
            def OMC_PATH(cls):
                return Component(String)

            @element
            def SYSTEM_PATH(cls):
                return Component(String)

            @element
            def OMDEV_PATH(cls):
                return Component(String)

            @element
            def OMC_FOUND(cls):
                return Component(Boolean)

            @element
            def MODELICAUSERCFLAGS(cls):
                return Component(String)

            @element
            def WORKING_DIRECTORY(cls):
                return Component(String)

            @element
            def CREATE_FILE_WORKS(cls):
                return Component(Boolean)

            @element
            def REMOVE_FILE_WORKS(cls):
                return Component(Boolean)

            @element
            def OS(cls):
                return Component(String)

            @element
            def SYSTEM_INFO(cls):
                return Component(String)

            @element
            def SENDDATALIBS(cls):
                return Component(String)

            @element
            def C_COMPILER(cls):
                return Component(String)

            @element
            def C_COMPILER_VERSION(cls):
                return Component(String)

            @element
            def C_COMPILER_RESPONDING(cls):
                return Component(Boolean)

            @element
            def HAVE_CORBA(cls):
                return Component(Boolean)

            @element
            def CONFIGURE_CMDLINE(cls):
                return Component(String)

        @modelica_name('OpenModelica.Scripting.Internal')
        class Internal(
            ModelicaPackage,
        ):
            @modelica_name('OpenModelica.Scripting.Internal.Time')
            class Time(
                ModelicaPackage,
            ):
                @modelica_name('OpenModelica.Scripting.Internal.Time.readableTime')
                class readableTime(
                    ModelicaFunction,
                ):
                    """
```modelica
function readableTime
  input Real sec;
  output String str;
end readableTime;
```
                    """
                    @external
                    def _(
                        _cls_,
                        _session_: AbstractOMCSession,
                        sec,
                    ):
                        return _session_.__omc__.call_function(
                            funcName='OpenModelica.Scripting.Internal.Time.readableTime',
                            inputArguments=[
                                (Component(Real), 'sec', sec, 'required'),
                            ],
                            outputArguments=[
                                (Component(String), 'str'),
                            ],
                            parser=parse_OMCValue,
                        )

                @modelica_name('OpenModelica.Scripting.Internal.Time.timerTick')
                class timerTick(
                    ModelicaFunction,
                ):
                    """
```modelica
function timerTick
  input Integer index;
end timerTick;
```
                    """
                    @external
                    def _(
                        _cls_,
                        _session_: AbstractOMCSession,
                        index,
                    ):
                        return _session_.__omc__.call_function(
                            funcName='OpenModelica.Scripting.Internal.Time.timerTick',
                            inputArguments=[
                                (Component(Integer), 'index', index, 'required'),
                            ],
                            outputArguments=[
                            ],
                            parser=parse_OMCValue,
                        )

                @modelica_name('OpenModelica.Scripting.Internal.Time.timerTock')
                class timerTock(
                    ModelicaFunction,
                ):
                    """
```modelica
function timerTock
  input Integer index;
  output Real elapsed;
end timerTock;
```
                    """
                    @external
                    def _(
                        _cls_,
                        _session_: AbstractOMCSession,
                        index,
                    ):
                        return _session_.__omc__.call_function(
                            funcName='OpenModelica.Scripting.Internal.Time.timerTock',
                            inputArguments=[
                                (Component(Integer), 'index', index, 'required'),
                            ],
                            outputArguments=[
                                (Component(Real), 'elapsed'),
                            ],
                            parser=parse_OMCValue,
                        )

                @modelica_name('OpenModelica.Scripting.Internal.Time.timerClear')
                class timerClear(
                    ModelicaFunction,
                ):
                    """
```modelica
function timerClear
  input Integer index;
end timerClear;
```
                    """
                    @external
                    def _(
                        _cls_,
                        _session_: AbstractOMCSession,
                        index,
                    ):
                        return _session_.__omc__.call_function(
                            funcName='OpenModelica.Scripting.Internal.Time.timerClear',
                            inputArguments=[
                                (Component(Integer), 'index', index, 'required'),
                            ],
                            outputArguments=[
                            ],
                            parser=parse_OMCValue,
                        )

            @modelica_name('OpenModelica.Scripting.Internal.FileType')
            class FileType(
                ModelicaEnumeration,
            ):
                """
```modelica
type FileType = enumeration(NoFile, RegularFile, Directory, SpecialFile);
```
                """
                NoFile = enum.auto()
                RegularFile = enum.auto()
                Directory = enum.auto()
                SpecialFile = enum.auto()

            @modelica_name('OpenModelica.Scripting.Internal.stat')
            class stat(
                ModelicaFunction,
            ):
                """
```modelica
function stat
  input String name;
  output FileType fileType;
end stat;
```
                """
                @external
                def _(
                    _cls_,
                    _session_: AbstractOMCSession,
                    name,
                ):
                    return _session_.__omc__.call_function(
                        funcName='OpenModelica.Scripting.Internal.stat',
                        inputArguments=[
                            (Component(String), 'name', name, 'required'),
                        ],
                        outputArguments=[
                            (Component(OpenModelica.Scripting.Internal.FileType), 'fileType'),
                        ],
                        parser=parse_OMCValue,
                    )

        @modelica_name('OpenModelica.Scripting.checkSettings')
        class checkSettings(
            ModelicaFunction,
        ):
            """
```modelica
function checkSettings
  output CheckSettingsResult result;
end checkSettings;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='checkSettings',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(OpenModelica.Scripting.CheckSettingsResult), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.loadFile')
        class loadFile(
            ModelicaFunction,
        ):
            """
```modelica
function loadFile
  input String fileName;
  input String encoding = "UTF-8";
  input Boolean uses = true;
  input Boolean notify = true "Give a notification of the libraries and versions that were loaded";
  input Boolean requireExactVersion = false "If the version is required to be exact, if there is a uses Modelica(version=\\"3.2\\"), Modelica 3.2.1 will not match it.";
  output Boolean success;
end loadFile;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
                encoding=None,
                uses=None,
                notify=None,
                requireExactVersion=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='loadFile',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                        (Component(String), 'encoding', encoding, 'optional'),
                        (Component(Boolean), 'uses', uses, 'optional'),
                        (Component(Boolean), 'notify', notify, 'optional'),
                        (Component(Boolean), 'requireExactVersion', requireExactVersion, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.loadFiles')
        class loadFiles(
            ModelicaFunction,
        ):
            """
```modelica
function loadFiles
  input String[:] fileNames;
  input String encoding = "UTF-8";
  input Integer numThreads = OpenModelica.Scripting.numProcessors();
  input Boolean uses = true;
  input Boolean notify = true "Give a notification of the libraries and versions that were loaded";
  input Boolean requireExactVersion = false "If the version is required to be exact, if there is a uses Modelica(version=\\"3.2\\"), Modelica 3.2.1 will not match it.";
  output Boolean success;
end loadFiles;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileNames,
                encoding=None,
                numThreads=None,
                uses=None,
                notify=None,
                requireExactVersion=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='loadFiles',
                    inputArguments=[
                        (Component(String)[:], 'fileNames', fileNames, 'required'),
                        (Component(String), 'encoding', encoding, 'optional'),
                        (Component(Integer), 'numThreads', numThreads, 'optional'),
                        (Component(Boolean), 'uses', uses, 'optional'),
                        (Component(Boolean), 'notify', notify, 'optional'),
                        (Component(Boolean), 'requireExactVersion', requireExactVersion, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.parseEncryptedPackage')
        class parseEncryptedPackage(
            ModelicaFunction,
        ):
            """
```modelica
function parseEncryptedPackage
  input String fileName;
  input String workdir = "<default>" "The output directory for imported encrypted files. <default> will put the files to current working directory.";
  output TypeName names[:];
end parseEncryptedPackage;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
                workdir=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='parseEncryptedPackage',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                        (Component(String), 'workdir', workdir, 'optional'),
                    ],
                    outputArguments=[
                        (Component(TypeName)[:], 'names'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.loadEncryptedPackage')
        class loadEncryptedPackage(
            ModelicaFunction,
        ):
            """
```modelica
function loadEncryptedPackage
  input String fileName;
  input String workdir = "<default>" "The output directory for imported encrypted files. <default> will put the files to current working directory.";
  input Boolean skipUnzip = false "Skips the unzip of .mol if true. In that case we expect the files are already extracted e.g., because of parseEncryptedPackage() call.";
  input Boolean uses = true;
  input Boolean notify = true "Give a notification of the libraries and versions that were loaded";
  input Boolean requireExactVersion = false "If the version is required to be exact, if there is a uses Modelica(version=\\"3.2\\"), Modelica 3.2.1 will not match it.";
  output Boolean success;
end loadEncryptedPackage;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
                workdir=None,
                skipUnzip=None,
                uses=None,
                notify=None,
                requireExactVersion=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='loadEncryptedPackage',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                        (Component(String), 'workdir', workdir, 'optional'),
                        (Component(Boolean), 'skipUnzip', skipUnzip, 'optional'),
                        (Component(Boolean), 'uses', uses, 'optional'),
                        (Component(Boolean), 'notify', notify, 'optional'),
                        (Component(Boolean), 'requireExactVersion', requireExactVersion, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.reloadClass')
        class reloadClass(
            ModelicaFunction,
        ):
            """
```modelica
function reloadClass
  input TypeName name;
  input String encoding = "UTF-8";
  output Boolean success;
end reloadClass;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                name,
                encoding=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='reloadClass',
                    inputArguments=[
                        (Component(TypeName), 'name', name, 'required'),
                        (Component(String), 'encoding', encoding, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.loadString')
        class loadString(
            ModelicaFunction,
        ):
            """
```modelica
function loadString
  input String data;
  input String filename = "<interactive>";
  input String encoding = "UTF-8";
  input Boolean merge = false "if merge is true the parsed AST is merged with the existing AST, default to false which means that is replaced, not merged";
  output Boolean success;
end loadString;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                data,
                filename=None,
                encoding=None,
                merge=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='loadString',
                    inputArguments=[
                        (Component(String), 'data', data, 'required'),
                        (Component(String), 'filename', filename, 'optional'),
                        (Component(String), 'encoding', encoding, 'optional'),
                        (Component(Boolean), 'merge', merge, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.parseString')
        class parseString(
            ModelicaFunction,
        ):
            """
```modelica
function parseString
  input String data;
  input String filename = "<interactive>";
  output TypeName names[:];
end parseString;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                data,
                filename=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='parseString',
                    inputArguments=[
                        (Component(String), 'data', data, 'required'),
                        (Component(String), 'filename', filename, 'optional'),
                    ],
                    outputArguments=[
                        (Component(TypeName)[:], 'names'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.parseFile')
        class parseFile(
            ModelicaFunction,
        ):
            """
```modelica
function parseFile
  input String filename;
  input String encoding = "UTF-8";
  output TypeName names[:];
end parseFile;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                filename,
                encoding=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='parseFile',
                    inputArguments=[
                        (Component(String), 'filename', filename, 'required'),
                        (Component(String), 'encoding', encoding, 'optional'),
                    ],
                    outputArguments=[
                        (Component(TypeName)[:], 'names'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.loadFileInteractiveQualified')
        class loadFileInteractiveQualified(
            ModelicaFunction,
        ):
            """
```modelica
function loadFileInteractiveQualified
  input String filename;
  input String encoding = "UTF-8";
  output TypeName names[:];
end loadFileInteractiveQualified;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                filename,
                encoding=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='loadFileInteractiveQualified',
                    inputArguments=[
                        (Component(String), 'filename', filename, 'required'),
                        (Component(String), 'encoding', encoding, 'optional'),
                    ],
                    outputArguments=[
                        (Component(TypeName)[:], 'names'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.loadFileInteractive')
        class loadFileInteractive(
            ModelicaFunction,
        ):
            """
```modelica
function loadFileInteractive
  input String filename;
  input String encoding = "UTF-8";
  input Boolean uses = true;
  input Boolean notify = true "Give a notification of the libraries and versions that were loaded";
  input Boolean requireExactVersion = false "If the version is required to be exact, if there is a uses Modelica(version=\\"3.2\\"), Modelica 3.2.1 will not match it.";
  output TypeName names[:];
end loadFileInteractive;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                filename,
                encoding=None,
                uses=None,
                notify=None,
                requireExactVersion=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='loadFileInteractive',
                    inputArguments=[
                        (Component(String), 'filename', filename, 'required'),
                        (Component(String), 'encoding', encoding, 'optional'),
                        (Component(Boolean), 'uses', uses, 'optional'),
                        (Component(Boolean), 'notify', notify, 'optional'),
                        (Component(Boolean), 'requireExactVersion', requireExactVersion, 'optional'),
                    ],
                    outputArguments=[
                        (Component(TypeName)[:], 'names'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.system')
        class system(
            ModelicaFunction,
        ):
            """
```modelica
impure function system
  input String callStr "String to call: sh -c $callStr";
  input String outputFile = "" "The output is redirected to this file (unless already done by callStr)";
  output Integer retval "Return value of the system call; usually 0 on success";
end system;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                callStr,
                outputFile=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='system',
                    inputArguments=[
                        (Component(String), 'callStr', callStr, 'required'),
                        (Component(String), 'outputFile', outputFile, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'retval'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.system_parallel')
        class system_parallel(
            ModelicaFunction,
        ):
            """
```modelica
impure function system_parallel
  input String callStr[:] "String to call: sh -c $callStr";
  input Integer numThreads = numProcessors();
  output Integer retval[:] "Return value of the system call; usually 0 on success";
end system_parallel;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                callStr,
                numThreads=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='system_parallel',
                    inputArguments=[
                        (Component(String)[:], 'callStr', callStr, 'required'),
                        (Component(Integer), 'numThreads', numThreads, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Integer)[:], 'retval'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.saveAll')
        class saveAll(
            ModelicaFunction,
        ):
            """
```modelica
function saveAll
  input String fileName;
  output Boolean success;
end saveAll;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
            ):
                return _session_.__omc__.call_function(
                    funcName='saveAll',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.help')
        class help(
            ModelicaFunction,
        ):
            """
```modelica
function help
  input String topic = "topics";
  output String helpText;
end help;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                topic=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='help',
                    inputArguments=[
                        (Component(String), 'topic', topic, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'helpText'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.clear')
        class clear(
            ModelicaFunction,
        ):
            """
```modelica
function clear
  output Boolean success;
end clear;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='clear',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.clearProgram')
        class clearProgram(
            ModelicaFunction,
        ):
            """
```modelica
function clearProgram
  output Boolean success;
end clearProgram;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='clearProgram',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.clearVariables')
        class clearVariables(
            ModelicaFunction,
        ):
            """
```modelica
function clearVariables
  output Boolean success;
end clearVariables;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='clearVariables',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.generateHeader')
        class generateHeader(
            ModelicaFunction,
        ):
            """
```modelica
function generateHeader
  input String fileName;
  output Boolean success;
end generateHeader;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
            ):
                return _session_.__omc__.call_function(
                    funcName='generateHeader',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.generateJuliaHeader')
        class generateJuliaHeader(
            ModelicaFunction,
        ):
            """
```modelica
function generateJuliaHeader
  input String fileName;
  output Boolean success;
end generateJuliaHeader;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
            ):
                return _session_.__omc__.call_function(
                    funcName='generateJuliaHeader',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.generateSeparateCode')
        class generateSeparateCode(
            ModelicaFunction,
        ):
            """
```modelica
function generateSeparateCode
  input TypeName className;
  input Boolean cleanCache = false "If true, the cache is reset between each generated package. This conserves memory at the cost of speed.";
  output Boolean success;
end generateSeparateCode;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                cleanCache=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='generateSeparateCode',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(Boolean), 'cleanCache', cleanCache, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.generateSeparateCodeDependencies')
        class generateSeparateCodeDependencies(
            ModelicaFunction,
        ):
            """
```modelica
function generateSeparateCodeDependencies
  input String stampSuffix = ".c" "Suffix to add to dependencies (often .c.stamp)";
  output String[:] dependencies;
end generateSeparateCodeDependencies;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                stampSuffix=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='generateSeparateCodeDependencies',
                    inputArguments=[
                        (Component(String), 'stampSuffix', stampSuffix, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'dependencies'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.generateSeparateCodeDependenciesMakefile')
        class generateSeparateCodeDependenciesMakefile(
            ModelicaFunction,
        ):
            """
```modelica
function generateSeparateCodeDependenciesMakefile
  input String filename "The file to write the makefile to";
  input String directory = "" "The relative path of the generated files";
  input String suffix = ".c" "Often .stamp since we do not update all the files";
  output Boolean success;
end generateSeparateCodeDependenciesMakefile;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                filename,
                directory=None,
                suffix=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='generateSeparateCodeDependenciesMakefile',
                    inputArguments=[
                        (Component(String), 'filename', filename, 'required'),
                        (Component(String), 'directory', directory, 'optional'),
                        (Component(String), 'suffix', suffix, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getLinker')
        class getLinker(
            ModelicaFunction,
        ):
            """
```modelica
function getLinker
  output String linker;
end getLinker;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getLinker',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'linker'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setLinker')
        class setLinker(
            ModelicaFunction,
        ):
            """
```modelica
function setLinker
  input String linker;
  output Boolean success;
end setLinker;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                linker,
            ):
                return _session_.__omc__.call_function(
                    funcName='setLinker',
                    inputArguments=[
                        (Component(String), 'linker', linker, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getLinkerFlags')
        class getLinkerFlags(
            ModelicaFunction,
        ):
            """
```modelica
function getLinkerFlags
  output String linkerFlags;
end getLinkerFlags;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getLinkerFlags',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'linkerFlags'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setLinkerFlags')
        class setLinkerFlags(
            ModelicaFunction,
        ):
            """
```modelica
function setLinkerFlags
  input String linkerFlags;
  output Boolean success;
end setLinkerFlags;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                linkerFlags,
            ):
                return _session_.__omc__.call_function(
                    funcName='setLinkerFlags',
                    inputArguments=[
                        (Component(String), 'linkerFlags', linkerFlags, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getCompiler')
        class getCompiler(
            ModelicaFunction,
        ):
            """
```modelica
function getCompiler
  output String compiler;
end getCompiler;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getCompiler',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'compiler'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setCompiler')
        class setCompiler(
            ModelicaFunction,
        ):
            """
```modelica
function setCompiler
  input String compiler;
  output Boolean success;
end setCompiler;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                compiler,
            ):
                return _session_.__omc__.call_function(
                    funcName='setCompiler',
                    inputArguments=[
                        (Component(String), 'compiler', compiler, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setCFlags')
        class setCFlags(
            ModelicaFunction,
        ):
            """
```modelica
function setCFlags
  input String inString;
  output Boolean success;
end setCFlags;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                inString,
            ):
                return _session_.__omc__.call_function(
                    funcName='setCFlags',
                    inputArguments=[
                        (Component(String), 'inString', inString, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getCFlags')
        class getCFlags(
            ModelicaFunction,
        ):
            """
```modelica
function getCFlags
  output String outString;
end getCFlags;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getCFlags',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'outString'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getCXXCompiler')
        class getCXXCompiler(
            ModelicaFunction,
        ):
            """
```modelica
function getCXXCompiler
  output String compiler;
end getCXXCompiler;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getCXXCompiler',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'compiler'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setCXXCompiler')
        class setCXXCompiler(
            ModelicaFunction,
        ):
            """
```modelica
function setCXXCompiler
  input String compiler;
  output Boolean success;
end setCXXCompiler;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                compiler,
            ):
                return _session_.__omc__.call_function(
                    funcName='setCXXCompiler',
                    inputArguments=[
                        (Component(String), 'compiler', compiler, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.verifyCompiler')
        class verifyCompiler(
            ModelicaFunction,
        ):
            """
```modelica
function verifyCompiler
  output Boolean compilerWorks;
end verifyCompiler;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='verifyCompiler',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Boolean), 'compilerWorks'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setCompilerPath')
        class setCompilerPath(
            ModelicaFunction,
        ):
            """
```modelica
function setCompilerPath
  input String compilerPath;
  output Boolean success;
end setCompilerPath;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                compilerPath,
            ):
                return _session_.__omc__.call_function(
                    funcName='setCompilerPath',
                    inputArguments=[
                        (Component(String), 'compilerPath', compilerPath, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getCompileCommand')
        class getCompileCommand(
            ModelicaFunction,
        ):
            """
```modelica
function getCompileCommand
  output String compileCommand;
end getCompileCommand;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getCompileCommand',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'compileCommand'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setCompileCommand')
        class setCompileCommand(
            ModelicaFunction,
        ):
            """
```modelica
function setCompileCommand
  input String compileCommand;
  output Boolean success;
end setCompileCommand;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                compileCommand,
            ):
                return _session_.__omc__.call_function(
                    funcName='setCompileCommand',
                    inputArguments=[
                        (Component(String), 'compileCommand', compileCommand, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setPlotCommand')
        class setPlotCommand(
            ModelicaFunction,
        ):
            """
```modelica
function setPlotCommand
  input String plotCommand;
  output Boolean success;
end setPlotCommand;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                plotCommand,
            ):
                return _session_.__omc__.call_function(
                    funcName='setPlotCommand',
                    inputArguments=[
                        (Component(String), 'plotCommand', plotCommand, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getSettings')
        class getSettings(
            ModelicaFunction,
        ):
            """
```modelica
function getSettings
  output String settings;
end getSettings;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getSettings',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'settings'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setTempDirectoryPath')
        class setTempDirectoryPath(
            ModelicaFunction,
        ):
            """
```modelica
function setTempDirectoryPath
  input String tempDirectoryPath;
  output Boolean success;
end setTempDirectoryPath;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                tempDirectoryPath,
            ):
                return _session_.__omc__.call_function(
                    funcName='setTempDirectoryPath',
                    inputArguments=[
                        (Component(String), 'tempDirectoryPath', tempDirectoryPath, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getTempDirectoryPath')
        class getTempDirectoryPath(
            ModelicaFunction,
        ):
            """
```modelica
function getTempDirectoryPath
  output String tempDirectoryPath;
end getTempDirectoryPath;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getTempDirectoryPath',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'tempDirectoryPath'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getEnvironmentVar')
        class getEnvironmentVar(
            ModelicaFunction,
        ):
            """
```modelica
function getEnvironmentVar
  input String var;
  output String value "returns empty string on failure";
end getEnvironmentVar;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                var,
            ):
                return _session_.__omc__.call_function(
                    funcName='getEnvironmentVar',
                    inputArguments=[
                        (Component(String), 'var', var, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'value'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setEnvironmentVar')
        class setEnvironmentVar(
            ModelicaFunction,
        ):
            """
```modelica
function setEnvironmentVar
  input String var;
  input String value;
  output Boolean success;
end setEnvironmentVar;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                var,
                value,
            ):
                return _session_.__omc__.call_function(
                    funcName='setEnvironmentVar',
                    inputArguments=[
                        (Component(String), 'var', var, 'required'),
                        (Component(String), 'value', value, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.appendEnvironmentVar')
        class appendEnvironmentVar(
            ModelicaFunction,
        ):
            """
```modelica
function appendEnvironmentVar
  input String var;
  input String value;
  output String result "returns \\"error\\" if the variable could not be appended";
end appendEnvironmentVar;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                var,
                value,
            ):
                return _session_.__omc__.call_function(
                    funcName='appendEnvironmentVar',
                    inputArguments=[
                        (Component(String), 'var', var, 'required'),
                        (Component(String), 'value', value, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setInstallationDirectoryPath')
        class setInstallationDirectoryPath(
            ModelicaFunction,
        ):
            """
```modelica
function setInstallationDirectoryPath
  input String installationDirectoryPath;
  output Boolean success;
end setInstallationDirectoryPath;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                installationDirectoryPath,
            ):
                return _session_.__omc__.call_function(
                    funcName='setInstallationDirectoryPath',
                    inputArguments=[
                        (Component(String), 'installationDirectoryPath', installationDirectoryPath, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getInstallationDirectoryPath')
        class getInstallationDirectoryPath(
            ModelicaFunction,
        ):
            """
```modelica
function getInstallationDirectoryPath
  output String installationDirectoryPath;
end getInstallationDirectoryPath;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getInstallationDirectoryPath',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'installationDirectoryPath'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setModelicaPath')
        class setModelicaPath(
            ModelicaFunction,
        ):
            """
```modelica
function setModelicaPath
  input String modelicaPath;
  output Boolean success;
end setModelicaPath;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                modelicaPath,
            ):
                return _session_.__omc__.call_function(
                    funcName='setModelicaPath',
                    inputArguments=[
                        (Component(String), 'modelicaPath', modelicaPath, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getModelicaPath')
        class getModelicaPath(
            ModelicaFunction,
        ):
            """
```modelica
function getModelicaPath
  output String modelicaPath;
end getModelicaPath;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getModelicaPath',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'modelicaPath'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setCompilerFlags')
        class setCompilerFlags(
            ModelicaFunction,
        ):
            """
```modelica
function setCompilerFlags
  input String compilerFlags;
  output Boolean success;
end setCompilerFlags;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                compilerFlags,
            ):
                return _session_.__omc__.call_function(
                    funcName='setCompilerFlags',
                    inputArguments=[
                        (Component(String), 'compilerFlags', compilerFlags, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.enableNewInstantiation')
        class enableNewInstantiation(
            ModelicaFunction,
        ):
            """
```modelica
function enableNewInstantiation
  output Boolean success;
end enableNewInstantiation;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='enableNewInstantiation',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.disableNewInstantiation')
        class disableNewInstantiation(
            ModelicaFunction,
        ):
            """
```modelica
function disableNewInstantiation
  output Boolean success;
end disableNewInstantiation;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='disableNewInstantiation',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setDebugFlags')
        class setDebugFlags(
            ModelicaFunction,
        ):
            """
```modelica
function setDebugFlags
  input String debugFlags;
  output Boolean success;
end setDebugFlags;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                debugFlags,
            ):
                return _session_.__omc__.call_function(
                    funcName='setDebugFlags',
                    inputArguments=[
                        (Component(String), 'debugFlags', debugFlags, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.clearDebugFlags')
        class clearDebugFlags(
            ModelicaFunction,
        ):
            """
```modelica
function clearDebugFlags
  output Boolean success;
end clearDebugFlags;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='clearDebugFlags',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setPreOptModules')
        class setPreOptModules(
            ModelicaFunction,
        ):
            """
```modelica
function setPreOptModules
  input String modules;
  output Boolean success;
end setPreOptModules;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                modules,
            ):
                return _session_.__omc__.call_function(
                    funcName='setPreOptModules',
                    inputArguments=[
                        (Component(String), 'modules', modules, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setCheapMatchingAlgorithm')
        class setCheapMatchingAlgorithm(
            ModelicaFunction,
        ):
            """
```modelica
function setCheapMatchingAlgorithm
  input Integer matchingAlgorithm;
  output Boolean success;
end setCheapMatchingAlgorithm;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                matchingAlgorithm,
            ):
                return _session_.__omc__.call_function(
                    funcName='setCheapMatchingAlgorithm',
                    inputArguments=[
                        (Component(Integer), 'matchingAlgorithm', matchingAlgorithm, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getMatchingAlgorithm')
        class getMatchingAlgorithm(
            ModelicaFunction,
        ):
            """
```modelica
function getMatchingAlgorithm
  output String selected;
end getMatchingAlgorithm;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getMatchingAlgorithm',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'selected'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getAvailableMatchingAlgorithms')
        class getAvailableMatchingAlgorithms(
            ModelicaFunction,
        ):
            """
```modelica
function getAvailableMatchingAlgorithms
  output String[:] allChoices;
  output String[:] allComments;
end getAvailableMatchingAlgorithms;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getAvailableMatchingAlgorithms',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String)[:], 'allChoices'),
                        (Component(String)[:], 'allComments'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setMatchingAlgorithm')
        class setMatchingAlgorithm(
            ModelicaFunction,
        ):
            """
```modelica
function setMatchingAlgorithm
  input String matchingAlgorithm;
  output Boolean success;
end setMatchingAlgorithm;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                matchingAlgorithm,
            ):
                return _session_.__omc__.call_function(
                    funcName='setMatchingAlgorithm',
                    inputArguments=[
                        (Component(String), 'matchingAlgorithm', matchingAlgorithm, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getIndexReductionMethod')
        class getIndexReductionMethod(
            ModelicaFunction,
        ):
            """
```modelica
function getIndexReductionMethod
  output String selected;
end getIndexReductionMethod;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getIndexReductionMethod',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'selected'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getAvailableIndexReductionMethods')
        class getAvailableIndexReductionMethods(
            ModelicaFunction,
        ):
            """
```modelica
function getAvailableIndexReductionMethods
  output String[:] allChoices;
  output String[:] allComments;
end getAvailableIndexReductionMethods;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getAvailableIndexReductionMethods',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String)[:], 'allChoices'),
                        (Component(String)[:], 'allComments'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setIndexReductionMethod')
        class setIndexReductionMethod(
            ModelicaFunction,
        ):
            """
```modelica
function setIndexReductionMethod
  input String method;
  output Boolean success;
end setIndexReductionMethod;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                method,
            ):
                return _session_.__omc__.call_function(
                    funcName='setIndexReductionMethod',
                    inputArguments=[
                        (Component(String), 'method', method, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setPostOptModules')
        class setPostOptModules(
            ModelicaFunction,
        ):
            """
```modelica
function setPostOptModules
  input String modules;
  output Boolean success;
end setPostOptModules;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                modules,
            ):
                return _session_.__omc__.call_function(
                    funcName='setPostOptModules',
                    inputArguments=[
                        (Component(String), 'modules', modules, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getTearingMethod')
        class getTearingMethod(
            ModelicaFunction,
        ):
            """
```modelica
function getTearingMethod
  output String selected;
end getTearingMethod;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getTearingMethod',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'selected'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getAvailableTearingMethods')
        class getAvailableTearingMethods(
            ModelicaFunction,
        ):
            """
```modelica
function getAvailableTearingMethods
  output String[:] allChoices;
  output String[:] allComments;
end getAvailableTearingMethods;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getAvailableTearingMethods',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String)[:], 'allChoices'),
                        (Component(String)[:], 'allComments'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setTearingMethod')
        class setTearingMethod(
            ModelicaFunction,
        ):
            """
```modelica
function setTearingMethod
  input String tearingMethod;
  output Boolean success;
end setTearingMethod;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                tearingMethod,
            ):
                return _session_.__omc__.call_function(
                    funcName='setTearingMethod',
                    inputArguments=[
                        (Component(String), 'tearingMethod', tearingMethod, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setCommandLineOptions')
        class setCommandLineOptions(
            ModelicaFunction,
        ):
            """
```modelica
function setCommandLineOptions
  input String option;
  output Boolean success;
end setCommandLineOptions;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                option,
            ):
                return _session_.__omc__.call_function(
                    funcName='setCommandLineOptions',
                    inputArguments=[
                        (Component(String), 'option', option, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getCommandLineOptions')
        class getCommandLineOptions(
            ModelicaFunction,
        ):
            """
```modelica
function getCommandLineOptions
  output String[:] flags;
end getCommandLineOptions;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getCommandLineOptions',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String)[:], 'flags'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getConfigFlagValidOptions')
        class getConfigFlagValidOptions(
            ModelicaFunction,
        ):
            """
```modelica
function getConfigFlagValidOptions
  input String flag;
  output String validOptions[:];
  output String mainDescription;
  output String descriptions[:];
end getConfigFlagValidOptions;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                flag,
            ):
                return _session_.__omc__.call_function(
                    funcName='getConfigFlagValidOptions',
                    inputArguments=[
                        (Component(String), 'flag', flag, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'validOptions'),
                        (Component(String), 'mainDescription'),
                        (Component(String)[:], 'descriptions'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.clearCommandLineOptions')
        class clearCommandLineOptions(
            ModelicaFunction,
        ):
            """
```modelica
function clearCommandLineOptions
  output Boolean success;
end clearCommandLineOptions;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='clearCommandLineOptions',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getVersion')
        class getVersion(
            ModelicaFunction,
        ):
            """
```modelica
function getVersion
  input TypeName cl = $Code(OpenModelica);
  output String version;
end getVersion;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='getVersion',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'version'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.regularFileExists')
        class regularFileExists(
            ModelicaFunction,
        ):
            """
```modelica
function regularFileExists
  input String fileName;
  output Boolean exists;
end regularFileExists;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
            ):
                return _session_.__omc__.call_function(
                    funcName='regularFileExists',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'exists'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.directoryExists')
        class directoryExists(
            ModelicaFunction,
        ):
            """
```modelica
function directoryExists
  input String dirName;
  output Boolean exists;
end directoryExists;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                dirName,
            ):
                return _session_.__omc__.call_function(
                    funcName='directoryExists',
                    inputArguments=[
                        (Component(String), 'dirName', dirName, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'exists'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.stat')
        class stat(
            ModelicaFunction,
        ):
            """
```modelica
impure function stat
  input String fileName;
  output Boolean success;
  output Real fileSize;
  output Real mtime;
end stat;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
            ):
                return _session_.__omc__.call_function(
                    funcName='stat',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                        (Component(Real), 'fileSize'),
                        (Component(Real), 'mtime'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.readFile')
        class readFile(
            ModelicaFunction,
        ):
            """
```modelica
impure function readFile
  input String fileName;
  output String contents;
end readFile;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
            ):
                return _session_.__omc__.call_function(
                    funcName='readFile',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'contents'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.writeFile')
        class writeFile(
            ModelicaFunction,
        ):
            """
```modelica
impure function writeFile
  input String fileName;
  input String data;
  input Boolean append = false;
  output Boolean success;
end writeFile;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
                data,
                append=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='writeFile',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                        (Component(String), 'data', data, 'required'),
                        (Component(Boolean), 'append', append, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.compareFilesAndMove')
        class compareFilesAndMove(
            ModelicaFunction,
        ):
            """
```modelica
impure function compareFilesAndMove
  input String newFile;
  input String oldFile;
  output Boolean success;
end compareFilesAndMove;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                newFile,
                oldFile,
            ):
                return _session_.__omc__.call_function(
                    funcName='compareFilesAndMove',
                    inputArguments=[
                        (Component(String), 'newFile', newFile, 'required'),
                        (Component(String), 'oldFile', oldFile, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.compareFiles')
        class compareFiles(
            ModelicaFunction,
        ):
            """
```modelica
impure function compareFiles
  input String file1;
  input String file2;
  output Boolean isEqual;
end compareFiles;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                file1,
                file2,
            ):
                return _session_.__omc__.call_function(
                    funcName='compareFiles',
                    inputArguments=[
                        (Component(String), 'file1', file1, 'required'),
                        (Component(String), 'file2', file2, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'isEqual'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.alarm')
        class alarm(
            ModelicaFunction,
        ):
            """
```modelica
impure function alarm
  input Integer seconds;
  output Integer previousSeconds;
end alarm;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                seconds,
            ):
                return _session_.__omc__.call_function(
                    funcName='alarm',
                    inputArguments=[
                        (Component(Integer), 'seconds', seconds, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'previousSeconds'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.regex')
        class regex(
            ModelicaFunction,
        ):
            """
```modelica
function regex
  input String str;
  input String re;
  input Integer maxMatches = 1 "The maximum number of matches that will be returned";
  input Boolean extended = true "Use POSIX extended or regular syntax";
  input Boolean caseInsensitive = false;
  output Integer numMatches "-1 is an error, 0 means no match, else returns a number 1..maxMatches";
  output String matchedSubstrings[maxMatches] "unmatched strings are returned as empty";
end regex;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                str,
                re,
                maxMatches=None,
                extended=None,
                caseInsensitive=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='regex',
                    inputArguments=[
                        (Component(String), 'str', str, 'required'),
                        (Component(String), 're', re, 'required'),
                        (Component(Integer), 'maxMatches', maxMatches, 'optional'),
                        (Component(Boolean), 'extended', extended, 'optional'),
                        (Component(Boolean), 'caseInsensitive', caseInsensitive, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'numMatches'),
                        (Component(String)[:], 'matchedSubstrings'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.regexBool')
        class regexBool(
            ModelicaFunction,
        ):
            """
```modelica
function regexBool
  input String str;
  input String re;
  input Boolean extended = true "Use POSIX extended or regular syntax";
  input Boolean caseInsensitive = false;
  output Boolean matches;
end regexBool;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                str,
                re,
                extended=None,
                caseInsensitive=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='regexBool',
                    inputArguments=[
                        (Component(String), 'str', str, 'required'),
                        (Component(String), 're', re, 'required'),
                        (Component(Boolean), 'extended', extended, 'optional'),
                        (Component(Boolean), 'caseInsensitive', caseInsensitive, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'matches'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.testsuiteFriendlyName')
        class testsuiteFriendlyName(
            ModelicaFunction,
        ):
            """
```modelica
function testsuiteFriendlyName
  input String path;
  output String fixed;
end testsuiteFriendlyName;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                path,
            ):
                return _session_.__omc__.call_function(
                    funcName='testsuiteFriendlyName',
                    inputArguments=[
                        (Component(String), 'path', path, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'fixed'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.readFileNoNumeric')
        class readFileNoNumeric(
            ModelicaFunction,
        ):
            """
```modelica
function readFileNoNumeric
  input String fileName;
  output String contents;
end readFileNoNumeric;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
            ):
                return _session_.__omc__.call_function(
                    funcName='readFileNoNumeric',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'contents'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getErrorString')
        class getErrorString(
            ModelicaFunction,
        ):
            """
```modelica
impure function getErrorString
  input Boolean warningsAsErrors = false;
  output String errorString;
end getErrorString;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                warningsAsErrors=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='getErrorString',
                    inputArguments=[
                        (Component(Boolean), 'warningsAsErrors', warningsAsErrors, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'errorString'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getMessagesString')
        class getMessagesString(
            ModelicaFunction,
        ):
            """
```modelica
function getMessagesString
  output String messagesString;
end getMessagesString;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getMessagesString',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'messagesString'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.SourceInfo')
        class SourceInfo(
            ModelicaRecord,
        ):
            """
```modelica
record SourceInfo
  String fileName;
  Boolean readonly;
  Integer lineStart;
  Integer columnStart;
  Integer lineEnd;
  Integer columnEnd;
  annotation(
    preferredView = "text");
end SourceInfo;
```
            """
            @element
            def fileName(cls):
                return Component(String)

            @element
            def readonly(cls):
                return Component(Boolean)

            @element
            def lineStart(cls):
                return Component(Integer)

            @element
            def columnStart(cls):
                return Component(Integer)

            @element
            def lineEnd(cls):
                return Component(Integer)

            @element
            def columnEnd(cls):
                return Component(Integer)

        @modelica_name('OpenModelica.Scripting.ErrorKind')
        class ErrorKind(
            ModelicaEnumeration,
        ):
            """
```modelica
type ErrorKind = enumeration(syntax "syntax errors", grammar "grammatical errors", translation "instantiation errors: up to flat modelica", symbolic "symbolic manipulation error, simcodegen, up to executable file", runtime "simulation/function runtime error", scripting "runtime scripting /interpretation error");
```
            """
            syntax = enum.auto()  # syntax errors
            grammar = enum.auto()  # grammatical errors
            translation = enum.auto()  # instantiation errors: up to flat modelica
            symbolic = enum.auto()  # symbolic manipulation error, simcodegen, up to executable file
            runtime = enum.auto()  # simulation/function runtime error
            scripting = enum.auto()  # runtime scripting /interpretation error

        @modelica_name('OpenModelica.Scripting.ErrorLevel')
        class ErrorLevel(
            ModelicaEnumeration,
        ):
            """
```modelica
type ErrorLevel = enumeration(internal, notification, warning, error);
```
            """
            internal = enum.auto()
            notification = enum.auto()
            warning = enum.auto()
            error = enum.auto()

        @modelica_name('OpenModelica.Scripting.ErrorMessage')
        class ErrorMessage(
            ModelicaRecord,
        ):
            """
```modelica
record ErrorMessage
  SourceInfo info;
  String message "After applying the individual arguments";
  ErrorKind kind;
  ErrorLevel level;
  Integer id "Internal ID of the error (just ignore this)";
  annotation(
    preferredView = "text");
end ErrorMessage;
```
            """
            @element
            def info(cls):
                return Component(OpenModelica.Scripting.SourceInfo)

            @element
            def message(cls):
                return Component(String)

            @element
            def kind(cls):
                return Component(OpenModelica.Scripting.ErrorKind)

            @element
            def level(cls):
                return Component(OpenModelica.Scripting.ErrorLevel)

            @element
            def id(cls):
                return Component(Integer)

        @modelica_name('OpenModelica.Scripting.getMessagesStringInternal')
        class getMessagesStringInternal(
            ModelicaFunction,
        ):
            """
```modelica
function getMessagesStringInternal
  input Boolean unique = true;
  output ErrorMessage[:] messagesString;
end getMessagesStringInternal;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                unique=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='getMessagesStringInternal',
                    inputArguments=[
                        (Component(Boolean), 'unique', unique, 'optional'),
                    ],
                    outputArguments=[
                        (Component(OpenModelica.Scripting.ErrorMessage)[:], 'messagesString'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.countMessages')
        class countMessages(
            ModelicaFunction,
        ):
            """
```modelica
function countMessages
  output Integer numMessages;
  output Integer numErrors;
  output Integer numWarnings;
end countMessages;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='countMessages',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Integer), 'numMessages'),
                        (Component(Integer), 'numErrors'),
                        (Component(Integer), 'numWarnings'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.clearMessages')
        class clearMessages(
            ModelicaFunction,
        ):
            """
```modelica
function clearMessages
  output Boolean success;
end clearMessages;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='clearMessages',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.runScript')
        class runScript(
            ModelicaFunction,
        ):
            """
```modelica
impure function runScript
  input String fileName "*.mos";
  output String result;
end runScript;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
            ):
                return _session_.__omc__.call_function(
                    funcName='runScript',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.echo')
        class echo(
            ModelicaFunction,
        ):
            """
```modelica
function echo
  input Boolean setEcho;
  output Boolean newEcho;
end echo;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                setEcho,
            ):
                return _session_.__omc__.call_function(
                    funcName='echo',
                    inputArguments=[
                        (Component(Boolean), 'setEcho', setEcho, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'newEcho'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getClassesInModelicaPath')
        class getClassesInModelicaPath(
            ModelicaFunction,
        ):
            """
```modelica
function getClassesInModelicaPath
  output String classesInModelicaPath;
end getClassesInModelicaPath;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getClassesInModelicaPath',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'classesInModelicaPath'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getAnnotationVersion')
        class getAnnotationVersion(
            ModelicaFunction,
        ):
            """
```modelica
function getAnnotationVersion
  output String annotationVersion;
end getAnnotationVersion;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getAnnotationVersion',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'annotationVersion'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setAnnotationVersion')
        class setAnnotationVersion(
            ModelicaFunction,
        ):
            """
```modelica
function setAnnotationVersion
  input String annotationVersion;
  output Boolean success;
end setAnnotationVersion;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                annotationVersion,
            ):
                return _session_.__omc__.call_function(
                    funcName='setAnnotationVersion',
                    inputArguments=[
                        (Component(String), 'annotationVersion', annotationVersion, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getNoSimplify')
        class getNoSimplify(
            ModelicaFunction,
        ):
            """
```modelica
function getNoSimplify
  output Boolean noSimplify;
end getNoSimplify;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getNoSimplify',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Boolean), 'noSimplify'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setNoSimplify')
        class setNoSimplify(
            ModelicaFunction,
        ):
            """
```modelica
function setNoSimplify
  input Boolean noSimplify;
  output Boolean success;
end setNoSimplify;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                noSimplify,
            ):
                return _session_.__omc__.call_function(
                    funcName='setNoSimplify',
                    inputArguments=[
                        (Component(Boolean), 'noSimplify', noSimplify, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getVectorizationLimit')
        class getVectorizationLimit(
            ModelicaFunction,
        ):
            """
```modelica
function getVectorizationLimit
  output Integer vectorizationLimit;
end getVectorizationLimit;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getVectorizationLimit',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Integer), 'vectorizationLimit'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setVectorizationLimit')
        class setVectorizationLimit(
            ModelicaFunction,
        ):
            """
```modelica
function setVectorizationLimit
  input Integer vectorizationLimit;
  output Boolean success;
end setVectorizationLimit;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                vectorizationLimit,
            ):
                return _session_.__omc__.call_function(
                    funcName='setVectorizationLimit',
                    inputArguments=[
                        (Component(Integer), 'vectorizationLimit', vectorizationLimit, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getDefaultOpenCLDevice')
        class getDefaultOpenCLDevice(
            ModelicaFunction,
        ):
            """
```modelica
function getDefaultOpenCLDevice
  output Integer defdevid;
end getDefaultOpenCLDevice;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getDefaultOpenCLDevice',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Integer), 'defdevid'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setDefaultOpenCLDevice')
        class setDefaultOpenCLDevice(
            ModelicaFunction,
        ):
            """
```modelica
function setDefaultOpenCLDevice
  input Integer defdevid;
  output Boolean success;
end setDefaultOpenCLDevice;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                defdevid,
            ):
                return _session_.__omc__.call_function(
                    funcName='setDefaultOpenCLDevice',
                    inputArguments=[
                        (Component(Integer), 'defdevid', defdevid, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setShowAnnotations')
        class setShowAnnotations(
            ModelicaFunction,
        ):
            """
```modelica
function setShowAnnotations
  input Boolean show;
  output Boolean success;
end setShowAnnotations;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                show,
            ):
                return _session_.__omc__.call_function(
                    funcName='setShowAnnotations',
                    inputArguments=[
                        (Component(Boolean), 'show', show, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getShowAnnotations')
        class getShowAnnotations(
            ModelicaFunction,
        ):
            """
```modelica
function getShowAnnotations
  output Boolean show;
end getShowAnnotations;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getShowAnnotations',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Boolean), 'show'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setOrderConnections')
        class setOrderConnections(
            ModelicaFunction,
        ):
            """
```modelica
function setOrderConnections
  input Boolean orderConnections;
  output Boolean success;
end setOrderConnections;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                orderConnections,
            ):
                return _session_.__omc__.call_function(
                    funcName='setOrderConnections',
                    inputArguments=[
                        (Component(Boolean), 'orderConnections', orderConnections, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getOrderConnections')
        class getOrderConnections(
            ModelicaFunction,
        ):
            """
```modelica
function getOrderConnections
  output Boolean orderConnections;
end getOrderConnections;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getOrderConnections',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Boolean), 'orderConnections'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setLanguageStandard')
        class setLanguageStandard(
            ModelicaFunction,
        ):
            """
```modelica
function setLanguageStandard
  input String inVersion;
  output Boolean success;
end setLanguageStandard;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                inVersion,
            ):
                return _session_.__omc__.call_function(
                    funcName='setLanguageStandard',
                    inputArguments=[
                        (Component(String), 'inVersion', inVersion, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getLanguageStandard')
        class getLanguageStandard(
            ModelicaFunction,
        ):
            """
```modelica
function getLanguageStandard
  output String outVersion;
end getLanguageStandard;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getLanguageStandard',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'outVersion'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getAstAsCorbaString')
        class getAstAsCorbaString(
            ModelicaFunction,
        ):
            """
```modelica
function getAstAsCorbaString
  input String fileName = "<interactive>";
  output String result "returns the string if fileName is interactive; else it returns ok or error depending on if writing the file succeeded";
end getAstAsCorbaString;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='getAstAsCorbaString',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.cd')
        class cd(
            ModelicaFunction,
        ):
            """
```modelica
function cd
  input String newWorkingDirectory = "";
  output String workingDirectory;
end cd;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                newWorkingDirectory=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='cd',
                    inputArguments=[
                        (Component(String), 'newWorkingDirectory', newWorkingDirectory, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'workingDirectory'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.mkdir')
        class mkdir(
            ModelicaFunction,
        ):
            """
```modelica
function mkdir
  input String newDirectory;
  output Boolean success;
end mkdir;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                newDirectory,
            ):
                return _session_.__omc__.call_function(
                    funcName='mkdir',
                    inputArguments=[
                        (Component(String), 'newDirectory', newDirectory, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.copy')
        class copy(
            ModelicaFunction,
        ):
            """
```modelica
function copy
  input String source;
  input String destination;
  output Boolean success;
end copy;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                source,
                destination,
            ):
                return _session_.__omc__.call_function(
                    funcName='copy',
                    inputArguments=[
                        (Component(String), 'source', source, 'required'),
                        (Component(String), 'destination', destination, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.remove')
        class remove(
            ModelicaFunction,
        ):
            """
```modelica
function remove
  input String path;
  output Boolean success "Returns true on success.";
end remove;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                path,
            ):
                return _session_.__omc__.call_function(
                    funcName='remove',
                    inputArguments=[
                        (Component(String), 'path', path, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.checkModel')
        class checkModel(
            ModelicaFunction,
        ):
            """
```modelica
function checkModel
  input TypeName className;
  output String result;
end checkModel;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
            ):
                return _session_.__omc__.call_function(
                    funcName='checkModel',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.checkAllModelsRecursive')
        class checkAllModelsRecursive(
            ModelicaFunction,
        ):
            """
```modelica
function checkAllModelsRecursive
  input TypeName className;
  input Boolean checkProtected = false "Checks also protected classes if true";
  output String result;
end checkAllModelsRecursive;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                checkProtected=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='checkAllModelsRecursive',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(Boolean), 'checkProtected', checkProtected, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.typeOf')
        class typeOf(
            ModelicaFunction,
        ):
            """
```modelica
function typeOf
  input VariableName variableName;
  output String result;
end typeOf;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                variableName,
            ):
                return _session_.__omc__.call_function(
                    funcName='typeOf',
                    inputArguments=[
                        (Component(VariableName), 'variableName', variableName, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.instantiateModel')
        class instantiateModel(
            ModelicaFunction,
        ):
            """
```modelica
function instantiateModel
  input TypeName className;
  output String result;
end instantiateModel;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
            ):
                return _session_.__omc__.call_function(
                    funcName='instantiateModel',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.buildOpenTURNSInterface')
        class buildOpenTURNSInterface(
            ModelicaFunction,
        ):
            """
```modelica
function buildOpenTURNSInterface
  input TypeName className;
  input String pythonTemplateFile;
  input Boolean showFlatModelica = false;
  output String outPythonScript;
end buildOpenTURNSInterface;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                pythonTemplateFile,
                showFlatModelica=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='buildOpenTURNSInterface',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(String), 'pythonTemplateFile', pythonTemplateFile, 'required'),
                        (Component(Boolean), 'showFlatModelica', showFlatModelica, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'outPythonScript'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.runOpenTURNSPythonScript')
        class runOpenTURNSPythonScript(
            ModelicaFunction,
        ):
            """
```modelica
function runOpenTURNSPythonScript
  input String pythonScriptFile;
  output String logOutputFile;
end runOpenTURNSPythonScript;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                pythonScriptFile,
            ):
                return _session_.__omc__.call_function(
                    funcName='runOpenTURNSPythonScript',
                    inputArguments=[
                        (Component(String), 'pythonScriptFile', pythonScriptFile, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'logOutputFile'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.generateCode')
        class generateCode(
            ModelicaFunction,
        ):
            """
```modelica
function generateCode
  input TypeName className;
  output Boolean success;
end generateCode;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
            ):
                return _session_.__omc__.call_function(
                    funcName='generateCode',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.loadModel')
        class loadModel(
            ModelicaFunction,
        ):
            """
```modelica
function loadModel
  input TypeName className;
  input String[:] priorityVersion = {"default"};
  input Boolean notify = false "Give a notification of the libraries and versions that were loaded";
  input String languageStandard = "" "Override the set language standard. Parse with the given setting, but do not change it permanently.";
  input Boolean requireExactVersion = false "If the version is required to be exact, if there is a uses Modelica(version=\\"3.2\\"), Modelica 3.2.1 will not match it.";
  output Boolean success;
end loadModel;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                priorityVersion=None,
                notify=None,
                languageStandard=None,
                requireExactVersion=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='loadModel',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(String)[:], 'priorityVersion', priorityVersion, 'optional'),
                        (Component(Boolean), 'notify', notify, 'optional'),
                        (Component(String), 'languageStandard', languageStandard, 'optional'),
                        (Component(Boolean), 'requireExactVersion', requireExactVersion, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.deleteFile')
        class deleteFile(
            ModelicaFunction,
        ):
            """
```modelica
function deleteFile
  input String fileName;
  output Boolean success;
end deleteFile;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
            ):
                return _session_.__omc__.call_function(
                    funcName='deleteFile',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.saveModel')
        class saveModel(
            ModelicaFunction,
        ):
            """
```modelica
function saveModel
  input String fileName;
  input TypeName className;
  output Boolean success;
end saveModel;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
                className,
            ):
                return _session_.__omc__.call_function(
                    funcName='saveModel',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                        (Component(TypeName), 'className', className, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.saveTotalModel')
        class saveTotalModel(
            ModelicaFunction,
        ):
            """
```modelica
function saveTotalModel
  input String fileName;
  input TypeName className;
  input Boolean stripAnnotations = false;
  input Boolean stripComments = false;
  output Boolean success;
end saveTotalModel;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
                className,
                stripAnnotations=None,
                stripComments=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='saveTotalModel',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(Boolean), 'stripAnnotations', stripAnnotations, 'optional'),
                        (Component(Boolean), 'stripComments', stripComments, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.save')
        class save(
            ModelicaFunction,
        ):
            """
```modelica
function save
  input TypeName className;
  output Boolean success;
end save;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
            ):
                return _session_.__omc__.call_function(
                    funcName='save',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.saveTotalSCode')
        @alias
        def saveTotalSCode(cls):
            return OpenModelica.Scripting.saveTotalModel

        @modelica_name('OpenModelica.Scripting.translateGraphics')
        class translateGraphics(
            ModelicaFunction,
        ):
            """
```modelica
function translateGraphics
  input TypeName className;
  output String result;
end translateGraphics;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
            ):
                return _session_.__omc__.call_function(
                    funcName='translateGraphics',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        # @modelica_name('OpenModelica.Scripting.codeToString')
        # class codeToString(
        #     ModelicaFunction,
        # ):
        #     """
        # ```modelica
        # function codeToString
        #   input $Code className;
        #   output String string;
        # end codeToString;
        # ```
        #     """
        #     @external
        #     def _(
        #         _cls_,
        #         _session_: AbstractOMCSession,
        #         className,
        #     ):
        #         return _session_.__omc__.call_function(
        #             funcName='codeToString',
        #             inputArguments=[
        #                 (Component(OpenModelica.$Code), 'className', className, 'required'),
        #             ],
        #             outputArguments=[
        #                 (Component(String), 'string'),
        #             ],
        #             parser=parse_OMCValue,
        #         )

        @modelica_name('OpenModelica.Scripting.dumpXMLDAE')
        class dumpXMLDAE(
            ModelicaFunction,
        ):
            """
```modelica
function dumpXMLDAE
  input TypeName className;
  input String translationLevel = "flat" "flat, optimiser, backEnd, or stateSpace";
  input Boolean addOriginalAdjacencyMatrix = false;
  input Boolean addSolvingInfo = false;
  input Boolean addMathMLCode = false;
  input Boolean dumpResiduals = false;
  input String fileNamePrefix = "<default>" "this is the className in string form by default";
  input String rewriteRulesFile = "" "the file from where the rewiteRules are read, default is empty which means no rewrite rules";
  output Boolean success "if the function succeeded true/false";
  output String xmlfileName "the Xml file";
end dumpXMLDAE;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                translationLevel=None,
                addOriginalAdjacencyMatrix=None,
                addSolvingInfo=None,
                addMathMLCode=None,
                dumpResiduals=None,
                fileNamePrefix=None,
                rewriteRulesFile=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='dumpXMLDAE',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(String), 'translationLevel', translationLevel, 'optional'),
                        (Component(Boolean), 'addOriginalAdjacencyMatrix', addOriginalAdjacencyMatrix, 'optional'),
                        (Component(Boolean), 'addSolvingInfo', addSolvingInfo, 'optional'),
                        (Component(Boolean), 'addMathMLCode', addMathMLCode, 'optional'),
                        (Component(Boolean), 'dumpResiduals', dumpResiduals, 'optional'),
                        (Component(String), 'fileNamePrefix', fileNamePrefix, 'optional'),
                        (Component(String), 'rewriteRulesFile', rewriteRulesFile, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                        (Component(String), 'xmlfileName'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.convertUnits')
        class convertUnits(
            ModelicaFunction,
        ):
            """
```modelica
function convertUnits
  input String s1;
  input String s2;
  output Boolean unitsCompatible;
  output Real scaleFactor;
  output Real offset;
end convertUnits;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                s1,
                s2,
            ):
                return _session_.__omc__.call_function(
                    funcName='convertUnits',
                    inputArguments=[
                        (Component(String), 's1', s1, 'required'),
                        (Component(String), 's2', s2, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'unitsCompatible'),
                        (Component(Real), 'scaleFactor'),
                        (Component(Real), 'offset'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getDerivedUnits')
        class getDerivedUnits(
            ModelicaFunction,
        ):
            """
```modelica
function getDerivedUnits
  input String baseUnit;
  output String[:] derivedUnits;
end getDerivedUnits;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                baseUnit,
            ):
                return _session_.__omc__.call_function(
                    funcName='getDerivedUnits',
                    inputArguments=[
                        (Component(String), 'baseUnit', baseUnit, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'derivedUnits'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.listVariables')
        class listVariables(
            ModelicaFunction,
        ):
            """
```modelica
function listVariables
  output TypeName variables[:];
end listVariables;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='listVariables',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(TypeName)[:], 'variables'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.strtok')
        class strtok(
            ModelicaFunction,
        ):
            """
```modelica
function strtok
  input String string;
  input String token;
  output String[:] strings;
end strtok;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                string,
                token,
            ):
                return _session_.__omc__.call_function(
                    funcName='strtok',
                    inputArguments=[
                        (Component(String), 'string', string, 'required'),
                        (Component(String), 'token', token, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'strings'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.stringSplit')
        class stringSplit(
            ModelicaFunction,
        ):
            """
```modelica
function stringSplit
  input String string;
  input String token "single character only";
  output String[:] strings;
end stringSplit;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                string,
                token,
            ):
                return _session_.__omc__.call_function(
                    funcName='stringSplit',
                    inputArguments=[
                        (Component(String), 'string', string, 'required'),
                        (Component(String), 'token', token, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'strings'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.stringReplace')
        class stringReplace(
            ModelicaFunction,
        ):
            """
```modelica
function stringReplace
  input String str;
  input String source;
  input String target;
  output String res;
end stringReplace;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                str,
                source,
                target,
            ):
                return _session_.__omc__.call_function(
                    funcName='stringReplace',
                    inputArguments=[
                        (Component(String), 'str', str, 'required'),
                        (Component(String), 'source', source, 'required'),
                        (Component(String), 'target', target, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'res'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.escapeXML')
        class escapeXML(
            ModelicaFunction,
        ):
            """
```modelica
function escapeXML
  input String inStr;
  output String outStr;
end escapeXML;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                inStr,
            ):
                return _session_.__omc__.call_function(
                    funcName='escapeXML',
                    inputArguments=[
                        (Component(String), 'inStr', inStr, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'outStr'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.ExportKind')
        class ExportKind(
            ModelicaEnumeration,
        ):
            """
```modelica
type ExportKind = enumeration(Absyn "Normal Absyn", SCode "Normal SCode", MetaModelicaInterface "A restricted MetaModelica package interface (protected parts are stripped)", Internal "True unparsing of the Absyn");
```
            """
            Absyn = enum.auto()  # Normal Absyn
            SCode = enum.auto()  # Normal SCode
            MetaModelicaInterface = enum.auto()  # A restricted MetaModelica package interface (protected parts are stripped)
            Internal = enum.auto()  # True unparsing of the Absyn

        @modelica_name('OpenModelica.Scripting.list')
        class list(
            ModelicaFunction,
        ):
            """
```modelica
function list
  input TypeName class_ = $Code(AllLoadedClasses);
  input Boolean interfaceOnly = false;
  input Boolean shortOnly = false "only short class definitions";
  input ExportKind exportKind = ExportKind.Absyn;
  output String contents;
end list;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_=None,
                interfaceOnly=None,
                shortOnly=None,
                exportKind=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='list',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'optional'),
                        (Component(Boolean), 'interfaceOnly', interfaceOnly, 'optional'),
                        (Component(Boolean), 'shortOnly', shortOnly, 'optional'),
                        (Component(OpenModelica.Scripting.ExportKind), 'exportKind', exportKind, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'contents'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.listFile')
        class listFile(
            ModelicaFunction,
        ):
            """
```modelica
function listFile
  input TypeName class_;
  input Boolean nestedClasses = true;
  output String contents;
end listFile;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                nestedClasses=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='listFile',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(Boolean), 'nestedClasses', nestedClasses, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'contents'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.DiffFormat')
        class DiffFormat(
            ModelicaEnumeration,
        ):
            """
```modelica
type DiffFormat = enumeration(plain "no deletions, no markup", color "terminal escape sequences", xml "XML tags");
```
            """
            plain = enum.auto()  # no deletions, no markup
            color = enum.auto()  # terminal escape sequences
            xml = enum.auto()  # XML tags

        @modelica_name('OpenModelica.Scripting.diffModelicaFileListings')
        class diffModelicaFileListings(
            ModelicaFunction,
        ):
            """
```modelica
function diffModelicaFileListings
  input String before, after;
  input DiffFormat diffFormat = DiffFormat.color;
  output String result;
end diffModelicaFileListings;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                before,
                after,
                diffFormat=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='diffModelicaFileListings',
                    inputArguments=[
                        (Component(String), 'before', before, 'required'),
                        (Component(String), 'after', after, 'required'),
                        (Component(OpenModelica.Scripting.DiffFormat), 'diffFormat', diffFormat, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.exportToFigaro')
        class exportToFigaro(
            ModelicaFunction,
        ):
            """
```modelica
function exportToFigaro
  input TypeName path;
  input String directory = cd();
  input String database;
  input String mode;
  input String options;
  input String processor;
  output Boolean success;
end exportToFigaro;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                path,
                database,
                mode,
                options,
                processor,
                directory=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='exportToFigaro',
                    inputArguments=[
                        (Component(TypeName), 'path', path, 'required'),
                        (Component(String), 'directory', directory, 'optional'),
                        (Component(String), 'database', database, 'required'),
                        (Component(String), 'mode', mode, 'required'),
                        (Component(String), 'options', options, 'required'),
                        (Component(String), 'processor', processor, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.inferBindings')
        class inferBindings(
            ModelicaFunction,
        ):
            """
```modelica
function inferBindings
  input TypeName path;
  output Boolean success;
end inferBindings;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                path,
            ):
                return _session_.__omc__.call_function(
                    funcName='inferBindings',
                    inputArguments=[
                        (Component(TypeName), 'path', path, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.generateVerificationScenarios')
        class generateVerificationScenarios(
            ModelicaFunction,
        ):
            """
```modelica
function generateVerificationScenarios
  input TypeName path;
  output Boolean success;
end generateVerificationScenarios;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                path,
            ):
                return _session_.__omc__.call_function(
                    funcName='generateVerificationScenarios',
                    inputArguments=[
                        (Component(TypeName), 'path', path, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.rewriteBlockCall')
        class rewriteBlockCall(
            ModelicaFunction,
        ):
            """
```modelica
function rewriteBlockCall
  input TypeName className;
  input TypeName inDefs;
  output Boolean success;
end rewriteBlockCall;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                inDefs,
            ):
                return _session_.__omc__.call_function(
                    funcName='rewriteBlockCall',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(TypeName), 'inDefs', inDefs, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.realpath')
        class realpath(
            ModelicaFunction,
        ):
            """
```modelica
function realpath
  input String name "Absolute or relative file or directory name";
  output String fullName "Full path of 'name'";
end realpath;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                name,
            ):
                return _session_.__omc__.call_function(
                    funcName='realpath',
                    inputArguments=[
                        (Component(String), 'name', name, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'fullName'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.uriToFilename')
        class uriToFilename(
            ModelicaFunction,
        ):
            """
```modelica
function uriToFilename
  input String uri;
  output String filename = "";
end uriToFilename;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                uri,
            ):
                return _session_.__omc__.call_function(
                    funcName='uriToFilename',
                    inputArguments=[
                        (Component(String), 'uri', uri, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'filename'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getLoadedLibraries')
        class getLoadedLibraries(
            ModelicaFunction,
        ):
            """
```modelica
function getLoadedLibraries
  output String[:, 2] libraries;
end getLoadedLibraries;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getLoadedLibraries',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String)[:, 2], 'libraries'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.LinearSystemSolver')
        class LinearSystemSolver(
            ModelicaEnumeration,
        ):
            """
```modelica
type LinearSystemSolver = enumeration(dgesv, lpsolve55);
```
            """
            dgesv = enum.auto()
            lpsolve55 = enum.auto()

        @modelica_name('OpenModelica.Scripting.solveLinearSystem')
        class solveLinearSystem(
            ModelicaFunction,
        ):
            """
```modelica
function solveLinearSystem
  input Real[size(B, 1), size(B, 1)] A;
  input Real[:] B;
  input LinearSystemSolver solver = LinearSystemSolver.dgesv;
  input Integer[:] isInt = {-1} "list of indices that are integers";
  output Real[size(B, 1)] X;
  output Integer info;
end solveLinearSystem;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                A,
                B,
                solver=None,
                isInt=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='solveLinearSystem',
                    inputArguments=[
                        (Component(Real)[:, :], 'A', A, 'required'),
                        (Component(Real)[:], 'B', B, 'required'),
                        (Component(OpenModelica.Scripting.LinearSystemSolver), 'solver', solver, 'optional'),
                        (Component(Integer)[:], 'isInt', isInt, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Real)[:], 'X'),
                        (Component(Integer), 'info'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.StandardStream')
        class StandardStream(
            ModelicaEnumeration,
        ):
            """
```modelica
type StandardStream = enumeration(stdin, stdout, stderr);
```
            """
            stdin = enum.auto()
            stdout = enum.auto()
            stderr = enum.auto()

        @modelica_name('OpenModelica.Scripting.reopenStandardStream')
        class reopenStandardStream(
            ModelicaFunction,
        ):
            """
```modelica
function reopenStandardStream
  input StandardStream _stream;
  input String filename;
  output Boolean success;
end reopenStandardStream;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                _stream,
                filename,
            ):
                return _session_.__omc__.call_function(
                    funcName='reopenStandardStream',
                    inputArguments=[
                        (Component(OpenModelica.Scripting.StandardStream), '_stream', _stream, 'required'),
                        (Component(String), 'filename', filename, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.importFMU')
        class importFMU(
            ModelicaFunction,
        ):
            """
```modelica
function importFMU
  input String filename "the fmu file name";
  input String workdir = "<default>" "The output directory for imported FMU files. <default> will put the files to current working directory.";
  input Integer loglevel = 3 "loglevel_nothing=0;loglevel_fatal=1;loglevel_error=2;loglevel_warning=3;loglevel_info=4;loglevel_verbose=5;loglevel_debug=6";
  input Boolean fullPath = false "When true the full output path is returned otherwise only the file name.";
  input Boolean debugLogging = false "When true the FMU's debug output is printed.";
  input Boolean generateInputConnectors = true "When true creates the input connector pins.";
  input Boolean generateOutputConnectors = true "When true creates the output connector pins.";
  output String generatedFileName "Returns the full path of the generated file.";
end importFMU;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                filename,
                workdir=None,
                loglevel=None,
                fullPath=None,
                debugLogging=None,
                generateInputConnectors=None,
                generateOutputConnectors=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='importFMU',
                    inputArguments=[
                        (Component(String), 'filename', filename, 'required'),
                        (Component(String), 'workdir', workdir, 'optional'),
                        (Component(Integer), 'loglevel', loglevel, 'optional'),
                        (Component(Boolean), 'fullPath', fullPath, 'optional'),
                        (Component(Boolean), 'debugLogging', debugLogging, 'optional'),
                        (Component(Boolean), 'generateInputConnectors', generateInputConnectors, 'optional'),
                        (Component(Boolean), 'generateOutputConnectors', generateOutputConnectors, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'generatedFileName'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.importFMUModelDescription')
        class importFMUModelDescription(
            ModelicaFunction,
        ):
            """
```modelica
function importFMUModelDescription
  input String filename "the fmu file name";
  input String workdir = "<default>" "The output directory for imported FMU files. <default> will put the files to current working directory.";
  input Integer loglevel = 3 "loglevel_nothing=0;loglevel_fatal=1;loglevel_error=2;loglevel_warning=3;loglevel_info=4;loglevel_verbose=5;loglevel_debug=6";
  input Boolean fullPath = false "When true the full output path is returned otherwise only the file name.";
  input Boolean debugLogging = false "When true the FMU's debug output is printed.";
  input Boolean generateInputConnectors = true "When true creates the input connector pins.";
  input Boolean generateOutputConnectors = true "When true creates the output connector pins.";
  output String generatedFileName "Returns the full path of the generated file.";
end importFMUModelDescription;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                filename,
                workdir=None,
                loglevel=None,
                fullPath=None,
                debugLogging=None,
                generateInputConnectors=None,
                generateOutputConnectors=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='importFMUModelDescription',
                    inputArguments=[
                        (Component(String), 'filename', filename, 'required'),
                        (Component(String), 'workdir', workdir, 'optional'),
                        (Component(Integer), 'loglevel', loglevel, 'optional'),
                        (Component(Boolean), 'fullPath', fullPath, 'optional'),
                        (Component(Boolean), 'debugLogging', debugLogging, 'optional'),
                        (Component(Boolean), 'generateInputConnectors', generateInputConnectors, 'optional'),
                        (Component(Boolean), 'generateOutputConnectors', generateOutputConnectors, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'generatedFileName'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.translateModelFMU')
        class translateModelFMU(
            ModelicaFunction,
        ):
            """
```modelica
function translateModelFMU
  input TypeName className "the class that should translated";
  input String version = "2.0" "FMU version, 1.0 or 2.0.";
  input String fmuType = "me" "FMU type, me (model exchange), cs (co-simulation), me_cs (both model exchange and co-simulation)";
  input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \\"className\\"";
  input Boolean includeResources = false "include Modelica based resources via loadResource or not";
  output String generatedFileName "Returns the full path of the generated FMU.";
end translateModelFMU;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                version=None,
                fmuType=None,
                fileNamePrefix=None,
                includeResources=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='translateModelFMU',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(String), 'version', version, 'optional'),
                        (Component(String), 'fmuType', fmuType, 'optional'),
                        (Component(String), 'fileNamePrefix', fileNamePrefix, 'optional'),
                        (Component(Boolean), 'includeResources', includeResources, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'generatedFileName'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.buildModelFMU')
        class buildModelFMU(
            ModelicaFunction,
        ):
            """
```modelica
function buildModelFMU
  input TypeName className "the class that should translated";
  input String version = "2.0" "FMU version, 1.0 or 2.0.";
  input String fmuType = "me" "FMU type, me (model exchange), cs (co-simulation), me_cs (both model exchange and co-simulation)";
  input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \\"className\\"";
  input String platforms[:] = {"static"} "The list of platforms to generate code for. \\"dynamic\\"=current platform, dynamically link the runtime. \\"static\\"=current platform, statically link everything. Else, use a host triple, e.g. \\"x86_64-linux-gnu\\" or \\"x86_64-w64-mingw32\\"";
  input Boolean includeResources = false "include Modelica based resources via loadResource or not";
  output String generatedFileName "Returns the full path of the generated FMU.";
end buildModelFMU;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                version=None,
                fmuType=None,
                fileNamePrefix=None,
                platforms=None,
                includeResources=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='buildModelFMU',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(String), 'version', version, 'optional'),
                        (Component(String), 'fmuType', fmuType, 'optional'),
                        (Component(String), 'fileNamePrefix', fileNamePrefix, 'optional'),
                        (Component(String)[:], 'platforms', platforms, 'optional'),
                        (Component(Boolean), 'includeResources', includeResources, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'generatedFileName'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.buildEncryptedPackage')
        class buildEncryptedPackage(
            ModelicaFunction,
        ):
            """
```modelica
function buildEncryptedPackage
  input TypeName className "the class that should encrypted";
  input Boolean encrypt = true;
  output Boolean success;
end buildEncryptedPackage;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                encrypt=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='buildEncryptedPackage',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(Boolean), 'encrypt', encrypt, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.simulate')
        class simulate(
            ModelicaFunction,
        ):
            """
```modelica
function simulate
  input TypeName className "the class that should simulated";
  input Real startTime = "<default>" "the start time of the simulation. <default> = 0.0";
  input Real stopTime = 1.0 "the stop time of the simulation. <default> = 1.0";
  input Real numberOfIntervals = 500 "number of intervals in the result file. <default> = 500";
  input Real tolerance = 1e-6 "tolerance used by the integration method. <default> = 1e-6";
  input String method = "<default>" "integration method used for simulation. <default> = dassl";
  input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \\"\\"";
  input String options = "<default>" "options. <default> = \\"\\"";
  input String outputFormat = "mat" "Format for the result file. <default> = \\"mat\\"";
  input String variableFilter = ".*" "Filter for variables that should store in result file. <default> = \\".*\\"";
  input String cflags = "<default>" "cflags. <default> = \\"\\"";
  input String simflags = "<default>" "simflags. <default> = \\"\\"";
  output SimulationResult simulationResults;

  record SimulationResult
    String resultFile;
    String simulationOptions;
    String messages;
    Real timeFrontend;
    Real timeBackend;
    Real timeSimCode;
    Real timeTemplates;
    Real timeCompile;
    Real timeSimulation;
    Real timeTotal;
  end SimulationResult;
end simulate;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                startTime=None,
                stopTime=None,
                numberOfIntervals=None,
                tolerance=None,
                method=None,
                fileNamePrefix=None,
                options=None,
                outputFormat=None,
                variableFilter=None,
                cflags=None,
                simflags=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='simulate',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(Real), 'startTime', startTime, 'optional'),
                        (Component(Real), 'stopTime', stopTime, 'optional'),
                        (Component(Real), 'numberOfIntervals', numberOfIntervals, 'optional'),
                        (Component(Real), 'tolerance', tolerance, 'optional'),
                        (Component(String), 'method', method, 'optional'),
                        (Component(String), 'fileNamePrefix', fileNamePrefix, 'optional'),
                        (Component(String), 'options', options, 'optional'),
                        (Component(String), 'outputFormat', outputFormat, 'optional'),
                        (Component(String), 'variableFilter', variableFilter, 'optional'),
                        (Component(String), 'cflags', cflags, 'optional'),
                        (Component(String), 'simflags', simflags, 'optional'),
                    ],
                    outputArguments=[
                        (Component(OpenModelica.Scripting.simulate.SimulationResult), 'simulationResults'),
                    ],
                    parser=parse_OMCValue,
                )

            @modelica_name('OpenModelica.Scripting.simulate.SimulationResult')
            class SimulationResult(
                ModelicaRecord,
            ):
                """
```modelica
record SimulationResult
  String resultFile;
  String simulationOptions;
  String messages;
  Real timeFrontend;
  Real timeBackend;
  Real timeSimCode;
  Real timeTemplates;
  Real timeCompile;
  Real timeSimulation;
  Real timeTotal;
end SimulationResult;
```
                """
                @element
                def resultFile(cls):
                    return Component(String)

                @element
                def simulationOptions(cls):
                    return Component(String)

                @element
                def messages(cls):
                    return Component(String)

                @element
                def timeFrontend(cls):
                    return Component(Real)

                @element
                def timeBackend(cls):
                    return Component(Real)

                @element
                def timeSimCode(cls):
                    return Component(Real)

                @element
                def timeTemplates(cls):
                    return Component(Real)

                @element
                def timeCompile(cls):
                    return Component(Real)

                @element
                def timeSimulation(cls):
                    return Component(Real)

                @element
                def timeTotal(cls):
                    return Component(Real)

        @modelica_name('OpenModelica.Scripting.buildModel')
        class buildModel(
            ModelicaFunction,
        ):
            """
```modelica
function buildModel
  input TypeName className "the class that should be built";
  input Real startTime = "<default>" "the start time of the simulation. <default> = 0.0";
  input Real stopTime = 1.0 "the stop time of the simulation. <default> = 1.0";
  input Real numberOfIntervals = 500 "number of intervals in the result file. <default> = 500";
  input Real tolerance = 1e-6 "tolerance used by the integration method. <default> = 1e-6";
  input String method = "<default>" "integration method used for simulation. <default> = dassl";
  input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \\"\\"";
  input String options = "<default>" "options. <default> = \\"\\"";
  input String outputFormat = "mat" "Format for the result file. <default> = \\"mat\\"";
  input String variableFilter = ".*" "Filter for variables that should store in result file. <default> = \\".*\\"";
  input String cflags = "<default>" "cflags. <default> = \\"\\"";
  input String simflags = "<default>" "simflags. <default> = \\"\\"";
  output String[2] buildModelResults;
end buildModel;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                startTime=None,
                stopTime=None,
                numberOfIntervals=None,
                tolerance=None,
                method=None,
                fileNamePrefix=None,
                options=None,
                outputFormat=None,
                variableFilter=None,
                cflags=None,
                simflags=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='buildModel',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(Real), 'startTime', startTime, 'optional'),
                        (Component(Real), 'stopTime', stopTime, 'optional'),
                        (Component(Real), 'numberOfIntervals', numberOfIntervals, 'optional'),
                        (Component(Real), 'tolerance', tolerance, 'optional'),
                        (Component(String), 'method', method, 'optional'),
                        (Component(String), 'fileNamePrefix', fileNamePrefix, 'optional'),
                        (Component(String), 'options', options, 'optional'),
                        (Component(String), 'outputFormat', outputFormat, 'optional'),
                        (Component(String), 'variableFilter', variableFilter, 'optional'),
                        (Component(String), 'cflags', cflags, 'optional'),
                        (Component(String), 'simflags', simflags, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String)[2], 'buildModelResults'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.buildLabel')
        class buildLabel(
            ModelicaFunction,
        ):
            """
```modelica
function buildLabel
  input TypeName className "the class that should be built";
  input Real startTime = 0.0 "the start time of the simulation. <default> = 0.0";
  input Real stopTime = 1.0 "the stop time of the simulation. <default> = 1.0";
  input Integer numberOfIntervals = 500 "number of intervals in the result file. <default> = 500";
  input Real tolerance = 1e-6 "tolerance used by the integration method. <default> = 1e-6";
  input String method = "dassl" "integration method used for simulation. <default> = dassl";
  input String fileNamePrefix = "" "fileNamePrefix. <default> = \\"\\"";
  input String options = "" "options. <default> = \\"\\"";
  input String outputFormat = "mat" "Format for the result file. <default> = \\"mat\\"";
  input String variableFilter = ".*" "Filter for variables that should store in result file. <default> = \\".*\\"";
  input String cflags = "" "cflags. <default> = \\"\\"";
  input String simflags = "" "simflags. <default> = \\"\\"";
  output String[2] buildModelResults;
end buildLabel;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                startTime=None,
                stopTime=None,
                numberOfIntervals=None,
                tolerance=None,
                method=None,
                fileNamePrefix=None,
                options=None,
                outputFormat=None,
                variableFilter=None,
                cflags=None,
                simflags=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='buildLabel',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(Real), 'startTime', startTime, 'optional'),
                        (Component(Real), 'stopTime', stopTime, 'optional'),
                        (Component(Integer), 'numberOfIntervals', numberOfIntervals, 'optional'),
                        (Component(Real), 'tolerance', tolerance, 'optional'),
                        (Component(String), 'method', method, 'optional'),
                        (Component(String), 'fileNamePrefix', fileNamePrefix, 'optional'),
                        (Component(String), 'options', options, 'optional'),
                        (Component(String), 'outputFormat', outputFormat, 'optional'),
                        (Component(String), 'variableFilter', variableFilter, 'optional'),
                        (Component(String), 'cflags', cflags, 'optional'),
                        (Component(String), 'simflags', simflags, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String)[2], 'buildModelResults'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.reduceTerms')
        class reduceTerms(
            ModelicaFunction,
        ):
            """
```modelica
function reduceTerms
  input TypeName className "the class that should be built";
  input Real startTime = 0.0 "the start time of the simulation. <default> = 0.0";
  input Real stopTime = 1.0 "the stop time of the simulation. <default> = 1.0";
  input Integer numberOfIntervals = 500 "number of intervals in the result file. <default> = 500";
  input Real tolerance = 1e-6 "tolerance used by the integration method. <default> = 1e-6";
  input String method = "dassl" "integration method used for simulation. <default> = dassl";
  input String fileNamePrefix = "" "fileNamePrefix. <default> = \\"\\"";
  input String options = "" "options. <default> = \\"\\"";
  input String outputFormat = "mat" "Format for the result file. <default> = \\"mat\\"";
  input String variableFilter = ".*" "Filter for variables that should store in result file. <default> = \\".*\\"";
  input String cflags = "" "cflags. <default> = \\"\\"";
  input String simflags = "" "simflags. <default> = \\"\\"";
  input String labelstoCancel = "";
  output String[2] buildModelResults;
end reduceTerms;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                startTime=None,
                stopTime=None,
                numberOfIntervals=None,
                tolerance=None,
                method=None,
                fileNamePrefix=None,
                options=None,
                outputFormat=None,
                variableFilter=None,
                cflags=None,
                simflags=None,
                labelstoCancel=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='reduceTerms',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(Real), 'startTime', startTime, 'optional'),
                        (Component(Real), 'stopTime', stopTime, 'optional'),
                        (Component(Integer), 'numberOfIntervals', numberOfIntervals, 'optional'),
                        (Component(Real), 'tolerance', tolerance, 'optional'),
                        (Component(String), 'method', method, 'optional'),
                        (Component(String), 'fileNamePrefix', fileNamePrefix, 'optional'),
                        (Component(String), 'options', options, 'optional'),
                        (Component(String), 'outputFormat', outputFormat, 'optional'),
                        (Component(String), 'variableFilter', variableFilter, 'optional'),
                        (Component(String), 'cflags', cflags, 'optional'),
                        (Component(String), 'simflags', simflags, 'optional'),
                        (Component(String), 'labelstoCancel', labelstoCancel, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String)[2], 'buildModelResults'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.moveClass')
        class moveClass(
            ModelicaFunction,
        ):
            """
```modelica
function moveClass
  input TypeName className "the class that should be moved";
  input Integer offset "Offset in the class list.";
  output Boolean result;
end moveClass;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                offset,
            ):
                return _session_.__omc__.call_function(
                    funcName='moveClass',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(Integer), 'offset', offset, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.moveClassToTop')
        class moveClassToTop(
            ModelicaFunction,
        ):
            """
```modelica
function moveClassToTop
  input TypeName className;
  output Boolean result;
end moveClassToTop;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
            ):
                return _session_.__omc__.call_function(
                    funcName='moveClassToTop',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.moveClassToBottom')
        class moveClassToBottom(
            ModelicaFunction,
        ):
            """
```modelica
function moveClassToBottom
  input TypeName className;
  output Boolean result;
end moveClassToBottom;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
            ):
                return _session_.__omc__.call_function(
                    funcName='moveClassToBottom',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.copyClass')
        class copyClass(
            ModelicaFunction,
        ):
            """
```modelica
function copyClass
  input TypeName className "the class that should be copied";
  input String newClassName "the name for new class";
  input TypeName withIn = $Code(TopLevel) "the with in path for new class";
  output Boolean result;
end copyClass;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                newClassName,
                withIn=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='copyClass',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(String), 'newClassName', newClassName, 'required'),
                        (Component(TypeName), 'withIn', withIn, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.linearize')
        class linearize(
            ModelicaFunction,
        ):
            """
```modelica
function linearize
  input TypeName className "the class that should simulated";
  input Real startTime = "<default>" "the start time of the simulation. <default> = 0.0";
  input Real stopTime = 1.0 "the stop time of the simulation. <default> = 1.0";
  input Real numberOfIntervals = 500 "number of intervals in the result file. <default> = 500";
  input Real stepSize = 0.002 "step size that is used for the result file. <default> = 0.002";
  input Real tolerance = 1e-6 "tolerance used by the integration method. <default> = 1e-6";
  input String method = "<default>" "integration method used for simulation. <default> = dassl";
  input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \\"\\"";
  input Boolean storeInTemp = false "storeInTemp. <default> = false";
  input Boolean noClean = false "noClean. <default> = false";
  input String options = "<default>" "options. <default> = \\"\\"";
  input String outputFormat = "mat" "Format for the result file. <default> = \\"mat\\"";
  input String variableFilter = ".*" "Filter for variables that should store in result file. <default> = \\".*\\"";
  input String cflags = "<default>" "cflags. <default> = \\"\\"";
  input String simflags = "<default>" "simflags. <default> = \\"\\"";
  output String linearizationResult;
end linearize;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                startTime=None,
                stopTime=None,
                numberOfIntervals=None,
                stepSize=None,
                tolerance=None,
                method=None,
                fileNamePrefix=None,
                storeInTemp=None,
                noClean=None,
                options=None,
                outputFormat=None,
                variableFilter=None,
                cflags=None,
                simflags=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='linearize',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(Real), 'startTime', startTime, 'optional'),
                        (Component(Real), 'stopTime', stopTime, 'optional'),
                        (Component(Real), 'numberOfIntervals', numberOfIntervals, 'optional'),
                        (Component(Real), 'stepSize', stepSize, 'optional'),
                        (Component(Real), 'tolerance', tolerance, 'optional'),
                        (Component(String), 'method', method, 'optional'),
                        (Component(String), 'fileNamePrefix', fileNamePrefix, 'optional'),
                        (Component(Boolean), 'storeInTemp', storeInTemp, 'optional'),
                        (Component(Boolean), 'noClean', noClean, 'optional'),
                        (Component(String), 'options', options, 'optional'),
                        (Component(String), 'outputFormat', outputFormat, 'optional'),
                        (Component(String), 'variableFilter', variableFilter, 'optional'),
                        (Component(String), 'cflags', cflags, 'optional'),
                        (Component(String), 'simflags', simflags, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'linearizationResult'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.optimize')
        class optimize(
            ModelicaFunction,
        ):
            """
```modelica
function optimize
  input TypeName className "the class that should simulated";
  input Real startTime = "<default>" "the start time of the simulation. <default> = 0.0";
  input Real stopTime = 1.0 "the stop time of the simulation. <default> = 1.0";
  input Real numberOfIntervals = 500 "number of intervals in the result file. <default> = 500";
  input Real stepSize = 0.002 "step size that is used for the result file. <default> = 0.002";
  input Real tolerance = 1e-6 "tolerance used by the integration method. <default> = 1e-6";
  input String method = DAE.SCONST("optimization") "optimize a modelica/optimica model.";
  input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \\"\\"";
  input Boolean storeInTemp = false "storeInTemp. <default> = false";
  input Boolean noClean = false "noClean. <default> = false";
  input String options = "<default>" "options. <default> = \\"\\"";
  input String outputFormat = "mat" "Format for the result file. <default> = \\"mat\\"";
  input String variableFilter = ".*" "Filter for variables that should store in result file. <default> = \\".*\\"";
  input String cflags = "<default>" "cflags. <default> = \\"\\"";
  input String simflags = "<default>" "simflags. <default> = \\"\\"";
  output String optimizationResults;
end optimize;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                startTime=None,
                stopTime=None,
                numberOfIntervals=None,
                stepSize=None,
                tolerance=None,
                method=None,
                fileNamePrefix=None,
                storeInTemp=None,
                noClean=None,
                options=None,
                outputFormat=None,
                variableFilter=None,
                cflags=None,
                simflags=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='optimize',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(Real), 'startTime', startTime, 'optional'),
                        (Component(Real), 'stopTime', stopTime, 'optional'),
                        (Component(Real), 'numberOfIntervals', numberOfIntervals, 'optional'),
                        (Component(Real), 'stepSize', stepSize, 'optional'),
                        (Component(Real), 'tolerance', tolerance, 'optional'),
                        (Component(String), 'method', method, 'optional'),
                        (Component(String), 'fileNamePrefix', fileNamePrefix, 'optional'),
                        (Component(Boolean), 'storeInTemp', storeInTemp, 'optional'),
                        (Component(Boolean), 'noClean', noClean, 'optional'),
                        (Component(String), 'options', options, 'optional'),
                        (Component(String), 'outputFormat', outputFormat, 'optional'),
                        (Component(String), 'variableFilter', variableFilter, 'optional'),
                        (Component(String), 'cflags', cflags, 'optional'),
                        (Component(String), 'simflags', simflags, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'optimizationResults'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getSourceFile')
        class getSourceFile(
            ModelicaFunction,
        ):
            """
```modelica
function getSourceFile
  input TypeName class_;
  output String filename "empty on failure";
end getSourceFile;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
            ):
                return _session_.__omc__.call_function(
                    funcName='getSourceFile',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'filename'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setSourceFile')
        class setSourceFile(
            ModelicaFunction,
        ):
            """
```modelica
function setSourceFile
  input TypeName class_;
  input String filename;
  output Boolean success;
end setSourceFile;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                filename,
            ):
                return _session_.__omc__.call_function(
                    funcName='setSourceFile',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(String), 'filename', filename, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.isShortDefinition')
        class isShortDefinition(
            ModelicaFunction,
        ):
            """
```modelica
function isShortDefinition
  input TypeName class_;
  output Boolean isShortCls;
end isShortDefinition;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
            ):
                return _session_.__omc__.call_function(
                    funcName='isShortDefinition',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'isShortCls'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setClassComment')
        class setClassComment(
            ModelicaFunction,
        ):
            """
```modelica
function setClassComment
  input TypeName class_;
  input String filename;
  output Boolean success;
end setClassComment;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                filename,
            ):
                return _session_.__omc__.call_function(
                    funcName='setClassComment',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(String), 'filename', filename, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getClassNames')
        class getClassNames(
            ModelicaFunction,
        ):
            """
```modelica
function getClassNames
  input TypeName class_ = $Code(AllLoadedClasses);
  input Boolean recursive = false;
  input Boolean qualified = false;
  input Boolean sort = false;
  input Boolean builtin = false "List also builtin classes if true";
  input Boolean showProtected = false "List also protected classes if true";
  input Boolean includeConstants = false "List also constants in the class if true";
  output TypeName classNames[:];
end getClassNames;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_=None,
                recursive=None,
                qualified=None,
                sort=None,
                builtin=None,
                showProtected=None,
                includeConstants=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='getClassNames',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'optional'),
                        (Component(Boolean), 'recursive', recursive, 'optional'),
                        (Component(Boolean), 'qualified', qualified, 'optional'),
                        (Component(Boolean), 'sort', sort, 'optional'),
                        (Component(Boolean), 'builtin', builtin, 'optional'),
                        (Component(Boolean), 'showProtected', showProtected, 'optional'),
                        (Component(Boolean), 'includeConstants', includeConstants, 'optional'),
                    ],
                    outputArguments=[
                        (Component(TypeName)[:], 'classNames'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getUsedClassNames')
        class getUsedClassNames(
            ModelicaFunction,
        ):
            """
```modelica
function getUsedClassNames
  input TypeName className;
  output TypeName classNames[:];
end getUsedClassNames;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
            ):
                return _session_.__omc__.call_function(
                    funcName='getUsedClassNames',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                    ],
                    outputArguments=[
                        (Component(TypeName)[:], 'classNames'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getPackages')
        class getPackages(
            ModelicaFunction,
        ):
            """
```modelica
function getPackages
  input TypeName class_ = $Code(AllLoadedClasses);
  output TypeName classNames[:];
end getPackages;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='getPackages',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'optional'),
                    ],
                    outputArguments=[
                        (Component(TypeName)[:], 'classNames'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getAllSubtypeOf')
        class getAllSubtypeOf(
            ModelicaFunction,
        ):
            """
```modelica
function getAllSubtypeOf
  input TypeName className;
  input TypeName parentClass = $Code(AllLoadedClasses);
  input Boolean qualified = false;
  input Boolean includePartial = false;
  input Boolean sort = false;
  output TypeName classNames[:];
end getAllSubtypeOf;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                parentClass=None,
                qualified=None,
                includePartial=None,
                sort=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='getAllSubtypeOf',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(TypeName), 'parentClass', parentClass, 'optional'),
                        (Component(Boolean), 'qualified', qualified, 'optional'),
                        (Component(Boolean), 'includePartial', includePartial, 'optional'),
                        (Component(Boolean), 'sort', sort, 'optional'),
                    ],
                    outputArguments=[
                        (Component(TypeName)[:], 'classNames'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.basePlotFunction')
        class basePlotFunction(
            ModelicaFunction,
        ):
            """
```modelica
partial function basePlotFunction
  input String fileName = "<default>" "The filename containing the variables. <default> will read the last simulation result";
  input String interpolation = "linear" "
      Determines if the simulation data should be interpolated to allow drawing of continuous lines in the diagram.
      \\"linear\\" results in linear interpolation between data points, \\"constant\\" keeps the value of the last known
      data point until a new one is found and \\"none\\" results in a diagram where only known data points are plotted.";
  input String title = "Plot by OpenModelica" "This text will be used as the diagram title.";
  input Boolean legend = true "Determines whether or not the variable legend is shown.";
  input Boolean grid = true "Determines whether or not a grid is shown in the diagram.";
  input Boolean logX = false "Determines whether or not the horizontal axis is logarithmically scaled.";
  input Boolean logY = false "Determines whether or not the vertical axis is logarithmically scaled.";
  input String xLabel = "time" "This text will be used as the horizontal label in the diagram.";
  input String yLabel = "" "This text will be used as the vertical label in the diagram.";
  input Boolean points = false "Determines whether or not the data points should be indicated by a dot in the diagram.";
  input Real xRange[2] = {0.0, 0.0} "Determines the horizontal interval that is visible in the diagram. {0,0} will select a suitable range.";
  input Real yRange[2] = {0.0, 0.0} "Determines the vertical interval that is visible in the diagram. {0,0} will select a suitable range.";
  output Boolean success "Returns true on success";
end basePlotFunction;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName=None,
                interpolation=None,
                title=None,
                legend=None,
                grid=None,
                logX=None,
                logY=None,
                xLabel=None,
                yLabel=None,
                points=None,
                xRange=None,
                yRange=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='basePlotFunction',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'optional'),
                        (Component(String), 'interpolation', interpolation, 'optional'),
                        (Component(String), 'title', title, 'optional'),
                        (Component(Boolean), 'legend', legend, 'optional'),
                        (Component(Boolean), 'grid', grid, 'optional'),
                        (Component(Boolean), 'logX', logX, 'optional'),
                        (Component(Boolean), 'logY', logY, 'optional'),
                        (Component(String), 'xLabel', xLabel, 'optional'),
                        (Component(String), 'yLabel', yLabel, 'optional'),
                        (Component(Boolean), 'points', points, 'optional'),
                        (Component(Real)[2], 'xRange', xRange, 'optional'),
                        (Component(Real)[2], 'yRange', yRange, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.plot')
        class plot(
            ModelicaFunction,
        ):
            """
```modelica
function plot
  input VariableNames vars "The variables you want to plot";
  input Boolean externalWindow = false "Opens the plot in a new plot window";
  input String fileName = "<default>" "The filename containing the variables. <default> will read the last simulation result";
  input String title = "" "This text will be used as the diagram title.";
  input String grid = "detailed" "Sets the grid for the plot i.e simple, detailed, none.";
  input Boolean logX = false "Determines whether or not the horizontal axis is logarithmically scaled.";
  input Boolean logY = false "Determines whether or not the vertical axis is logarithmically scaled.";
  input String xLabel = "time" "This text will be used as the horizontal label in the diagram.";
  input String yLabel = "" "This text will be used as the vertical label in the diagram.";
  input Real xRange[2] = {0.0, 0.0} "Determines the horizontal interval that is visible in the diagram. {0,0} will select a suitable range.";
  input Real yRange[2] = {0.0, 0.0} "Determines the vertical interval that is visible in the diagram. {0,0} will select a suitable range.";
  input Real curveWidth = 1.0 "Sets the width of the curve.";
  input Integer curveStyle = 1 "Sets the style of the curve. SolidLine=1, DashLine=2, DotLine=3, DashDotLine=4, DashDotDotLine=5, Sticks=6, Steps=7.";
  input String legendPosition = "top" "Sets the POSITION of the legend i.e left, right, top, bottom, none.";
  input String footer = "" "This text will be used as the diagram footer.";
  input Boolean autoScale = true "Use auto scale while plotting.";
  input Boolean forceOMPlot = false "if true launches OMPlot and doesn't call callback function even if it is defined.";
  output Boolean success "Returns true on success";
end plot;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                vars,
                externalWindow=None,
                fileName=None,
                title=None,
                grid=None,
                logX=None,
                logY=None,
                xLabel=None,
                yLabel=None,
                xRange=None,
                yRange=None,
                curveWidth=None,
                curveStyle=None,
                legendPosition=None,
                footer=None,
                autoScale=None,
                forceOMPlot=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='plot',
                    inputArguments=[
                        (Component(VariableName)[:], 'vars', vars, 'required'),
                        (Component(Boolean), 'externalWindow', externalWindow, 'optional'),
                        (Component(String), 'fileName', fileName, 'optional'),
                        (Component(String), 'title', title, 'optional'),
                        (Component(String), 'grid', grid, 'optional'),
                        (Component(Boolean), 'logX', logX, 'optional'),
                        (Component(Boolean), 'logY', logY, 'optional'),
                        (Component(String), 'xLabel', xLabel, 'optional'),
                        (Component(String), 'yLabel', yLabel, 'optional'),
                        (Component(Real)[2], 'xRange', xRange, 'optional'),
                        (Component(Real)[2], 'yRange', yRange, 'optional'),
                        (Component(Real), 'curveWidth', curveWidth, 'optional'),
                        (Component(Integer), 'curveStyle', curveStyle, 'optional'),
                        (Component(String), 'legendPosition', legendPosition, 'optional'),
                        (Component(String), 'footer', footer, 'optional'),
                        (Component(Boolean), 'autoScale', autoScale, 'optional'),
                        (Component(Boolean), 'forceOMPlot', forceOMPlot, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.plotAll')
        class plotAll(
            ModelicaFunction,
        ):
            """
```modelica
function plotAll
  input Boolean externalWindow = false "Opens the plot in a new plot window";
  input String fileName = "<default>" "The filename containing the variables. <default> will read the last simulation result";
  input String title = "" "This text will be used as the diagram title.";
  input String grid = "detailed" "Sets the grid for the plot i.e simple, detailed, none.";
  input Boolean logX = false "Determines whether or not the horizontal axis is logarithmically scaled.";
  input Boolean logY = false "Determines whether or not the vertical axis is logarithmically scaled.";
  input String xLabel = "time" "This text will be used as the horizontal label in the diagram.";
  input String yLabel = "" "This text will be used as the vertical label in the diagram.";
  input Real xRange[2] = {0.0, 0.0} "Determines the horizontal interval that is visible in the diagram. {0,0} will select a suitable range.";
  input Real yRange[2] = {0.0, 0.0} "Determines the vertical interval that is visible in the diagram. {0,0} will select a suitable range.";
  input Real curveWidth = 1.0 "Sets the width of the curve.";
  input Integer curveStyle = 1 "Sets the style of the curve. SolidLine=1, DashLine=2, DotLine=3, DashDotLine=4, DashDotDotLine=5, Sticks=6, Steps=7.";
  input String legendPosition = "top" "Sets the POSITION of the legend i.e left, right, top, bottom, none.";
  input String footer = "" "This text will be used as the diagram footer.";
  input Boolean autoScale = true "Use auto scale while plotting.";
  input Boolean forceOMPlot = false "if true launches OMPlot and doesn't call callback function even if it is defined.";
  output Boolean success "Returns true on success";
end plotAll;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                externalWindow=None,
                fileName=None,
                title=None,
                grid=None,
                logX=None,
                logY=None,
                xLabel=None,
                yLabel=None,
                xRange=None,
                yRange=None,
                curveWidth=None,
                curveStyle=None,
                legendPosition=None,
                footer=None,
                autoScale=None,
                forceOMPlot=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='plotAll',
                    inputArguments=[
                        (Component(Boolean), 'externalWindow', externalWindow, 'optional'),
                        (Component(String), 'fileName', fileName, 'optional'),
                        (Component(String), 'title', title, 'optional'),
                        (Component(String), 'grid', grid, 'optional'),
                        (Component(Boolean), 'logX', logX, 'optional'),
                        (Component(Boolean), 'logY', logY, 'optional'),
                        (Component(String), 'xLabel', xLabel, 'optional'),
                        (Component(String), 'yLabel', yLabel, 'optional'),
                        (Component(Real)[2], 'xRange', xRange, 'optional'),
                        (Component(Real)[2], 'yRange', yRange, 'optional'),
                        (Component(Real), 'curveWidth', curveWidth, 'optional'),
                        (Component(Integer), 'curveStyle', curveStyle, 'optional'),
                        (Component(String), 'legendPosition', legendPosition, 'optional'),
                        (Component(String), 'footer', footer, 'optional'),
                        (Component(Boolean), 'autoScale', autoScale, 'optional'),
                        (Component(Boolean), 'forceOMPlot', forceOMPlot, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.plotParametric')
        class plotParametric(
            ModelicaFunction,
        ):
            """
```modelica
function plotParametric
  input VariableName xVariable;
  input VariableName yVariable;
  input Boolean externalWindow = false "Opens the plot in a new plot window";
  input String fileName = "<default>" "The filename containing the variables. <default> will read the last simulation result";
  input String title = "" "This text will be used as the diagram title.";
  input String grid = "detailed" "Sets the grid for the plot i.e simple, detailed, none.";
  input Boolean logX = false "Determines whether or not the horizontal axis is logarithmically scaled.";
  input Boolean logY = false "Determines whether or not the vertical axis is logarithmically scaled.";
  input String xLabel = "time" "This text will be used as the horizontal label in the diagram.";
  input String yLabel = "" "This text will be used as the vertical label in the diagram.";
  input Real xRange[2] = {0.0, 0.0} "Determines the horizontal interval that is visible in the diagram. {0,0} will select a suitable range.";
  input Real yRange[2] = {0.0, 0.0} "Determines the vertical interval that is visible in the diagram. {0,0} will select a suitable range.";
  input Real curveWidth = 1.0 "Sets the width of the curve.";
  input Integer curveStyle = 1 "Sets the style of the curve. SolidLine=1, DashLine=2, DotLine=3, DashDotLine=4, DashDotDotLine=5, Sticks=6, Steps=7.";
  input String legendPosition = "top" "Sets the POSITION of the legend i.e left, right, top, bottom, none.";
  input String footer = "" "This text will be used as the diagram footer.";
  input Boolean autoScale = true "Use auto scale while plotting.";
  input Boolean forceOMPlot = false "if true launches OMPlot and doesn't call callback function even if it is defined.";
  output Boolean success "Returns true on success";
end plotParametric;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                xVariable,
                yVariable,
                externalWindow=None,
                fileName=None,
                title=None,
                grid=None,
                logX=None,
                logY=None,
                xLabel=None,
                yLabel=None,
                xRange=None,
                yRange=None,
                curveWidth=None,
                curveStyle=None,
                legendPosition=None,
                footer=None,
                autoScale=None,
                forceOMPlot=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='plotParametric',
                    inputArguments=[
                        (Component(VariableName), 'xVariable', xVariable, 'required'),
                        (Component(VariableName), 'yVariable', yVariable, 'required'),
                        (Component(Boolean), 'externalWindow', externalWindow, 'optional'),
                        (Component(String), 'fileName', fileName, 'optional'),
                        (Component(String), 'title', title, 'optional'),
                        (Component(String), 'grid', grid, 'optional'),
                        (Component(Boolean), 'logX', logX, 'optional'),
                        (Component(Boolean), 'logY', logY, 'optional'),
                        (Component(String), 'xLabel', xLabel, 'optional'),
                        (Component(String), 'yLabel', yLabel, 'optional'),
                        (Component(Real)[2], 'xRange', xRange, 'optional'),
                        (Component(Real)[2], 'yRange', yRange, 'optional'),
                        (Component(Real), 'curveWidth', curveWidth, 'optional'),
                        (Component(Integer), 'curveStyle', curveStyle, 'optional'),
                        (Component(String), 'legendPosition', legendPosition, 'optional'),
                        (Component(String), 'footer', footer, 'optional'),
                        (Component(Boolean), 'autoScale', autoScale, 'optional'),
                        (Component(Boolean), 'forceOMPlot', forceOMPlot, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.readSimulationResult')
        class readSimulationResult(
            ModelicaFunction,
        ):
            """
```modelica
function readSimulationResult
  input String filename;
  input VariableNames variables;
  input Integer size = 0 "0=read any size... If the size is not the same as the result-file, this function fails";
  output Real result[:, :];
end readSimulationResult;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                filename,
                variables,
                size=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='readSimulationResult',
                    inputArguments=[
                        (Component(String), 'filename', filename, 'required'),
                        (Component(VariableName)[:], 'variables', variables, 'required'),
                        (Component(Integer), 'size', size, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Real)[:, :], 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.readSimulationResultSize')
        class readSimulationResultSize(
            ModelicaFunction,
        ):
            """
```modelica
function readSimulationResultSize
  input String fileName;
  output Integer sz;
end readSimulationResultSize;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
            ):
                return _session_.__omc__.call_function(
                    funcName='readSimulationResultSize',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'sz'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.readSimulationResultVars')
        class readSimulationResultVars(
            ModelicaFunction,
        ):
            """
```modelica
function readSimulationResultVars
  input String fileName;
  input Boolean readParameters = true;
  input Boolean openmodelicaStyle = false;
  output String[:] vars;
end readSimulationResultVars;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
                readParameters=None,
                openmodelicaStyle=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='readSimulationResultVars',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                        (Component(Boolean), 'readParameters', readParameters, 'optional'),
                        (Component(Boolean), 'openmodelicaStyle', openmodelicaStyle, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'vars'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.filterSimulationResults')
        class filterSimulationResults(
            ModelicaFunction,
        ):
            """
```modelica
function filterSimulationResults
  input String inFile;
  input String outFile;
  input String[:] vars;
  input Integer numberOfIntervals = 0 "0=Do not resample";
  input Boolean removeDescription = false;
  output Boolean success;
end filterSimulationResults;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                inFile,
                outFile,
                vars,
                numberOfIntervals=None,
                removeDescription=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='filterSimulationResults',
                    inputArguments=[
                        (Component(String), 'inFile', inFile, 'required'),
                        (Component(String), 'outFile', outFile, 'required'),
                        (Component(String)[:], 'vars', vars, 'required'),
                        (Component(Integer), 'numberOfIntervals', numberOfIntervals, 'optional'),
                        (Component(Boolean), 'removeDescription', removeDescription, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.compareSimulationResults')
        class compareSimulationResults(
            ModelicaFunction,
        ):
            """
```modelica
function compareSimulationResults
  input String filename;
  input String reffilename;
  input String logfilename;
  input Real relTol = 0.01;
  input Real absTol = 0.0001;
  input String[:] vars = fill("", 0);
  output String[:] result;
end compareSimulationResults;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                filename,
                reffilename,
                logfilename,
                relTol=None,
                absTol=None,
                vars=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='compareSimulationResults',
                    inputArguments=[
                        (Component(String), 'filename', filename, 'required'),
                        (Component(String), 'reffilename', reffilename, 'required'),
                        (Component(String), 'logfilename', logfilename, 'required'),
                        (Component(Real), 'relTol', relTol, 'optional'),
                        (Component(Real), 'absTol', absTol, 'optional'),
                        (Component(String)[:], 'vars', vars, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.deltaSimulationResults')
        class deltaSimulationResults(
            ModelicaFunction,
        ):
            """
```modelica
function deltaSimulationResults
  input String filename;
  input String reffilename;
  input String method "method to compute then error. choose 1norm, 2norm, maxerr";
  input String[:] vars = fill("", 0);
  output Real result;
end deltaSimulationResults;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                filename,
                reffilename,
                method,
                vars=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='deltaSimulationResults',
                    inputArguments=[
                        (Component(String), 'filename', filename, 'required'),
                        (Component(String), 'reffilename', reffilename, 'required'),
                        (Component(String), 'method', method, 'required'),
                        (Component(String)[:], 'vars', vars, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Real), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.diffSimulationResults')
        class diffSimulationResults(
            ModelicaFunction,
        ):
            """
```modelica
function diffSimulationResults
  input String actualFile;
  input String expectedFile;
  input String diffPrefix;
  input Real relTol = 1e-3 "y tolerance";
  input Real relTolDiffMinMax = 1e-4 "y tolerance based on the difference between the maximum and minimum of the signal";
  input Real rangeDelta = 0.002 "x tolerance";
  input String[:] vars = fill("", 0);
  input Boolean keepEqualResults = false;
  output Boolean success;
  output String[:] failVars;
end diffSimulationResults;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                actualFile,
                expectedFile,
                diffPrefix,
                relTol=None,
                relTolDiffMinMax=None,
                rangeDelta=None,
                vars=None,
                keepEqualResults=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='diffSimulationResults',
                    inputArguments=[
                        (Component(String), 'actualFile', actualFile, 'required'),
                        (Component(String), 'expectedFile', expectedFile, 'required'),
                        (Component(String), 'diffPrefix', diffPrefix, 'required'),
                        (Component(Real), 'relTol', relTol, 'optional'),
                        (Component(Real), 'relTolDiffMinMax', relTolDiffMinMax, 'optional'),
                        (Component(Real), 'rangeDelta', rangeDelta, 'optional'),
                        (Component(String)[:], 'vars', vars, 'optional'),
                        (Component(Boolean), 'keepEqualResults', keepEqualResults, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                        (Component(String)[:], 'failVars'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.diffSimulationResultsHtml')
        class diffSimulationResultsHtml(
            ModelicaFunction,
        ):
            """
```modelica
function diffSimulationResultsHtml
  input String var;
  input String actualFile;
  input String expectedFile;
  input Real relTol = 1e-3 "y tolerance";
  input Real relTolDiffMinMax = 1e-4 "y tolerance based on the difference between the maximum and minimum of the signal";
  input Real rangeDelta = 0.002 "x tolerance";
  output String html;
end diffSimulationResultsHtml;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                var,
                actualFile,
                expectedFile,
                relTol=None,
                relTolDiffMinMax=None,
                rangeDelta=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='diffSimulationResultsHtml',
                    inputArguments=[
                        (Component(String), 'var', var, 'required'),
                        (Component(String), 'actualFile', actualFile, 'required'),
                        (Component(String), 'expectedFile', expectedFile, 'required'),
                        (Component(Real), 'relTol', relTol, 'optional'),
                        (Component(Real), 'relTolDiffMinMax', relTolDiffMinMax, 'optional'),
                        (Component(Real), 'rangeDelta', rangeDelta, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'html'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.checkTaskGraph')
        class checkTaskGraph(
            ModelicaFunction,
        ):
            """
```modelica
function checkTaskGraph
  input String filename;
  input String reffilename;
  output String[:] result;
end checkTaskGraph;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                filename,
                reffilename,
            ):
                return _session_.__omc__.call_function(
                    funcName='checkTaskGraph',
                    inputArguments=[
                        (Component(String), 'filename', filename, 'required'),
                        (Component(String), 'reffilename', reffilename, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.checkCodeGraph')
        class checkCodeGraph(
            ModelicaFunction,
        ):
            """
```modelica
function checkCodeGraph
  input String graphfile;
  input String codefile;
  output String[:] result;
end checkCodeGraph;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                graphfile,
                codefile,
            ):
                return _session_.__omc__.call_function(
                    funcName='checkCodeGraph',
                    inputArguments=[
                        (Component(String), 'graphfile', graphfile, 'required'),
                        (Component(String), 'codefile', codefile, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.val')
        class val(
            ModelicaFunction,
        ):
            """
```modelica
function val
  input VariableName var;
  input Real timePoint = 0.0;
  input String fileName = "<default>" "The contents of the currentSimulationResult variable";
  output Real valAtTime;
end val;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                var,
                timePoint=None,
                fileName=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='val',
                    inputArguments=[
                        (Component(VariableName), 'var', var, 'required'),
                        (Component(Real), 'timePoint', timePoint, 'optional'),
                        (Component(String), 'fileName', fileName, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Real), 'valAtTime'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.closeSimulationResultFile')
        class closeSimulationResultFile(
            ModelicaFunction,
        ):
            """
```modelica
function closeSimulationResultFile
  output Boolean success;
end closeSimulationResultFile;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='closeSimulationResultFile',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        # @modelica_name('OpenModelica.Scripting.addClassAnnotation')
        # class addClassAnnotation(
        #     ModelicaFunction,
        # ):
        #     """
        # ```modelica
        # function addClassAnnotation
        #   input TypeName class_;
        #   input ExpressionOrModification annotate;
        #   output Boolean bool;
        # end addClassAnnotation;
        # ```
        #     """
        #     @external
        #     def _(
        #         _cls_,
        #         _session_: AbstractOMCSession,
        #         class_,
        #         annotate,
        #     ):
        #         return _session_.__omc__.call_function(
        #             funcName='addClassAnnotation',
        #             inputArguments=[
        #                 (Component(TypeName), 'class_', class_, 'required'),
        #                 (Component(OpenModelica.$Code.ExpressionOrModification), 'annotate', annotate, 'required'),
        #             ],
        #             outputArguments=[
        #                 (Component(Boolean), 'bool'),
        #             ],
        #             parser=parse_OMCValue,
        #         )

        @modelica_name('OpenModelica.Scripting.getParameterNames')
        class getParameterNames(
            ModelicaFunction,
        ):
            """
```modelica
function getParameterNames
  input TypeName class_;
  output String[:] parameters;
end getParameterNames;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
            ):
                return _session_.__omc__.call_function(
                    funcName='getParameterNames',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'parameters'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getParameterValue')
        class getParameterValue(
            ModelicaFunction,
        ):
            """
```modelica
function getParameterValue
  input TypeName class_;
  input String parameterName;
  output String parameterValue;
end getParameterValue;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                parameterName,
            ):
                return _session_.__omc__.call_function(
                    funcName='getParameterValue',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(String), 'parameterName', parameterName, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'parameterValue'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getComponentModifierNames')
        class getComponentModifierNames(
            ModelicaFunction,
        ):
            """
```modelica
function getComponentModifierNames
  input TypeName class_;
  input String componentName;
  output String[:] modifiers;
end getComponentModifierNames;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                componentName,
            ):
                return _session_.__omc__.call_function(
                    funcName='getComponentModifierNames',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(String), 'componentName', componentName, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'modifiers'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getComponentModifierValue')
        class getComponentModifierValue(
            ModelicaFunction,
        ):
            """
```modelica
function getComponentModifierValue
  input TypeName class_;
  input TypeName modifier;
  output String value;
end getComponentModifierValue;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                modifier,
            ):
                return _session_.__omc__.call_function(
                    funcName='getComponentModifierValue',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(TypeName), 'modifier', modifier, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'value'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getComponentModifierValues')
        class getComponentModifierValues(
            ModelicaFunction,
        ):
            """
```modelica
function getComponentModifierValues
  input TypeName class_;
  input TypeName modifier;
  output String value;
end getComponentModifierValues;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                modifier,
            ):
                return _session_.__omc__.call_function(
                    funcName='getComponentModifierValues',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(TypeName), 'modifier', modifier, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'value'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.removeComponentModifiers')
        class removeComponentModifiers(
            ModelicaFunction,
        ):
            """
```modelica
function removeComponentModifiers
  input TypeName class_;
  input String componentName;
  input Boolean keepRedeclares = false;
  output Boolean success;
end removeComponentModifiers;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                componentName,
                keepRedeclares=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='removeComponentModifiers',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(String), 'componentName', componentName, 'required'),
                        (Component(Boolean), 'keepRedeclares', keepRedeclares, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getElementModifierNames')
        class getElementModifierNames(
            ModelicaFunction,
        ):
            """
```modelica
function getElementModifierNames
  input TypeName className;
  input String elementName;
  output String[:] modifiers;
end getElementModifierNames;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                elementName,
            ):
                return _session_.__omc__.call_function(
                    funcName='getElementModifierNames',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(String), 'elementName', elementName, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'modifiers'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getElementModifierValue')
        class getElementModifierValue(
            ModelicaFunction,
        ):
            """
```modelica
function getElementModifierValue
  input TypeName className;
  input TypeName modifier;
  output String value;
end getElementModifierValue;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                modifier,
            ):
                return _session_.__omc__.call_function(
                    funcName='getElementModifierValue',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(TypeName), 'modifier', modifier, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'value'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getElementModifierValues')
        class getElementModifierValues(
            ModelicaFunction,
        ):
            """
```modelica
function getElementModifierValues
  input TypeName className;
  input TypeName modifier;
  output String value;
end getElementModifierValues;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                modifier,
            ):
                return _session_.__omc__.call_function(
                    funcName='getElementModifierValues',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(TypeName), 'modifier', modifier, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'value'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.removeElementModifiers')
        class removeElementModifiers(
            ModelicaFunction,
        ):
            """
```modelica
function removeElementModifiers
  input TypeName className;
  input String componentName;
  input Boolean keepRedeclares = false;
  output Boolean success;
end removeElementModifiers;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                componentName,
                keepRedeclares=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='removeElementModifiers',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(String), 'componentName', componentName, 'required'),
                        (Component(Boolean), 'keepRedeclares', keepRedeclares, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getInstantiatedParametersAndValues')
        class getInstantiatedParametersAndValues(
            ModelicaFunction,
        ):
            """
```modelica
function getInstantiatedParametersAndValues
  input TypeName cls;
  output String[:] values;
end getInstantiatedParametersAndValues;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cls,
            ):
                return _session_.__omc__.call_function(
                    funcName='getInstantiatedParametersAndValues',
                    inputArguments=[
                        (Component(TypeName), 'cls', cls, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'values'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.removeExtendsModifiers')
        class removeExtendsModifiers(
            ModelicaFunction,
        ):
            """
```modelica
function removeExtendsModifiers
  input TypeName className;
  input TypeName baseClassName;
  input Boolean keepRedeclares = false;
  output Boolean success;
end removeExtendsModifiers;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                baseClassName,
                keepRedeclares=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='removeExtendsModifiers',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(TypeName), 'baseClassName', baseClassName, 'required'),
                        (Component(Boolean), 'keepRedeclares', keepRedeclares, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        # @modelica_name('OpenModelica.Scripting.updateConnection')
        # class updateConnection(
        #     ModelicaFunction,
        # ):
        #     """
        # ```modelica
        # function updateConnection
        #   input TypeName className;
        #   input String from;
        #   input String to;
        #   input ExpressionOrModification annotate;
        #   output Boolean result;
        # end updateConnection;
        # ```
        #     """
        #     @external
        #     def _(
        #         _cls_,
        #         _session_: AbstractOMCSession,
        #         className,
        #         from_,
        #         to,
        #         annotate,
        #     ):
        #         return _session_.__omc__.call_function(
        #             funcName='updateConnection',
        #             inputArguments=[
        #                 (Component(TypeName), 'className', className, 'required'),
        #                 (Component(String), 'from', from_, 'required'),
        #                 (Component(String), 'to', to, 'required'),
        #                 (Component(OpenModelica.$Code.ExpressionOrModification), 'annotate', annotate, 'required'),
        #             ],
        #             outputArguments=[
        #                 (Component(Boolean), 'result'),
        #             ],
        #             parser=parse_OMCValue,
        #         )

        @modelica_name('OpenModelica.Scripting.updateConnectionAnnotation')
        class updateConnectionAnnotation(
            ModelicaFunction,
        ):
            """
```modelica
function updateConnectionAnnotation
  input TypeName className;
  input String from;
  input String to;
  input String annotate;
  output Boolean result;
end updateConnectionAnnotation;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                from_,
                to,
                annotate,
            ):
                return _session_.__omc__.call_function(
                    funcName='updateConnectionAnnotation',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(String), 'from', from_, 'required'),
                        (Component(String), 'to', to, 'required'),
                        (Component(String), 'annotate', annotate, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.updateConnectionNames')
        class updateConnectionNames(
            ModelicaFunction,
        ):
            """
```modelica
function updateConnectionNames
  input TypeName className;
  input String from;
  input String to;
  input String fromNew;
  input String toNew;
  output Boolean result;
end updateConnectionNames;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                from_,
                to,
                fromNew,
                toNew,
            ):
                return _session_.__omc__.call_function(
                    funcName='updateConnectionNames',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(String), 'from', from_, 'required'),
                        (Component(String), 'to', to, 'required'),
                        (Component(String), 'fromNew', fromNew, 'required'),
                        (Component(String), 'toNew', toNew, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getConnectionCount')
        class getConnectionCount(
            ModelicaFunction,
        ):
            """
```modelica
function getConnectionCount
  input TypeName className;
  output Integer count;
end getConnectionCount;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
            ):
                return _session_.__omc__.call_function(
                    funcName='getConnectionCount',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'count'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getNthConnection')
        class getNthConnection(
            ModelicaFunction,
        ):
            """
```modelica
function getNthConnection
  input TypeName className;
  input Integer index;
  output String[:] result;
end getNthConnection;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                index,
            ):
                return _session_.__omc__.call_function(
                    funcName='getNthConnection',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(Integer), 'index', index, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getAlgorithmCount')
        class getAlgorithmCount(
            ModelicaFunction,
        ):
            """
```modelica
function getAlgorithmCount
  input TypeName class_;
  output Integer count;
end getAlgorithmCount;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
            ):
                return _session_.__omc__.call_function(
                    funcName='getAlgorithmCount',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'count'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getNthAlgorithm')
        class getNthAlgorithm(
            ModelicaFunction,
        ):
            """
```modelica
function getNthAlgorithm
  input TypeName class_;
  input Integer index;
  output String result;
end getNthAlgorithm;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                index,
            ):
                return _session_.__omc__.call_function(
                    funcName='getNthAlgorithm',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(Integer), 'index', index, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getInitialAlgorithmCount')
        class getInitialAlgorithmCount(
            ModelicaFunction,
        ):
            """
```modelica
function getInitialAlgorithmCount
  input TypeName class_;
  output Integer count;
end getInitialAlgorithmCount;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
            ):
                return _session_.__omc__.call_function(
                    funcName='getInitialAlgorithmCount',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'count'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getNthInitialAlgorithm')
        class getNthInitialAlgorithm(
            ModelicaFunction,
        ):
            """
```modelica
function getNthInitialAlgorithm
  input TypeName class_;
  input Integer index;
  output String result;
end getNthInitialAlgorithm;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                index,
            ):
                return _session_.__omc__.call_function(
                    funcName='getNthInitialAlgorithm',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(Integer), 'index', index, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getAlgorithmItemsCount')
        class getAlgorithmItemsCount(
            ModelicaFunction,
        ):
            """
```modelica
function getAlgorithmItemsCount
  input TypeName class_;
  output Integer count;
end getAlgorithmItemsCount;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
            ):
                return _session_.__omc__.call_function(
                    funcName='getAlgorithmItemsCount',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'count'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getNthAlgorithmItem')
        class getNthAlgorithmItem(
            ModelicaFunction,
        ):
            """
```modelica
function getNthAlgorithmItem
  input TypeName class_;
  input Integer index;
  output String result;
end getNthAlgorithmItem;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                index,
            ):
                return _session_.__omc__.call_function(
                    funcName='getNthAlgorithmItem',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(Integer), 'index', index, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getInitialAlgorithmItemsCount')
        class getInitialAlgorithmItemsCount(
            ModelicaFunction,
        ):
            """
```modelica
function getInitialAlgorithmItemsCount
  input TypeName class_;
  output Integer count;
end getInitialAlgorithmItemsCount;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
            ):
                return _session_.__omc__.call_function(
                    funcName='getInitialAlgorithmItemsCount',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'count'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getNthInitialAlgorithmItem')
        class getNthInitialAlgorithmItem(
            ModelicaFunction,
        ):
            """
```modelica
function getNthInitialAlgorithmItem
  input TypeName class_;
  input Integer index;
  output String result;
end getNthInitialAlgorithmItem;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                index,
            ):
                return _session_.__omc__.call_function(
                    funcName='getNthInitialAlgorithmItem',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(Integer), 'index', index, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getEquationCount')
        class getEquationCount(
            ModelicaFunction,
        ):
            """
```modelica
function getEquationCount
  input TypeName class_;
  output Integer count;
end getEquationCount;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
            ):
                return _session_.__omc__.call_function(
                    funcName='getEquationCount',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'count'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getNthEquation')
        class getNthEquation(
            ModelicaFunction,
        ):
            """
```modelica
function getNthEquation
  input TypeName class_;
  input Integer index;
  output String result;
end getNthEquation;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                index,
            ):
                return _session_.__omc__.call_function(
                    funcName='getNthEquation',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(Integer), 'index', index, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getInitialEquationCount')
        class getInitialEquationCount(
            ModelicaFunction,
        ):
            """
```modelica
function getInitialEquationCount
  input TypeName class_;
  output Integer count;
end getInitialEquationCount;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
            ):
                return _session_.__omc__.call_function(
                    funcName='getInitialEquationCount',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'count'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getNthInitialEquation')
        class getNthInitialEquation(
            ModelicaFunction,
        ):
            """
```modelica
function getNthInitialEquation
  input TypeName class_;
  input Integer index;
  output String result;
end getNthInitialEquation;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                index,
            ):
                return _session_.__omc__.call_function(
                    funcName='getNthInitialEquation',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(Integer), 'index', index, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getEquationItemsCount')
        class getEquationItemsCount(
            ModelicaFunction,
        ):
            """
```modelica
function getEquationItemsCount
  input TypeName class_;
  output Integer count;
end getEquationItemsCount;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
            ):
                return _session_.__omc__.call_function(
                    funcName='getEquationItemsCount',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'count'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getNthEquationItem')
        class getNthEquationItem(
            ModelicaFunction,
        ):
            """
```modelica
function getNthEquationItem
  input TypeName class_;
  input Integer index;
  output String result;
end getNthEquationItem;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                index,
            ):
                return _session_.__omc__.call_function(
                    funcName='getNthEquationItem',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(Integer), 'index', index, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getInitialEquationItemsCount')
        class getInitialEquationItemsCount(
            ModelicaFunction,
        ):
            """
```modelica
function getInitialEquationItemsCount
  input TypeName class_;
  output Integer count;
end getInitialEquationItemsCount;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
            ):
                return _session_.__omc__.call_function(
                    funcName='getInitialEquationItemsCount',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'count'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getNthInitialEquationItem')
        class getNthInitialEquationItem(
            ModelicaFunction,
        ):
            """
```modelica
function getNthInitialEquationItem
  input TypeName class_;
  input Integer index;
  output String result;
end getNthInitialEquationItem;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                index,
            ):
                return _session_.__omc__.call_function(
                    funcName='getNthInitialEquationItem',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(Integer), 'index', index, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getAnnotationCount')
        class getAnnotationCount(
            ModelicaFunction,
        ):
            """
```modelica
function getAnnotationCount
  input TypeName class_;
  output Integer count;
end getAnnotationCount;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
            ):
                return _session_.__omc__.call_function(
                    funcName='getAnnotationCount',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'count'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getNthAnnotationString')
        class getNthAnnotationString(
            ModelicaFunction,
        ):
            """
```modelica
function getNthAnnotationString
  input TypeName class_;
  input Integer index;
  output String result;
end getNthAnnotationString;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                index,
            ):
                return _session_.__omc__.call_function(
                    funcName='getNthAnnotationString',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(Integer), 'index', index, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getImportCount')
        class getImportCount(
            ModelicaFunction,
        ):
            """
```modelica
function getImportCount
  input TypeName class_;
  output Integer count;
end getImportCount;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
            ):
                return _session_.__omc__.call_function(
                    funcName='getImportCount',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'count'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getMMfileTotalDependencies')
        class getMMfileTotalDependencies(
            ModelicaFunction,
        ):
            """
```modelica
function getMMfileTotalDependencies
  input String in_package_name;
  input String public_imports_dir;
  output String[:] total_pub_imports;
end getMMfileTotalDependencies;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                in_package_name,
                public_imports_dir,
            ):
                return _session_.__omc__.call_function(
                    funcName='getMMfileTotalDependencies',
                    inputArguments=[
                        (Component(String), 'in_package_name', in_package_name, 'required'),
                        (Component(String), 'public_imports_dir', public_imports_dir, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'total_pub_imports'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getImportedNames')
        class getImportedNames(
            ModelicaFunction,
        ):
            """
```modelica
function getImportedNames
  input TypeName class_;
  output String[:] out_public;
  output String[:] out_protected;
end getImportedNames;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
            ):
                return _session_.__omc__.call_function(
                    funcName='getImportedNames',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'out_public'),
                        (Component(String)[:], 'out_protected'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getNthImport')
        class getNthImport(
            ModelicaFunction,
        ):
            """
```modelica
function getNthImport
  input TypeName class_;
  input Integer index;
  output String out[3] "{\\"Path\\",\\"Id\\",\\"Kind\\"}";
end getNthImport;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                index,
            ):
                return _session_.__omc__.call_function(
                    funcName='getNthImport',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(Integer), 'index', index, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[3], 'out'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.iconv')
        class iconv(
            ModelicaFunction,
        ):
            """
```modelica
function iconv
  input String string;
  input String from;
  input String to = "UTF-8";
  output String result;
end iconv;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                string,
                from_,
                to=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='iconv',
                    inputArguments=[
                        (Component(String), 'string', string, 'required'),
                        (Component(String), 'from', from_, 'required'),
                        (Component(String), 'to', to, 'optional'),
                    ],
                    outputArguments=[
                        (Component(String), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getDocumentationAnnotation')
        class getDocumentationAnnotation(
            ModelicaFunction,
        ):
            """
```modelica
function getDocumentationAnnotation
  input TypeName cl;
  output String out[3] "{info,revision,infoHeader} TODO: Should be changed to have 2 outputs instead of an array of 2 Strings...";
end getDocumentationAnnotation;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='getDocumentationAnnotation',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[3], 'out'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setDocumentationAnnotation')
        class setDocumentationAnnotation(
            ModelicaFunction,
        ):
            """
```modelica
function setDocumentationAnnotation
  input TypeName class_;
  input String info = "";
  input String revisions = "";
  output Boolean bool;
end setDocumentationAnnotation;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                class_,
                info=None,
                revisions=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='setDocumentationAnnotation',
                    inputArguments=[
                        (Component(TypeName), 'class_', class_, 'required'),
                        (Component(String), 'info', info, 'optional'),
                        (Component(String), 'revisions', revisions, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'bool'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getTimeStamp')
        class getTimeStamp(
            ModelicaFunction,
        ):
            """
```modelica
function getTimeStamp
  input TypeName cl;
  output Real timeStamp;
  output String timeStampAsString;
end getTimeStamp;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='getTimeStamp',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(Real), 'timeStamp'),
                        (Component(String), 'timeStampAsString'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.stringTypeName')
        class stringTypeName(
            ModelicaFunction,
        ):
            """
```modelica
function stringTypeName
  input String str;
  output TypeName cl;
end stringTypeName;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                str,
            ):
                return _session_.__omc__.call_function(
                    funcName='stringTypeName',
                    inputArguments=[
                        (Component(String), 'str', str, 'required'),
                    ],
                    outputArguments=[
                        (Component(TypeName), 'cl'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.stringVariableName')
        class stringVariableName(
            ModelicaFunction,
        ):
            """
```modelica
function stringVariableName
  input String str;
  output VariableName cl;
end stringVariableName;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                str,
            ):
                return _session_.__omc__.call_function(
                    funcName='stringVariableName',
                    inputArguments=[
                        (Component(String), 'str', str, 'required'),
                    ],
                    outputArguments=[
                        (Component(VariableName), 'cl'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.typeNameString')
        class typeNameString(
            ModelicaFunction,
        ):
            """
```modelica
function typeNameString
  input TypeName cl;
  output String out;
end typeNameString;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='typeNameString',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'out'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.typeNameStrings')
        class typeNameStrings(
            ModelicaFunction,
        ):
            """
```modelica
function typeNameStrings
  input TypeName cl;
  output String out[:];
end typeNameStrings;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='typeNameStrings',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'out'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getClassComment')
        class getClassComment(
            ModelicaFunction,
        ):
            """
```modelica
function getClassComment
  input TypeName cl;
  output String comment;
end getClassComment;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='getClassComment',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'comment'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.dirname')
        class dirname(
            ModelicaFunction,
        ):
            """
```modelica
function dirname
  input String path;
  output String dirname;
end dirname;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                path,
            ):
                return _session_.__omc__.call_function(
                    funcName='dirname',
                    inputArguments=[
                        (Component(String), 'path', path, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'dirname'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.basename')
        class basename(
            ModelicaFunction,
        ):
            """
```modelica
function basename
  input String path;
  output String basename;
end basename;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                path,
            ):
                return _session_.__omc__.call_function(
                    funcName='basename',
                    inputArguments=[
                        (Component(String), 'path', path, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'basename'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getClassRestriction')
        class getClassRestriction(
            ModelicaFunction,
        ):
            """
```modelica
function getClassRestriction
  input TypeName cl;
  output String restriction;
end getClassRestriction;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='getClassRestriction',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'restriction'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.isType')
        class isType(
            ModelicaFunction,
        ):
            """
```modelica
function isType
  input TypeName cl;
  output Boolean b;
end isType;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='isType',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'b'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.isPackage')
        class isPackage(
            ModelicaFunction,
        ):
            """
```modelica
function isPackage
  input TypeName cl;
  output Boolean b;
end isPackage;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='isPackage',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'b'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.isClass')
        class isClass(
            ModelicaFunction,
        ):
            """
```modelica
function isClass
  input TypeName cl;
  output Boolean b;
end isClass;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='isClass',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'b'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.isRecord')
        class isRecord(
            ModelicaFunction,
        ):
            """
```modelica
function isRecord
  input TypeName cl;
  output Boolean b;
end isRecord;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='isRecord',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'b'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.isBlock')
        class isBlock(
            ModelicaFunction,
        ):
            """
```modelica
function isBlock
  input TypeName cl;
  output Boolean b;
end isBlock;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='isBlock',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'b'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.isFunction')
        class isFunction(
            ModelicaFunction,
        ):
            """
```modelica
function isFunction
  input TypeName cl;
  output Boolean b;
end isFunction;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='isFunction',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'b'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.isPartial')
        class isPartial(
            ModelicaFunction,
        ):
            """
```modelica
function isPartial
  input TypeName cl;
  output Boolean b;
end isPartial;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='isPartial',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'b'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.isModel')
        class isModel(
            ModelicaFunction,
        ):
            """
```modelica
function isModel
  input TypeName cl;
  output Boolean b;
end isModel;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='isModel',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'b'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.isConnector')
        class isConnector(
            ModelicaFunction,
        ):
            """
```modelica
function isConnector
  input TypeName cl;
  output Boolean b;
end isConnector;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='isConnector',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'b'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.isOptimization')
        class isOptimization(
            ModelicaFunction,
        ):
            """
```modelica
function isOptimization
  input TypeName cl;
  output Boolean b;
end isOptimization;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='isOptimization',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'b'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.isEnumeration')
        class isEnumeration(
            ModelicaFunction,
        ):
            """
```modelica
function isEnumeration
  input TypeName cl;
  output Boolean b;
end isEnumeration;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='isEnumeration',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'b'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.isOperator')
        class isOperator(
            ModelicaFunction,
        ):
            """
```modelica
function isOperator
  input TypeName cl;
  output Boolean b;
end isOperator;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='isOperator',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'b'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.isOperatorRecord')
        class isOperatorRecord(
            ModelicaFunction,
        ):
            """
```modelica
function isOperatorRecord
  input TypeName cl;
  output Boolean b;
end isOperatorRecord;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='isOperatorRecord',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'b'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.isOperatorFunction')
        class isOperatorFunction(
            ModelicaFunction,
        ):
            """
```modelica
function isOperatorFunction
  input TypeName cl;
  output Boolean b;
end isOperatorFunction;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='isOperatorFunction',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'b'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.isProtectedClass')
        class isProtectedClass(
            ModelicaFunction,
        ):
            """
```modelica
function isProtectedClass
  input TypeName cl;
  input String c2;
  output Boolean b;
end isProtectedClass;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
                c2,
            ):
                return _session_.__omc__.call_function(
                    funcName='isProtectedClass',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                        (Component(String), 'c2', c2, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'b'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getBuiltinType')
        class getBuiltinType(
            ModelicaFunction,
        ):
            """
```modelica
function getBuiltinType
  input TypeName cl;
  output String name;
end getBuiltinType;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='getBuiltinType',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'name'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.setInitXmlStartValue')
        class setInitXmlStartValue(
            ModelicaFunction,
        ):
            """
```modelica
function setInitXmlStartValue
  input String fileName;
  input String variableName;
  input String startValue;
  input String outputFile;
  output Boolean success = false;
end setInitXmlStartValue;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
                variableName,
                startValue,
                outputFile,
            ):
                return _session_.__omc__.call_function(
                    funcName='setInitXmlStartValue',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                        (Component(String), 'variableName', variableName, 'required'),
                        (Component(String), 'startValue', startValue, 'required'),
                        (Component(String), 'outputFile', outputFile, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.ngspicetoModelica')
        class ngspicetoModelica(
            ModelicaFunction,
        ):
            """
```modelica
function ngspicetoModelica
  input String netlistfileName;
  output Boolean success = false;
end ngspicetoModelica;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                netlistfileName,
            ):
                return _session_.__omc__.call_function(
                    funcName='ngspicetoModelica',
                    inputArguments=[
                        (Component(String), 'netlistfileName', netlistfileName, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getInheritedClasses')
        class getInheritedClasses(
            ModelicaFunction,
        ):
            """
```modelica
function getInheritedClasses
  input TypeName name;
  output TypeName inheritedClasses[:];
end getInheritedClasses;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                name,
            ):
                return _session_.__omc__.call_function(
                    funcName='getInheritedClasses',
                    inputArguments=[
                        (Component(TypeName), 'name', name, 'required'),
                    ],
                    outputArguments=[
                        (Component(TypeName)[:], 'inheritedClasses'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getComponentsTest')
        class getComponentsTest(
            ModelicaFunction,
        ):
            """
```modelica
function getComponentsTest
  input TypeName name;
  output Component[:] components;

  record Component
    String className;
    // when building record the constructor. Records are allowed to contain only components of basic types, arrays of basic types or other records.
    String name;
    String comment;
    Boolean isProtected;
    Boolean isFinal;
    Boolean isFlow;
    Boolean isStream;
    Boolean isReplaceable;
    String variability "'constant', 'parameter', 'discrete', ''";
    String innerOuter "'inner', 'outer', ''";
    String inputOutput "'input', 'output', ''";
    String dimensions[:];
  end Component;
end getComponentsTest;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                name,
            ):
                return _session_.__omc__.call_function(
                    funcName='getComponentsTest',
                    inputArguments=[
                        (Component(TypeName), 'name', name, 'required'),
                    ],
                    outputArguments=[
                        (Component(OpenModelica.Scripting.getComponentsTest.Component)[:], 'components'),
                    ],
                    parser=parse_OMCValue,
                )

            @modelica_name('OpenModelica.Scripting.getComponentsTest.Component')
            class Component(
                ModelicaRecord,
            ):
                """
```modelica
record Component
  String className;
  // when building record the constructor. Records are allowed to contain only components of basic types, arrays of basic types or other records.
  String name;
  String comment;
  Boolean isProtected;
  Boolean isFinal;
  Boolean isFlow;
  Boolean isStream;
  Boolean isReplaceable;
  String variability "'constant', 'parameter', 'discrete', ''";
  String innerOuter "'inner', 'outer', ''";
  String inputOutput "'input', 'output', ''";
  String dimensions[:];
end Component;
```
                """
                @element
                def className(cls):
                    return Component(String)

                @element
                def name(cls):
                    return Component(String)

                @element
                def comment(cls):
                    return Component(String)

                @element
                def isProtected(cls):
                    return Component(Boolean)

                @element
                def isFinal(cls):
                    return Component(Boolean)

                @element
                def isFlow(cls):
                    return Component(Boolean)

                @element
                def isStream(cls):
                    return Component(Boolean)

                @element
                def isReplaceable(cls):
                    return Component(Boolean)

                @element
                def variability(cls):
                    return Component(String)

                @element
                def innerOuter(cls):
                    return Component(String)

                @element
                def inputOutput(cls):
                    return Component(String)

                @element
                def dimensions(cls):
                    return Component(String)[:]

        @modelica_name('OpenModelica.Scripting.isExperiment')
        class isExperiment(
            ModelicaFunction,
        ):
            """
```modelica
function isExperiment
  input TypeName name;
  output Boolean res;
end isExperiment;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                name,
            ):
                return _session_.__omc__.call_function(
                    funcName='isExperiment',
                    inputArguments=[
                        (Component(TypeName), 'name', name, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'res'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getSimulationOptions')
        class getSimulationOptions(
            ModelicaFunction,
        ):
            """
```modelica
function getSimulationOptions
  input TypeName name;
  input Real defaultStartTime = 0.0;
  input Real defaultStopTime = 1.0;
  input Real defaultTolerance = 1e-6;
  input Integer defaultNumberOfIntervals = 500 "May be overridden by defining defaultInterval instead";
  input Real defaultInterval = 0.0 "If = 0.0, then numberOfIntervals is used to calculate the step size";
  output Real startTime;
  output Real stopTime;
  output Real tolerance;
  output Integer numberOfIntervals;
  output Real interval;
end getSimulationOptions;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                name,
                defaultStartTime=None,
                defaultStopTime=None,
                defaultTolerance=None,
                defaultNumberOfIntervals=None,
                defaultInterval=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='getSimulationOptions',
                    inputArguments=[
                        (Component(TypeName), 'name', name, 'required'),
                        (Component(Real), 'defaultStartTime', defaultStartTime, 'optional'),
                        (Component(Real), 'defaultStopTime', defaultStopTime, 'optional'),
                        (Component(Real), 'defaultTolerance', defaultTolerance, 'optional'),
                        (Component(Integer), 'defaultNumberOfIntervals', defaultNumberOfIntervals, 'optional'),
                        (Component(Real), 'defaultInterval', defaultInterval, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Real), 'startTime'),
                        (Component(Real), 'stopTime'),
                        (Component(Real), 'tolerance'),
                        (Component(Integer), 'numberOfIntervals'),
                        (Component(Real), 'interval'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getAnnotationNamedModifiers')
        class getAnnotationNamedModifiers(
            ModelicaFunction,
        ):
            """
```modelica
function getAnnotationNamedModifiers
  input TypeName name;
  input String vendorannotation;
  output String[:] modifiernamelist;
end getAnnotationNamedModifiers;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                name,
                vendorannotation,
            ):
                return _session_.__omc__.call_function(
                    funcName='getAnnotationNamedModifiers',
                    inputArguments=[
                        (Component(TypeName), 'name', name, 'required'),
                        (Component(String), 'vendorannotation', vendorannotation, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'modifiernamelist'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getAnnotationModifierValue')
        class getAnnotationModifierValue(
            ModelicaFunction,
        ):
            """
```modelica
function getAnnotationModifierValue
  input TypeName name;
  input String vendorannotation;
  input String modifiername;
  output String modifiernamevalue;
end getAnnotationModifierValue;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                name,
                vendorannotation,
                modifiername,
            ):
                return _session_.__omc__.call_function(
                    funcName='getAnnotationModifierValue',
                    inputArguments=[
                        (Component(TypeName), 'name', name, 'required'),
                        (Component(String), 'vendorannotation', vendorannotation, 'required'),
                        (Component(String), 'modifiername', modifiername, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'modifiernamevalue'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.classAnnotationExists')
        class classAnnotationExists(
            ModelicaFunction,
        ):
            """
```modelica
function classAnnotationExists
  input TypeName className;
  input TypeName annotationName;
  output Boolean exists;
end classAnnotationExists;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                annotationName,
            ):
                return _session_.__omc__.call_function(
                    funcName='classAnnotationExists',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(TypeName), 'annotationName', annotationName, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'exists'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getBooleanClassAnnotation')
        class getBooleanClassAnnotation(
            ModelicaFunction,
        ):
            """
```modelica
function getBooleanClassAnnotation
  input TypeName className;
  input TypeName annotationName;
  output Boolean value;
end getBooleanClassAnnotation;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                annotationName,
            ):
                return _session_.__omc__.call_function(
                    funcName='getBooleanClassAnnotation',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(TypeName), 'annotationName', annotationName, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'value'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.extendsFrom')
        class extendsFrom(
            ModelicaFunction,
        ):
            """
```modelica
function extendsFrom
  input TypeName className;
  input TypeName baseClassName;
  output Boolean res;
end extendsFrom;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                baseClassName,
            ):
                return _session_.__omc__.call_function(
                    funcName='extendsFrom',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(TypeName), 'baseClassName', baseClassName, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'res'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.loadModelica3D')
        class loadModelica3D(
            ModelicaFunction,
        ):
            """
```modelica
function loadModelica3D
  input String version = "3.2.1";
  output Boolean status;
end loadModelica3D;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                version=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='loadModelica3D',
                    inputArguments=[
                        (Component(String), 'version', version, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.searchClassNames')
        class searchClassNames(
            ModelicaFunction,
        ):
            """
```modelica
function searchClassNames
  input String searchText;
  input Boolean findInText = false;
  output TypeName classNames[:];
end searchClassNames;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                searchText,
                findInText=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='searchClassNames',
                    inputArguments=[
                        (Component(String), 'searchText', searchText, 'required'),
                        (Component(Boolean), 'findInText', findInText, 'optional'),
                    ],
                    outputArguments=[
                        (Component(TypeName)[:], 'classNames'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getAvailableLibraries')
        class getAvailableLibraries(
            ModelicaFunction,
        ):
            """
```modelica
function getAvailableLibraries
  output String[:] libraries;
end getAvailableLibraries;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getAvailableLibraries',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String)[:], 'libraries'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.installPackage')
        class installPackage(
            ModelicaFunction,
        ):
            """
```modelica
function installPackage
  input TypeName pkg;
  input String version = "";
  input Boolean exactMatch = false;
  output Boolean result;
end installPackage;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                pkg,
                version=None,
                exactMatch=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='installPackage',
                    inputArguments=[
                        (Component(TypeName), 'pkg', pkg, 'required'),
                        (Component(String), 'version', version, 'optional'),
                        (Component(Boolean), 'exactMatch', exactMatch, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.updatePackageIndex')
        class updatePackageIndex(
            ModelicaFunction,
        ):
            """
```modelica
function updatePackageIndex
  output Boolean result;
end updatePackageIndex;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='updatePackageIndex',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Boolean), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.upgradeInstalledPackages')
        class upgradeInstalledPackages(
            ModelicaFunction,
        ):
            """
```modelica
function upgradeInstalledPackages
  input Boolean installNewestVersions = true;
  output Boolean result;
end upgradeInstalledPackages;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                installNewestVersions=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='upgradeInstalledPackages',
                    inputArguments=[
                        (Component(Boolean), 'installNewestVersions', installNewestVersions, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getUses')
        class getUses(
            ModelicaFunction,
        ):
            """
```modelica
function getUses
  input TypeName pack;
  output String[:, :] uses;
end getUses;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                pack,
            ):
                return _session_.__omc__.call_function(
                    funcName='getUses',
                    inputArguments=[
                        (Component(TypeName), 'pack', pack, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:, :], 'uses'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getConversionsFromVersions')
        class getConversionsFromVersions(
            ModelicaFunction,
        ):
            """
```modelica
function getConversionsFromVersions
  input TypeName pack;
  output String[:] withoutConversion;
  output String[:] withConversion;
end getConversionsFromVersions;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                pack,
            ):
                return _session_.__omc__.call_function(
                    funcName='getConversionsFromVersions',
                    inputArguments=[
                        (Component(TypeName), 'pack', pack, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'withoutConversion'),
                        (Component(String)[:], 'withConversion'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getDerivedClassModifierNames')
        class getDerivedClassModifierNames(
            ModelicaFunction,
        ):
            """
```modelica
function getDerivedClassModifierNames
  input TypeName className;
  output String[:] modifierNames;
end getDerivedClassModifierNames;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
            ):
                return _session_.__omc__.call_function(
                    funcName='getDerivedClassModifierNames',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'modifierNames'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getDerivedClassModifierValue')
        class getDerivedClassModifierValue(
            ModelicaFunction,
        ):
            """
```modelica
function getDerivedClassModifierValue
  input TypeName className;
  input TypeName modifierName;
  output String modifierValue;
end getDerivedClassModifierValue;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                className,
                modifierName,
            ):
                return _session_.__omc__.call_function(
                    funcName='getDerivedClassModifierValue',
                    inputArguments=[
                        (Component(TypeName), 'className', className, 'required'),
                        (Component(TypeName), 'modifierName', modifierName, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'modifierValue'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.generateEntryPoint')
        class generateEntryPoint(
            ModelicaFunction,
        ):
            """
```modelica
function generateEntryPoint
  input String fileName;
  input TypeName entryPoint;
  input String url = "https://trac.openmodelica.org/OpenModelica/newticket";
end generateEntryPoint;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                fileName,
                entryPoint,
                url=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='generateEntryPoint',
                    inputArguments=[
                        (Component(String), 'fileName', fileName, 'required'),
                        (Component(TypeName), 'entryPoint', entryPoint, 'required'),
                        (Component(String), 'url', url, 'optional'),
                    ],
                    outputArguments=[
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.numProcessors')
        class numProcessors(
            ModelicaFunction,
        ):
            """
```modelica
function numProcessors
  output Integer result;
end numProcessors;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='numProcessors',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Integer), 'result'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.runScriptParallel')
        class runScriptParallel(
            ModelicaFunction,
        ):
            """
```modelica
function runScriptParallel
  input String scripts[:];
  input Integer numThreads = numProcessors();
  input Boolean useThreads = false;
  output Boolean results[:];
end runScriptParallel;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                scripts,
                numThreads=None,
                useThreads=None,
            ):
                return _session_.__omc__.call_function(
                    funcName='runScriptParallel',
                    inputArguments=[
                        (Component(String)[:], 'scripts', scripts, 'required'),
                        (Component(Integer), 'numThreads', numThreads, 'optional'),
                        (Component(Boolean), 'useThreads', useThreads, 'optional'),
                    ],
                    outputArguments=[
                        (Component(Boolean)[:], 'results'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.exit')
        class exit(
            ModelicaFunction,
        ):
            """
```modelica
function exit
  input Integer status;
end exit;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                status,
            ):
                return _session_.__omc__.call_function(
                    funcName='exit',
                    inputArguments=[
                        (Component(Integer), 'status', status, 'required'),
                    ],
                    outputArguments=[
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.threadWorkFailed')
        class threadWorkFailed(
            ModelicaFunction,
        ):
            """
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='threadWorkFailed',
                    inputArguments=[
                    ],
                    outputArguments=[
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getMemorySize')
        class getMemorySize(
            ModelicaFunction,
        ):
            """
```modelica
function getMemorySize
  output Real memory(unit = "MiB");
end getMemorySize;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='getMemorySize',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Real), 'memory'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.GC_gcollect_and_unmap')
        class GC_gcollect_and_unmap(
            ModelicaFunction,
        ):
            """
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='GC_gcollect_and_unmap',
                    inputArguments=[
                    ],
                    outputArguments=[
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.GC_expand_hp')
        class GC_expand_hp(
            ModelicaFunction,
        ):
            """
```modelica
function GC_expand_hp
  input Integer size;
  output Boolean success;
end GC_expand_hp;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                size,
            ):
                return _session_.__omc__.call_function(
                    funcName='GC_expand_hp',
                    inputArguments=[
                        (Component(Integer), 'size', size, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.GC_set_max_heap_size')
        class GC_set_max_heap_size(
            ModelicaFunction,
        ):
            """
```modelica
function GC_set_max_heap_size
  input Integer size;
  output Boolean success;
end GC_set_max_heap_size;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                size,
            ):
                return _session_.__omc__.call_function(
                    funcName='GC_set_max_heap_size',
                    inputArguments=[
                        (Component(Integer), 'size', size, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.GC_PROFSTATS')
        class GC_PROFSTATS(
            ModelicaRecord,
        ):
            """
```modelica
record GC_PROFSTATS
  Integer heapsize_full;
  Integer free_bytes_full;
  Integer unmapped_bytes;
  Integer bytes_allocd_since_gc;
  Integer allocd_bytes_before_gc;
  Integer non_gc_bytes;
  Integer gc_no;
  Integer markers_m1;
  Integer bytes_reclaimed_since_gc;
  Integer reclaimed_bytes_before_gc;
end GC_PROFSTATS;
```
            """
            @element
            def heapsize_full(cls):
                return Component(Integer)

            @element
            def free_bytes_full(cls):
                return Component(Integer)

            @element
            def unmapped_bytes(cls):
                return Component(Integer)

            @element
            def bytes_allocd_since_gc(cls):
                return Component(Integer)

            @element
            def allocd_bytes_before_gc(cls):
                return Component(Integer)

            @element
            def non_gc_bytes(cls):
                return Component(Integer)

            @element
            def gc_no(cls):
                return Component(Integer)

            @element
            def markers_m1(cls):
                return Component(Integer)

            @element
            def bytes_reclaimed_since_gc(cls):
                return Component(Integer)

            @element
            def reclaimed_bytes_before_gc(cls):
                return Component(Integer)

        @modelica_name('OpenModelica.Scripting.GC_get_prof_stats')
        class GC_get_prof_stats(
            ModelicaFunction,
        ):
            """
```modelica
function GC_get_prof_stats
  output GC_PROFSTATS gcStats;
end GC_get_prof_stats;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='GC_get_prof_stats',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(OpenModelica.Scripting.GC_PROFSTATS), 'gcStats'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.checkInterfaceOfPackages')
        class checkInterfaceOfPackages(
            ModelicaFunction,
        ):
            """
```modelica
function checkInterfaceOfPackages
  input TypeName cl;
  input String dependencyMatrix[:, :];
  output Boolean success;
end checkInterfaceOfPackages;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
                dependencyMatrix,
            ):
                return _session_.__omc__.call_function(
                    funcName='checkInterfaceOfPackages',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                        (Component(String)[:, :], 'dependencyMatrix', dependencyMatrix, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.sortStrings')
        class sortStrings(
            ModelicaFunction,
        ):
            """
```modelica
function sortStrings
  input String arr[:];
  output String sorted[:];
end sortStrings;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                arr,
            ):
                return _session_.__omc__.call_function(
                    funcName='sortStrings',
                    inputArguments=[
                        (Component(String)[:], 'arr', arr, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:], 'sorted'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getClassInformation')
        class getClassInformation(
            ModelicaFunction,
        ):
            """
```modelica
function getClassInformation
  input TypeName cl;
  output String restriction, comment;
  output Boolean partialPrefix, finalPrefix, encapsulatedPrefix;
  output String fileName;
  output Boolean fileReadOnly;
  output Integer lineNumberStart, columnNumberStart, lineNumberEnd, columnNumberEnd;
  output String dimensions[:];
  output Boolean isProtectedClass;
  output Boolean isDocumentationClass;
  output String version;
  output String preferredView;
  output Boolean state;
  output String access;
end getClassInformation;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='getClassInformation',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'restriction'),
                        (Component(String), 'comment'),
                        (Component(Boolean), 'partialPrefix'),
                        (Component(Boolean), 'finalPrefix'),
                        (Component(Boolean), 'encapsulatedPrefix'),
                        (Component(String), 'fileName'),
                        (Component(Boolean), 'fileReadOnly'),
                        (Component(Integer), 'lineNumberStart'),
                        (Component(Integer), 'columnNumberStart'),
                        (Component(Integer), 'lineNumberEnd'),
                        (Component(Integer), 'columnNumberEnd'),
                        (Component(String)[:], 'dimensions'),
                        (Component(Boolean), 'isProtectedClass'),
                        (Component(Boolean), 'isDocumentationClass'),
                        (Component(String), 'version'),
                        (Component(String), 'preferredView'),
                        (Component(Boolean), 'state'),
                        (Component(String), 'access'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.getTransitions')
        class getTransitions(
            ModelicaFunction,
        ):
            """
```modelica
function getTransitions
  input TypeName cl;
  output String[:, :] transitions;
end getTransitions;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='getTransitions',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:, :], 'transitions'),
                    ],
                    parser=parse_OMCValue,
                )

        # @modelica_name('OpenModelica.Scripting.addTransition')
        # class addTransition(
        #     ModelicaFunction,
        # ):
        #     """
        # ```modelica
        # function addTransition
        #   input TypeName cl;
        #   input String from;
        #   input String to;
        #   input String condition;
        #   input Boolean immediate = true;
        #   input Boolean reset = true;
        #   input Boolean synchronize = false;
        #   input Integer priority = 1;
        #   input ExpressionOrModification annotate;
        #   output Boolean bool;
        # end addTransition;
        # ```
        #     """
        #     @external
        #     def _(
        #         _cls_,
        #         _session_: AbstractOMCSession,
        #         cl,
        #         from_,
        #         to,
        #         condition,
        #         annotate,
        #         immediate=None,
        #         reset=None,
        #         synchronize=None,
        #         priority=None,
        #     ):
        #         return _session_.__omc__.call_function(
        #             funcName='addTransition',
        #             inputArguments=[
        #                 (Component(TypeName), 'cl', cl, 'required'),
        #                 (Component(String), 'from', from_, 'required'),
        #                 (Component(String), 'to', to, 'required'),
        #                 (Component(String), 'condition', condition, 'required'),
        #                 (Component(Boolean), 'immediate', immediate, 'optional'),
        #                 (Component(Boolean), 'reset', reset, 'optional'),
        #                 (Component(Boolean), 'synchronize', synchronize, 'optional'),
        #                 (Component(Integer), 'priority', priority, 'optional'),
        #                 (Component(OpenModelica.$Code.ExpressionOrModification), 'annotate', annotate, 'required'),
        #             ],
        #             outputArguments=[
        #                 (Component(Boolean), 'bool'),
        #             ],
        #             parser=parse_OMCValue,
        #         )

        @modelica_name('OpenModelica.Scripting.deleteTransition')
        class deleteTransition(
            ModelicaFunction,
        ):
            """
```modelica
function deleteTransition
  input TypeName cl;
  input String from;
  input String to;
  input String condition;
  input Boolean immediate;
  input Boolean reset;
  input Boolean synchronize;
  input Integer priority;
  output Boolean bool;
end deleteTransition;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
                from_,
                to,
                condition,
                immediate,
                reset,
                synchronize,
                priority,
            ):
                return _session_.__omc__.call_function(
                    funcName='deleteTransition',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                        (Component(String), 'from', from_, 'required'),
                        (Component(String), 'to', to, 'required'),
                        (Component(String), 'condition', condition, 'required'),
                        (Component(Boolean), 'immediate', immediate, 'required'),
                        (Component(Boolean), 'reset', reset, 'required'),
                        (Component(Boolean), 'synchronize', synchronize, 'required'),
                        (Component(Integer), 'priority', priority, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'bool'),
                    ],
                    parser=parse_OMCValue,
                )

        # @modelica_name('OpenModelica.Scripting.updateTransition')
        # class updateTransition(
        #     ModelicaFunction,
        # ):
        #     """
        # ```modelica
        # function updateTransition
        #   input TypeName cl;
        #   input String from;
        #   input String to;
        #   input String oldCondition;
        #   input Boolean oldImmediate;
        #   input Boolean oldReset;
        #   input Boolean oldSynchronize;
        #   input Integer oldPriority;
        #   input String newCondition;
        #   input Boolean newImmediate;
        #   input Boolean newReset;
        #   input Boolean newSynchronize;
        #   input Integer newPriority;
        #   input ExpressionOrModification annotate;
        #   output Boolean bool;
        # end updateTransition;
        # ```
        #     """
        #     @external
        #     def _(
        #         _cls_,
        #         _session_: AbstractOMCSession,
        #         cl,
        #         from_,
        #         to,
        #         oldCondition,
        #         oldImmediate,
        #         oldReset,
        #         oldSynchronize,
        #         oldPriority,
        #         newCondition,
        #         newImmediate,
        #         newReset,
        #         newSynchronize,
        #         newPriority,
        #         annotate,
        #     ):
        #         return _session_.__omc__.call_function(
        #             funcName='updateTransition',
        #             inputArguments=[
        #                 (Component(TypeName), 'cl', cl, 'required'),
        #                 (Component(String), 'from', from_, 'required'),
        #                 (Component(String), 'to', to, 'required'),
        #                 (Component(String), 'oldCondition', oldCondition, 'required'),
        #                 (Component(Boolean), 'oldImmediate', oldImmediate, 'required'),
        #                 (Component(Boolean), 'oldReset', oldReset, 'required'),
        #                 (Component(Boolean), 'oldSynchronize', oldSynchronize, 'required'),
        #                 (Component(Integer), 'oldPriority', oldPriority, 'required'),
        #                 (Component(String), 'newCondition', newCondition, 'required'),
        #                 (Component(Boolean), 'newImmediate', newImmediate, 'required'),
        #                 (Component(Boolean), 'newReset', newReset, 'required'),
        #                 (Component(Boolean), 'newSynchronize', newSynchronize, 'required'),
        #                 (Component(Integer), 'newPriority', newPriority, 'required'),
        #                 (Component(OpenModelica.$Code.ExpressionOrModification), 'annotate', annotate, 'required'),
        #             ],
        #             outputArguments=[
        #                 (Component(Boolean), 'bool'),
        #             ],
        #             parser=parse_OMCValue,
        #         )

        @modelica_name('OpenModelica.Scripting.getInitialStates')
        class getInitialStates(
            ModelicaFunction,
        ):
            """
```modelica
function getInitialStates
  input TypeName cl;
  output String[:, :] initialStates;
end getInitialStates;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
            ):
                return _session_.__omc__.call_function(
                    funcName='getInitialStates',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                    ],
                    outputArguments=[
                        (Component(String)[:, :], 'initialStates'),
                    ],
                    parser=parse_OMCValue,
                )

        # @modelica_name('OpenModelica.Scripting.addInitialState')
        # class addInitialState(
        #     ModelicaFunction,
        # ):
        #     """
        # ```modelica
        # function addInitialState
        #   input TypeName cl;
        #   input String state;
        #   input ExpressionOrModification annotate;
        #   output Boolean bool;
        # end addInitialState;
        # ```
        #     """
        #     @external
        #     def _(
        #         _cls_,
        #         _session_: AbstractOMCSession,
        #         cl,
        #         state,
        #         annotate,
        #     ):
        #         return _session_.__omc__.call_function(
        #             funcName='addInitialState',
        #             inputArguments=[
        #                 (Component(TypeName), 'cl', cl, 'required'),
        #                 (Component(String), 'state', state, 'required'),
        #                 (Component(OpenModelica.$Code.ExpressionOrModification), 'annotate', annotate, 'required'),
        #             ],
        #             outputArguments=[
        #                 (Component(Boolean), 'bool'),
        #             ],
        #             parser=parse_OMCValue,
        #         )

        @modelica_name('OpenModelica.Scripting.deleteInitialState')
        class deleteInitialState(
            ModelicaFunction,
        ):
            """
```modelica
function deleteInitialState
  input TypeName cl;
  input String state;
  output Boolean bool;
end deleteInitialState;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
                state,
            ):
                return _session_.__omc__.call_function(
                    funcName='deleteInitialState',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                        (Component(String), 'state', state, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'bool'),
                    ],
                    parser=parse_OMCValue,
                )

        # @modelica_name('OpenModelica.Scripting.updateInitialState')
        # class updateInitialState(
        #     ModelicaFunction,
        # ):
        #     """
        # ```modelica
        # function updateInitialState
        #   input TypeName cl;
        #   input String state;
        #   input ExpressionOrModification annotate;
        #   output Boolean bool;
        # end updateInitialState;
        # ```
        #     """
        #     @external
        #     def _(
        #         _cls_,
        #         _session_: AbstractOMCSession,
        #         cl,
        #         state,
        #         annotate,
        #     ):
        #         return _session_.__omc__.call_function(
        #             funcName='updateInitialState',
        #             inputArguments=[
        #                 (Component(TypeName), 'cl', cl, 'required'),
        #                 (Component(String), 'state', state, 'required'),
        #                 (Component(OpenModelica.$Code.ExpressionOrModification), 'annotate', annotate, 'required'),
        #             ],
        #             outputArguments=[
        #                 (Component(Boolean), 'bool'),
        #             ],
        #             parser=parse_OMCValue,
        #         )

        @modelica_name('OpenModelica.Scripting.generateScriptingAPI')
        class generateScriptingAPI(
            ModelicaFunction,
        ):
            """
```modelica
function generateScriptingAPI
  input TypeName cl;
  input String name;
  output Boolean success;
  output String moFile;
  output String qtFile;
  output String qtHeader;
end generateScriptingAPI;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cl,
                name,
            ):
                return _session_.__omc__.call_function(
                    funcName='generateScriptingAPI',
                    inputArguments=[
                        (Component(TypeName), 'cl', cl, 'required'),
                        (Component(String), 'name', name, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'success'),
                        (Component(String), 'moFile'),
                        (Component(String), 'qtFile'),
                        (Component(String), 'qtHeader'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_system')
        class oms_system(
            ModelicaEnumeration,
        ):
            """
```modelica
type oms_system = enumeration(oms_system_none, oms_system_tlm, oms_system_wc, oms_system_sc);
```
            """
            oms_system_none = enum.auto()
            oms_system_tlm = enum.auto()
            oms_system_wc = enum.auto()
            oms_system_sc = enum.auto()

        @modelica_name('OpenModelica.Scripting.oms_causality')
        class oms_causality(
            ModelicaEnumeration,
        ):
            """
```modelica
type oms_causality = enumeration(oms_causality_input, oms_causality_output, oms_causality_parameter, oms_causality_bidir, oms_causality_undefined);
```
            """
            oms_causality_input = enum.auto()
            oms_causality_output = enum.auto()
            oms_causality_parameter = enum.auto()
            oms_causality_bidir = enum.auto()
            oms_causality_undefined = enum.auto()

        @modelica_name('OpenModelica.Scripting.oms_signal_type')
        class oms_signal_type(
            ModelicaEnumeration,
        ):
            """
```modelica
type oms_signal_type = enumeration(oms_signal_type_real, oms_signal_type_integer, oms_signal_type_boolean, oms_signal_type_string, oms_signal_type_enum, oms_signal_type_bus);
```
            """
            oms_signal_type_real = enum.auto()
            oms_signal_type_integer = enum.auto()
            oms_signal_type_boolean = enum.auto()
            oms_signal_type_string = enum.auto()
            oms_signal_type_enum = enum.auto()
            oms_signal_type_bus = enum.auto()

        @modelica_name('OpenModelica.Scripting.oms_solver')
        class oms_solver(
            ModelicaEnumeration,
        ):
            """
```modelica
type oms_solver = enumeration(oms_solver_none, oms_solver_sc_min, oms_solver_sc_explicit_euler, oms_solver_sc_cvode, oms_solver_sc_max, oms_solver_wc_min, oms_solver_wc_ma, oms_solver_wc_mav, oms_solver_wc_assc, oms_solver_wc_mav2, oms_solver_wc_max);
```
            """
            oms_solver_none = enum.auto()
            oms_solver_sc_min = enum.auto()
            oms_solver_sc_explicit_euler = enum.auto()
            oms_solver_sc_cvode = enum.auto()
            oms_solver_sc_max = enum.auto()
            oms_solver_wc_min = enum.auto()
            oms_solver_wc_ma = enum.auto()
            oms_solver_wc_mav = enum.auto()
            oms_solver_wc_assc = enum.auto()
            oms_solver_wc_mav2 = enum.auto()
            oms_solver_wc_max = enum.auto()

        @modelica_name('OpenModelica.Scripting.oms_tlm_domain')
        class oms_tlm_domain(
            ModelicaEnumeration,
        ):
            """
```modelica
type oms_tlm_domain = enumeration(oms_tlm_domain_input, oms_tlm_domain_output, oms_tlm_domain_mechanical, oms_tlm_domain_rotational, oms_tlm_domain_hydraulic, oms_tlm_domain_electric);
```
            """
            oms_tlm_domain_input = enum.auto()
            oms_tlm_domain_output = enum.auto()
            oms_tlm_domain_mechanical = enum.auto()
            oms_tlm_domain_rotational = enum.auto()
            oms_tlm_domain_hydraulic = enum.auto()
            oms_tlm_domain_electric = enum.auto()

        @modelica_name('OpenModelica.Scripting.oms_tlm_interpolation')
        class oms_tlm_interpolation(
            ModelicaEnumeration,
        ):
            """
```modelica
type oms_tlm_interpolation = enumeration(oms_tlm_no_interpolation, oms_tlm_coarse_grained, oms_tlm_fine_grained);
```
            """
            oms_tlm_no_interpolation = enum.auto()
            oms_tlm_coarse_grained = enum.auto()
            oms_tlm_fine_grained = enum.auto()

        @modelica_name('OpenModelica.Scripting.oms_fault_type')
        class oms_fault_type(
            ModelicaEnumeration,
        ):
            """
```modelica
type oms_fault_type = enumeration(oms_fault_type_bias, oms_fault_type_gain, oms_fault_type_const);
```
            """
            oms_fault_type_bias = enum.auto()
            oms_fault_type_gain = enum.auto()
            oms_fault_type_const = enum.auto()

        @modelica_name('OpenModelica.Scripting.loadOMSimulator')
        class loadOMSimulator(
            ModelicaFunction,
        ):
            """
```modelica
function loadOMSimulator
  output Integer status;
end loadOMSimulator;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='loadOMSimulator',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.unloadOMSimulator')
        class unloadOMSimulator(
            ModelicaFunction,
        ):
            """
```modelica
function unloadOMSimulator
  output Integer status;
end unloadOMSimulator;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='unloadOMSimulator',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_addBus')
        class oms_addBus(
            ModelicaFunction,
        ):
            """
```modelica
function oms_addBus
  input String cref;
  output Integer status;
end oms_addBus;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_addBus',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_addConnection')
        class oms_addConnection(
            ModelicaFunction,
        ):
            """
```modelica
function oms_addConnection
  input String crefA;
  input String crefB;
  output Integer status;
end oms_addConnection;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                crefA,
                crefB,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_addConnection',
                    inputArguments=[
                        (Component(String), 'crefA', crefA, 'required'),
                        (Component(String), 'crefB', crefB, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_addConnector')
        class oms_addConnector(
            ModelicaFunction,
        ):
            """
```modelica
function oms_addConnector
  input String cref;
  input oms_causality causality;
  input oms_signal_type type_;
  output Integer status;
end oms_addConnector;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                causality,
                type_,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_addConnector',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(OpenModelica.Scripting.oms_causality), 'causality', causality, 'required'),
                        (Component(OpenModelica.Scripting.oms_signal_type), 'type_', type_, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_addConnectorToBus')
        class oms_addConnectorToBus(
            ModelicaFunction,
        ):
            """
```modelica
function oms_addConnectorToBus
  input String busCref;
  input String connectorCref;
  output Integer status;
end oms_addConnectorToBus;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                busCref,
                connectorCref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_addConnectorToBus',
                    inputArguments=[
                        (Component(String), 'busCref', busCref, 'required'),
                        (Component(String), 'connectorCref', connectorCref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_addConnectorToTLMBus')
        class oms_addConnectorToTLMBus(
            ModelicaFunction,
        ):
            """
```modelica
function oms_addConnectorToTLMBus
  input String busCref;
  input String connectorCref;
  input String type_;
  output Integer status;
end oms_addConnectorToTLMBus;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                busCref,
                connectorCref,
                type_,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_addConnectorToTLMBus',
                    inputArguments=[
                        (Component(String), 'busCref', busCref, 'required'),
                        (Component(String), 'connectorCref', connectorCref, 'required'),
                        (Component(String), 'type_', type_, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_addDynamicValueIndicator')
        class oms_addDynamicValueIndicator(
            ModelicaFunction,
        ):
            """
```modelica
function oms_addDynamicValueIndicator
  input String signal;
  input String lower;
  input String upper;
  input Real stepSize;
  output Integer status;
end oms_addDynamicValueIndicator;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                signal,
                lower,
                upper,
                stepSize,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_addDynamicValueIndicator',
                    inputArguments=[
                        (Component(String), 'signal', signal, 'required'),
                        (Component(String), 'lower', lower, 'required'),
                        (Component(String), 'upper', upper, 'required'),
                        (Component(Real), 'stepSize', stepSize, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_addEventIndicator')
        class oms_addEventIndicator(
            ModelicaFunction,
        ):
            """
```modelica
function oms_addEventIndicator
  input String signal;
  output Integer status;
end oms_addEventIndicator;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                signal,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_addEventIndicator',
                    inputArguments=[
                        (Component(String), 'signal', signal, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_addExternalModel')
        class oms_addExternalModel(
            ModelicaFunction,
        ):
            """
```modelica
function oms_addExternalModel
  input String cref;
  input String path;
  input String startscript;
  output Integer status;
end oms_addExternalModel;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                path,
                startscript,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_addExternalModel',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(String), 'path', path, 'required'),
                        (Component(String), 'startscript', startscript, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_addSignalsToResults')
        class oms_addSignalsToResults(
            ModelicaFunction,
        ):
            """
```modelica
function oms_addSignalsToResults
  input String cref;
  input String regex;
  output Integer status;
end oms_addSignalsToResults;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                regex,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_addSignalsToResults',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(String), 'regex', regex, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_addStaticValueIndicator')
        class oms_addStaticValueIndicator(
            ModelicaFunction,
        ):
            """
```modelica
function oms_addStaticValueIndicator
  input String signal;
  input Real lower;
  input Real upper;
  input Real stepSize;
  output Integer status;
end oms_addStaticValueIndicator;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                signal,
                lower,
                upper,
                stepSize,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_addStaticValueIndicator',
                    inputArguments=[
                        (Component(String), 'signal', signal, 'required'),
                        (Component(Real), 'lower', lower, 'required'),
                        (Component(Real), 'upper', upper, 'required'),
                        (Component(Real), 'stepSize', stepSize, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_addSubModel')
        class oms_addSubModel(
            ModelicaFunction,
        ):
            """
```modelica
function oms_addSubModel
  input String cref;
  input String fmuPath;
  output Integer status;
end oms_addSubModel;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                fmuPath,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_addSubModel',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(String), 'fmuPath', fmuPath, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_addSystem')
        class oms_addSystem(
            ModelicaFunction,
        ):
            """
```modelica
function oms_addSystem
  input String cref;
  input oms_system type_;
  output Integer status;
end oms_addSystem;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                type_,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_addSystem',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(OpenModelica.Scripting.oms_system), 'type_', type_, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_addTimeIndicator')
        class oms_addTimeIndicator(
            ModelicaFunction,
        ):
            """
```modelica
function oms_addTimeIndicator
  input String signal;
  output Integer status;
end oms_addTimeIndicator;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                signal,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_addTimeIndicator',
                    inputArguments=[
                        (Component(String), 'signal', signal, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_addTLMBus')
        class oms_addTLMBus(
            ModelicaFunction,
        ):
            """
```modelica
function oms_addTLMBus
  input String cref;
  input oms_tlm_domain domain;
  input Integer dimensions;
  input oms_tlm_interpolation interpolation;
  output Integer status;
end oms_addTLMBus;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                domain,
                dimensions,
                interpolation,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_addTLMBus',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(OpenModelica.Scripting.oms_tlm_domain), 'domain', domain, 'required'),
                        (Component(Integer), 'dimensions', dimensions, 'required'),
                        (Component(OpenModelica.Scripting.oms_tlm_interpolation), 'interpolation', interpolation, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_addTLMConnection')
        class oms_addTLMConnection(
            ModelicaFunction,
        ):
            """
```modelica
function oms_addTLMConnection
  input String crefA;
  input String crefB;
  input Real delay;
  input Real alpha;
  input Real linearimpedance;
  input Real angularimpedance;
  output Integer status;
end oms_addTLMConnection;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                crefA,
                crefB,
                delay,
                alpha,
                linearimpedance,
                angularimpedance,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_addTLMConnection',
                    inputArguments=[
                        (Component(String), 'crefA', crefA, 'required'),
                        (Component(String), 'crefB', crefB, 'required'),
                        (Component(Real), 'delay', delay, 'required'),
                        (Component(Real), 'alpha', alpha, 'required'),
                        (Component(Real), 'linearimpedance', linearimpedance, 'required'),
                        (Component(Real), 'angularimpedance', angularimpedance, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_cancelSimulation_asynchronous')
        class oms_cancelSimulation_asynchronous(
            ModelicaFunction,
        ):
            """
```modelica
function oms_cancelSimulation_asynchronous
  input String cref;
  output Integer status;
end oms_cancelSimulation_asynchronous;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_cancelSimulation_asynchronous',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_compareSimulationResults')
        class oms_compareSimulationResults(
            ModelicaFunction,
        ):
            """
```modelica
function oms_compareSimulationResults
  input String filenameA;
  input String filenameB;
  input String var;
  input Real relTol;
  input Real absTol;
  output Integer status;
end oms_compareSimulationResults;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                filenameA,
                filenameB,
                var,
                relTol,
                absTol,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_compareSimulationResults',
                    inputArguments=[
                        (Component(String), 'filenameA', filenameA, 'required'),
                        (Component(String), 'filenameB', filenameB, 'required'),
                        (Component(String), 'var', var, 'required'),
                        (Component(Real), 'relTol', relTol, 'required'),
                        (Component(Real), 'absTol', absTol, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_copySystem')
        class oms_copySystem(
            ModelicaFunction,
        ):
            """
```modelica
function oms_copySystem
  input String source;
  input String target;
  output Integer status;
end oms_copySystem;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                source,
                target,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_copySystem',
                    inputArguments=[
                        (Component(String), 'source', source, 'required'),
                        (Component(String), 'target', target, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_delete')
        class oms_delete(
            ModelicaFunction,
        ):
            """
```modelica
function oms_delete
  input String cref;
  output Integer status;
end oms_delete;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_delete',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_deleteConnection')
        class oms_deleteConnection(
            ModelicaFunction,
        ):
            """
```modelica
function oms_deleteConnection
  input String crefA;
  input String crefB;
  output Integer status;
end oms_deleteConnection;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                crefA,
                crefB,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_deleteConnection',
                    inputArguments=[
                        (Component(String), 'crefA', crefA, 'required'),
                        (Component(String), 'crefB', crefB, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_deleteConnectorFromBus')
        class oms_deleteConnectorFromBus(
            ModelicaFunction,
        ):
            """
```modelica
function oms_deleteConnectorFromBus
  input String busCref;
  input String connectorCref;
  output Integer status;
end oms_deleteConnectorFromBus;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                busCref,
                connectorCref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_deleteConnectorFromBus',
                    inputArguments=[
                        (Component(String), 'busCref', busCref, 'required'),
                        (Component(String), 'connectorCref', connectorCref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_deleteConnectorFromTLMBus')
        class oms_deleteConnectorFromTLMBus(
            ModelicaFunction,
        ):
            """
```modelica
function oms_deleteConnectorFromTLMBus
  input String busCref;
  input String connectorCref;
  output Integer status;
end oms_deleteConnectorFromTLMBus;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                busCref,
                connectorCref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_deleteConnectorFromTLMBus',
                    inputArguments=[
                        (Component(String), 'busCref', busCref, 'required'),
                        (Component(String), 'connectorCref', connectorCref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_export')
        class oms_export(
            ModelicaFunction,
        ):
            """
```modelica
function oms_export
  input String cref;
  input String filename;
  output Integer status;
end oms_export;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                filename,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_export',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(String), 'filename', filename, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_exportDependencyGraphs')
        class oms_exportDependencyGraphs(
            ModelicaFunction,
        ):
            """
```modelica
function oms_exportDependencyGraphs
  input String cref;
  input String initialization;
  input String event;
  input String simulation;
  output Integer status;
end oms_exportDependencyGraphs;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                initialization,
                event,
                simulation,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_exportDependencyGraphs',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(String), 'initialization', initialization, 'required'),
                        (Component(String), 'event', event, 'required'),
                        (Component(String), 'simulation', simulation, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_exportSnapshot')
        class oms_exportSnapshot(
            ModelicaFunction,
        ):
            """
```modelica
function oms_exportSnapshot
  input String cref;
  output String contents;
  output Integer status;
end oms_exportSnapshot;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_exportSnapshot',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'contents'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_extractFMIKind')
        class oms_extractFMIKind(
            ModelicaFunction,
        ):
            """
```modelica
function oms_extractFMIKind
  input String filename;
  output Integer kind;
  output Integer status;
end oms_extractFMIKind;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                filename,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_extractFMIKind',
                    inputArguments=[
                        (Component(String), 'filename', filename, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'kind'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_getBoolean')
        class oms_getBoolean(
            ModelicaFunction,
        ):
            """
```modelica
function oms_getBoolean
  input String cref;
  output Boolean value;
  output Integer status;
end oms_getBoolean;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_getBoolean',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Boolean), 'value'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_getFixedStepSize')
        class oms_getFixedStepSize(
            ModelicaFunction,
        ):
            """
```modelica
function oms_getFixedStepSize
  input String cref;
  output Real stepSize;
  output Integer status;
end oms_getFixedStepSize;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_getFixedStepSize',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Real), 'stepSize'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_getInteger')
        class oms_getInteger(
            ModelicaFunction,
        ):
            """
```modelica
function oms_getInteger
  input String cref;
  input Integer value;
  output Integer status;
end oms_getInteger;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                value,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_getInteger',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(Integer), 'value', value, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_getModelState')
        class oms_getModelState(
            ModelicaFunction,
        ):
            """
```modelica
function oms_getModelState
  input String cref;
  output Integer modelState;
  output Integer status;
end oms_getModelState;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_getModelState',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'modelState'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_getReal')
        class oms_getReal(
            ModelicaFunction,
        ):
            """
```modelica
function oms_getReal
  input String cref;
  output Real value;
  output Integer status;
end oms_getReal;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_getReal',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Real), 'value'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_getSolver')
        class oms_getSolver(
            ModelicaFunction,
        ):
            """
```modelica
function oms_getSolver
  input String cref;
  output Integer solver;
  output Integer status;
end oms_getSolver;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_getSolver',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'solver'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_getStartTime')
        class oms_getStartTime(
            ModelicaFunction,
        ):
            """
```modelica
function oms_getStartTime
  input String cref;
  output Real startTime;
  output Integer status;
end oms_getStartTime;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_getStartTime',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Real), 'startTime'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_getStopTime')
        class oms_getStopTime(
            ModelicaFunction,
        ):
            """
```modelica
function oms_getStopTime
  input String cref;
  output Real stopTime;
  output Integer status;
end oms_getStopTime;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_getStopTime',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Real), 'stopTime'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_getSubModelPath')
        class oms_getSubModelPath(
            ModelicaFunction,
        ):
            """
```modelica
function oms_getSubModelPath
  input String cref;
  output String path;
  output Integer status;
end oms_getSubModelPath;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_getSubModelPath',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'path'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_getSystemType')
        class oms_getSystemType(
            ModelicaFunction,
        ):
            """
```modelica
function oms_getSystemType
  input String cref;
  output Integer type_;
  output Integer status;
end oms_getSystemType;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_getSystemType',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'type_'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_getTolerance')
        class oms_getTolerance(
            ModelicaFunction,
        ):
            """
```modelica
function oms_getTolerance
  input String cref;
  output Real absoluteTolerance;
  output Real relativeTolerance;
  output Integer status;
end oms_getTolerance;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_getTolerance',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Real), 'absoluteTolerance'),
                        (Component(Real), 'relativeTolerance'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_getVariableStepSize')
        class oms_getVariableStepSize(
            ModelicaFunction,
        ):
            """
```modelica
function oms_getVariableStepSize
  input String cref;
  output Real initialStepSize;
  output Real minimumStepSize;
  output Real maximumStepSize;
  output Integer status;
end oms_getVariableStepSize;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_getVariableStepSize',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Real), 'initialStepSize'),
                        (Component(Real), 'minimumStepSize'),
                        (Component(Real), 'maximumStepSize'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_faultInjection')
        class oms_faultInjection(
            ModelicaFunction,
        ):
            """
```modelica
function oms_faultInjection
  input String signal;
  input oms_fault_type faultType;
  input Real faultValue;
  output Integer status;
end oms_faultInjection;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                signal,
                faultType,
                faultValue,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_faultInjection',
                    inputArguments=[
                        (Component(String), 'signal', signal, 'required'),
                        (Component(OpenModelica.Scripting.oms_fault_type), 'faultType', faultType, 'required'),
                        (Component(Real), 'faultValue', faultValue, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_importFile')
        class oms_importFile(
            ModelicaFunction,
        ):
            """
```modelica
function oms_importFile
  input String filename;
  output String cref;
  output Integer status;
end oms_importFile;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                filename,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_importFile',
                    inputArguments=[
                        (Component(String), 'filename', filename, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'cref'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_importSnapshot')
        class oms_importSnapshot(
            ModelicaFunction,
        ):
            """
```modelica
function oms_importSnapshot
  input String cref;
  input String snapshot;
  output Integer status;
end oms_importSnapshot;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                snapshot,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_importSnapshot',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(String), 'snapshot', snapshot, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_initialize')
        class oms_initialize(
            ModelicaFunction,
        ):
            """
```modelica
function oms_initialize
  input String cref;
  output Integer status;
end oms_initialize;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_initialize',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_instantiate')
        class oms_instantiate(
            ModelicaFunction,
        ):
            """
```modelica
function oms_instantiate
  input String cref;
  output Integer status;
end oms_instantiate;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_instantiate',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_list')
        class oms_list(
            ModelicaFunction,
        ):
            """
```modelica
function oms_list
  input String cref;
  output String contents;
  output Integer status;
end oms_list;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_list',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'contents'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_listUnconnectedConnectors')
        class oms_listUnconnectedConnectors(
            ModelicaFunction,
        ):
            """
```modelica
function oms_listUnconnectedConnectors
  input String cref;
  output String contents;
  output Integer status;
end oms_listUnconnectedConnectors;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_listUnconnectedConnectors',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'contents'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_loadSnapshot')
        class oms_loadSnapshot(
            ModelicaFunction,
        ):
            """
```modelica
function oms_loadSnapshot
  input String cref;
  input String snapshot;
  output Integer status;
end oms_loadSnapshot;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                snapshot,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_loadSnapshot',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(String), 'snapshot', snapshot, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_newModel')
        class oms_newModel(
            ModelicaFunction,
        ):
            """
```modelica
function oms_newModel
  input String cref;
  output Integer status;
end oms_newModel;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_newModel',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_parseModelName')
        class oms_parseModelName(
            ModelicaFunction,
        ):
            """
```modelica
function oms_parseModelName
  input String contents;
  output String cref;
  output Integer status;
end oms_parseModelName;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                contents,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_parseModelName',
                    inputArguments=[
                        (Component(String), 'contents', contents, 'required'),
                    ],
                    outputArguments=[
                        (Component(String), 'cref'),
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_removeSignalsFromResults')
        class oms_removeSignalsFromResults(
            ModelicaFunction,
        ):
            """
```modelica
function oms_removeSignalsFromResults
  input String cref;
  input String regex;
  output Integer status;
end oms_removeSignalsFromResults;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                regex,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_removeSignalsFromResults',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(String), 'regex', regex, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_rename')
        class oms_rename(
            ModelicaFunction,
        ):
            """
```modelica
function oms_rename
  input String cref;
  input String newCref;
  output Integer status;
end oms_rename;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                newCref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_rename',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(String), 'newCref', newCref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_reset')
        class oms_reset(
            ModelicaFunction,
        ):
            """
```modelica
function oms_reset
  input String cref;
  output Integer status;
end oms_reset;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_reset',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_RunFile')
        class oms_RunFile(
            ModelicaFunction,
        ):
            """
```modelica
function oms_RunFile
  input String filename;
  output Integer status;
end oms_RunFile;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                filename,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_RunFile',
                    inputArguments=[
                        (Component(String), 'filename', filename, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setBoolean')
        class oms_setBoolean(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setBoolean
  input String cref;
  input Boolean value;
  output Integer status;
end oms_setBoolean;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                value,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setBoolean',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(Boolean), 'value', value, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setCommandLineOption')
        class oms_setCommandLineOption(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setCommandLineOption
  input String cmd;
  output Integer status;
end oms_setCommandLineOption;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cmd,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setCommandLineOption',
                    inputArguments=[
                        (Component(String), 'cmd', cmd, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setFixedStepSize')
        class oms_setFixedStepSize(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setFixedStepSize
  input String cref;
  input Real stepSize;
  output Integer status;
end oms_setFixedStepSize;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                stepSize,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setFixedStepSize',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(Real), 'stepSize', stepSize, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setInteger')
        class oms_setInteger(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setInteger
  input String cref;
  input Integer value;
  output Integer status;
end oms_setInteger;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                value,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setInteger',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(Integer), 'value', value, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setLogFile')
        class oms_setLogFile(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setLogFile
  input String filename;
  output Integer status;
end oms_setLogFile;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                filename,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setLogFile',
                    inputArguments=[
                        (Component(String), 'filename', filename, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setLoggingInterval')
        class oms_setLoggingInterval(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setLoggingInterval
  input String cref;
  input Real loggingInterval;
  output Integer status;
end oms_setLoggingInterval;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                loggingInterval,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setLoggingInterval',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(Real), 'loggingInterval', loggingInterval, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setLoggingLevel')
        class oms_setLoggingLevel(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setLoggingLevel
  input Integer logLevel;
  output Integer status;
end oms_setLoggingLevel;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                logLevel,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setLoggingLevel',
                    inputArguments=[
                        (Component(Integer), 'logLevel', logLevel, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setReal')
        class oms_setReal(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setReal
  input String cref;
  input Real value;
  output Integer status;
end oms_setReal;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                value,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setReal',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(Real), 'value', value, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setRealInputDerivative')
        class oms_setRealInputDerivative(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setRealInputDerivative
  input String cref;
  input Real value;
  output Integer status;
end oms_setRealInputDerivative;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                value,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setRealInputDerivative',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(Real), 'value', value, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setResultFile')
        class oms_setResultFile(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setResultFile
  input String cref;
  input String filename;
  input Integer bufferSize;
  output Integer status;
end oms_setResultFile;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                filename,
                bufferSize,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setResultFile',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(String), 'filename', filename, 'required'),
                        (Component(Integer), 'bufferSize', bufferSize, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setSignalFilter')
        class oms_setSignalFilter(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setSignalFilter
  input String cref;
  input String regex;
  output Integer status;
end oms_setSignalFilter;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                regex,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setSignalFilter',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(String), 'regex', regex, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setSolver')
        class oms_setSolver(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setSolver
  input String cref;
  input oms_solver solver;
  output Integer status;
end oms_setSolver;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                solver,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setSolver',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(OpenModelica.Scripting.oms_solver), 'solver', solver, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setStartTime')
        class oms_setStartTime(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setStartTime
  input String cref;
  input Real startTime;
  output Integer status;
end oms_setStartTime;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                startTime,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setStartTime',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(Real), 'startTime', startTime, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setStopTime')
        class oms_setStopTime(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setStopTime
  input String cref;
  input Real stopTime;
  output Integer status;
end oms_setStopTime;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                stopTime,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setStopTime',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(Real), 'stopTime', stopTime, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setTempDirectory')
        class oms_setTempDirectory(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setTempDirectory
  input String newTempDir;
  output Integer status;
end oms_setTempDirectory;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                newTempDir,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setTempDirectory',
                    inputArguments=[
                        (Component(String), 'newTempDir', newTempDir, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setTLMPositionAndOrientation')
        class oms_setTLMPositionAndOrientation(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setTLMPositionAndOrientation
  input String cref;
  input Real x1;
  input Real x2;
  input Real x3;
  input Real A11;
  input Real A12;
  input Real A13;
  input Real A21;
  input Real A22;
  input Real A23;
  input Real A31;
  input Real A32;
  input Real A33;
  output Integer status;
end oms_setTLMPositionAndOrientation;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                x1,
                x2,
                x3,
                A11,
                A12,
                A13,
                A21,
                A22,
                A23,
                A31,
                A32,
                A33,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setTLMPositionAndOrientation',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(Real), 'x1', x1, 'required'),
                        (Component(Real), 'x2', x2, 'required'),
                        (Component(Real), 'x3', x3, 'required'),
                        (Component(Real), 'A11', A11, 'required'),
                        (Component(Real), 'A12', A12, 'required'),
                        (Component(Real), 'A13', A13, 'required'),
                        (Component(Real), 'A21', A21, 'required'),
                        (Component(Real), 'A22', A22, 'required'),
                        (Component(Real), 'A23', A23, 'required'),
                        (Component(Real), 'A31', A31, 'required'),
                        (Component(Real), 'A32', A32, 'required'),
                        (Component(Real), 'A33', A33, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setTLMSocketData')
        class oms_setTLMSocketData(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setTLMSocketData
  input String cref;
  input String address;
  input Integer managerPort;
  input Integer monitorPort;
  output Integer status;
end oms_setTLMSocketData;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                address,
                managerPort,
                monitorPort,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setTLMSocketData',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(String), 'address', address, 'required'),
                        (Component(Integer), 'managerPort', managerPort, 'required'),
                        (Component(Integer), 'monitorPort', monitorPort, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setTolerance')
        class oms_setTolerance(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setTolerance
  input String cref;
  input Real absoluteTolerance;
  input Real relativeTolerance;
  output Integer status;
end oms_setTolerance;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                absoluteTolerance,
                relativeTolerance,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setTolerance',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(Real), 'absoluteTolerance', absoluteTolerance, 'required'),
                        (Component(Real), 'relativeTolerance', relativeTolerance, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setVariableStepSize')
        class oms_setVariableStepSize(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setVariableStepSize
  input String cref;
  input Real initialStepSize;
  input Real minimumStepSize;
  input Real maximumStepSize;
  output Integer status;
end oms_setVariableStepSize;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                initialStepSize,
                minimumStepSize,
                maximumStepSize,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setVariableStepSize',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(Real), 'initialStepSize', initialStepSize, 'required'),
                        (Component(Real), 'minimumStepSize', minimumStepSize, 'required'),
                        (Component(Real), 'maximumStepSize', maximumStepSize, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_setWorkingDirectory')
        class oms_setWorkingDirectory(
            ModelicaFunction,
        ):
            """
```modelica
function oms_setWorkingDirectory
  input String newWorkingDir;
  output Integer status;
end oms_setWorkingDirectory;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                newWorkingDir,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_setWorkingDirectory',
                    inputArguments=[
                        (Component(String), 'newWorkingDir', newWorkingDir, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_simulate')
        class oms_simulate(
            ModelicaFunction,
        ):
            """
```modelica
function oms_simulate
  input String cref;
  output Integer status;
end oms_simulate;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_simulate',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_stepUntil')
        class oms_stepUntil(
            ModelicaFunction,
        ):
            """
```modelica
function oms_stepUntil
  input String cref;
  input Real stopTime;
  output Integer status;
end oms_stepUntil;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
                stopTime,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_stepUntil',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                        (Component(Real), 'stopTime', stopTime, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_terminate')
        class oms_terminate(
            ModelicaFunction,
        ):
            """
```modelica
function oms_terminate
  input String cref;
  output Integer status;
end oms_terminate;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
                cref,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_terminate',
                    inputArguments=[
                        (Component(String), 'cref', cref, 'required'),
                    ],
                    outputArguments=[
                        (Component(Integer), 'status'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.oms_getVersion')
        class oms_getVersion(
            ModelicaFunction,
        ):
            """
```modelica
function oms_getVersion
  output String version;
end oms_getVersion;
```
            """
            @external
            def _(
                _cls_,
                _session_: AbstractOMCSession,
            ):
                return _session_.__omc__.call_function(
                    funcName='oms_getVersion',
                    inputArguments=[
                    ],
                    outputArguments=[
                        (Component(String), 'version'),
                    ],
                    parser=parse_OMCValue,
                )

        @modelica_name('OpenModelica.Scripting.Experimental')
        class Experimental(
            ModelicaPackage,
        ):
            @modelica_name('OpenModelica.Scripting.Experimental.relocateFunctions')
            class relocateFunctions(
                ModelicaFunction,
            ):
                """
```modelica
function relocateFunctions
  input String fileName;
  input String names[:, 2];
  output Boolean success;
end relocateFunctions;
```
                """
                @external
                def _(
                    _cls_,
                    _session_: AbstractOMCSession,
                    fileName,
                    names,
                ):
                    return _session_.__omc__.call_function(
                        funcName='OpenModelica.Scripting.Experimental.relocateFunctions',
                        inputArguments=[
                            (Component(String), 'fileName', fileName, 'required'),
                            (Component(String)[:, 2], 'names', names, 'required'),
                        ],
                        outputArguments=[
                            (Component(Boolean), 'success'),
                        ],
                        parser=parse_OMCValue,
                    )

            @modelica_name('OpenModelica.Scripting.Experimental.toJulia')
            class toJulia(
                ModelicaFunction,
            ):
                """
```modelica
function toJulia
  output String res;
end toJulia;
```
                """
                @external
                def _(
                    _cls_,
                    _session_: AbstractOMCSession,
                ):
                    return _session_.__omc__.call_function(
                        funcName='OpenModelica.Scripting.Experimental.toJulia',
                        inputArguments=[
                        ],
                        outputArguments=[
                            (Component(String), 'res'),
                        ],
                        parser=parse_OMCValue,
                    )

            @modelica_name('OpenModelica.Scripting.Experimental.interactiveDumpAbsynToJL')
            class interactiveDumpAbsynToJL(
                ModelicaFunction,
            ):
                """
```modelica
function interactiveDumpAbsynToJL
  output String res;
end interactiveDumpAbsynToJL;
```
                """
                @external
                def _(
                    _cls_,
                    _session_: AbstractOMCSession,
                ):
                    return _session_.__omc__.call_function(
                        funcName='OpenModelica.Scripting.Experimental.interactiveDumpAbsynToJL',
                        inputArguments=[
                        ],
                        outputArguments=[
                            (Component(String), 'res'),
                        ],
                        parser=parse_OMCValue,
                    )


class OMCSession(
    OMCSessionBase,
):
    OpenModelica = OpenModelica
    CheckSettingsResult = OpenModelica.Scripting.CheckSettingsResult
    checkSettings = OpenModelica.Scripting.checkSettings
    loadFile = OpenModelica.Scripting.loadFile
    loadFiles = OpenModelica.Scripting.loadFiles
    parseEncryptedPackage = OpenModelica.Scripting.parseEncryptedPackage
    loadEncryptedPackage = OpenModelica.Scripting.loadEncryptedPackage
    reloadClass = OpenModelica.Scripting.reloadClass
    loadString = OpenModelica.Scripting.loadString
    parseString = OpenModelica.Scripting.parseString
    parseFile = OpenModelica.Scripting.parseFile
    loadFileInteractiveQualified = OpenModelica.Scripting.loadFileInteractiveQualified
    loadFileInteractive = OpenModelica.Scripting.loadFileInteractive
    system = OpenModelica.Scripting.system
    system_parallel = OpenModelica.Scripting.system_parallel
    saveAll = OpenModelica.Scripting.saveAll
    help = OpenModelica.Scripting.help
    clear = OpenModelica.Scripting.clear
    clearProgram = OpenModelica.Scripting.clearProgram
    clearVariables = OpenModelica.Scripting.clearVariables
    generateHeader = OpenModelica.Scripting.generateHeader
    generateJuliaHeader = OpenModelica.Scripting.generateJuliaHeader
    generateSeparateCode = OpenModelica.Scripting.generateSeparateCode
    generateSeparateCodeDependencies = OpenModelica.Scripting.generateSeparateCodeDependencies
    generateSeparateCodeDependenciesMakefile = OpenModelica.Scripting.generateSeparateCodeDependenciesMakefile
    getLinker = OpenModelica.Scripting.getLinker
    setLinker = OpenModelica.Scripting.setLinker
    getLinkerFlags = OpenModelica.Scripting.getLinkerFlags
    setLinkerFlags = OpenModelica.Scripting.setLinkerFlags
    getCompiler = OpenModelica.Scripting.getCompiler
    setCompiler = OpenModelica.Scripting.setCompiler
    setCFlags = OpenModelica.Scripting.setCFlags
    getCFlags = OpenModelica.Scripting.getCFlags
    getCXXCompiler = OpenModelica.Scripting.getCXXCompiler
    setCXXCompiler = OpenModelica.Scripting.setCXXCompiler
    verifyCompiler = OpenModelica.Scripting.verifyCompiler
    setCompilerPath = OpenModelica.Scripting.setCompilerPath
    getCompileCommand = OpenModelica.Scripting.getCompileCommand
    setCompileCommand = OpenModelica.Scripting.setCompileCommand
    setPlotCommand = OpenModelica.Scripting.setPlotCommand
    getSettings = OpenModelica.Scripting.getSettings
    setTempDirectoryPath = OpenModelica.Scripting.setTempDirectoryPath
    getTempDirectoryPath = OpenModelica.Scripting.getTempDirectoryPath
    getEnvironmentVar = OpenModelica.Scripting.getEnvironmentVar
    setEnvironmentVar = OpenModelica.Scripting.setEnvironmentVar
    appendEnvironmentVar = OpenModelica.Scripting.appendEnvironmentVar
    setInstallationDirectoryPath = OpenModelica.Scripting.setInstallationDirectoryPath
    getInstallationDirectoryPath = OpenModelica.Scripting.getInstallationDirectoryPath
    setModelicaPath = OpenModelica.Scripting.setModelicaPath
    getModelicaPath = OpenModelica.Scripting.getModelicaPath
    setCompilerFlags = OpenModelica.Scripting.setCompilerFlags
    enableNewInstantiation = OpenModelica.Scripting.enableNewInstantiation
    disableNewInstantiation = OpenModelica.Scripting.disableNewInstantiation
    setDebugFlags = OpenModelica.Scripting.setDebugFlags
    clearDebugFlags = OpenModelica.Scripting.clearDebugFlags
    setPreOptModules = OpenModelica.Scripting.setPreOptModules
    setCheapMatchingAlgorithm = OpenModelica.Scripting.setCheapMatchingAlgorithm
    getMatchingAlgorithm = OpenModelica.Scripting.getMatchingAlgorithm
    getAvailableMatchingAlgorithms = OpenModelica.Scripting.getAvailableMatchingAlgorithms
    setMatchingAlgorithm = OpenModelica.Scripting.setMatchingAlgorithm
    getIndexReductionMethod = OpenModelica.Scripting.getIndexReductionMethod
    getAvailableIndexReductionMethods = OpenModelica.Scripting.getAvailableIndexReductionMethods
    setIndexReductionMethod = OpenModelica.Scripting.setIndexReductionMethod
    setPostOptModules = OpenModelica.Scripting.setPostOptModules
    getTearingMethod = OpenModelica.Scripting.getTearingMethod
    getAvailableTearingMethods = OpenModelica.Scripting.getAvailableTearingMethods
    setTearingMethod = OpenModelica.Scripting.setTearingMethod
    setCommandLineOptions = OpenModelica.Scripting.setCommandLineOptions
    getCommandLineOptions = OpenModelica.Scripting.getCommandLineOptions
    getConfigFlagValidOptions = OpenModelica.Scripting.getConfigFlagValidOptions
    clearCommandLineOptions = OpenModelica.Scripting.clearCommandLineOptions
    getVersion = OpenModelica.Scripting.getVersion
    regularFileExists = OpenModelica.Scripting.regularFileExists
    directoryExists = OpenModelica.Scripting.directoryExists
    stat = OpenModelica.Scripting.stat
    readFile = OpenModelica.Scripting.readFile
    writeFile = OpenModelica.Scripting.writeFile
    compareFilesAndMove = OpenModelica.Scripting.compareFilesAndMove
    compareFiles = OpenModelica.Scripting.compareFiles
    alarm = OpenModelica.Scripting.alarm
    regex = OpenModelica.Scripting.regex
    regexBool = OpenModelica.Scripting.regexBool
    testsuiteFriendlyName = OpenModelica.Scripting.testsuiteFriendlyName
    readFileNoNumeric = OpenModelica.Scripting.readFileNoNumeric
    getErrorString = OpenModelica.Scripting.getErrorString
    getMessagesString = OpenModelica.Scripting.getMessagesString
    SourceInfo = OpenModelica.Scripting.SourceInfo
    ErrorKind = OpenModelica.Scripting.ErrorKind
    ErrorLevel = OpenModelica.Scripting.ErrorLevel
    ErrorMessage = OpenModelica.Scripting.ErrorMessage
    getMessagesStringInternal = OpenModelica.Scripting.getMessagesStringInternal
    countMessages = OpenModelica.Scripting.countMessages
    clearMessages = OpenModelica.Scripting.clearMessages
    runScript = OpenModelica.Scripting.runScript
    echo = OpenModelica.Scripting.echo
    getClassesInModelicaPath = OpenModelica.Scripting.getClassesInModelicaPath
    getAnnotationVersion = OpenModelica.Scripting.getAnnotationVersion
    setAnnotationVersion = OpenModelica.Scripting.setAnnotationVersion
    getNoSimplify = OpenModelica.Scripting.getNoSimplify
    setNoSimplify = OpenModelica.Scripting.setNoSimplify
    getVectorizationLimit = OpenModelica.Scripting.getVectorizationLimit
    setVectorizationLimit = OpenModelica.Scripting.setVectorizationLimit
    getDefaultOpenCLDevice = OpenModelica.Scripting.getDefaultOpenCLDevice
    setDefaultOpenCLDevice = OpenModelica.Scripting.setDefaultOpenCLDevice
    setShowAnnotations = OpenModelica.Scripting.setShowAnnotations
    getShowAnnotations = OpenModelica.Scripting.getShowAnnotations
    setOrderConnections = OpenModelica.Scripting.setOrderConnections
    getOrderConnections = OpenModelica.Scripting.getOrderConnections
    setLanguageStandard = OpenModelica.Scripting.setLanguageStandard
    getLanguageStandard = OpenModelica.Scripting.getLanguageStandard
    getAstAsCorbaString = OpenModelica.Scripting.getAstAsCorbaString
    cd = OpenModelica.Scripting.cd
    mkdir = OpenModelica.Scripting.mkdir
    copy = OpenModelica.Scripting.copy
    remove = OpenModelica.Scripting.remove
    checkModel = OpenModelica.Scripting.checkModel
    checkAllModelsRecursive = OpenModelica.Scripting.checkAllModelsRecursive
    typeOf = OpenModelica.Scripting.typeOf
    instantiateModel = OpenModelica.Scripting.instantiateModel
    buildOpenTURNSInterface = OpenModelica.Scripting.buildOpenTURNSInterface
    runOpenTURNSPythonScript = OpenModelica.Scripting.runOpenTURNSPythonScript
    generateCode = OpenModelica.Scripting.generateCode
    loadModel = OpenModelica.Scripting.loadModel
    deleteFile = OpenModelica.Scripting.deleteFile
    saveModel = OpenModelica.Scripting.saveModel
    saveTotalModel = OpenModelica.Scripting.saveTotalModel
    save = OpenModelica.Scripting.save
    saveTotalSCode = OpenModelica.Scripting.saveTotalSCode
    translateGraphics = OpenModelica.Scripting.translateGraphics
    # codeToString = OpenModelica.Scripting.codeToString
    dumpXMLDAE = OpenModelica.Scripting.dumpXMLDAE
    convertUnits = OpenModelica.Scripting.convertUnits
    getDerivedUnits = OpenModelica.Scripting.getDerivedUnits
    listVariables = OpenModelica.Scripting.listVariables
    strtok = OpenModelica.Scripting.strtok
    stringSplit = OpenModelica.Scripting.stringSplit
    stringReplace = OpenModelica.Scripting.stringReplace
    escapeXML = OpenModelica.Scripting.escapeXML
    ExportKind = OpenModelica.Scripting.ExportKind
    list = OpenModelica.Scripting.list
    listFile = OpenModelica.Scripting.listFile
    DiffFormat = OpenModelica.Scripting.DiffFormat
    diffModelicaFileListings = OpenModelica.Scripting.diffModelicaFileListings
    exportToFigaro = OpenModelica.Scripting.exportToFigaro
    inferBindings = OpenModelica.Scripting.inferBindings
    generateVerificationScenarios = OpenModelica.Scripting.generateVerificationScenarios
    rewriteBlockCall = OpenModelica.Scripting.rewriteBlockCall
    realpath = OpenModelica.Scripting.realpath
    uriToFilename = OpenModelica.Scripting.uriToFilename
    getLoadedLibraries = OpenModelica.Scripting.getLoadedLibraries
    LinearSystemSolver = OpenModelica.Scripting.LinearSystemSolver
    solveLinearSystem = OpenModelica.Scripting.solveLinearSystem
    StandardStream = OpenModelica.Scripting.StandardStream
    reopenStandardStream = OpenModelica.Scripting.reopenStandardStream
    importFMU = OpenModelica.Scripting.importFMU
    importFMUModelDescription = OpenModelica.Scripting.importFMUModelDescription
    translateModelFMU = OpenModelica.Scripting.translateModelFMU
    buildModelFMU = OpenModelica.Scripting.buildModelFMU
    buildEncryptedPackage = OpenModelica.Scripting.buildEncryptedPackage
    simulate = OpenModelica.Scripting.simulate
    buildModel = OpenModelica.Scripting.buildModel
    buildLabel = OpenModelica.Scripting.buildLabel
    reduceTerms = OpenModelica.Scripting.reduceTerms
    moveClass = OpenModelica.Scripting.moveClass
    moveClassToTop = OpenModelica.Scripting.moveClassToTop
    moveClassToBottom = OpenModelica.Scripting.moveClassToBottom
    copyClass = OpenModelica.Scripting.copyClass
    linearize = OpenModelica.Scripting.linearize
    optimize = OpenModelica.Scripting.optimize
    getSourceFile = OpenModelica.Scripting.getSourceFile
    setSourceFile = OpenModelica.Scripting.setSourceFile
    isShortDefinition = OpenModelica.Scripting.isShortDefinition
    setClassComment = OpenModelica.Scripting.setClassComment
    getClassNames = OpenModelica.Scripting.getClassNames
    getUsedClassNames = OpenModelica.Scripting.getUsedClassNames
    getPackages = OpenModelica.Scripting.getPackages
    getAllSubtypeOf = OpenModelica.Scripting.getAllSubtypeOf
    basePlotFunction = OpenModelica.Scripting.basePlotFunction
    plot = OpenModelica.Scripting.plot
    plotAll = OpenModelica.Scripting.plotAll
    plotParametric = OpenModelica.Scripting.plotParametric
    readSimulationResult = OpenModelica.Scripting.readSimulationResult
    readSimulationResultSize = OpenModelica.Scripting.readSimulationResultSize
    readSimulationResultVars = OpenModelica.Scripting.readSimulationResultVars
    filterSimulationResults = OpenModelica.Scripting.filterSimulationResults
    compareSimulationResults = OpenModelica.Scripting.compareSimulationResults
    deltaSimulationResults = OpenModelica.Scripting.deltaSimulationResults
    diffSimulationResults = OpenModelica.Scripting.diffSimulationResults
    diffSimulationResultsHtml = OpenModelica.Scripting.diffSimulationResultsHtml
    checkTaskGraph = OpenModelica.Scripting.checkTaskGraph
    checkCodeGraph = OpenModelica.Scripting.checkCodeGraph
    val = OpenModelica.Scripting.val
    closeSimulationResultFile = OpenModelica.Scripting.closeSimulationResultFile
    # addClassAnnotation = OpenModelica.Scripting.addClassAnnotation
    getParameterNames = OpenModelica.Scripting.getParameterNames
    getParameterValue = OpenModelica.Scripting.getParameterValue
    getComponentModifierNames = OpenModelica.Scripting.getComponentModifierNames
    getComponentModifierValue = OpenModelica.Scripting.getComponentModifierValue
    getComponentModifierValues = OpenModelica.Scripting.getComponentModifierValues
    removeComponentModifiers = OpenModelica.Scripting.removeComponentModifiers
    getElementModifierNames = OpenModelica.Scripting.getElementModifierNames
    getElementModifierValue = OpenModelica.Scripting.getElementModifierValue
    getElementModifierValues = OpenModelica.Scripting.getElementModifierValues
    removeElementModifiers = OpenModelica.Scripting.removeElementModifiers
    getInstantiatedParametersAndValues = OpenModelica.Scripting.getInstantiatedParametersAndValues
    removeExtendsModifiers = OpenModelica.Scripting.removeExtendsModifiers
    # updateConnection = OpenModelica.Scripting.updateConnection
    updateConnectionAnnotation = OpenModelica.Scripting.updateConnectionAnnotation
    updateConnectionNames = OpenModelica.Scripting.updateConnectionNames
    getConnectionCount = OpenModelica.Scripting.getConnectionCount
    getNthConnection = OpenModelica.Scripting.getNthConnection
    getAlgorithmCount = OpenModelica.Scripting.getAlgorithmCount
    getNthAlgorithm = OpenModelica.Scripting.getNthAlgorithm
    getInitialAlgorithmCount = OpenModelica.Scripting.getInitialAlgorithmCount
    getNthInitialAlgorithm = OpenModelica.Scripting.getNthInitialAlgorithm
    getAlgorithmItemsCount = OpenModelica.Scripting.getAlgorithmItemsCount
    getNthAlgorithmItem = OpenModelica.Scripting.getNthAlgorithmItem
    getInitialAlgorithmItemsCount = OpenModelica.Scripting.getInitialAlgorithmItemsCount
    getNthInitialAlgorithmItem = OpenModelica.Scripting.getNthInitialAlgorithmItem
    getEquationCount = OpenModelica.Scripting.getEquationCount
    getNthEquation = OpenModelica.Scripting.getNthEquation
    getInitialEquationCount = OpenModelica.Scripting.getInitialEquationCount
    getNthInitialEquation = OpenModelica.Scripting.getNthInitialEquation
    getEquationItemsCount = OpenModelica.Scripting.getEquationItemsCount
    getNthEquationItem = OpenModelica.Scripting.getNthEquationItem
    getInitialEquationItemsCount = OpenModelica.Scripting.getInitialEquationItemsCount
    getNthInitialEquationItem = OpenModelica.Scripting.getNthInitialEquationItem
    getAnnotationCount = OpenModelica.Scripting.getAnnotationCount
    getNthAnnotationString = OpenModelica.Scripting.getNthAnnotationString
    getImportCount = OpenModelica.Scripting.getImportCount
    getMMfileTotalDependencies = OpenModelica.Scripting.getMMfileTotalDependencies
    getImportedNames = OpenModelica.Scripting.getImportedNames
    getNthImport = OpenModelica.Scripting.getNthImport
    iconv = OpenModelica.Scripting.iconv
    getDocumentationAnnotation = OpenModelica.Scripting.getDocumentationAnnotation
    setDocumentationAnnotation = OpenModelica.Scripting.setDocumentationAnnotation
    getTimeStamp = OpenModelica.Scripting.getTimeStamp
    stringTypeName = OpenModelica.Scripting.stringTypeName
    stringVariableName = OpenModelica.Scripting.stringVariableName
    typeNameString = OpenModelica.Scripting.typeNameString
    typeNameStrings = OpenModelica.Scripting.typeNameStrings
    getClassComment = OpenModelica.Scripting.getClassComment
    dirname = OpenModelica.Scripting.dirname
    basename = OpenModelica.Scripting.basename
    getClassRestriction = OpenModelica.Scripting.getClassRestriction
    isType = OpenModelica.Scripting.isType
    isPackage = OpenModelica.Scripting.isPackage
    isClass = OpenModelica.Scripting.isClass
    isRecord = OpenModelica.Scripting.isRecord
    isBlock = OpenModelica.Scripting.isBlock
    isFunction = OpenModelica.Scripting.isFunction
    isPartial = OpenModelica.Scripting.isPartial
    isModel = OpenModelica.Scripting.isModel
    isConnector = OpenModelica.Scripting.isConnector
    isOptimization = OpenModelica.Scripting.isOptimization
    isEnumeration = OpenModelica.Scripting.isEnumeration
    isOperator = OpenModelica.Scripting.isOperator
    isOperatorRecord = OpenModelica.Scripting.isOperatorRecord
    isOperatorFunction = OpenModelica.Scripting.isOperatorFunction
    isProtectedClass = OpenModelica.Scripting.isProtectedClass
    getBuiltinType = OpenModelica.Scripting.getBuiltinType
    setInitXmlStartValue = OpenModelica.Scripting.setInitXmlStartValue
    ngspicetoModelica = OpenModelica.Scripting.ngspicetoModelica
    getInheritedClasses = OpenModelica.Scripting.getInheritedClasses
    getComponentsTest = OpenModelica.Scripting.getComponentsTest
    isExperiment = OpenModelica.Scripting.isExperiment
    getSimulationOptions = OpenModelica.Scripting.getSimulationOptions
    getAnnotationNamedModifiers = OpenModelica.Scripting.getAnnotationNamedModifiers
    getAnnotationModifierValue = OpenModelica.Scripting.getAnnotationModifierValue
    classAnnotationExists = OpenModelica.Scripting.classAnnotationExists
    getBooleanClassAnnotation = OpenModelica.Scripting.getBooleanClassAnnotation
    extendsFrom = OpenModelica.Scripting.extendsFrom
    loadModelica3D = OpenModelica.Scripting.loadModelica3D
    searchClassNames = OpenModelica.Scripting.searchClassNames
    getAvailableLibraries = OpenModelica.Scripting.getAvailableLibraries
    installPackage = OpenModelica.Scripting.installPackage
    updatePackageIndex = OpenModelica.Scripting.updatePackageIndex
    upgradeInstalledPackages = OpenModelica.Scripting.upgradeInstalledPackages
    getUses = OpenModelica.Scripting.getUses
    getConversionsFromVersions = OpenModelica.Scripting.getConversionsFromVersions
    getDerivedClassModifierNames = OpenModelica.Scripting.getDerivedClassModifierNames
    getDerivedClassModifierValue = OpenModelica.Scripting.getDerivedClassModifierValue
    generateEntryPoint = OpenModelica.Scripting.generateEntryPoint
    numProcessors = OpenModelica.Scripting.numProcessors
    runScriptParallel = OpenModelica.Scripting.runScriptParallel
    exit = OpenModelica.Scripting.exit
    threadWorkFailed = OpenModelica.Scripting.threadWorkFailed
    getMemorySize = OpenModelica.Scripting.getMemorySize
    GC_gcollect_and_unmap = OpenModelica.Scripting.GC_gcollect_and_unmap
    GC_expand_hp = OpenModelica.Scripting.GC_expand_hp
    GC_set_max_heap_size = OpenModelica.Scripting.GC_set_max_heap_size
    GC_PROFSTATS = OpenModelica.Scripting.GC_PROFSTATS
    GC_get_prof_stats = OpenModelica.Scripting.GC_get_prof_stats
    checkInterfaceOfPackages = OpenModelica.Scripting.checkInterfaceOfPackages
    sortStrings = OpenModelica.Scripting.sortStrings
    getClassInformation = OpenModelica.Scripting.getClassInformation
    getTransitions = OpenModelica.Scripting.getTransitions
    # addTransition = OpenModelica.Scripting.addTransition
    deleteTransition = OpenModelica.Scripting.deleteTransition
    # updateTransition = OpenModelica.Scripting.updateTransition
    getInitialStates = OpenModelica.Scripting.getInitialStates
    # addInitialState = OpenModelica.Scripting.addInitialState
    deleteInitialState = OpenModelica.Scripting.deleteInitialState
    # updateInitialState = OpenModelica.Scripting.updateInitialState
    generateScriptingAPI = OpenModelica.Scripting.generateScriptingAPI
    oms_system = OpenModelica.Scripting.oms_system
    oms_causality = OpenModelica.Scripting.oms_causality
    oms_signal_type = OpenModelica.Scripting.oms_signal_type
    oms_solver = OpenModelica.Scripting.oms_solver
    oms_tlm_domain = OpenModelica.Scripting.oms_tlm_domain
    oms_tlm_interpolation = OpenModelica.Scripting.oms_tlm_interpolation
    oms_fault_type = OpenModelica.Scripting.oms_fault_type
    loadOMSimulator = OpenModelica.Scripting.loadOMSimulator
    unloadOMSimulator = OpenModelica.Scripting.unloadOMSimulator
    oms_addBus = OpenModelica.Scripting.oms_addBus
    oms_addConnection = OpenModelica.Scripting.oms_addConnection
    oms_addConnector = OpenModelica.Scripting.oms_addConnector
    oms_addConnectorToBus = OpenModelica.Scripting.oms_addConnectorToBus
    oms_addConnectorToTLMBus = OpenModelica.Scripting.oms_addConnectorToTLMBus
    oms_addDynamicValueIndicator = OpenModelica.Scripting.oms_addDynamicValueIndicator
    oms_addEventIndicator = OpenModelica.Scripting.oms_addEventIndicator
    oms_addExternalModel = OpenModelica.Scripting.oms_addExternalModel
    oms_addSignalsToResults = OpenModelica.Scripting.oms_addSignalsToResults
    oms_addStaticValueIndicator = OpenModelica.Scripting.oms_addStaticValueIndicator
    oms_addSubModel = OpenModelica.Scripting.oms_addSubModel
    oms_addSystem = OpenModelica.Scripting.oms_addSystem
    oms_addTimeIndicator = OpenModelica.Scripting.oms_addTimeIndicator
    oms_addTLMBus = OpenModelica.Scripting.oms_addTLMBus
    oms_addTLMConnection = OpenModelica.Scripting.oms_addTLMConnection
    oms_cancelSimulation_asynchronous = OpenModelica.Scripting.oms_cancelSimulation_asynchronous
    oms_compareSimulationResults = OpenModelica.Scripting.oms_compareSimulationResults
    oms_copySystem = OpenModelica.Scripting.oms_copySystem
    oms_delete = OpenModelica.Scripting.oms_delete
    oms_deleteConnection = OpenModelica.Scripting.oms_deleteConnection
    oms_deleteConnectorFromBus = OpenModelica.Scripting.oms_deleteConnectorFromBus
    oms_deleteConnectorFromTLMBus = OpenModelica.Scripting.oms_deleteConnectorFromTLMBus
    oms_export = OpenModelica.Scripting.oms_export
    oms_exportDependencyGraphs = OpenModelica.Scripting.oms_exportDependencyGraphs
    oms_exportSnapshot = OpenModelica.Scripting.oms_exportSnapshot
    oms_extractFMIKind = OpenModelica.Scripting.oms_extractFMIKind
    oms_getBoolean = OpenModelica.Scripting.oms_getBoolean
    oms_getFixedStepSize = OpenModelica.Scripting.oms_getFixedStepSize
    oms_getInteger = OpenModelica.Scripting.oms_getInteger
    oms_getModelState = OpenModelica.Scripting.oms_getModelState
    oms_getReal = OpenModelica.Scripting.oms_getReal
    oms_getSolver = OpenModelica.Scripting.oms_getSolver
    oms_getStartTime = OpenModelica.Scripting.oms_getStartTime
    oms_getStopTime = OpenModelica.Scripting.oms_getStopTime
    oms_getSubModelPath = OpenModelica.Scripting.oms_getSubModelPath
    oms_getSystemType = OpenModelica.Scripting.oms_getSystemType
    oms_getTolerance = OpenModelica.Scripting.oms_getTolerance
    oms_getVariableStepSize = OpenModelica.Scripting.oms_getVariableStepSize
    oms_faultInjection = OpenModelica.Scripting.oms_faultInjection
    oms_importFile = OpenModelica.Scripting.oms_importFile
    oms_importSnapshot = OpenModelica.Scripting.oms_importSnapshot
    oms_initialize = OpenModelica.Scripting.oms_initialize
    oms_instantiate = OpenModelica.Scripting.oms_instantiate
    oms_list = OpenModelica.Scripting.oms_list
    oms_listUnconnectedConnectors = OpenModelica.Scripting.oms_listUnconnectedConnectors
    oms_loadSnapshot = OpenModelica.Scripting.oms_loadSnapshot
    oms_newModel = OpenModelica.Scripting.oms_newModel
    oms_parseModelName = OpenModelica.Scripting.oms_parseModelName
    oms_removeSignalsFromResults = OpenModelica.Scripting.oms_removeSignalsFromResults
    oms_rename = OpenModelica.Scripting.oms_rename
    oms_reset = OpenModelica.Scripting.oms_reset
    oms_RunFile = OpenModelica.Scripting.oms_RunFile
    oms_setBoolean = OpenModelica.Scripting.oms_setBoolean
    oms_setCommandLineOption = OpenModelica.Scripting.oms_setCommandLineOption
    oms_setFixedStepSize = OpenModelica.Scripting.oms_setFixedStepSize
    oms_setInteger = OpenModelica.Scripting.oms_setInteger
    oms_setLogFile = OpenModelica.Scripting.oms_setLogFile
    oms_setLoggingInterval = OpenModelica.Scripting.oms_setLoggingInterval
    oms_setLoggingLevel = OpenModelica.Scripting.oms_setLoggingLevel
    oms_setReal = OpenModelica.Scripting.oms_setReal
    oms_setRealInputDerivative = OpenModelica.Scripting.oms_setRealInputDerivative
    oms_setResultFile = OpenModelica.Scripting.oms_setResultFile
    oms_setSignalFilter = OpenModelica.Scripting.oms_setSignalFilter
    oms_setSolver = OpenModelica.Scripting.oms_setSolver
    oms_setStartTime = OpenModelica.Scripting.oms_setStartTime
    oms_setStopTime = OpenModelica.Scripting.oms_setStopTime
    oms_setTempDirectory = OpenModelica.Scripting.oms_setTempDirectory
    oms_setTLMPositionAndOrientation = OpenModelica.Scripting.oms_setTLMPositionAndOrientation
    oms_setTLMSocketData = OpenModelica.Scripting.oms_setTLMSocketData
    oms_setTolerance = OpenModelica.Scripting.oms_setTolerance
    oms_setVariableStepSize = OpenModelica.Scripting.oms_setVariableStepSize
    oms_setWorkingDirectory = OpenModelica.Scripting.oms_setWorkingDirectory
    oms_simulate = OpenModelica.Scripting.oms_simulate
    oms_stepUntil = OpenModelica.Scripting.oms_stepUntil
    oms_terminate = OpenModelica.Scripting.oms_terminate
    oms_getVersion = OpenModelica.Scripting.oms_getVersion
