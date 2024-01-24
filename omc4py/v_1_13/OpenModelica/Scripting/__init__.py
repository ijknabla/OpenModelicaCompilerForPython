from __future__ import annotations as _

from dataclasses import dataclass
from typing import (
    Coroutine,
    List,
    Literal,
    NamedTuple,
    Sequence,
    Union,
    overload,
)

from omc4py.modelica import enumeration, external, package, record
from omc4py.openmodelica import TypeName, VariableName
from omc4py.protocol import (
    Asynchronous,
    PathLike,
    SupportsInteractiveProperty,
    Synchronous,
    T_Calling,
)

from . import Experimental as experimental
from . import Internal as internal


@dataclass(frozen=True)
class CheckSettingsResult(record):
    """
    .. code-block:: modelica

        record CheckSettingsResult
          String OPENMODELICAHOME, OPENMODELICALIBRARY, OMC_PATH, SYSTEM_PATH, OMDEV_PATH;
          Boolean OMC_FOUND;
          String MODELICAUSERCFLAGS, WORKING_DIRECTORY;
          Boolean CREATE_FILE_WORKS, REMOVE_FILE_WORKS;
          // String OS, SYSTEM_INFO, SENDDATALIBS, C_COMPILER, C_COMPILER_VERSION;
             String OS, SYSTEM_INFO, RTLIBS, C_COMPILER, C_COMPILER_VERSION;
          Boolean C_COMPILER_RESPONDING, HAVE_CORBA;
          String CONFIGURE_CMDLINE;
          annotation(
            preferredView = "text");
        end CheckSettingsResult;"""

    __omc_class__ = TypeName("OpenModelica.Scripting.CheckSettingsResult")
    OPENMODELICAHOME: str
    OPENMODELICALIBRARY: str
    OMC_PATH: str
    SYSTEM_PATH: str
    OMDEV_PATH: str
    OMC_FOUND: bool
    MODELICAUSERCFLAGS: str
    WORKING_DIRECTORY: str
    CREATE_FILE_WORKS: bool
    REMOVE_FILE_WORKS: bool
    OS: str
    SYSTEM_INFO: str
    RTLIBS: str
    C_COMPILER: str
    C_COMPILER_VERSION: str
    C_COMPILER_RESPONDING: bool
    HAVE_CORBA: bool
    CONFIGURE_CMDLINE: str


class Internal(package[T_Calling]):
    __omc_class__ = TypeName("OpenModelica.Scripting.Internal")

    @property
    def Time(self) -> internal.Time[T_Calling]:
        return internal.Time(self.__omc_interactive__)

    FileType = internal.FileType
    stat = internal.stat


@overload
def checkSettings(
    self: SupportsInteractiveProperty[Synchronous],
) -> CheckSettingsResult:
    ...


@overload
async def checkSettings(
    self: SupportsInteractiveProperty[Asynchronous],
) -> CheckSettingsResult:
    ...


@external("checkSettings")
def checkSettings(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[CheckSettingsResult, Coroutine[None, None, CheckSettingsResult]]:
    """
    .. code-block:: modelica

        function checkSettings
          output CheckSettingsResult result;
        end checkSettings;"""
    return ...  # type: ignore


@overload
def loadFile(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
    encoding: Union[str, None] = None,
    uses: Union[bool, None] = None,
) -> bool:
    ...


@overload
async def loadFile(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
    encoding: Union[str, None] = None,
    uses: Union[bool, None] = None,
) -> bool:
    ...


@external("loadFile")
def loadFile(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
    encoding: Union[str, None] = None,
    uses: Union[bool, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function loadFile
          input String fileName;
          input String encoding = "UTF-8";
          input Boolean uses = true;
          output Boolean success;
        end loadFile;"""
    return ...  # type: ignore


@overload
def loadFiles(
    self: SupportsInteractiveProperty[Synchronous],
    fileNames: Sequence[Union[PathLike[str], str]],
    encoding: Union[str, None] = None,
    numThreads: Union[int, None] = None,
) -> bool:
    ...


@overload
async def loadFiles(
    self: SupportsInteractiveProperty[Asynchronous],
    fileNames: Sequence[Union[PathLike[str], str]],
    encoding: Union[str, None] = None,
    numThreads: Union[int, None] = None,
) -> bool:
    ...


@external("loadFiles")
def loadFiles(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileNames: Sequence[Union[PathLike[str], str]],
    encoding: Union[str, None] = None,
    numThreads: Union[int, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function loadFiles
          input String[:] fileNames;
          input String encoding = "UTF-8";
          input Integer numThreads = OpenModelica.Scripting.numProcessors();
          output Boolean success;
        end loadFiles;"""
    return ...  # type: ignore


@overload
def loadEncryptedPackage(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
    workdir: Union[PathLike[str], str, None] = None,
) -> bool:
    ...


@overload
async def loadEncryptedPackage(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
    workdir: Union[PathLike[str], str, None] = None,
) -> bool:
    ...


@external("loadEncryptedPackage")
def loadEncryptedPackage(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
    workdir: Union[PathLike[str], str, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function loadEncryptedPackage
          input String fileName;
          input String workdir = "<default>" "The output directory for imported encrypted files. <default> will put the files to current working directory.";
          output Boolean success;
        end loadEncryptedPackage;"""
    return ...  # type: ignore


@overload
def reloadClass(
    self: SupportsInteractiveProperty[Synchronous],
    name: Union[TypeName, str],
    encoding: Union[str, None] = None,
) -> bool:
    ...


@overload
async def reloadClass(
    self: SupportsInteractiveProperty[Asynchronous],
    name: Union[TypeName, str],
    encoding: Union[str, None] = None,
) -> bool:
    ...


@external("reloadClass")
def reloadClass(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    name: Union[TypeName, str],
    encoding: Union[str, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function reloadClass
          input TypeName name;
          input String encoding = "UTF-8";
          output Boolean success;
        end reloadClass;"""
    return ...  # type: ignore


@overload
def loadString(
    self: SupportsInteractiveProperty[Synchronous],
    data: str,
    filename: Union[PathLike[str], str, None] = None,
    encoding: Union[str, None] = None,
    merge: Union[bool, None] = None,
) -> bool:
    ...


@overload
async def loadString(
    self: SupportsInteractiveProperty[Asynchronous],
    data: str,
    filename: Union[PathLike[str], str, None] = None,
    encoding: Union[str, None] = None,
    merge: Union[bool, None] = None,
) -> bool:
    ...


@external("loadString")
def loadString(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    data: str,
    filename: Union[PathLike[str], str, None] = None,
    encoding: Union[str, None] = None,
    merge: Union[bool, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function loadString
          input String data;
          input String filename = "<interactive>";
          input String encoding = "UTF-8";
          input Boolean merge = false "if merge is true the parsed AST is merged with the existing AST, default to false which means that is replaced, not merged";
          output Boolean success;
        end loadString;"""
    return ...  # type: ignore


@overload
def parseString(
    self: SupportsInteractiveProperty[Synchronous],
    data: str,
    filename: Union[PathLike[str], str, None] = None,
) -> List[TypeName]:
    ...


@overload
async def parseString(
    self: SupportsInteractiveProperty[Asynchronous],
    data: str,
    filename: Union[PathLike[str], str, None] = None,
) -> List[TypeName]:
    ...


@external("parseString")
def parseString(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    data: str,
    filename: Union[PathLike[str], str, None] = None,
) -> Union[List[TypeName], Coroutine[None, None, List[TypeName]]]:
    """
    .. code-block:: modelica

        function parseString
          input String data;
          input String filename = "<interactive>";
          output TypeName names[:];
        end parseString;"""
    return ...  # type: ignore


@overload
def parseFile(
    self: SupportsInteractiveProperty[Synchronous],
    filename: Union[PathLike[str], str],
    encoding: Union[str, None] = None,
) -> List[TypeName]:
    ...


@overload
async def parseFile(
    self: SupportsInteractiveProperty[Asynchronous],
    filename: Union[PathLike[str], str],
    encoding: Union[str, None] = None,
) -> List[TypeName]:
    ...


@external("parseFile")
def parseFile(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    filename: Union[PathLike[str], str],
    encoding: Union[str, None] = None,
) -> Union[List[TypeName], Coroutine[None, None, List[TypeName]]]:
    """
    .. code-block:: modelica

        function parseFile
          input String filename;
          input String encoding = "UTF-8";
          output TypeName names[:];
        end parseFile;"""
    return ...  # type: ignore


@overload
def loadFileInteractiveQualified(
    self: SupportsInteractiveProperty[Synchronous],
    filename: Union[PathLike[str], str],
    encoding: Union[str, None] = None,
) -> List[TypeName]:
    ...


@overload
async def loadFileInteractiveQualified(
    self: SupportsInteractiveProperty[Asynchronous],
    filename: Union[PathLike[str], str],
    encoding: Union[str, None] = None,
) -> List[TypeName]:
    ...


@external("loadFileInteractiveQualified")
def loadFileInteractiveQualified(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    filename: Union[PathLike[str], str],
    encoding: Union[str, None] = None,
) -> Union[List[TypeName], Coroutine[None, None, List[TypeName]]]:
    """
    .. code-block:: modelica

        function loadFileInteractiveQualified
          input String filename;
          input String encoding = "UTF-8";
          output TypeName names[:];
        end loadFileInteractiveQualified;"""
    return ...  # type: ignore


@overload
def loadFileInteractive(
    self: SupportsInteractiveProperty[Synchronous],
    filename: Union[PathLike[str], str],
    encoding: Union[str, None] = None,
) -> List[TypeName]:
    ...


@overload
async def loadFileInteractive(
    self: SupportsInteractiveProperty[Asynchronous],
    filename: Union[PathLike[str], str],
    encoding: Union[str, None] = None,
) -> List[TypeName]:
    ...


@external("loadFileInteractive")
def loadFileInteractive(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    filename: Union[PathLike[str], str],
    encoding: Union[str, None] = None,
) -> Union[List[TypeName], Coroutine[None, None, List[TypeName]]]:
    """
    .. code-block:: modelica

        function loadFileInteractive
          input String filename;
          input String encoding = "UTF-8";
          output TypeName names[:];
        end loadFileInteractive;"""
    return ...  # type: ignore


@overload
def system(
    self: SupportsInteractiveProperty[Synchronous],
    callStr: str,
    outputFile: Union[PathLike[str], str, None] = None,
) -> int:
    ...


@overload
async def system(
    self: SupportsInteractiveProperty[Asynchronous],
    callStr: str,
    outputFile: Union[PathLike[str], str, None] = None,
) -> int:
    ...


@external("system")
def system(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    callStr: str,
    outputFile: Union[PathLike[str], str, None] = None,
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        impure function system
          input String callStr "String to call: sh -c $callStr";
          input String outputFile = "" "The output is redirected to this file (unless already done by callStr)";
          output Integer retval "Return value of the system call; usually 0 on success";
        end system;"""
    return ...  # type: ignore


@overload
def system_parallel(
    self: SupportsInteractiveProperty[Synchronous],
    callStr: Sequence[str],
    numThreads: Union[int, None] = None,
) -> List[int]:
    ...


@overload
async def system_parallel(
    self: SupportsInteractiveProperty[Asynchronous],
    callStr: Sequence[str],
    numThreads: Union[int, None] = None,
) -> List[int]:
    ...


@external("system_parallel")
def system_parallel(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    callStr: Sequence[str],
    numThreads: Union[int, None] = None,
) -> Union[List[int], Coroutine[None, None, List[int]]]:
    """
    .. code-block:: modelica

        impure function system_parallel
          input String callStr[:] "String to call: sh -c $callStr";
          input Integer numThreads = numProcessors();
          output Integer retval[:] "Return value of the system call; usually 0 on success";
        end system_parallel;"""
    return ...  # type: ignore


@overload
def saveAll(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
) -> bool:
    ...


@overload
async def saveAll(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
) -> bool:
    ...


@external("saveAll")
def saveAll(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function saveAll
          input String fileName;
          output Boolean success;
        end saveAll;"""
    return ...  # type: ignore


@overload
def help(
    self: SupportsInteractiveProperty[Synchronous],
    topic: Union[str, None] = None,
) -> str:
    ...


@overload
async def help(
    self: SupportsInteractiveProperty[Asynchronous],
    topic: Union[str, None] = None,
) -> str:
    ...


@external("help")
def help(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    topic: Union[str, None] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function help
          input String topic = "topics";
          output String helpText;
        end help;"""
    return ...  # type: ignore


@overload
def clear(self: SupportsInteractiveProperty[Synchronous]) -> bool:
    ...


@overload
async def clear(self: SupportsInteractiveProperty[Asynchronous]) -> bool:
    ...


@external("clear")
def clear(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function clear
          output Boolean success;
        end clear;"""
    return ...  # type: ignore


@overload
def clearProgram(self: SupportsInteractiveProperty[Synchronous]) -> bool:
    ...


@overload
async def clearProgram(
    self: SupportsInteractiveProperty[Asynchronous],
) -> bool:
    ...


@external("clearProgram")
def clearProgram(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function clearProgram
          output Boolean success;
        end clearProgram;"""
    return ...  # type: ignore


@overload
def clearVariables(self: SupportsInteractiveProperty[Synchronous]) -> bool:
    ...


@overload
async def clearVariables(
    self: SupportsInteractiveProperty[Asynchronous],
) -> bool:
    ...


@external("clearVariables")
def clearVariables(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function clearVariables
          output Boolean success;
        end clearVariables;"""
    return ...  # type: ignore


@overload
def generateHeader(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
) -> bool:
    ...


@overload
async def generateHeader(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
) -> bool:
    ...


@external("generateHeader")
def generateHeader(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function generateHeader
          input String fileName;
          output Boolean success;
        end generateHeader;"""
    return ...  # type: ignore


@overload
def generateSeparateCode(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    cleanCache: Union[bool, None] = None,
) -> bool:
    ...


@overload
async def generateSeparateCode(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    cleanCache: Union[bool, None] = None,
) -> bool:
    ...


@external("generateSeparateCode")
def generateSeparateCode(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    cleanCache: Union[bool, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function generateSeparateCode
          input TypeName className;
          input Boolean cleanCache = false "If true, the cache is reset between each generated package. This conserves memory at the cost of speed.";
          output Boolean success;
        end generateSeparateCode;"""
    return ...  # type: ignore


@overload
def generateSeparateCodeDependencies(
    self: SupportsInteractiveProperty[Synchronous],
    stampSuffix: Union[str, None] = None,
) -> List[str]:
    ...


@overload
async def generateSeparateCodeDependencies(
    self: SupportsInteractiveProperty[Asynchronous],
    stampSuffix: Union[str, None] = None,
) -> List[str]:
    ...


@external("generateSeparateCodeDependencies")
def generateSeparateCodeDependencies(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    stampSuffix: Union[str, None] = None,
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function generateSeparateCodeDependencies
          input String stampSuffix = ".c" "Suffix to add to dependencies (often .c.stamp)";
          output String[:] dependencies;
        end generateSeparateCodeDependencies;"""
    return ...  # type: ignore


@overload
def generateSeparateCodeDependenciesMakefile(
    self: SupportsInteractiveProperty[Synchronous],
    filename: Union[PathLike[str], str],
    directory: Union[PathLike[str], str, None] = None,
    suffix: Union[str, None] = None,
) -> bool:
    ...


@overload
async def generateSeparateCodeDependenciesMakefile(
    self: SupportsInteractiveProperty[Asynchronous],
    filename: Union[PathLike[str], str],
    directory: Union[PathLike[str], str, None] = None,
    suffix: Union[str, None] = None,
) -> bool:
    ...


@external("generateSeparateCodeDependenciesMakefile")
def generateSeparateCodeDependenciesMakefile(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    filename: Union[PathLike[str], str],
    directory: Union[PathLike[str], str, None] = None,
    suffix: Union[str, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function generateSeparateCodeDependenciesMakefile
          input String filename "The file to write the makefile to";
          input String directory = "" "The relative path of the generated files";
          input String suffix = ".c" "Often .stamp since we do not update all the files";
          output Boolean success;
        end generateSeparateCodeDependenciesMakefile;"""
    return ...  # type: ignore


@overload
def getLinker(self: SupportsInteractiveProperty[Synchronous]) -> str:
    ...


@overload
async def getLinker(self: SupportsInteractiveProperty[Asynchronous]) -> str:
    ...


@external("getLinker")
def getLinker(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getLinker
          output String linker;
        end getLinker;"""
    return ...  # type: ignore


@overload
def setLinker(
    self: SupportsInteractiveProperty[Synchronous], linker: str
) -> bool:
    ...


@overload
async def setLinker(
    self: SupportsInteractiveProperty[Asynchronous], linker: str
) -> bool:
    ...


@external("setLinker")
def setLinker(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    linker: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setLinker
          input String linker;
          output Boolean success;
        end setLinker;"""
    return ...  # type: ignore


@overload
def getLinkerFlags(self: SupportsInteractiveProperty[Synchronous]) -> str:
    ...


@overload
async def getLinkerFlags(
    self: SupportsInteractiveProperty[Asynchronous],
) -> str:
    ...


@external("getLinkerFlags")
def getLinkerFlags(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getLinkerFlags
          output String linkerFlags;
        end getLinkerFlags;"""
    return ...  # type: ignore


@overload
def setLinkerFlags(
    self: SupportsInteractiveProperty[Synchronous], linkerFlags: str
) -> bool:
    ...


@overload
async def setLinkerFlags(
    self: SupportsInteractiveProperty[Asynchronous], linkerFlags: str
) -> bool:
    ...


@external("setLinkerFlags")
def setLinkerFlags(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    linkerFlags: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setLinkerFlags
          input String linkerFlags;
          output Boolean success;
        end setLinkerFlags;"""
    return ...  # type: ignore


@overload
def getCompiler(self: SupportsInteractiveProperty[Synchronous]) -> str:
    ...


@overload
async def getCompiler(self: SupportsInteractiveProperty[Asynchronous]) -> str:
    ...


@external("getCompiler")
def getCompiler(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getCompiler
          output String compiler;
        end getCompiler;"""
    return ...  # type: ignore


@overload
def setCompiler(
    self: SupportsInteractiveProperty[Synchronous], compiler: str
) -> bool:
    ...


@overload
async def setCompiler(
    self: SupportsInteractiveProperty[Asynchronous], compiler: str
) -> bool:
    ...


@external("setCompiler")
def setCompiler(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    compiler: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setCompiler
          input String compiler;
          output Boolean success;
        end setCompiler;"""
    return ...  # type: ignore


@overload
def setCFlags(
    self: SupportsInteractiveProperty[Synchronous], inString: str
) -> bool:
    ...


@overload
async def setCFlags(
    self: SupportsInteractiveProperty[Asynchronous], inString: str
) -> bool:
    ...


@external("setCFlags")
def setCFlags(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    inString: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setCFlags
          input String inString;
          output Boolean success;
        end setCFlags;"""
    return ...  # type: ignore


@overload
def getCFlags(self: SupportsInteractiveProperty[Synchronous]) -> str:
    ...


@overload
async def getCFlags(self: SupportsInteractiveProperty[Asynchronous]) -> str:
    ...


@external("getCFlags")
def getCFlags(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getCFlags
          output String outString;
        end getCFlags;"""
    return ...  # type: ignore


@overload
def getCXXCompiler(self: SupportsInteractiveProperty[Synchronous]) -> str:
    ...


@overload
async def getCXXCompiler(
    self: SupportsInteractiveProperty[Asynchronous],
) -> str:
    ...


@external("getCXXCompiler")
def getCXXCompiler(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getCXXCompiler
          output String compiler;
        end getCXXCompiler;"""
    return ...  # type: ignore


@overload
def setCXXCompiler(
    self: SupportsInteractiveProperty[Synchronous], compiler: str
) -> bool:
    ...


@overload
async def setCXXCompiler(
    self: SupportsInteractiveProperty[Asynchronous], compiler: str
) -> bool:
    ...


@external("setCXXCompiler")
def setCXXCompiler(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    compiler: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setCXXCompiler
          input String compiler;
          output Boolean success;
        end setCXXCompiler;"""
    return ...  # type: ignore


@overload
def verifyCompiler(self: SupportsInteractiveProperty[Synchronous]) -> bool:
    ...


@overload
async def verifyCompiler(
    self: SupportsInteractiveProperty[Asynchronous],
) -> bool:
    ...


@external("verifyCompiler")
def verifyCompiler(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function verifyCompiler
          output Boolean compilerWorks;
        end verifyCompiler;"""
    return ...  # type: ignore


@overload
def setCompilerPath(
    self: SupportsInteractiveProperty[Synchronous],
    compilerPath: Union[PathLike[str], str],
) -> bool:
    ...


@overload
async def setCompilerPath(
    self: SupportsInteractiveProperty[Asynchronous],
    compilerPath: Union[PathLike[str], str],
) -> bool:
    ...


@external("setCompilerPath")
def setCompilerPath(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    compilerPath: Union[PathLike[str], str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setCompilerPath
          input String compilerPath;
          output Boolean success;
        end setCompilerPath;"""
    return ...  # type: ignore


@overload
def getCompileCommand(self: SupportsInteractiveProperty[Synchronous]) -> str:
    ...


@overload
async def getCompileCommand(
    self: SupportsInteractiveProperty[Asynchronous],
) -> str:
    ...


@external("getCompileCommand")
def getCompileCommand(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getCompileCommand
          output String compileCommand;
        end getCompileCommand;"""
    return ...  # type: ignore


@overload
def setCompileCommand(
    self: SupportsInteractiveProperty[Synchronous], compileCommand: str
) -> bool:
    ...


@overload
async def setCompileCommand(
    self: SupportsInteractiveProperty[Asynchronous], compileCommand: str
) -> bool:
    ...


@external("setCompileCommand")
def setCompileCommand(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    compileCommand: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setCompileCommand
          input String compileCommand;
          output Boolean success;
        end setCompileCommand;"""
    return ...  # type: ignore


@overload
def setPlotCommand(
    self: SupportsInteractiveProperty[Synchronous], plotCommand: str
) -> bool:
    ...


@overload
async def setPlotCommand(
    self: SupportsInteractiveProperty[Asynchronous], plotCommand: str
) -> bool:
    ...


@external("setPlotCommand")
def setPlotCommand(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    plotCommand: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setPlotCommand
          input String plotCommand;
          output Boolean success;
        end setPlotCommand;"""
    return ...  # type: ignore


@overload
def getSettings(self: SupportsInteractiveProperty[Synchronous]) -> str:
    ...


@overload
async def getSettings(self: SupportsInteractiveProperty[Asynchronous]) -> str:
    ...


@external("getSettings")
def getSettings(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getSettings
          output String settings;
        end getSettings;"""
    return ...  # type: ignore


@overload
def setTempDirectoryPath(
    self: SupportsInteractiveProperty[Synchronous],
    tempDirectoryPath: Union[PathLike[str], str],
) -> bool:
    ...


@overload
async def setTempDirectoryPath(
    self: SupportsInteractiveProperty[Asynchronous],
    tempDirectoryPath: Union[PathLike[str], str],
) -> bool:
    ...


@external("setTempDirectoryPath")
def setTempDirectoryPath(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    tempDirectoryPath: Union[PathLike[str], str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setTempDirectoryPath
          input String tempDirectoryPath;
          output Boolean success;
        end setTempDirectoryPath;"""
    return ...  # type: ignore


@overload
def getTempDirectoryPath(
    self: SupportsInteractiveProperty[Synchronous],
) -> str:
    ...


@overload
async def getTempDirectoryPath(
    self: SupportsInteractiveProperty[Asynchronous],
) -> str:
    ...


@external("getTempDirectoryPath")
def getTempDirectoryPath(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getTempDirectoryPath
          output String tempDirectoryPath;
        end getTempDirectoryPath;"""
    return ...  # type: ignore


@overload
def getEnvironmentVar(
    self: SupportsInteractiveProperty[Synchronous], var: str
) -> str:
    ...


@overload
async def getEnvironmentVar(
    self: SupportsInteractiveProperty[Asynchronous], var: str
) -> str:
    ...


@external("getEnvironmentVar")
def getEnvironmentVar(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    var: str,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getEnvironmentVar
          input String var;
          output String value "returns empty string on failure";
        end getEnvironmentVar;"""
    return ...  # type: ignore


@overload
def setEnvironmentVar(
    self: SupportsInteractiveProperty[Synchronous], var: str, value: str
) -> bool:
    ...


@overload
async def setEnvironmentVar(
    self: SupportsInteractiveProperty[Asynchronous], var: str, value: str
) -> bool:
    ...


@external("setEnvironmentVar")
def setEnvironmentVar(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    var: str,
    value: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setEnvironmentVar
          input String var;
          input String value;
          output Boolean success;
        end setEnvironmentVar;"""
    return ...  # type: ignore


@overload
def appendEnvironmentVar(
    self: SupportsInteractiveProperty[Synchronous], var: str, value: str
) -> str:
    ...


@overload
async def appendEnvironmentVar(
    self: SupportsInteractiveProperty[Asynchronous], var: str, value: str
) -> str:
    ...


@external("appendEnvironmentVar")
def appendEnvironmentVar(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    var: str,
    value: str,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function appendEnvironmentVar
          input String var;
          input String value;
          output String result "returns \\"error\\" if the variable could not be appended";
        end appendEnvironmentVar;"""
    return ...  # type: ignore


@overload
def setInstallationDirectoryPath(
    self: SupportsInteractiveProperty[Synchronous],
    installationDirectoryPath: Union[PathLike[str], str],
) -> bool:
    ...


@overload
async def setInstallationDirectoryPath(
    self: SupportsInteractiveProperty[Asynchronous],
    installationDirectoryPath: Union[PathLike[str], str],
) -> bool:
    ...


@external("setInstallationDirectoryPath")
def setInstallationDirectoryPath(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    installationDirectoryPath: Union[PathLike[str], str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setInstallationDirectoryPath
          input String installationDirectoryPath;
          output Boolean success;
        end setInstallationDirectoryPath;"""
    return ...  # type: ignore


@overload
def getInstallationDirectoryPath(
    self: SupportsInteractiveProperty[Synchronous],
) -> str:
    ...


@overload
async def getInstallationDirectoryPath(
    self: SupportsInteractiveProperty[Asynchronous],
) -> str:
    ...


@external("getInstallationDirectoryPath")
def getInstallationDirectoryPath(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getInstallationDirectoryPath
          output String installationDirectoryPath;
        end getInstallationDirectoryPath;"""
    return ...  # type: ignore


@overload
def setModelicaPath(
    self: SupportsInteractiveProperty[Synchronous],
    modelicaPath: Union[PathLike[str], str],
) -> bool:
    ...


@overload
async def setModelicaPath(
    self: SupportsInteractiveProperty[Asynchronous],
    modelicaPath: Union[PathLike[str], str],
) -> bool:
    ...


@external("setModelicaPath")
def setModelicaPath(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    modelicaPath: Union[PathLike[str], str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setModelicaPath
          input String modelicaPath;
          output Boolean success;
        end setModelicaPath;"""
    return ...  # type: ignore


@overload
def getModelicaPath(self: SupportsInteractiveProperty[Synchronous]) -> str:
    ...


@overload
async def getModelicaPath(
    self: SupportsInteractiveProperty[Asynchronous],
) -> str:
    ...


@external("getModelicaPath")
def getModelicaPath(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getModelicaPath
          output String modelicaPath;
        end getModelicaPath;"""
    return ...  # type: ignore


@overload
def setCompilerFlags(
    self: SupportsInteractiveProperty[Synchronous], compilerFlags: str
) -> bool:
    ...


@overload
async def setCompilerFlags(
    self: SupportsInteractiveProperty[Asynchronous], compilerFlags: str
) -> bool:
    ...


@external("setCompilerFlags")
def setCompilerFlags(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    compilerFlags: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setCompilerFlags
          input String compilerFlags;
          output Boolean success;
        end setCompilerFlags;"""
    return ...  # type: ignore


@overload
def setDebugFlags(
    self: SupportsInteractiveProperty[Synchronous], debugFlags: str
) -> bool:
    ...


@overload
async def setDebugFlags(
    self: SupportsInteractiveProperty[Asynchronous], debugFlags: str
) -> bool:
    ...


@external("setDebugFlags")
def setDebugFlags(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    debugFlags: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setDebugFlags
          input String debugFlags;
          output Boolean success;
        end setDebugFlags;"""
    return ...  # type: ignore


@overload
def clearDebugFlags(self: SupportsInteractiveProperty[Synchronous]) -> bool:
    ...


@overload
async def clearDebugFlags(
    self: SupportsInteractiveProperty[Asynchronous],
) -> bool:
    ...


@external("clearDebugFlags")
def clearDebugFlags(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function clearDebugFlags
          output Boolean success;
        end clearDebugFlags;"""
    return ...  # type: ignore


@overload
def setPreOptModules(
    self: SupportsInteractiveProperty[Synchronous], modules: str
) -> bool:
    ...


@overload
async def setPreOptModules(
    self: SupportsInteractiveProperty[Asynchronous], modules: str
) -> bool:
    ...


@external("setPreOptModules")
def setPreOptModules(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    modules: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setPreOptModules
          input String modules;
          output Boolean success;
        end setPreOptModules;"""
    return ...  # type: ignore


@overload
def setCheapMatchingAlgorithm(
    self: SupportsInteractiveProperty[Synchronous], matchingAlgorithm: int
) -> bool:
    ...


@overload
async def setCheapMatchingAlgorithm(
    self: SupportsInteractiveProperty[Asynchronous], matchingAlgorithm: int
) -> bool:
    ...


@external("setCheapMatchingAlgorithm")
def setCheapMatchingAlgorithm(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    matchingAlgorithm: int,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setCheapMatchingAlgorithm
          input Integer matchingAlgorithm;
          output Boolean success;
        end setCheapMatchingAlgorithm;"""
    return ...  # type: ignore


@overload
def getMatchingAlgorithm(
    self: SupportsInteractiveProperty[Synchronous],
) -> str:
    ...


@overload
async def getMatchingAlgorithm(
    self: SupportsInteractiveProperty[Asynchronous],
) -> str:
    ...


@external("getMatchingAlgorithm")
def getMatchingAlgorithm(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getMatchingAlgorithm
          output String selected;
        end getMatchingAlgorithm;"""
    return ...  # type: ignore


class Getavailablematchingalgorithms(NamedTuple):
    allChoices: List[str]
    allComments: List[str]


@overload
def getAvailableMatchingAlgorithms(
    self: SupportsInteractiveProperty[Synchronous],
) -> Getavailablematchingalgorithms:
    ...


@overload
async def getAvailableMatchingAlgorithms(
    self: SupportsInteractiveProperty[Asynchronous],
) -> Getavailablematchingalgorithms:
    ...


@external("getAvailableMatchingAlgorithms")
def getAvailableMatchingAlgorithms(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[
    Getavailablematchingalgorithms,
    Coroutine[None, None, Getavailablematchingalgorithms],
]:
    """
    .. code-block:: modelica

        function getAvailableMatchingAlgorithms
          output String[:] allChoices;
          output String[:] allComments;
        end getAvailableMatchingAlgorithms;"""
    return ...  # type: ignore


@overload
def setMatchingAlgorithm(
    self: SupportsInteractiveProperty[Synchronous], matchingAlgorithm: str
) -> bool:
    ...


@overload
async def setMatchingAlgorithm(
    self: SupportsInteractiveProperty[Asynchronous], matchingAlgorithm: str
) -> bool:
    ...


@external("setMatchingAlgorithm")
def setMatchingAlgorithm(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    matchingAlgorithm: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setMatchingAlgorithm
          input String matchingAlgorithm;
          output Boolean success;
        end setMatchingAlgorithm;"""
    return ...  # type: ignore


@overload
def getIndexReductionMethod(
    self: SupportsInteractiveProperty[Synchronous],
) -> str:
    ...


@overload
async def getIndexReductionMethod(
    self: SupportsInteractiveProperty[Asynchronous],
) -> str:
    ...


@external("getIndexReductionMethod")
def getIndexReductionMethod(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getIndexReductionMethod
          output String selected;
        end getIndexReductionMethod;"""
    return ...  # type: ignore


class Getavailableindexreductionmethods(NamedTuple):
    allChoices: List[str]
    allComments: List[str]


@overload
def getAvailableIndexReductionMethods(
    self: SupportsInteractiveProperty[Synchronous],
) -> Getavailableindexreductionmethods:
    ...


@overload
async def getAvailableIndexReductionMethods(
    self: SupportsInteractiveProperty[Asynchronous],
) -> Getavailableindexreductionmethods:
    ...


@external("getAvailableIndexReductionMethods")
def getAvailableIndexReductionMethods(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[
    Getavailableindexreductionmethods,
    Coroutine[None, None, Getavailableindexreductionmethods],
]:
    """
    .. code-block:: modelica

        function getAvailableIndexReductionMethods
          output String[:] allChoices;
          output String[:] allComments;
        end getAvailableIndexReductionMethods;"""
    return ...  # type: ignore


@overload
def setIndexReductionMethod(
    self: SupportsInteractiveProperty[Synchronous], method: str
) -> bool:
    ...


@overload
async def setIndexReductionMethod(
    self: SupportsInteractiveProperty[Asynchronous], method: str
) -> bool:
    ...


@external("setIndexReductionMethod")
def setIndexReductionMethod(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    method: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setIndexReductionMethod
          input String method;
          output Boolean success;
        end setIndexReductionMethod;"""
    return ...  # type: ignore


@overload
def setPostOptModules(
    self: SupportsInteractiveProperty[Synchronous], modules: str
) -> bool:
    ...


@overload
async def setPostOptModules(
    self: SupportsInteractiveProperty[Asynchronous], modules: str
) -> bool:
    ...


@external("setPostOptModules")
def setPostOptModules(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    modules: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setPostOptModules
          input String modules;
          output Boolean success;
        end setPostOptModules;"""
    return ...  # type: ignore


@overload
def getTearingMethod(self: SupportsInteractiveProperty[Synchronous]) -> str:
    ...


@overload
async def getTearingMethod(
    self: SupportsInteractiveProperty[Asynchronous],
) -> str:
    ...


@external("getTearingMethod")
def getTearingMethod(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getTearingMethod
          output String selected;
        end getTearingMethod;"""
    return ...  # type: ignore


class Getavailabletearingmethods(NamedTuple):
    allChoices: List[str]
    allComments: List[str]


@overload
def getAvailableTearingMethods(
    self: SupportsInteractiveProperty[Synchronous],
) -> Getavailabletearingmethods:
    ...


@overload
async def getAvailableTearingMethods(
    self: SupportsInteractiveProperty[Asynchronous],
) -> Getavailabletearingmethods:
    ...


@external("getAvailableTearingMethods")
def getAvailableTearingMethods(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[
    Getavailabletearingmethods,
    Coroutine[None, None, Getavailabletearingmethods],
]:
    """
    .. code-block:: modelica

        function getAvailableTearingMethods
          output String[:] allChoices;
          output String[:] allComments;
        end getAvailableTearingMethods;"""
    return ...  # type: ignore


@overload
def setTearingMethod(
    self: SupportsInteractiveProperty[Synchronous], tearingMethod: str
) -> bool:
    ...


@overload
async def setTearingMethod(
    self: SupportsInteractiveProperty[Asynchronous], tearingMethod: str
) -> bool:
    ...


@external("setTearingMethod")
def setTearingMethod(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    tearingMethod: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setTearingMethod
          input String tearingMethod;
          output Boolean success;
        end setTearingMethod;"""
    return ...  # type: ignore


@overload
def setCommandLineOptions(
    self: SupportsInteractiveProperty[Synchronous], option: str
) -> bool:
    ...


@overload
async def setCommandLineOptions(
    self: SupportsInteractiveProperty[Asynchronous], option: str
) -> bool:
    ...


@external("setCommandLineOptions")
def setCommandLineOptions(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    option: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setCommandLineOptions
          input String option;
          output Boolean success;
        end setCommandLineOptions;"""
    return ...  # type: ignore


@overload
def getCommandLineOptions(
    self: SupportsInteractiveProperty[Synchronous],
) -> List[str]:
    ...


@overload
async def getCommandLineOptions(
    self: SupportsInteractiveProperty[Asynchronous],
) -> List[str]:
    ...


@external("getCommandLineOptions")
def getCommandLineOptions(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function getCommandLineOptions
          output String[:] flags;
        end getCommandLineOptions;"""
    return ...  # type: ignore


class Getconfigflagvalidoptions(NamedTuple):
    validOptions: List[str]
    mainDescription: str
    descriptions: List[str]


@overload
def getConfigFlagValidOptions(
    self: SupportsInteractiveProperty[Synchronous], flag: str
) -> Getconfigflagvalidoptions:
    ...


@overload
async def getConfigFlagValidOptions(
    self: SupportsInteractiveProperty[Asynchronous], flag: str
) -> Getconfigflagvalidoptions:
    ...


@external("getConfigFlagValidOptions")
def getConfigFlagValidOptions(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    flag: str,
) -> Union[
    Getconfigflagvalidoptions, Coroutine[None, None, Getconfigflagvalidoptions]
]:
    """
    .. code-block:: modelica

        function getConfigFlagValidOptions
          input String flag;
          output String validOptions[:];
          output String mainDescription;
          output String descriptions[:];
        end getConfigFlagValidOptions;"""
    return ...  # type: ignore


@overload
def clearCommandLineOptions(
    self: SupportsInteractiveProperty[Synchronous],
) -> bool:
    ...


@overload
async def clearCommandLineOptions(
    self: SupportsInteractiveProperty[Asynchronous],
) -> bool:
    ...


@external("clearCommandLineOptions")
def clearCommandLineOptions(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function clearCommandLineOptions
          output Boolean success;
        end clearCommandLineOptions;"""
    return ...  # type: ignore


@overload
def getVersion(
    self: SupportsInteractiveProperty[Synchronous],
    cl: Union[TypeName, str, None] = None,
) -> str:
    ...


@overload
async def getVersion(
    self: SupportsInteractiveProperty[Asynchronous],
    cl: Union[TypeName, str, None] = None,
) -> str:
    ...


@external("getVersion")
def getVersion(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str, None] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getVersion
          input TypeName cl = $Code(OpenModelica);
          output String version;
        end getVersion;"""
    return ...  # type: ignore


@overload
def regularFileExists(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
) -> bool:
    ...


@overload
async def regularFileExists(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
) -> bool:
    ...


@external("regularFileExists")
def regularFileExists(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function regularFileExists
          input String fileName;
          output Boolean exists;
        end regularFileExists;"""
    return ...  # type: ignore


@overload
def directoryExists(
    self: SupportsInteractiveProperty[Synchronous],
    dirName: Union[PathLike[str], str],
) -> bool:
    ...


@overload
async def directoryExists(
    self: SupportsInteractiveProperty[Asynchronous],
    dirName: Union[PathLike[str], str],
) -> bool:
    ...


@external("directoryExists")
def directoryExists(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    dirName: Union[PathLike[str], str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function directoryExists
          input String dirName;
          output Boolean exists;
        end directoryExists;"""
    return ...  # type: ignore


class Stat(NamedTuple):
    success: bool
    fileSize: float
    mtime: float


@overload
def stat(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
) -> Stat:
    ...


@overload
async def stat(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
) -> Stat:
    ...


@external("stat")
def stat(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
) -> Union[Stat, Coroutine[None, None, Stat]]:
    """
    .. code-block:: modelica

        impure function stat
          input String fileName;
          output Boolean success;
          output Real fileSize;
          output Real mtime;
        end stat;"""
    return ...  # type: ignore


@overload
def readFile(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
) -> str:
    ...


@overload
async def readFile(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
) -> str:
    ...


@external("readFile")
def readFile(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        impure function readFile
          input String fileName;
          output String contents;
        end readFile;"""
    return ...  # type: ignore


@overload
def writeFile(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
    data: str,
    append: Union[bool, None] = None,
) -> bool:
    ...


@overload
async def writeFile(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
    data: str,
    append: Union[bool, None] = None,
) -> bool:
    ...


@external("writeFile")
def writeFile(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
    data: str,
    append: Union[bool, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        impure function writeFile
          input String fileName;
          input String data;
          input Boolean append = false;
          output Boolean success;
        end writeFile;"""
    return ...  # type: ignore


@overload
def compareFilesAndMove(
    self: SupportsInteractiveProperty[Synchronous],
    newFile: Union[PathLike[str], str],
    oldFile: Union[PathLike[str], str],
) -> bool:
    ...


@overload
async def compareFilesAndMove(
    self: SupportsInteractiveProperty[Asynchronous],
    newFile: Union[PathLike[str], str],
    oldFile: Union[PathLike[str], str],
) -> bool:
    ...


@external("compareFilesAndMove")
def compareFilesAndMove(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    newFile: Union[PathLike[str], str],
    oldFile: Union[PathLike[str], str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        impure function compareFilesAndMove
          input String newFile;
          input String oldFile;
          output Boolean success;
        end compareFilesAndMove;"""
    return ...  # type: ignore


@overload
def compareFiles(
    self: SupportsInteractiveProperty[Synchronous],
    file1: Union[PathLike[str], str],
    file2: Union[PathLike[str], str],
) -> bool:
    ...


@overload
async def compareFiles(
    self: SupportsInteractiveProperty[Asynchronous],
    file1: Union[PathLike[str], str],
    file2: Union[PathLike[str], str],
) -> bool:
    ...


@external("compareFiles")
def compareFiles(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    file1: Union[PathLike[str], str],
    file2: Union[PathLike[str], str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        impure function compareFiles
          input String file1;
          input String file2;
          output Boolean isEqual;
        end compareFiles;"""
    return ...  # type: ignore


@overload
def alarm(self: SupportsInteractiveProperty[Synchronous], seconds: int) -> int:
    ...


@overload
async def alarm(
    self: SupportsInteractiveProperty[Asynchronous], seconds: int
) -> int:
    ...


@external("alarm")
def alarm(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    seconds: int,
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        impure function alarm
          input Integer seconds;
          output Integer previousSeconds;
        end alarm;"""
    return ...  # type: ignore


class Regex(NamedTuple):
    numMatches: int
    matchedSubstrings: List[str]


@overload
def regex(
    self: SupportsInteractiveProperty[Synchronous],
    str: str,
    re: str,
    maxMatches: Union[int, None] = None,
    extended: Union[bool, None] = None,
    caseInsensitive: Union[bool, None] = None,
) -> Regex:
    ...


@overload
async def regex(
    self: SupportsInteractiveProperty[Asynchronous],
    str: str,
    re: str,
    maxMatches: Union[int, None] = None,
    extended: Union[bool, None] = None,
    caseInsensitive: Union[bool, None] = None,
) -> Regex:
    ...


@external("regex")
def regex(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    str: str,
    re: str,
    maxMatches: Union[int, None] = None,
    extended: Union[bool, None] = None,
    caseInsensitive: Union[bool, None] = None,
) -> Union[Regex, Coroutine[None, None, Regex]]:
    """
    .. code-block:: modelica

        function regex
          input String str;
          input String re;
          input Integer maxMatches = 1 "The maximum number of matches that will be returned";
          input Boolean extended = true "Use POSIX extended or regular syntax";
          input Boolean caseInsensitive = false;
          output Integer numMatches "-1 is an error, 0 means no match, else returns a number 1..maxMatches";
          output String matchedSubstrings[maxMatches] "unmatched strings are returned as empty";
        end regex;"""
    return ...  # type: ignore


@overload
def regexBool(
    self: SupportsInteractiveProperty[Synchronous],
    str: str,
    re: str,
    extended: Union[bool, None] = None,
    caseInsensitive: Union[bool, None] = None,
) -> bool:
    ...


@overload
async def regexBool(
    self: SupportsInteractiveProperty[Asynchronous],
    str: str,
    re: str,
    extended: Union[bool, None] = None,
    caseInsensitive: Union[bool, None] = None,
) -> bool:
    ...


@external("regexBool")
def regexBool(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    str: str,
    re: str,
    extended: Union[bool, None] = None,
    caseInsensitive: Union[bool, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function regexBool
          input String str;
          input String re;
          input Boolean extended = true "Use POSIX extended or regular syntax";
          input Boolean caseInsensitive = false;
          output Boolean matches;
        end regexBool;"""
    return ...  # type: ignore


@overload
def testsuiteFriendlyName(
    self: SupportsInteractiveProperty[Synchronous],
    path: Union[PathLike[str], str],
) -> str:
    ...


@overload
async def testsuiteFriendlyName(
    self: SupportsInteractiveProperty[Asynchronous],
    path: Union[PathLike[str], str],
) -> str:
    ...


@external("testsuiteFriendlyName")
def testsuiteFriendlyName(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    path: Union[PathLike[str], str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function testsuiteFriendlyName
          input String path;
          output String fixed;
        end testsuiteFriendlyName;"""
    return ...  # type: ignore


@overload
def readFileNoNumeric(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
) -> str:
    ...


@overload
async def readFileNoNumeric(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
) -> str:
    ...


@external("readFileNoNumeric")
def readFileNoNumeric(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function readFileNoNumeric
          input String fileName;
          output String contents;
        end readFileNoNumeric;"""
    return ...  # type: ignore


@overload
def getErrorString(
    self: SupportsInteractiveProperty[Synchronous],
    warningsAsErrors: Union[bool, None] = None,
) -> str:
    ...


@overload
async def getErrorString(
    self: SupportsInteractiveProperty[Asynchronous],
    warningsAsErrors: Union[bool, None] = None,
) -> str:
    ...


@external("getErrorString")
def getErrorString(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    warningsAsErrors: Union[bool, None] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        impure function getErrorString
          input Boolean warningsAsErrors = false;
          output String errorString;
        end getErrorString;"""
    return ...  # type: ignore


@overload
def getMessagesString(self: SupportsInteractiveProperty[Synchronous]) -> str:
    ...


@overload
async def getMessagesString(
    self: SupportsInteractiveProperty[Asynchronous],
) -> str:
    ...


@external("getMessagesString")
def getMessagesString(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getMessagesString
          output String messagesString;
        end getMessagesString;"""
    return ...  # type: ignore


@dataclass(frozen=True)
class SourceInfo(record):
    """
    .. code-block:: modelica

        record SourceInfo
          String fileName;
          Boolean readonly;
          Integer lineStart;
          Integer columnStart;
          Integer lineEnd;
          Integer columnEnd;
          annotation(
            preferredView = "text");
        end SourceInfo;"""

    __omc_class__ = TypeName("OpenModelica.Scripting.SourceInfo")
    fileName: str
    readonly: bool
    lineStart: int
    columnStart: int
    lineEnd: int
    columnEnd: int


class ErrorKind(enumeration):
    """
    .. code-block:: modelica

        type ErrorKind = enumeration(syntax "syntax errors", grammar "grammatical errors", translation "instantiation errors: up to flat modelica", symbolic "symbolic manipulation error, simcodegen, up to executable file", runtime "simulation/function runtime error", scripting "runtime scripting /interpretation error");
    """

    __omc_class__ = TypeName("OpenModelica.Scripting.ErrorKind")
    syntax = 1
    "syntax errors"
    grammar = 2
    "grammatical errors"
    translation = 3
    "instantiation errors: up to flat modelica"
    symbolic = 4
    "symbolic manipulation error, simcodegen, up to executable file"
    runtime = 5
    "simulation/function runtime error"
    scripting = 6
    "runtime scripting /interpretation error"


class ErrorLevel(enumeration):
    """
    .. code-block:: modelica

        type ErrorLevel = enumeration(notification, warning, error);"""

    __omc_class__ = TypeName("OpenModelica.Scripting.ErrorLevel")
    notification = 1
    warning = 2
    error = 3


@dataclass(frozen=True)
class ErrorMessage(record):
    """
    .. code-block:: modelica

        record ErrorMessage
          SourceInfo info;
          String message "After applying the individual arguments";
          ErrorKind kind;
          ErrorLevel level;
          Integer id "Internal ID of the error (just ignore this)";
          annotation(
            preferredView = "text");
        end ErrorMessage;"""

    __omc_class__ = TypeName("OpenModelica.Scripting.ErrorMessage")
    info: SourceInfo
    message: str
    kind: ErrorKind
    level: ErrorLevel
    id: int


@overload
def getMessagesStringInternal(
    self: SupportsInteractiveProperty[Synchronous],
    unique: Union[bool, None] = None,
) -> List[ErrorMessage]:
    ...


@overload
async def getMessagesStringInternal(
    self: SupportsInteractiveProperty[Asynchronous],
    unique: Union[bool, None] = None,
) -> List[ErrorMessage]:
    ...


@external("getMessagesStringInternal")
def getMessagesStringInternal(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    unique: Union[bool, None] = None,
) -> Union[List[ErrorMessage], Coroutine[None, None, List[ErrorMessage]]]:
    """
    .. code-block:: modelica

        function getMessagesStringInternal
          input Boolean unique = true;
          output ErrorMessage[:] messagesString;
        end getMessagesStringInternal;"""
    return ...  # type: ignore


class Countmessages(NamedTuple):
    numMessages: int
    numErrors: int
    numWarnings: int


@overload
def countMessages(
    self: SupportsInteractiveProperty[Synchronous],
) -> Countmessages:
    ...


@overload
async def countMessages(
    self: SupportsInteractiveProperty[Asynchronous],
) -> Countmessages:
    ...


@external("countMessages")
def countMessages(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[Countmessages, Coroutine[None, None, Countmessages]]:
    """
    .. code-block:: modelica

        function countMessages
          output Integer numMessages;
          output Integer numErrors;
          output Integer numWarnings;
        end countMessages;"""
    return ...  # type: ignore


@overload
def clearMessages(self: SupportsInteractiveProperty[Synchronous]) -> bool:
    ...


@overload
async def clearMessages(
    self: SupportsInteractiveProperty[Asynchronous],
) -> bool:
    ...


@external("clearMessages")
def clearMessages(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function clearMessages
          output Boolean success;
        end clearMessages;"""
    return ...  # type: ignore


@overload
def runScript(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
) -> str:
    ...


@overload
async def runScript(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
) -> str:
    ...


@external("runScript")
def runScript(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        impure function runScript
          input String fileName "*.mos";
          output String result;
        end runScript;"""
    return ...  # type: ignore


@overload
def echo(
    self: SupportsInteractiveProperty[Synchronous], setEcho: bool
) -> bool:
    ...


@overload
async def echo(
    self: SupportsInteractiveProperty[Asynchronous], setEcho: bool
) -> bool:
    ...


@external("echo")
def echo(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    setEcho: bool,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function echo
          input Boolean setEcho;
          output Boolean newEcho;
        end echo;"""
    return ...  # type: ignore


@overload
def getClassesInModelicaPath(
    self: SupportsInteractiveProperty[Synchronous],
) -> str:
    ...


@overload
async def getClassesInModelicaPath(
    self: SupportsInteractiveProperty[Asynchronous],
) -> str:
    ...


@external("getClassesInModelicaPath")
def getClassesInModelicaPath(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getClassesInModelicaPath
          output String classesInModelicaPath;
        end getClassesInModelicaPath;"""
    return ...  # type: ignore


@overload
def getAnnotationVersion(
    self: SupportsInteractiveProperty[Synchronous],
) -> str:
    ...


@overload
async def getAnnotationVersion(
    self: SupportsInteractiveProperty[Asynchronous],
) -> str:
    ...


@external("getAnnotationVersion")
def getAnnotationVersion(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getAnnotationVersion
          output String annotationVersion;
        end getAnnotationVersion;"""
    return ...  # type: ignore


@overload
def setAnnotationVersion(
    self: SupportsInteractiveProperty[Synchronous], annotationVersion: str
) -> bool:
    ...


@overload
async def setAnnotationVersion(
    self: SupportsInteractiveProperty[Asynchronous], annotationVersion: str
) -> bool:
    ...


@external("setAnnotationVersion")
def setAnnotationVersion(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    annotationVersion: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setAnnotationVersion
          input String annotationVersion;
          output Boolean success;
        end setAnnotationVersion;"""
    return ...  # type: ignore


@overload
def getNoSimplify(self: SupportsInteractiveProperty[Synchronous]) -> bool:
    ...


@overload
async def getNoSimplify(
    self: SupportsInteractiveProperty[Asynchronous],
) -> bool:
    ...


@external("getNoSimplify")
def getNoSimplify(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function getNoSimplify
          output Boolean noSimplify;
        end getNoSimplify;"""
    return ...  # type: ignore


@overload
def setNoSimplify(
    self: SupportsInteractiveProperty[Synchronous], noSimplify: bool
) -> bool:
    ...


@overload
async def setNoSimplify(
    self: SupportsInteractiveProperty[Asynchronous], noSimplify: bool
) -> bool:
    ...


@external("setNoSimplify")
def setNoSimplify(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    noSimplify: bool,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setNoSimplify
          input Boolean noSimplify;
          output Boolean success;
        end setNoSimplify;"""
    return ...  # type: ignore


@overload
def getVectorizationLimit(
    self: SupportsInteractiveProperty[Synchronous],
) -> int:
    ...


@overload
async def getVectorizationLimit(
    self: SupportsInteractiveProperty[Asynchronous],
) -> int:
    ...


@external("getVectorizationLimit")
def getVectorizationLimit(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function getVectorizationLimit
          output Integer vectorizationLimit;
        end getVectorizationLimit;"""
    return ...  # type: ignore


@overload
def setVectorizationLimit(
    self: SupportsInteractiveProperty[Synchronous], vectorizationLimit: int
) -> bool:
    ...


@overload
async def setVectorizationLimit(
    self: SupportsInteractiveProperty[Asynchronous], vectorizationLimit: int
) -> bool:
    ...


@external("setVectorizationLimit")
def setVectorizationLimit(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    vectorizationLimit: int,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setVectorizationLimit
          input Integer vectorizationLimit;
          output Boolean success;
        end setVectorizationLimit;"""
    return ...  # type: ignore


@overload
def getDefaultOpenCLDevice(
    self: SupportsInteractiveProperty[Synchronous],
) -> int:
    ...


@overload
async def getDefaultOpenCLDevice(
    self: SupportsInteractiveProperty[Asynchronous],
) -> int:
    ...


@external("getDefaultOpenCLDevice")
def getDefaultOpenCLDevice(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function getDefaultOpenCLDevice
          output Integer defdevid;
        end getDefaultOpenCLDevice;"""
    return ...  # type: ignore


@overload
def setDefaultOpenCLDevice(
    self: SupportsInteractiveProperty[Synchronous], defdevid: int
) -> bool:
    ...


@overload
async def setDefaultOpenCLDevice(
    self: SupportsInteractiveProperty[Asynchronous], defdevid: int
) -> bool:
    ...


@external("setDefaultOpenCLDevice")
def setDefaultOpenCLDevice(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    defdevid: int,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setDefaultOpenCLDevice
          input Integer defdevid;
          output Boolean success;
        end setDefaultOpenCLDevice;"""
    return ...  # type: ignore


@overload
def setShowAnnotations(
    self: SupportsInteractiveProperty[Synchronous], show: bool
) -> bool:
    ...


@overload
async def setShowAnnotations(
    self: SupportsInteractiveProperty[Asynchronous], show: bool
) -> bool:
    ...


@external("setShowAnnotations")
def setShowAnnotations(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    show: bool,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setShowAnnotations
          input Boolean show;
          output Boolean success;
        end setShowAnnotations;"""
    return ...  # type: ignore


@overload
def getShowAnnotations(self: SupportsInteractiveProperty[Synchronous]) -> bool:
    ...


@overload
async def getShowAnnotations(
    self: SupportsInteractiveProperty[Asynchronous],
) -> bool:
    ...


@external("getShowAnnotations")
def getShowAnnotations(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function getShowAnnotations
          output Boolean show;
        end getShowAnnotations;"""
    return ...  # type: ignore


@overload
def setOrderConnections(
    self: SupportsInteractiveProperty[Synchronous], orderConnections: bool
) -> bool:
    ...


@overload
async def setOrderConnections(
    self: SupportsInteractiveProperty[Asynchronous], orderConnections: bool
) -> bool:
    ...


@external("setOrderConnections")
def setOrderConnections(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    orderConnections: bool,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setOrderConnections
          input Boolean orderConnections;
          output Boolean success;
        end setOrderConnections;"""
    return ...  # type: ignore


@overload
def getOrderConnections(
    self: SupportsInteractiveProperty[Synchronous],
) -> bool:
    ...


@overload
async def getOrderConnections(
    self: SupportsInteractiveProperty[Asynchronous],
) -> bool:
    ...


@external("getOrderConnections")
def getOrderConnections(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function getOrderConnections
          output Boolean orderConnections;
        end getOrderConnections;"""
    return ...  # type: ignore


@overload
def setLanguageStandard(
    self: SupportsInteractiveProperty[Synchronous], inVersion: str
) -> bool:
    ...


@overload
async def setLanguageStandard(
    self: SupportsInteractiveProperty[Asynchronous], inVersion: str
) -> bool:
    ...


@external("setLanguageStandard")
def setLanguageStandard(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    inVersion: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setLanguageStandard
          input String inVersion;
          output Boolean success;
        end setLanguageStandard;"""
    return ...  # type: ignore


@overload
def getLanguageStandard(self: SupportsInteractiveProperty[Synchronous]) -> str:
    ...


@overload
async def getLanguageStandard(
    self: SupportsInteractiveProperty[Asynchronous],
) -> str:
    ...


@external("getLanguageStandard")
def getLanguageStandard(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getLanguageStandard
          output String outVersion;
        end getLanguageStandard;"""
    return ...  # type: ignore


@overload
def getAstAsCorbaString(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str, None] = None,
) -> str:
    ...


@overload
async def getAstAsCorbaString(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str, None] = None,
) -> str:
    ...


@external("getAstAsCorbaString")
def getAstAsCorbaString(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str, None] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getAstAsCorbaString
          input String fileName = "<interactive>";
          output String result "returns the string if fileName is interactive; else it returns ok or error depending on if writing the file succeeded";
        end getAstAsCorbaString;"""
    return ...  # type: ignore


@overload
def cd(
    self: SupportsInteractiveProperty[Synchronous],
    newWorkingDirectory: Union[PathLike[str], str, None] = None,
) -> str:
    ...


@overload
async def cd(
    self: SupportsInteractiveProperty[Asynchronous],
    newWorkingDirectory: Union[PathLike[str], str, None] = None,
) -> str:
    ...


@external("cd")
def cd(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    newWorkingDirectory: Union[PathLike[str], str, None] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function cd
          input String newWorkingDirectory = "";
          output String workingDirectory;
        end cd;"""
    return ...  # type: ignore


@overload
def mkdir(
    self: SupportsInteractiveProperty[Synchronous],
    newDirectory: Union[PathLike[str], str],
) -> bool:
    ...


@overload
async def mkdir(
    self: SupportsInteractiveProperty[Asynchronous],
    newDirectory: Union[PathLike[str], str],
) -> bool:
    ...


@external("mkdir")
def mkdir(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    newDirectory: Union[PathLike[str], str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function mkdir
          input String newDirectory;
          output Boolean success;
        end mkdir;"""
    return ...  # type: ignore


@overload
def copy(
    self: SupportsInteractiveProperty[Synchronous],
    source: str,
    destination: str,
) -> bool:
    ...


@overload
async def copy(
    self: SupportsInteractiveProperty[Asynchronous],
    source: str,
    destination: str,
) -> bool:
    ...


@external("copy")
def copy(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    source: str,
    destination: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function copy
          input String source;
          input String destination;
          output Boolean success;
        end copy;"""
    return ...  # type: ignore


@overload
def remove(
    self: SupportsInteractiveProperty[Synchronous],
    path: Union[PathLike[str], str],
) -> bool:
    ...


@overload
async def remove(
    self: SupportsInteractiveProperty[Asynchronous],
    path: Union[PathLike[str], str],
) -> bool:
    ...


@external("remove")
def remove(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    path: Union[PathLike[str], str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function remove
          input String path;
          output Boolean success "Returns true on success.";
        end remove;"""
    return ...  # type: ignore


@overload
def checkModel(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
) -> str:
    ...


@overload
async def checkModel(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
) -> str:
    ...


@external("checkModel")
def checkModel(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function checkModel
          input TypeName className;
          output String result;
        end checkModel;"""
    return ...  # type: ignore


@overload
def checkAllModelsRecursive(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    checkProtected: Union[bool, None] = None,
) -> str:
    ...


@overload
async def checkAllModelsRecursive(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    checkProtected: Union[bool, None] = None,
) -> str:
    ...


@external("checkAllModelsRecursive")
def checkAllModelsRecursive(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    checkProtected: Union[bool, None] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function checkAllModelsRecursive
          input TypeName className;
          input Boolean checkProtected = false "Checks also protected classes if true";
          output String result;
        end checkAllModelsRecursive;"""
    return ...  # type: ignore


@overload
def typeOf(
    self: SupportsInteractiveProperty[Synchronous],
    variableName: Union[VariableName, str],
) -> str:
    ...


@overload
async def typeOf(
    self: SupportsInteractiveProperty[Asynchronous],
    variableName: Union[VariableName, str],
) -> str:
    ...


@external("typeOf")
def typeOf(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    variableName: Union[VariableName, str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function typeOf
          input VariableName variableName;
          output String result;
        end typeOf;"""
    return ...  # type: ignore


@overload
def instantiateModel(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
) -> str:
    ...


@overload
async def instantiateModel(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
) -> str:
    ...


@external("instantiateModel")
def instantiateModel(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function instantiateModel
          input TypeName className;
          output String result;
        end instantiateModel;"""
    return ...  # type: ignore


@overload
def buildOpenTURNSInterface(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    pythonTemplateFile: Union[PathLike[str], str],
    showFlatModelica: Union[bool, None] = None,
) -> str:
    ...


@overload
async def buildOpenTURNSInterface(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    pythonTemplateFile: Union[PathLike[str], str],
    showFlatModelica: Union[bool, None] = None,
) -> str:
    ...


@external("buildOpenTURNSInterface")
def buildOpenTURNSInterface(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    pythonTemplateFile: Union[PathLike[str], str],
    showFlatModelica: Union[bool, None] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function buildOpenTURNSInterface
          input TypeName className;
          input String pythonTemplateFile;
          input Boolean showFlatModelica = false;
          output String outPythonScript;
        end buildOpenTURNSInterface;"""
    return ...  # type: ignore


@overload
def runOpenTURNSPythonScript(
    self: SupportsInteractiveProperty[Synchronous],
    pythonScriptFile: Union[PathLike[str], str],
) -> str:
    ...


@overload
async def runOpenTURNSPythonScript(
    self: SupportsInteractiveProperty[Asynchronous],
    pythonScriptFile: Union[PathLike[str], str],
) -> str:
    ...


@external("runOpenTURNSPythonScript")
def runOpenTURNSPythonScript(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    pythonScriptFile: Union[PathLike[str], str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function runOpenTURNSPythonScript
          input String pythonScriptFile;
          output String logOutputFile;
        end runOpenTURNSPythonScript;"""
    return ...  # type: ignore


@overload
def generateCode(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
) -> bool:
    ...


@overload
async def generateCode(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
) -> bool:
    ...


@external("generateCode")
def generateCode(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function generateCode
          input TypeName className;
          output Boolean success;
        end generateCode;"""
    return ...  # type: ignore


@overload
def loadModel(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    priorityVersion: Union[Sequence[str], None] = None,
    notify: Union[bool, None] = None,
    languageStandard: Union[str, None] = None,
    requireExactVersion: Union[bool, None] = None,
) -> bool:
    ...


@overload
async def loadModel(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    priorityVersion: Union[Sequence[str], None] = None,
    notify: Union[bool, None] = None,
    languageStandard: Union[str, None] = None,
    requireExactVersion: Union[bool, None] = None,
) -> bool:
    ...


@external("loadModel")
def loadModel(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    priorityVersion: Union[Sequence[str], None] = None,
    notify: Union[bool, None] = None,
    languageStandard: Union[str, None] = None,
    requireExactVersion: Union[bool, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function loadModel
          input TypeName className;
          input String[:] priorityVersion = {"default"};
          input Boolean notify = false "Give a notification of the libraries and versions that were loaded";
          input String languageStandard = "" "Override the set language standard. Parse with the given setting, but do not change it permanently.";
          input Boolean requireExactVersion = false "If the version is required to be exact, if there is a uses Modelica(version=\\"3.2\\"), Modelica 3.2.1 will not match it.";
          output Boolean success;
        end loadModel;"""
    return ...  # type: ignore


@overload
def deleteFile(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
) -> bool:
    ...


@overload
async def deleteFile(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
) -> bool:
    ...


@external("deleteFile")
def deleteFile(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function deleteFile
          input String fileName;
          output Boolean success;
        end deleteFile;"""
    return ...  # type: ignore


@overload
def saveModel(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
    className: Union[TypeName, str],
) -> bool:
    ...


@overload
async def saveModel(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
    className: Union[TypeName, str],
) -> bool:
    ...


@external("saveModel")
def saveModel(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
    className: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function saveModel
          input String fileName;
          input TypeName className;
          output Boolean success;
        end saveModel;"""
    return ...  # type: ignore


@overload
def saveTotalModel(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
    className: Union[TypeName, str],
    stripAnnotations: Union[bool, None] = None,
    stripComments: Union[bool, None] = None,
) -> bool:
    ...


@overload
async def saveTotalModel(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
    className: Union[TypeName, str],
    stripAnnotations: Union[bool, None] = None,
    stripComments: Union[bool, None] = None,
) -> bool:
    ...


@external("saveTotalModel")
def saveTotalModel(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
    className: Union[TypeName, str],
    stripAnnotations: Union[bool, None] = None,
    stripComments: Union[bool, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function saveTotalModel
          input String fileName;
          input TypeName className;
          input Boolean stripAnnotations = false;
          input Boolean stripComments = false;
          output Boolean success;
        end saveTotalModel;"""
    return ...  # type: ignore


@overload
def save(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
) -> bool:
    ...


@overload
async def save(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
) -> bool:
    ...


@external("save")
def save(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function save
          input TypeName className;
          output Boolean success;
        end save;"""
    return ...  # type: ignore


@overload
def saveTotalSCode(self: SupportsInteractiveProperty[Synchronous]) -> None:
    ...


@overload
async def saveTotalSCode(
    self: SupportsInteractiveProperty[Asynchronous],
) -> None:
    ...


@external("saveTotalSCode")
def saveTotalSCode(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[None, Coroutine[None, None, None]]:
    ...


@overload
def translateGraphics(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
) -> str:
    ...


@overload
async def translateGraphics(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
) -> str:
    ...


@external("translateGraphics")
def translateGraphics(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function translateGraphics
          input TypeName className;
          output String result;
        end translateGraphics;"""
    return ...  # type: ignore


class Dumpxmldae(NamedTuple):
    success: bool
    xmlfileName: str


@overload
def dumpXMLDAE(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    translationLevel: Union[str, None] = None,
    addOriginalIncidenceMatrix: Union[bool, None] = None,
    addSolvingInfo: Union[bool, None] = None,
    addMathMLCode: Union[bool, None] = None,
    dumpResiduals: Union[bool, None] = None,
    fileNamePrefix: Union[str, None] = None,
    rewriteRulesFile: Union[PathLike[str], str, None] = None,
) -> Dumpxmldae:
    ...


@overload
async def dumpXMLDAE(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    translationLevel: Union[str, None] = None,
    addOriginalIncidenceMatrix: Union[bool, None] = None,
    addSolvingInfo: Union[bool, None] = None,
    addMathMLCode: Union[bool, None] = None,
    dumpResiduals: Union[bool, None] = None,
    fileNamePrefix: Union[str, None] = None,
    rewriteRulesFile: Union[PathLike[str], str, None] = None,
) -> Dumpxmldae:
    ...


@external("dumpXMLDAE")
def dumpXMLDAE(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    translationLevel: Union[str, None] = None,
    addOriginalIncidenceMatrix: Union[bool, None] = None,
    addSolvingInfo: Union[bool, None] = None,
    addMathMLCode: Union[bool, None] = None,
    dumpResiduals: Union[bool, None] = None,
    fileNamePrefix: Union[str, None] = None,
    rewriteRulesFile: Union[PathLike[str], str, None] = None,
) -> Union[Dumpxmldae, Coroutine[None, None, Dumpxmldae]]:
    """
    .. code-block:: modelica

        function dumpXMLDAE
          input TypeName className;
          input String translationLevel = "flat" "flat, optimiser, backEnd, or stateSpace";
          input Boolean addOriginalIncidenceMatrix = false;
          input Boolean addSolvingInfo = false;
          input Boolean addMathMLCode = false;
          input Boolean dumpResiduals = false;
          input String fileNamePrefix = "<default>" "this is the className in string form by default";
          input String rewriteRulesFile = "" "the file from where the rewiteRules are read, default is empty which means no rewrite rules";
          output Boolean success "if the function succeeded true/false";
          output String xmlfileName "the Xml file";
        end dumpXMLDAE;"""
    return ...  # type: ignore


class Convertunits(NamedTuple):
    unitsCompatible: bool
    scaleFactor: float
    offset: float


@overload
def convertUnits(
    self: SupportsInteractiveProperty[Synchronous], s1: str, s2: str
) -> Convertunits:
    ...


@overload
async def convertUnits(
    self: SupportsInteractiveProperty[Asynchronous], s1: str, s2: str
) -> Convertunits:
    ...


@external("convertUnits")
def convertUnits(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    s1: str,
    s2: str,
) -> Union[Convertunits, Coroutine[None, None, Convertunits]]:
    """
    .. code-block:: modelica

        function convertUnits
          input String s1;
          input String s2;
          output Boolean unitsCompatible;
          output Real scaleFactor;
          output Real offset;
        end convertUnits;"""
    return ...  # type: ignore


@overload
def getDerivedUnits(
    self: SupportsInteractiveProperty[Synchronous], baseUnit: str
) -> List[str]:
    ...


@overload
async def getDerivedUnits(
    self: SupportsInteractiveProperty[Asynchronous], baseUnit: str
) -> List[str]:
    ...


@external("getDerivedUnits")
def getDerivedUnits(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    baseUnit: str,
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function getDerivedUnits
          input String baseUnit;
          output String[:] derivedUnits;
        end getDerivedUnits;"""
    return ...  # type: ignore


@overload
def listVariables(
    self: SupportsInteractiveProperty[Synchronous],
) -> List[TypeName]:
    ...


@overload
async def listVariables(
    self: SupportsInteractiveProperty[Asynchronous],
) -> List[TypeName]:
    ...


@external("listVariables")
def listVariables(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[List[TypeName], Coroutine[None, None, List[TypeName]]]:
    """
    .. code-block:: modelica

        function listVariables
          output TypeName variables[:];
        end listVariables;"""
    return ...  # type: ignore


@overload
def strtok(
    self: SupportsInteractiveProperty[Synchronous], string: str, token: str
) -> List[str]:
    ...


@overload
async def strtok(
    self: SupportsInteractiveProperty[Asynchronous], string: str, token: str
) -> List[str]:
    ...


@external("strtok")
def strtok(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    string: str,
    token: str,
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function strtok
          input String string;
          input String token;
          output String[:] strings;
        end strtok;"""
    return ...  # type: ignore


@overload
def stringSplit(
    self: SupportsInteractiveProperty[Synchronous], string: str, token: str
) -> List[str]:
    ...


@overload
async def stringSplit(
    self: SupportsInteractiveProperty[Asynchronous], string: str, token: str
) -> List[str]:
    ...


@external("stringSplit")
def stringSplit(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    string: str,
    token: str,
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function stringSplit
          input String string;
          input String token "single character only";
          output String[:] strings;
        end stringSplit;"""
    return ...  # type: ignore


@overload
def stringReplace(
    self: SupportsInteractiveProperty[Synchronous],
    str: str,
    source: str,
    target: str,
) -> str:
    ...


@overload
async def stringReplace(
    self: SupportsInteractiveProperty[Asynchronous],
    str: str,
    source: str,
    target: str,
) -> str:
    ...


@external("stringReplace")
def stringReplace(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    str: str,
    source: str,
    target: str,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function stringReplace
          input String str;
          input String source;
          input String target;
          output String res;
        end stringReplace;"""
    return ...  # type: ignore


@overload
def escapeXML(
    self: SupportsInteractiveProperty[Synchronous], inStr: str
) -> str:
    ...


@overload
async def escapeXML(
    self: SupportsInteractiveProperty[Asynchronous], inStr: str
) -> str:
    ...


@external("escapeXML")
def escapeXML(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    inStr: str,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function escapeXML
          input String inStr;
          output String outStr;
        end escapeXML;"""
    return ...  # type: ignore


class ExportKind(enumeration):
    """
    .. code-block:: modelica

        type ExportKind = enumeration(Absyn "Normal Absyn", SCode "Normal SCode", MetaModelicaInterface "A restricted MetaModelica package interface (protected parts are stripped)", Internal "True unparsing of the Absyn");
    """

    __omc_class__ = TypeName("OpenModelica.Scripting.ExportKind")
    Absyn = 1
    "Normal Absyn"
    SCode = 2
    "Normal SCode"
    MetaModelicaInterface = 3
    "A restricted MetaModelica package interface (protected parts are stripped)"
    Internal = 4
    "True unparsing of the Absyn"


@overload
def list(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str, None] = None,
    interfaceOnly: Union[bool, None] = None,
    shortOnly: Union[bool, None] = None,
    exportKind: Union[
        ExportKind,
        Literal["Absyn", "SCode", "MetaModelicaInterface", "Internal"],
        None,
    ] = None,
) -> str:
    ...


@overload
async def list(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str, None] = None,
    interfaceOnly: Union[bool, None] = None,
    shortOnly: Union[bool, None] = None,
    exportKind: Union[
        ExportKind,
        Literal["Absyn", "SCode", "MetaModelicaInterface", "Internal"],
        None,
    ] = None,
) -> str:
    ...


@external("list")
def list(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str, None] = None,
    interfaceOnly: Union[bool, None] = None,
    shortOnly: Union[bool, None] = None,
    exportKind: Union[
        ExportKind,
        Literal["Absyn", "SCode", "MetaModelicaInterface", "Internal"],
        None,
    ] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function list
          input TypeName class_ = $Code(AllLoadedClasses);
          input Boolean interfaceOnly = false;
          input Boolean shortOnly = false "only short class definitions";
          input ExportKind exportKind = ExportKind.Absyn;
          output String contents;
        end list;"""
    return ...  # type: ignore


@overload
def listFile(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
) -> str:
    ...


@overload
async def listFile(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
) -> str:
    ...


@external("listFile")
def listFile(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function listFile
          input TypeName class_;
          output String contents;
        end listFile;"""
    return ...  # type: ignore


class DiffFormat(enumeration):
    """
    .. code-block:: modelica

        type DiffFormat = enumeration(plain "no deletions, no markup", color "terminal escape sequences", xml "XML tags");
    """

    __omc_class__ = TypeName("OpenModelica.Scripting.DiffFormat")
    plain = 1
    "no deletions, no markup"
    color = 2
    "terminal escape sequences"
    xml = 3
    "XML tags"


@overload
def diffModelicaFileListings(
    self: SupportsInteractiveProperty[Synchronous],
    before: str,
    after: str,
    diffFormat: Union[
        DiffFormat, Literal["plain", "color", "xml"], None
    ] = None,
) -> str:
    ...


@overload
async def diffModelicaFileListings(
    self: SupportsInteractiveProperty[Asynchronous],
    before: str,
    after: str,
    diffFormat: Union[
        DiffFormat, Literal["plain", "color", "xml"], None
    ] = None,
) -> str:
    ...


@external("diffModelicaFileListings")
def diffModelicaFileListings(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    before: str,
    after: str,
    diffFormat: Union[
        DiffFormat, Literal["plain", "color", "xml"], None
    ] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function diffModelicaFileListings
          input String before, after;
          input DiffFormat diffFormat = DiffFormat.color;
          output String result;
        end diffModelicaFileListings;"""
    return ...  # type: ignore


@overload
def exportToFigaro(
    self: SupportsInteractiveProperty[Synchronous],
    path: Union[TypeName, str],
    database: str,
    mode: str,
    options: str,
    processor: str,
    directory: Union[PathLike[str], str, None] = None,
) -> bool:
    ...


@overload
async def exportToFigaro(
    self: SupportsInteractiveProperty[Asynchronous],
    path: Union[TypeName, str],
    database: str,
    mode: str,
    options: str,
    processor: str,
    directory: Union[PathLike[str], str, None] = None,
) -> bool:
    ...


@external("exportToFigaro")
def exportToFigaro(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    path: Union[TypeName, str],
    database: str,
    mode: str,
    options: str,
    processor: str,
    directory: Union[PathLike[str], str, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function exportToFigaro
          input TypeName path;
          input String directory = cd();
          input String database;
          input String mode;
          input String options;
          input String processor;
          output Boolean success;
        end exportToFigaro;"""
    return ...  # type: ignore


@overload
def inferBindings(
    self: SupportsInteractiveProperty[Synchronous], path: Union[TypeName, str]
) -> bool:
    ...


@overload
async def inferBindings(
    self: SupportsInteractiveProperty[Asynchronous], path: Union[TypeName, str]
) -> bool:
    ...


@external("inferBindings")
def inferBindings(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    path: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function inferBindings
          input TypeName path;
          output Boolean success;
        end inferBindings;"""
    return ...  # type: ignore


@overload
def generateVerificationScenarios(
    self: SupportsInteractiveProperty[Synchronous], path: Union[TypeName, str]
) -> bool:
    ...


@overload
async def generateVerificationScenarios(
    self: SupportsInteractiveProperty[Asynchronous], path: Union[TypeName, str]
) -> bool:
    ...


@external("generateVerificationScenarios")
def generateVerificationScenarios(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    path: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function generateVerificationScenarios
          input TypeName path;
          output Boolean success;
        end generateVerificationScenarios;"""
    return ...  # type: ignore


@overload
def rewriteBlockCall(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    inDefs: Union[TypeName, str],
) -> bool:
    ...


@overload
async def rewriteBlockCall(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    inDefs: Union[TypeName, str],
) -> bool:
    ...


@external("rewriteBlockCall")
def rewriteBlockCall(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    inDefs: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function rewriteBlockCall
          input TypeName className;
          input TypeName inDefs;
          output Boolean success;
        end rewriteBlockCall;"""
    return ...  # type: ignore


@overload
def realpath(self: SupportsInteractiveProperty[Synchronous], name: str) -> str:
    ...


@overload
async def realpath(
    self: SupportsInteractiveProperty[Asynchronous], name: str
) -> str:
    ...


@external("realpath")
def realpath(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    name: str,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function realpath
          input String name "Absolute or relative file or directory name";
          output String fullName "Full path of 'name'";
        end realpath;"""
    return ...  # type: ignore


@overload
def uriToFilename(
    self: SupportsInteractiveProperty[Synchronous], uri: str
) -> Union[str, None]:
    ...


@overload
async def uriToFilename(
    self: SupportsInteractiveProperty[Asynchronous], uri: str
) -> Union[str, None]:
    ...


@external("uriToFilename")
def uriToFilename(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    uri: str,
) -> Union[Union[str, None], Coroutine[None, None, Union[str, None]]]:
    """
    .. code-block:: modelica

        function uriToFilename
          input String uri;
          output String filename = "";
        end uriToFilename;"""
    return ...  # type: ignore


@overload
def getLoadedLibraries(
    self: SupportsInteractiveProperty[Synchronous],
) -> List[List[str]]:
    ...


@overload
async def getLoadedLibraries(
    self: SupportsInteractiveProperty[Asynchronous],
) -> List[List[str]]:
    ...


@external("getLoadedLibraries")
def getLoadedLibraries(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[List[List[str]], Coroutine[None, None, List[List[str]]]]:
    """
    .. code-block:: modelica

        function getLoadedLibraries
          output String[:, 2] libraries;
        end getLoadedLibraries;"""
    return ...  # type: ignore


class LinearSystemSolver(enumeration):
    """
    .. code-block:: modelica

        type LinearSystemSolver = enumeration(dgesv, lpsolve55);"""

    __omc_class__ = TypeName("OpenModelica.Scripting.LinearSystemSolver")
    dgesv = 1
    lpsolve55 = 2


class Solvelinearsystem(NamedTuple):
    X: List[float]
    info: int


@overload
def solveLinearSystem(
    self: SupportsInteractiveProperty[Synchronous],
    A: Sequence[Sequence[float]],
    B: Sequence[float],
    solver: Union[
        LinearSystemSolver, Literal["dgesv", "lpsolve55"], None
    ] = None,
    isInt: Union[Sequence[int], None] = None,
) -> Solvelinearsystem:
    ...


@overload
async def solveLinearSystem(
    self: SupportsInteractiveProperty[Asynchronous],
    A: Sequence[Sequence[float]],
    B: Sequence[float],
    solver: Union[
        LinearSystemSolver, Literal["dgesv", "lpsolve55"], None
    ] = None,
    isInt: Union[Sequence[int], None] = None,
) -> Solvelinearsystem:
    ...


@external("solveLinearSystem")
def solveLinearSystem(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    A: Sequence[Sequence[float]],
    B: Sequence[float],
    solver: Union[
        LinearSystemSolver, Literal["dgesv", "lpsolve55"], None
    ] = None,
    isInt: Union[Sequence[int], None] = None,
) -> Union[Solvelinearsystem, Coroutine[None, None, Solvelinearsystem]]:
    """
    .. code-block:: modelica

        function solveLinearSystem
          input Real[size(B, 1), size(B, 1)] A;
          input Real[:] B;
          input LinearSystemSolver solver = LinearSystemSolver.dgesv;
          input Integer[:] isInt = {-1} "list of indices that are integers";
          output Real[size(B, 1)] X;
          output Integer info;
        end solveLinearSystem;"""
    return ...  # type: ignore


class StandardStream(enumeration):
    """
    .. code-block:: modelica

        type StandardStream = enumeration(stdin, stdout, stderr);"""

    __omc_class__ = TypeName("OpenModelica.Scripting.StandardStream")
    stdin = 1
    stdout = 2
    stderr = 3


@overload
def reopenStandardStream(
    self: SupportsInteractiveProperty[Synchronous],
    _stream: Union[StandardStream, Literal["stdin", "stdout", "stderr"]],
    filename: Union[PathLike[str], str],
) -> bool:
    ...


@overload
async def reopenStandardStream(
    self: SupportsInteractiveProperty[Asynchronous],
    _stream: Union[StandardStream, Literal["stdin", "stdout", "stderr"]],
    filename: Union[PathLike[str], str],
) -> bool:
    ...


@external("reopenStandardStream")
def reopenStandardStream(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    _stream: Union[StandardStream, Literal["stdin", "stdout", "stderr"]],
    filename: Union[PathLike[str], str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function reopenStandardStream
          input StandardStream _stream;
          input String filename;
          output Boolean success;
        end reopenStandardStream;"""
    return ...  # type: ignore


@overload
def importFMU(
    self: SupportsInteractiveProperty[Synchronous],
    filename: Union[PathLike[str], str],
    workdir: Union[PathLike[str], str, None] = None,
    loglevel: Union[int, None] = None,
    fullPath: Union[bool, None] = None,
    debugLogging: Union[bool, None] = None,
    generateInputConnectors: Union[bool, None] = None,
    generateOutputConnectors: Union[bool, None] = None,
) -> str:
    ...


@overload
async def importFMU(
    self: SupportsInteractiveProperty[Asynchronous],
    filename: Union[PathLike[str], str],
    workdir: Union[PathLike[str], str, None] = None,
    loglevel: Union[int, None] = None,
    fullPath: Union[bool, None] = None,
    debugLogging: Union[bool, None] = None,
    generateInputConnectors: Union[bool, None] = None,
    generateOutputConnectors: Union[bool, None] = None,
) -> str:
    ...


@external("importFMU")
def importFMU(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    filename: Union[PathLike[str], str],
    workdir: Union[PathLike[str], str, None] = None,
    loglevel: Union[int, None] = None,
    fullPath: Union[bool, None] = None,
    debugLogging: Union[bool, None] = None,
    generateInputConnectors: Union[bool, None] = None,
    generateOutputConnectors: Union[bool, None] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function importFMU
          input String filename "the fmu file name";
          input String workdir = "<default>" "The output directory for imported FMU files. <default> will put the files to current working directory.";
          input Integer loglevel = 3 "loglevel_nothing=0;loglevel_fatal=1;loglevel_error=2;loglevel_warning=3;loglevel_info=4;loglevel_verbose=5;loglevel_debug=6";
          input Boolean fullPath = false "When true the full output path is returned otherwise only the file name.";
          input Boolean debugLogging = false "When true the FMU's debug output is printed.";
          input Boolean generateInputConnectors = true "When true creates the input connector pins.";
          input Boolean generateOutputConnectors = true "When true creates the output connector pins.";
          output String generatedFileName "Returns the full path of the generated file.";
        end importFMU;"""
    return ...  # type: ignore


@overload
def importFMUModelDescription(
    self: SupportsInteractiveProperty[Synchronous],
    filename: Union[PathLike[str], str],
    workdir: Union[PathLike[str], str, None] = None,
    loglevel: Union[int, None] = None,
    fullPath: Union[bool, None] = None,
    debugLogging: Union[bool, None] = None,
    generateInputConnectors: Union[bool, None] = None,
    generateOutputConnectors: Union[bool, None] = None,
) -> str:
    ...


@overload
async def importFMUModelDescription(
    self: SupportsInteractiveProperty[Asynchronous],
    filename: Union[PathLike[str], str],
    workdir: Union[PathLike[str], str, None] = None,
    loglevel: Union[int, None] = None,
    fullPath: Union[bool, None] = None,
    debugLogging: Union[bool, None] = None,
    generateInputConnectors: Union[bool, None] = None,
    generateOutputConnectors: Union[bool, None] = None,
) -> str:
    ...


@external("importFMUModelDescription")
def importFMUModelDescription(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    filename: Union[PathLike[str], str],
    workdir: Union[PathLike[str], str, None] = None,
    loglevel: Union[int, None] = None,
    fullPath: Union[bool, None] = None,
    debugLogging: Union[bool, None] = None,
    generateInputConnectors: Union[bool, None] = None,
    generateOutputConnectors: Union[bool, None] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function importFMUModelDescription
          input String filename "the fmu file name";
          input String workdir = "<default>" "The output directory for imported FMU files. <default> will put the files to current working directory.";
          input Integer loglevel = 3 "loglevel_nothing=0;loglevel_fatal=1;loglevel_error=2;loglevel_warning=3;loglevel_info=4;loglevel_verbose=5;loglevel_debug=6";
          input Boolean fullPath = false "When true the full output path is returned otherwise only the file name.";
          input Boolean debugLogging = false "When true the FMU's debug output is printed.";
          input Boolean generateInputConnectors = true "When true creates the input connector pins.";
          input Boolean generateOutputConnectors = true "When true creates the output connector pins.";
          output String generatedFileName "Returns the full path of the generated file.";
        end importFMUModelDescription;"""
    return ...  # type: ignore


@overload
def translateModelFMU(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    version: Union[str, None] = None,
    fmuType: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    includeResources: Union[bool, None] = None,
) -> str:
    ...


@overload
async def translateModelFMU(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    version: Union[str, None] = None,
    fmuType: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    includeResources: Union[bool, None] = None,
) -> str:
    ...


@external("translateModelFMU")
def translateModelFMU(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    version: Union[str, None] = None,
    fmuType: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    includeResources: Union[bool, None] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function translateModelFMU
          input TypeName className "the class that should translated";
          input String version = "2.0" "FMU version, 1.0 or 2.0.";
          input String fmuType = "me" "FMU type, me (model exchange), cs (co-simulation), me_cs (both model exchange and co-simulation)";
          input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \\"className\\"";
          input Boolean includeResources = false "include Modelica based resources via loadResource or not";
          output String generatedFileName "Returns the full path of the generated FMU.";
        end translateModelFMU;"""
    return ...  # type: ignore


@overload
def buildModelFMU(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    version: Union[str, None] = None,
    fmuType: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    platforms: Union[Sequence[str], None] = None,
    includeResources: Union[bool, None] = None,
) -> str:
    ...


@overload
async def buildModelFMU(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    version: Union[str, None] = None,
    fmuType: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    platforms: Union[Sequence[str], None] = None,
    includeResources: Union[bool, None] = None,
) -> str:
    ...


@external("buildModelFMU")
def buildModelFMU(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    version: Union[str, None] = None,
    fmuType: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    platforms: Union[Sequence[str], None] = None,
    includeResources: Union[bool, None] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function buildModelFMU
          input TypeName className "the class that should translated";
          input String version = "2.0" "FMU version, 1.0 or 2.0.";
          input String fmuType = "me" "FMU type, me (model exchange), cs (co-simulation), me_cs (both model exchange and co-simulation)";
          input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \\"className\\"";
          input String platforms[:] = {"static"} "The list of platforms to generate code for. \\"dynamic\\"=current platform, dynamically link the runtime. \\"static\\"=current platform, statically link everything. Else, use a host triple, e.g. \\"x86_64-linux-gnu\\" or \\"x86_64-w64-mingw32\\"";
          input Boolean includeResources = false "include Modelica based resources via loadResource or not";
          output String generatedFileName "Returns the full path of the generated FMU.";
        end buildModelFMU;"""
    return ...  # type: ignore


class Buildencryptedpackage(NamedTuple):
    success: bool
    commandOutput: str


@overload
def buildEncryptedPackage(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
) -> Buildencryptedpackage:
    ...


@overload
async def buildEncryptedPackage(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
) -> Buildencryptedpackage:
    ...


@external("buildEncryptedPackage")
def buildEncryptedPackage(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
) -> Union[
    Buildencryptedpackage, Coroutine[None, None, Buildencryptedpackage]
]:
    """
    .. code-block:: modelica

        function buildEncryptedPackage
          input TypeName className "the class that should encrypted";
          output Boolean success;
          output String commandOutput "Output of the packagetool executable";
        end buildEncryptedPackage;"""
    return ...  # type: ignore


@overload
def simulate(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[float, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
) -> SimulationResult:
    ...


@overload
async def simulate(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[float, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
) -> SimulationResult:
    ...


@external("simulate")
def simulate(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[float, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
) -> Union[SimulationResult, Coroutine[None, None, SimulationResult]]:
    """
    .. code-block:: modelica

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
        end simulate;"""
    return ...  # type: ignore


@dataclass(frozen=True)
class SimulationResult(record):
    """
    .. code-block:: modelica

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
        end SimulationResult;"""

    __omc_class__ = TypeName(
        "OpenModelica.Scripting.simulate.SimulationResult"
    )
    resultFile: str
    simulationOptions: str
    messages: str
    timeFrontend: float
    timeBackend: float
    timeSimCode: float
    timeTemplates: float
    timeCompile: float
    timeSimulation: float
    timeTotal: float


@overload
def buildModel(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[float, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
) -> List[str]:
    ...


@overload
async def buildModel(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[float, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
) -> List[str]:
    ...


@external("buildModel")
def buildModel(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[float, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

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
        end buildModel;"""
    return ...  # type: ignore


@overload
def buildLabel(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[int, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
) -> List[str]:
    ...


@overload
async def buildLabel(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[int, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
) -> List[str]:
    ...


@external("buildLabel")
def buildLabel(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[int, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

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
        end buildLabel;"""
    return ...  # type: ignore


@overload
def reduceTerms(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[int, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
    labelstoCancel: Union[str, None] = None,
) -> List[str]:
    ...


@overload
async def reduceTerms(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[int, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
    labelstoCancel: Union[str, None] = None,
) -> List[str]:
    ...


@external("reduceTerms")
def reduceTerms(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[int, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
    labelstoCancel: Union[str, None] = None,
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

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
        end reduceTerms;"""
    return ...  # type: ignore


@overload
def moveClass(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    offset: int,
) -> bool:
    ...


@overload
async def moveClass(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    offset: int,
) -> bool:
    ...


@external("moveClass")
def moveClass(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    offset: int,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function moveClass
          input TypeName className "the class that should be moved";
          input Integer offset "Offset in the class list.";
          output Boolean result;
        end moveClass;"""
    return ...  # type: ignore


@overload
def moveClassToTop(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
) -> bool:
    ...


@overload
async def moveClassToTop(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
) -> bool:
    ...


@external("moveClassToTop")
def moveClassToTop(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function moveClassToTop
          input TypeName className;
          output Boolean result;
        end moveClassToTop;"""
    return ...  # type: ignore


@overload
def moveClassToBottom(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
) -> bool:
    ...


@overload
async def moveClassToBottom(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
) -> bool:
    ...


@external("moveClassToBottom")
def moveClassToBottom(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function moveClassToBottom
          input TypeName className;
          output Boolean result;
        end moveClassToBottom;"""
    return ...  # type: ignore


@overload
def copyClass(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    newClassName: str,
    withIn: Union[TypeName, str, None] = None,
) -> bool:
    ...


@overload
async def copyClass(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    newClassName: str,
    withIn: Union[TypeName, str, None] = None,
) -> bool:
    ...


@external("copyClass")
def copyClass(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    newClassName: str,
    withIn: Union[TypeName, str, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function copyClass
          input TypeName className "the class that should be copied";
          input String newClassName "the name for new class";
          input TypeName withIn = $Code(TopLevel) "the with in path for new class";
          output Boolean result;
        end copyClass;"""
    return ...  # type: ignore


@overload
def linearize(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[float, None] = None,
    stepSize: Union[float, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    storeInTemp: Union[bool, None] = None,
    noClean: Union[bool, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
) -> str:
    ...


@overload
async def linearize(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[float, None] = None,
    stepSize: Union[float, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    storeInTemp: Union[bool, None] = None,
    noClean: Union[bool, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
) -> str:
    ...


@external("linearize")
def linearize(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[float, None] = None,
    stepSize: Union[float, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    storeInTemp: Union[bool, None] = None,
    noClean: Union[bool, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

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
        end linearize;"""
    return ...  # type: ignore


@overload
def optimize(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[float, None] = None,
    stepSize: Union[float, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    storeInTemp: Union[bool, None] = None,
    noClean: Union[bool, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
) -> str:
    ...


@overload
async def optimize(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[float, None] = None,
    stepSize: Union[float, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    storeInTemp: Union[bool, None] = None,
    noClean: Union[bool, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
) -> str:
    ...


@external("optimize")
def optimize(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    startTime: Union[float, None] = None,
    stopTime: Union[float, None] = None,
    numberOfIntervals: Union[float, None] = None,
    stepSize: Union[float, None] = None,
    tolerance: Union[float, None] = None,
    method: Union[str, None] = None,
    fileNamePrefix: Union[str, None] = None,
    storeInTemp: Union[bool, None] = None,
    noClean: Union[bool, None] = None,
    options: Union[str, None] = None,
    outputFormat: Union[str, None] = None,
    variableFilter: Union[str, None] = None,
    cflags: Union[str, None] = None,
    simflags: Union[str, None] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

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
        end optimize;"""
    return ...  # type: ignore


@overload
def getSourceFile(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
) -> str:
    ...


@overload
async def getSourceFile(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
) -> str:
    ...


@external("getSourceFile")
def getSourceFile(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getSourceFile
          input TypeName class_;
          output String filename "empty on failure";
        end getSourceFile;"""
    return ...  # type: ignore


@overload
def setSourceFile(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    filename: Union[PathLike[str], str],
) -> bool:
    ...


@overload
async def setSourceFile(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    filename: Union[PathLike[str], str],
) -> bool:
    ...


@external("setSourceFile")
def setSourceFile(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    filename: Union[PathLike[str], str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setSourceFile
          input TypeName class_;
          input String filename;
          output Boolean success;
        end setSourceFile;"""
    return ...  # type: ignore


@overload
def isShortDefinition(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
) -> bool:
    ...


@overload
async def isShortDefinition(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
) -> bool:
    ...


@external("isShortDefinition")
def isShortDefinition(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isShortDefinition
          input TypeName class_;
          output Boolean isShortCls;
        end isShortDefinition;"""
    return ...  # type: ignore


@overload
def setClassComment(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    filename: Union[PathLike[str], str],
) -> bool:
    ...


@overload
async def setClassComment(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    filename: Union[PathLike[str], str],
) -> bool:
    ...


@external("setClassComment")
def setClassComment(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    filename: Union[PathLike[str], str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setClassComment
          input TypeName class_;
          input String filename;
          output Boolean success;
        end setClassComment;"""
    return ...  # type: ignore


@overload
def getClassNames(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str, None] = None,
    recursive: Union[bool, None] = None,
    qualified: Union[bool, None] = None,
    sort: Union[bool, None] = None,
    builtin: Union[bool, None] = None,
    showProtected: Union[bool, None] = None,
    includeConstants: Union[bool, None] = None,
) -> List[TypeName]:
    ...


@overload
async def getClassNames(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str, None] = None,
    recursive: Union[bool, None] = None,
    qualified: Union[bool, None] = None,
    sort: Union[bool, None] = None,
    builtin: Union[bool, None] = None,
    showProtected: Union[bool, None] = None,
    includeConstants: Union[bool, None] = None,
) -> List[TypeName]:
    ...


@external("getClassNames")
def getClassNames(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str, None] = None,
    recursive: Union[bool, None] = None,
    qualified: Union[bool, None] = None,
    sort: Union[bool, None] = None,
    builtin: Union[bool, None] = None,
    showProtected: Union[bool, None] = None,
    includeConstants: Union[bool, None] = None,
) -> Union[List[TypeName], Coroutine[None, None, List[TypeName]]]:
    """
    .. code-block:: modelica

        function getClassNames
          input TypeName class_ = $Code(AllLoadedClasses);
          input Boolean recursive = false;
          input Boolean qualified = false;
          input Boolean sort = false;
          input Boolean builtin = false "List also builtin classes if true";
          input Boolean showProtected = false "List also protected classes if true";
          input Boolean includeConstants = false "List also constants in the class if true";
          output TypeName classNames[:];
        end getClassNames;"""
    return ...  # type: ignore


@overload
def getUsedClassNames(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
) -> List[TypeName]:
    ...


@overload
async def getUsedClassNames(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
) -> List[TypeName]:
    ...


@external("getUsedClassNames")
def getUsedClassNames(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
) -> Union[List[TypeName], Coroutine[None, None, List[TypeName]]]:
    """
    .. code-block:: modelica

        function getUsedClassNames
          input TypeName className;
          output TypeName classNames[:];
        end getUsedClassNames;"""
    return ...  # type: ignore


@overload
def getPackages(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str, None] = None,
) -> List[TypeName]:
    ...


@overload
async def getPackages(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str, None] = None,
) -> List[TypeName]:
    ...


@external("getPackages")
def getPackages(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str, None] = None,
) -> Union[List[TypeName], Coroutine[None, None, List[TypeName]]]:
    """
    .. code-block:: modelica

        function getPackages
          input TypeName class_ = $Code(AllLoadedClasses);
          output TypeName classNames[:];
        end getPackages;"""
    return ...  # type: ignore


@overload
def basePlotFunction(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str, None] = None,
    interpolation: Union[str, None] = None,
    title: Union[str, None] = None,
    legend: Union[bool, None] = None,
    grid: Union[bool, None] = None,
    logX: Union[bool, None] = None,
    logY: Union[bool, None] = None,
    xLabel: Union[str, None] = None,
    yLabel: Union[str, None] = None,
    points: Union[bool, None] = None,
    xRange: Union[Sequence[float], None] = None,
    yRange: Union[Sequence[float], None] = None,
) -> bool:
    ...


@overload
async def basePlotFunction(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str, None] = None,
    interpolation: Union[str, None] = None,
    title: Union[str, None] = None,
    legend: Union[bool, None] = None,
    grid: Union[bool, None] = None,
    logX: Union[bool, None] = None,
    logY: Union[bool, None] = None,
    xLabel: Union[str, None] = None,
    yLabel: Union[str, None] = None,
    points: Union[bool, None] = None,
    xRange: Union[Sequence[float], None] = None,
    yRange: Union[Sequence[float], None] = None,
) -> bool:
    ...


@external("basePlotFunction")
def basePlotFunction(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str, None] = None,
    interpolation: Union[str, None] = None,
    title: Union[str, None] = None,
    legend: Union[bool, None] = None,
    grid: Union[bool, None] = None,
    logX: Union[bool, None] = None,
    logY: Union[bool, None] = None,
    xLabel: Union[str, None] = None,
    yLabel: Union[str, None] = None,
    points: Union[bool, None] = None,
    xRange: Union[Sequence[float], None] = None,
    yRange: Union[Sequence[float], None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

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
        end basePlotFunction;"""
    return ...  # type: ignore


@overload
def plot(
    self: SupportsInteractiveProperty[Synchronous],
    vars: Sequence[Union[VariableName, str]],
    externalWindow: Union[bool, None] = None,
    fileName: Union[PathLike[str], str, None] = None,
    title: Union[str, None] = None,
    grid: Union[str, None] = None,
    logX: Union[bool, None] = None,
    logY: Union[bool, None] = None,
    xLabel: Union[str, None] = None,
    yLabel: Union[str, None] = None,
    xRange: Union[Sequence[float], None] = None,
    yRange: Union[Sequence[float], None] = None,
    curveWidth: Union[float, None] = None,
    curveStyle: Union[int, None] = None,
    legendPosition: Union[str, None] = None,
    footer: Union[str, None] = None,
    autoScale: Union[bool, None] = None,
    forceOMPlot: Union[bool, None] = None,
) -> bool:
    ...


@overload
async def plot(
    self: SupportsInteractiveProperty[Asynchronous],
    vars: Sequence[Union[VariableName, str]],
    externalWindow: Union[bool, None] = None,
    fileName: Union[PathLike[str], str, None] = None,
    title: Union[str, None] = None,
    grid: Union[str, None] = None,
    logX: Union[bool, None] = None,
    logY: Union[bool, None] = None,
    xLabel: Union[str, None] = None,
    yLabel: Union[str, None] = None,
    xRange: Union[Sequence[float], None] = None,
    yRange: Union[Sequence[float], None] = None,
    curveWidth: Union[float, None] = None,
    curveStyle: Union[int, None] = None,
    legendPosition: Union[str, None] = None,
    footer: Union[str, None] = None,
    autoScale: Union[bool, None] = None,
    forceOMPlot: Union[bool, None] = None,
) -> bool:
    ...


@external("plot")
def plot(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    vars: Sequence[Union[VariableName, str]],
    externalWindow: Union[bool, None] = None,
    fileName: Union[PathLike[str], str, None] = None,
    title: Union[str, None] = None,
    grid: Union[str, None] = None,
    logX: Union[bool, None] = None,
    logY: Union[bool, None] = None,
    xLabel: Union[str, None] = None,
    yLabel: Union[str, None] = None,
    xRange: Union[Sequence[float], None] = None,
    yRange: Union[Sequence[float], None] = None,
    curveWidth: Union[float, None] = None,
    curveStyle: Union[int, None] = None,
    legendPosition: Union[str, None] = None,
    footer: Union[str, None] = None,
    autoScale: Union[bool, None] = None,
    forceOMPlot: Union[bool, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

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
        end plot;"""
    return ...  # type: ignore


@overload
def plotAll(
    self: SupportsInteractiveProperty[Synchronous],
    externalWindow: Union[bool, None] = None,
    fileName: Union[PathLike[str], str, None] = None,
    title: Union[str, None] = None,
    grid: Union[str, None] = None,
    logX: Union[bool, None] = None,
    logY: Union[bool, None] = None,
    xLabel: Union[str, None] = None,
    yLabel: Union[str, None] = None,
    xRange: Union[Sequence[float], None] = None,
    yRange: Union[Sequence[float], None] = None,
    curveWidth: Union[float, None] = None,
    curveStyle: Union[int, None] = None,
    legendPosition: Union[str, None] = None,
    footer: Union[str, None] = None,
    autoScale: Union[bool, None] = None,
    forceOMPlot: Union[bool, None] = None,
) -> bool:
    ...


@overload
async def plotAll(
    self: SupportsInteractiveProperty[Asynchronous],
    externalWindow: Union[bool, None] = None,
    fileName: Union[PathLike[str], str, None] = None,
    title: Union[str, None] = None,
    grid: Union[str, None] = None,
    logX: Union[bool, None] = None,
    logY: Union[bool, None] = None,
    xLabel: Union[str, None] = None,
    yLabel: Union[str, None] = None,
    xRange: Union[Sequence[float], None] = None,
    yRange: Union[Sequence[float], None] = None,
    curveWidth: Union[float, None] = None,
    curveStyle: Union[int, None] = None,
    legendPosition: Union[str, None] = None,
    footer: Union[str, None] = None,
    autoScale: Union[bool, None] = None,
    forceOMPlot: Union[bool, None] = None,
) -> bool:
    ...


@external("plotAll")
def plotAll(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    externalWindow: Union[bool, None] = None,
    fileName: Union[PathLike[str], str, None] = None,
    title: Union[str, None] = None,
    grid: Union[str, None] = None,
    logX: Union[bool, None] = None,
    logY: Union[bool, None] = None,
    xLabel: Union[str, None] = None,
    yLabel: Union[str, None] = None,
    xRange: Union[Sequence[float], None] = None,
    yRange: Union[Sequence[float], None] = None,
    curveWidth: Union[float, None] = None,
    curveStyle: Union[int, None] = None,
    legendPosition: Union[str, None] = None,
    footer: Union[str, None] = None,
    autoScale: Union[bool, None] = None,
    forceOMPlot: Union[bool, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

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
        end plotAll;"""
    return ...  # type: ignore


@overload
def plotParametric(
    self: SupportsInteractiveProperty[Synchronous],
    xVariable: Union[VariableName, str],
    yVariable: Union[VariableName, str],
    externalWindow: Union[bool, None] = None,
    fileName: Union[PathLike[str], str, None] = None,
    title: Union[str, None] = None,
    grid: Union[str, None] = None,
    logX: Union[bool, None] = None,
    logY: Union[bool, None] = None,
    xLabel: Union[str, None] = None,
    yLabel: Union[str, None] = None,
    xRange: Union[Sequence[float], None] = None,
    yRange: Union[Sequence[float], None] = None,
    curveWidth: Union[float, None] = None,
    curveStyle: Union[int, None] = None,
    legendPosition: Union[str, None] = None,
    footer: Union[str, None] = None,
    autoScale: Union[bool, None] = None,
    forceOMPlot: Union[bool, None] = None,
) -> bool:
    ...


@overload
async def plotParametric(
    self: SupportsInteractiveProperty[Asynchronous],
    xVariable: Union[VariableName, str],
    yVariable: Union[VariableName, str],
    externalWindow: Union[bool, None] = None,
    fileName: Union[PathLike[str], str, None] = None,
    title: Union[str, None] = None,
    grid: Union[str, None] = None,
    logX: Union[bool, None] = None,
    logY: Union[bool, None] = None,
    xLabel: Union[str, None] = None,
    yLabel: Union[str, None] = None,
    xRange: Union[Sequence[float], None] = None,
    yRange: Union[Sequence[float], None] = None,
    curveWidth: Union[float, None] = None,
    curveStyle: Union[int, None] = None,
    legendPosition: Union[str, None] = None,
    footer: Union[str, None] = None,
    autoScale: Union[bool, None] = None,
    forceOMPlot: Union[bool, None] = None,
) -> bool:
    ...


@external("plotParametric")
def plotParametric(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    xVariable: Union[VariableName, str],
    yVariable: Union[VariableName, str],
    externalWindow: Union[bool, None] = None,
    fileName: Union[PathLike[str], str, None] = None,
    title: Union[str, None] = None,
    grid: Union[str, None] = None,
    logX: Union[bool, None] = None,
    logY: Union[bool, None] = None,
    xLabel: Union[str, None] = None,
    yLabel: Union[str, None] = None,
    xRange: Union[Sequence[float], None] = None,
    yRange: Union[Sequence[float], None] = None,
    curveWidth: Union[float, None] = None,
    curveStyle: Union[int, None] = None,
    legendPosition: Union[str, None] = None,
    footer: Union[str, None] = None,
    autoScale: Union[bool, None] = None,
    forceOMPlot: Union[bool, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

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
        end plotParametric;"""
    return ...  # type: ignore


@overload
def readSimulationResult(
    self: SupportsInteractiveProperty[Synchronous],
    filename: Union[PathLike[str], str],
    variables: Sequence[Union[VariableName, str]],
    size: Union[int, None] = None,
) -> List[List[float]]:
    ...


@overload
async def readSimulationResult(
    self: SupportsInteractiveProperty[Asynchronous],
    filename: Union[PathLike[str], str],
    variables: Sequence[Union[VariableName, str]],
    size: Union[int, None] = None,
) -> List[List[float]]:
    ...


@external("readSimulationResult")
def readSimulationResult(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    filename: Union[PathLike[str], str],
    variables: Sequence[Union[VariableName, str]],
    size: Union[int, None] = None,
) -> Union[List[List[float]], Coroutine[None, None, List[List[float]]]]:
    """
    .. code-block:: modelica

        function readSimulationResult
          input String filename;
          input VariableNames variables;
          input Integer size = 0 "0=read any size... If the size is not the same as the result-file, this function fails";
          output Real result[:, :];
        end readSimulationResult;"""
    return ...  # type: ignore


@overload
def readSimulationResultSize(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
) -> int:
    ...


@overload
async def readSimulationResultSize(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
) -> int:
    ...


@external("readSimulationResultSize")
def readSimulationResultSize(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function readSimulationResultSize
          input String fileName;
          output Integer sz;
        end readSimulationResultSize;"""
    return ...  # type: ignore


@overload
def readSimulationResultVars(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
    readParameters: Union[bool, None] = None,
    openmodelicaStyle: Union[bool, None] = None,
) -> List[str]:
    ...


@overload
async def readSimulationResultVars(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
    readParameters: Union[bool, None] = None,
    openmodelicaStyle: Union[bool, None] = None,
) -> List[str]:
    ...


@external("readSimulationResultVars")
def readSimulationResultVars(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
    readParameters: Union[bool, None] = None,
    openmodelicaStyle: Union[bool, None] = None,
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function readSimulationResultVars
          input String fileName;
          input Boolean readParameters = true;
          input Boolean openmodelicaStyle = false;
          output String[:] vars;
        end readSimulationResultVars;"""
    return ...  # type: ignore


@overload
def filterSimulationResults(
    self: SupportsInteractiveProperty[Synchronous],
    inFile: Union[PathLike[str], str],
    outFile: Union[PathLike[str], str],
    vars: Sequence[str],
    numberOfIntervals: Union[int, None] = None,
    removeDescription: Union[bool, None] = None,
) -> bool:
    ...


@overload
async def filterSimulationResults(
    self: SupportsInteractiveProperty[Asynchronous],
    inFile: Union[PathLike[str], str],
    outFile: Union[PathLike[str], str],
    vars: Sequence[str],
    numberOfIntervals: Union[int, None] = None,
    removeDescription: Union[bool, None] = None,
) -> bool:
    ...


@external("filterSimulationResults")
def filterSimulationResults(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    inFile: Union[PathLike[str], str],
    outFile: Union[PathLike[str], str],
    vars: Sequence[str],
    numberOfIntervals: Union[int, None] = None,
    removeDescription: Union[bool, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function filterSimulationResults
          input String inFile;
          input String outFile;
          input String[:] vars;
          input Integer numberOfIntervals = 0 "0=Do not resample";
          input Boolean removeDescription = false;
          output Boolean success;
        end filterSimulationResults;"""
    return ...  # type: ignore


@overload
def compareSimulationResults(
    self: SupportsInteractiveProperty[Synchronous],
    filename: Union[PathLike[str], str],
    reffilename: Union[PathLike[str], str],
    logfilename: Union[PathLike[str], str],
    relTol: Union[float, None] = None,
    absTol: Union[float, None] = None,
    vars: Union[Sequence[str], None] = None,
) -> List[str]:
    ...


@overload
async def compareSimulationResults(
    self: SupportsInteractiveProperty[Asynchronous],
    filename: Union[PathLike[str], str],
    reffilename: Union[PathLike[str], str],
    logfilename: Union[PathLike[str], str],
    relTol: Union[float, None] = None,
    absTol: Union[float, None] = None,
    vars: Union[Sequence[str], None] = None,
) -> List[str]:
    ...


@external("compareSimulationResults")
def compareSimulationResults(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    filename: Union[PathLike[str], str],
    reffilename: Union[PathLike[str], str],
    logfilename: Union[PathLike[str], str],
    relTol: Union[float, None] = None,
    absTol: Union[float, None] = None,
    vars: Union[Sequence[str], None] = None,
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function compareSimulationResults
          input String filename;
          input String reffilename;
          input String logfilename;
          input Real relTol = 0.01;
          input Real absTol = 0.0001;
          input String[:] vars = fill("", 0);
          output String[:] result;
        end compareSimulationResults;"""
    return ...  # type: ignore


@overload
def deltaSimulationResults(
    self: SupportsInteractiveProperty[Synchronous],
    filename: Union[PathLike[str], str],
    reffilename: Union[PathLike[str], str],
    method: str,
    vars: Union[Sequence[str], None] = None,
) -> float:
    ...


@overload
async def deltaSimulationResults(
    self: SupportsInteractiveProperty[Asynchronous],
    filename: Union[PathLike[str], str],
    reffilename: Union[PathLike[str], str],
    method: str,
    vars: Union[Sequence[str], None] = None,
) -> float:
    ...


@external("deltaSimulationResults")
def deltaSimulationResults(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    filename: Union[PathLike[str], str],
    reffilename: Union[PathLike[str], str],
    method: str,
    vars: Union[Sequence[str], None] = None,
) -> Union[float, Coroutine[None, None, float]]:
    """
    .. code-block:: modelica

        function deltaSimulationResults
          input String filename;
          input String reffilename;
          input String method "method to compute then error. choose 1norm, 2norm, maxerr";
          input String[:] vars = fill("", 0);
          output Real result;
        end deltaSimulationResults;"""
    return ...  # type: ignore


class Diffsimulationresults(NamedTuple):
    success: bool
    failVars: List[str]


@overload
def diffSimulationResults(
    self: SupportsInteractiveProperty[Synchronous],
    actualFile: Union[PathLike[str], str],
    expectedFile: Union[PathLike[str], str],
    diffPrefix: str,
    relTol: Union[float, None] = None,
    relTolDiffMinMax: Union[float, None] = None,
    rangeDelta: Union[float, None] = None,
    vars: Union[Sequence[str], None] = None,
    keepEqualResults: Union[bool, None] = None,
) -> Diffsimulationresults:
    ...


@overload
async def diffSimulationResults(
    self: SupportsInteractiveProperty[Asynchronous],
    actualFile: Union[PathLike[str], str],
    expectedFile: Union[PathLike[str], str],
    diffPrefix: str,
    relTol: Union[float, None] = None,
    relTolDiffMinMax: Union[float, None] = None,
    rangeDelta: Union[float, None] = None,
    vars: Union[Sequence[str], None] = None,
    keepEqualResults: Union[bool, None] = None,
) -> Diffsimulationresults:
    ...


@external("diffSimulationResults")
def diffSimulationResults(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    actualFile: Union[PathLike[str], str],
    expectedFile: Union[PathLike[str], str],
    diffPrefix: str,
    relTol: Union[float, None] = None,
    relTolDiffMinMax: Union[float, None] = None,
    rangeDelta: Union[float, None] = None,
    vars: Union[Sequence[str], None] = None,
    keepEqualResults: Union[bool, None] = None,
) -> Union[
    Diffsimulationresults, Coroutine[None, None, Diffsimulationresults]
]:
    """
    .. code-block:: modelica

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
        end diffSimulationResults;"""
    return ...  # type: ignore


@overload
def diffSimulationResultsHtml(
    self: SupportsInteractiveProperty[Synchronous],
    var: str,
    actualFile: Union[PathLike[str], str],
    expectedFile: Union[PathLike[str], str],
    relTol: Union[float, None] = None,
    relTolDiffMinMax: Union[float, None] = None,
    rangeDelta: Union[float, None] = None,
) -> str:
    ...


@overload
async def diffSimulationResultsHtml(
    self: SupportsInteractiveProperty[Asynchronous],
    var: str,
    actualFile: Union[PathLike[str], str],
    expectedFile: Union[PathLike[str], str],
    relTol: Union[float, None] = None,
    relTolDiffMinMax: Union[float, None] = None,
    rangeDelta: Union[float, None] = None,
) -> str:
    ...


@external("diffSimulationResultsHtml")
def diffSimulationResultsHtml(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    var: str,
    actualFile: Union[PathLike[str], str],
    expectedFile: Union[PathLike[str], str],
    relTol: Union[float, None] = None,
    relTolDiffMinMax: Union[float, None] = None,
    rangeDelta: Union[float, None] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function diffSimulationResultsHtml
          input String var;
          input String actualFile;
          input String expectedFile;
          input Real relTol = 1e-3 "y tolerance";
          input Real relTolDiffMinMax = 1e-4 "y tolerance based on the difference between the maximum and minimum of the signal";
          input Real rangeDelta = 0.002 "x tolerance";
          output String html;
        end diffSimulationResultsHtml;"""
    return ...  # type: ignore


@overload
def checkTaskGraph(
    self: SupportsInteractiveProperty[Synchronous],
    filename: Union[PathLike[str], str],
    reffilename: Union[PathLike[str], str],
) -> List[str]:
    ...


@overload
async def checkTaskGraph(
    self: SupportsInteractiveProperty[Asynchronous],
    filename: Union[PathLike[str], str],
    reffilename: Union[PathLike[str], str],
) -> List[str]:
    ...


@external("checkTaskGraph")
def checkTaskGraph(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    filename: Union[PathLike[str], str],
    reffilename: Union[PathLike[str], str],
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function checkTaskGraph
          input String filename;
          input String reffilename;
          output String[:] result;
        end checkTaskGraph;"""
    return ...  # type: ignore


@overload
def checkCodeGraph(
    self: SupportsInteractiveProperty[Synchronous],
    graphfile: Union[PathLike[str], str],
    codefile: Union[PathLike[str], str],
) -> List[str]:
    ...


@overload
async def checkCodeGraph(
    self: SupportsInteractiveProperty[Asynchronous],
    graphfile: Union[PathLike[str], str],
    codefile: Union[PathLike[str], str],
) -> List[str]:
    ...


@external("checkCodeGraph")
def checkCodeGraph(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    graphfile: Union[PathLike[str], str],
    codefile: Union[PathLike[str], str],
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function checkCodeGraph
          input String graphfile;
          input String codefile;
          output String[:] result;
        end checkCodeGraph;"""
    return ...  # type: ignore


@overload
def val(
    self: SupportsInteractiveProperty[Synchronous],
    var: Union[VariableName, str],
    timePoint: Union[float, None] = None,
    fileName: Union[PathLike[str], str, None] = None,
) -> float:
    ...


@overload
async def val(
    self: SupportsInteractiveProperty[Asynchronous],
    var: Union[VariableName, str],
    timePoint: Union[float, None] = None,
    fileName: Union[PathLike[str], str, None] = None,
) -> float:
    ...


@external("val")
def val(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    var: Union[VariableName, str],
    timePoint: Union[float, None] = None,
    fileName: Union[PathLike[str], str, None] = None,
) -> Union[float, Coroutine[None, None, float]]:
    """
    .. code-block:: modelica

        function val
          input VariableName var;
          input Real timePoint = 0.0;
          input String fileName = "<default>" "The contents of the currentSimulationResult variable";
          output Real valAtTime;
        end val;"""
    return ...  # type: ignore


@overload
def closeSimulationResultFile(
    self: SupportsInteractiveProperty[Synchronous],
) -> bool:
    ...


@overload
async def closeSimulationResultFile(
    self: SupportsInteractiveProperty[Asynchronous],
) -> bool:
    ...


@external("closeSimulationResultFile")
def closeSimulationResultFile(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function closeSimulationResultFile
          output Boolean success;
        end closeSimulationResultFile;"""
    return ...  # type: ignore


@overload
def getParameterNames(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
) -> List[str]:
    ...


@overload
async def getParameterNames(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
) -> List[str]:
    ...


@external("getParameterNames")
def getParameterNames(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function getParameterNames
          input TypeName class_;
          output String[:] parameters;
        end getParameterNames;"""
    return ...  # type: ignore


@overload
def getParameterValue(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    parameterName: str,
) -> str:
    ...


@overload
async def getParameterValue(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    parameterName: str,
) -> str:
    ...


@external("getParameterValue")
def getParameterValue(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    parameterName: str,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getParameterValue
          input TypeName class_;
          input String parameterName;
          output String parameterValue;
        end getParameterValue;"""
    return ...  # type: ignore


@overload
def getComponentModifierNames(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    componentName: str,
) -> List[str]:
    ...


@overload
async def getComponentModifierNames(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    componentName: str,
) -> List[str]:
    ...


@external("getComponentModifierNames")
def getComponentModifierNames(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    componentName: str,
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function getComponentModifierNames
          input TypeName class_;
          input String componentName;
          output String[:] modifiers;
        end getComponentModifierNames;"""
    return ...  # type: ignore


@overload
def getComponentModifierValue(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    modifier: Union[TypeName, str],
) -> str:
    ...


@overload
async def getComponentModifierValue(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    modifier: Union[TypeName, str],
) -> str:
    ...


@external("getComponentModifierValue")
def getComponentModifierValue(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    modifier: Union[TypeName, str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getComponentModifierValue
          input TypeName class_;
          input TypeName modifier;
          output String value;
        end getComponentModifierValue;"""
    return ...  # type: ignore


@overload
def getComponentModifierValues(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    modifier: Union[TypeName, str],
) -> str:
    ...


@overload
async def getComponentModifierValues(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    modifier: Union[TypeName, str],
) -> str:
    ...


@external("getComponentModifierValues")
def getComponentModifierValues(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    modifier: Union[TypeName, str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getComponentModifierValues
          input TypeName class_;
          input TypeName modifier;
          output String value;
        end getComponentModifierValues;"""
    return ...  # type: ignore


@overload
def getInstantiatedParametersAndValues(
    self: SupportsInteractiveProperty[Synchronous], cls: Union[TypeName, str]
) -> List[str]:
    ...


@overload
async def getInstantiatedParametersAndValues(
    self: SupportsInteractiveProperty[Asynchronous], cls: Union[TypeName, str]
) -> List[str]:
    ...


@external("getInstantiatedParametersAndValues")
def getInstantiatedParametersAndValues(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cls: Union[TypeName, str],
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function getInstantiatedParametersAndValues
          input TypeName cls;
          output String[:] values;
        end getInstantiatedParametersAndValues;"""
    return ...  # type: ignore


@overload
def removeComponentModifiers(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    componentName: str,
    keepRedeclares: Union[bool, None] = None,
) -> bool:
    ...


@overload
async def removeComponentModifiers(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    componentName: str,
    keepRedeclares: Union[bool, None] = None,
) -> bool:
    ...


@external("removeComponentModifiers")
def removeComponentModifiers(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    componentName: str,
    keepRedeclares: Union[bool, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function removeComponentModifiers
          input TypeName class_;
          input String componentName;
          input Boolean keepRedeclares = false;
          output Boolean success;
        end removeComponentModifiers;"""
    return ...  # type: ignore


@overload
def removeExtendsModifiers(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    baseClassName: Union[TypeName, str],
    keepRedeclares: Union[bool, None] = None,
) -> bool:
    ...


@overload
async def removeExtendsModifiers(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    baseClassName: Union[TypeName, str],
    keepRedeclares: Union[bool, None] = None,
) -> bool:
    ...


@external("removeExtendsModifiers")
def removeExtendsModifiers(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    baseClassName: Union[TypeName, str],
    keepRedeclares: Union[bool, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function removeExtendsModifiers
          input TypeName className;
          input TypeName baseClassName;
          input Boolean keepRedeclares = false;
          output Boolean success;
        end removeExtendsModifiers;"""
    return ...  # type: ignore


@overload
def getConnectionCount(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
) -> int:
    ...


@overload
async def getConnectionCount(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
) -> int:
    ...


@external("getConnectionCount")
def getConnectionCount(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function getConnectionCount
          input TypeName className;
          output Integer count;
        end getConnectionCount;"""
    return ...  # type: ignore


@overload
def getNthConnection(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    index: int,
) -> List[str]:
    ...


@overload
async def getNthConnection(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    index: int,
) -> List[str]:
    ...


@external("getNthConnection")
def getNthConnection(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    index: int,
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function getNthConnection
          input TypeName className;
          input Integer index;
          output String[:] result;
        end getNthConnection;"""
    return ...  # type: ignore


@overload
def getAlgorithmCount(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@overload
async def getAlgorithmCount(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@external("getAlgorithmCount")
def getAlgorithmCount(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function getAlgorithmCount
          input TypeName class_;
          output Integer count;
        end getAlgorithmCount;"""
    return ...  # type: ignore


@overload
def getNthAlgorithm(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@overload
async def getNthAlgorithm(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@external("getNthAlgorithm")
def getNthAlgorithm(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    index: int,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getNthAlgorithm
          input TypeName class_;
          input Integer index;
          output String result;
        end getNthAlgorithm;"""
    return ...  # type: ignore


@overload
def getInitialAlgorithmCount(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@overload
async def getInitialAlgorithmCount(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@external("getInitialAlgorithmCount")
def getInitialAlgorithmCount(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function getInitialAlgorithmCount
          input TypeName class_;
          output Integer count;
        end getInitialAlgorithmCount;"""
    return ...  # type: ignore


@overload
def getNthInitialAlgorithm(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@overload
async def getNthInitialAlgorithm(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@external("getNthInitialAlgorithm")
def getNthInitialAlgorithm(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    index: int,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getNthInitialAlgorithm
          input TypeName class_;
          input Integer index;
          output String result;
        end getNthInitialAlgorithm;"""
    return ...  # type: ignore


@overload
def getAlgorithmItemsCount(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@overload
async def getAlgorithmItemsCount(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@external("getAlgorithmItemsCount")
def getAlgorithmItemsCount(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function getAlgorithmItemsCount
          input TypeName class_;
          output Integer count;
        end getAlgorithmItemsCount;"""
    return ...  # type: ignore


@overload
def getNthAlgorithmItem(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@overload
async def getNthAlgorithmItem(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@external("getNthAlgorithmItem")
def getNthAlgorithmItem(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    index: int,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getNthAlgorithmItem
          input TypeName class_;
          input Integer index;
          output String result;
        end getNthAlgorithmItem;"""
    return ...  # type: ignore


@overload
def getInitialAlgorithmItemsCount(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@overload
async def getInitialAlgorithmItemsCount(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@external("getInitialAlgorithmItemsCount")
def getInitialAlgorithmItemsCount(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function getInitialAlgorithmItemsCount
          input TypeName class_;
          output Integer count;
        end getInitialAlgorithmItemsCount;"""
    return ...  # type: ignore


@overload
def getNthInitialAlgorithmItem(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@overload
async def getNthInitialAlgorithmItem(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@external("getNthInitialAlgorithmItem")
def getNthInitialAlgorithmItem(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    index: int,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getNthInitialAlgorithmItem
          input TypeName class_;
          input Integer index;
          output String result;
        end getNthInitialAlgorithmItem;"""
    return ...  # type: ignore


@overload
def getEquationCount(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@overload
async def getEquationCount(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@external("getEquationCount")
def getEquationCount(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function getEquationCount
          input TypeName class_;
          output Integer count;
        end getEquationCount;"""
    return ...  # type: ignore


@overload
def getNthEquation(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@overload
async def getNthEquation(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@external("getNthEquation")
def getNthEquation(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    index: int,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getNthEquation
          input TypeName class_;
          input Integer index;
          output String result;
        end getNthEquation;"""
    return ...  # type: ignore


@overload
def getInitialEquationCount(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@overload
async def getInitialEquationCount(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@external("getInitialEquationCount")
def getInitialEquationCount(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function getInitialEquationCount
          input TypeName class_;
          output Integer count;
        end getInitialEquationCount;"""
    return ...  # type: ignore


@overload
def getNthInitialEquation(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@overload
async def getNthInitialEquation(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@external("getNthInitialEquation")
def getNthInitialEquation(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    index: int,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getNthInitialEquation
          input TypeName class_;
          input Integer index;
          output String result;
        end getNthInitialEquation;"""
    return ...  # type: ignore


@overload
def getEquationItemsCount(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@overload
async def getEquationItemsCount(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@external("getEquationItemsCount")
def getEquationItemsCount(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function getEquationItemsCount
          input TypeName class_;
          output Integer count;
        end getEquationItemsCount;"""
    return ...  # type: ignore


@overload
def getNthEquationItem(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@overload
async def getNthEquationItem(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@external("getNthEquationItem")
def getNthEquationItem(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    index: int,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getNthEquationItem
          input TypeName class_;
          input Integer index;
          output String result;
        end getNthEquationItem;"""
    return ...  # type: ignore


@overload
def getInitialEquationItemsCount(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@overload
async def getInitialEquationItemsCount(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@external("getInitialEquationItemsCount")
def getInitialEquationItemsCount(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function getInitialEquationItemsCount
          input TypeName class_;
          output Integer count;
        end getInitialEquationItemsCount;"""
    return ...  # type: ignore


@overload
def getNthInitialEquationItem(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@overload
async def getNthInitialEquationItem(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@external("getNthInitialEquationItem")
def getNthInitialEquationItem(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    index: int,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getNthInitialEquationItem
          input TypeName class_;
          input Integer index;
          output String result;
        end getNthInitialEquationItem;"""
    return ...  # type: ignore


@overload
def getAnnotationCount(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@overload
async def getAnnotationCount(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@external("getAnnotationCount")
def getAnnotationCount(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function getAnnotationCount
          input TypeName class_;
          output Integer count;
        end getAnnotationCount;"""
    return ...  # type: ignore


@overload
def getNthAnnotationString(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@overload
async def getNthAnnotationString(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    index: int,
) -> str:
    ...


@external("getNthAnnotationString")
def getNthAnnotationString(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    index: int,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getNthAnnotationString
          input TypeName class_;
          input Integer index;
          output String result;
        end getNthAnnotationString;"""
    return ...  # type: ignore


@overload
def getImportCount(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@overload
async def getImportCount(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
) -> int:
    ...


@external("getImportCount")
def getImportCount(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function getImportCount
          input TypeName class_;
          output Integer count;
        end getImportCount;"""
    return ...  # type: ignore


@overload
def getNthImport(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    index: int,
) -> List[str]:
    ...


@overload
async def getNthImport(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    index: int,
) -> List[str]:
    ...


@external("getNthImport")
def getNthImport(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    index: int,
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function getNthImport
          input TypeName class_;
          input Integer index;
          output String out[3] "{\\"Path\\",\\"Id\\",\\"Kind\\"}";
        end getNthImport;"""
    return ...  # type: ignore


@overload
def iconv(
    self: SupportsInteractiveProperty[Synchronous],
    string: str,
    from_: str,
    to: Union[str, None] = None,
) -> str:
    ...


@overload
async def iconv(
    self: SupportsInteractiveProperty[Asynchronous],
    string: str,
    from_: str,
    to: Union[str, None] = None,
) -> str:
    ...


@external("iconv")
def iconv(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    string: str,
    from_: str,
    to: Union[str, None] = None,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function iconv
          input String string;
          input String from;
          input String to = "UTF-8";
          output String result;
        end iconv;"""
    return ...  # type: ignore


@overload
def getDocumentationAnnotation(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> List[str]:
    ...


@overload
async def getDocumentationAnnotation(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> List[str]:
    ...


@external("getDocumentationAnnotation")
def getDocumentationAnnotation(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function getDocumentationAnnotation
          input TypeName cl;
          output String out[3] "{info,revision,infoHeader} TODO: Should be changed to have 2 outputs instead of an array of 2 Strings...";
        end getDocumentationAnnotation;"""
    return ...  # type: ignore


@overload
def setDocumentationAnnotation(
    self: SupportsInteractiveProperty[Synchronous],
    class_: Union[TypeName, str],
    info: Union[str, None] = None,
    revisions: Union[str, None] = None,
) -> bool:
    ...


@overload
async def setDocumentationAnnotation(
    self: SupportsInteractiveProperty[Asynchronous],
    class_: Union[TypeName, str],
    info: Union[str, None] = None,
    revisions: Union[str, None] = None,
) -> bool:
    ...


@external("setDocumentationAnnotation")
def setDocumentationAnnotation(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    class_: Union[TypeName, str],
    info: Union[str, None] = None,
    revisions: Union[str, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function setDocumentationAnnotation
          input TypeName class_;
          input String info = "";
          input String revisions = "";
          output Boolean bool;
        end setDocumentationAnnotation;"""
    return ...  # type: ignore


class Gettimestamp(NamedTuple):
    timeStamp: float
    timeStampAsString: str


@overload
def getTimeStamp(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> Gettimestamp:
    ...


@overload
async def getTimeStamp(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> Gettimestamp:
    ...


@external("getTimeStamp")
def getTimeStamp(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[Gettimestamp, Coroutine[None, None, Gettimestamp]]:
    """
    .. code-block:: modelica

        function getTimeStamp
          input TypeName cl;
          output Real timeStamp;
          output String timeStampAsString;
        end getTimeStamp;"""
    return ...  # type: ignore


@overload
def stringTypeName(
    self: SupportsInteractiveProperty[Synchronous], str: str
) -> TypeName:
    ...


@overload
async def stringTypeName(
    self: SupportsInteractiveProperty[Asynchronous], str: str
) -> TypeName:
    ...


@external("stringTypeName")
def stringTypeName(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    str: str,
) -> Union[TypeName, Coroutine[None, None, TypeName]]:
    """
    .. code-block:: modelica

        function stringTypeName
          input String str;
          output TypeName cl;
        end stringTypeName;"""
    return ...  # type: ignore


@overload
def stringVariableName(
    self: SupportsInteractiveProperty[Synchronous], str: str
) -> VariableName:
    ...


@overload
async def stringVariableName(
    self: SupportsInteractiveProperty[Asynchronous], str: str
) -> VariableName:
    ...


@external("stringVariableName")
def stringVariableName(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    str: str,
) -> Union[VariableName, Coroutine[None, None, VariableName]]:
    """
    .. code-block:: modelica

        function stringVariableName
          input String str;
          output VariableName cl;
        end stringVariableName;"""
    return ...  # type: ignore


@overload
def typeNameString(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> str:
    ...


@overload
async def typeNameString(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> str:
    ...


@external("typeNameString")
def typeNameString(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function typeNameString
          input TypeName cl;
          output String out;
        end typeNameString;"""
    return ...  # type: ignore


@overload
def typeNameStrings(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> List[str]:
    ...


@overload
async def typeNameStrings(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> List[str]:
    ...


@external("typeNameStrings")
def typeNameStrings(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function typeNameStrings
          input TypeName cl;
          output String out[:];
        end typeNameStrings;"""
    return ...  # type: ignore


@overload
def getClassComment(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> str:
    ...


@overload
async def getClassComment(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> str:
    ...


@external("getClassComment")
def getClassComment(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getClassComment
          input TypeName cl;
          output String comment;
        end getClassComment;"""
    return ...  # type: ignore


@overload
def dirname(
    self: SupportsInteractiveProperty[Synchronous],
    path: Union[PathLike[str], str],
) -> str:
    ...


@overload
async def dirname(
    self: SupportsInteractiveProperty[Asynchronous],
    path: Union[PathLike[str], str],
) -> str:
    ...


@external("dirname")
def dirname(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    path: Union[PathLike[str], str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function dirname
          input String path;
          output String dirname;
        end dirname;"""
    return ...  # type: ignore


@overload
def basename(
    self: SupportsInteractiveProperty[Synchronous],
    path: Union[PathLike[str], str],
) -> str:
    ...


@overload
async def basename(
    self: SupportsInteractiveProperty[Asynchronous],
    path: Union[PathLike[str], str],
) -> str:
    ...


@external("basename")
def basename(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    path: Union[PathLike[str], str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function basename
          input String path;
          output String basename;
        end basename;"""
    return ...  # type: ignore


@overload
def getClassRestriction(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> str:
    ...


@overload
async def getClassRestriction(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> str:
    ...


@external("getClassRestriction")
def getClassRestriction(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getClassRestriction
          input TypeName cl;
          output String restriction;
        end getClassRestriction;"""
    return ...  # type: ignore


@overload
def isType(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@overload
async def isType(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@external("isType")
def isType(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isType
          input TypeName cl;
          output Boolean b;
        end isType;"""
    return ...  # type: ignore


@overload
def isPackage(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@overload
async def isPackage(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@external("isPackage")
def isPackage(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isPackage
          input TypeName cl;
          output Boolean b;
        end isPackage;"""
    return ...  # type: ignore


@overload
def isClass(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@overload
async def isClass(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@external("isClass")
def isClass(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isClass
          input TypeName cl;
          output Boolean b;
        end isClass;"""
    return ...  # type: ignore


@overload
def isRecord(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@overload
async def isRecord(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@external("isRecord")
def isRecord(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isRecord
          input TypeName cl;
          output Boolean b;
        end isRecord;"""
    return ...  # type: ignore


@overload
def isBlock(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@overload
async def isBlock(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@external("isBlock")
def isBlock(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isBlock
          input TypeName cl;
          output Boolean b;
        end isBlock;"""
    return ...  # type: ignore


@overload
def isFunction(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@overload
async def isFunction(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@external("isFunction")
def isFunction(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isFunction
          input TypeName cl;
          output Boolean b;
        end isFunction;"""
    return ...  # type: ignore


@overload
def isPartial(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@overload
async def isPartial(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@external("isPartial")
def isPartial(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isPartial
          input TypeName cl;
          output Boolean b;
        end isPartial;"""
    return ...  # type: ignore


@overload
def isModel(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@overload
async def isModel(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@external("isModel")
def isModel(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isModel
          input TypeName cl;
          output Boolean b;
        end isModel;"""
    return ...  # type: ignore


@overload
def isConnector(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@overload
async def isConnector(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@external("isConnector")
def isConnector(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isConnector
          input TypeName cl;
          output Boolean b;
        end isConnector;"""
    return ...  # type: ignore


@overload
def isOptimization(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@overload
async def isOptimization(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@external("isOptimization")
def isOptimization(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isOptimization
          input TypeName cl;
          output Boolean b;
        end isOptimization;"""
    return ...  # type: ignore


@overload
def isEnumeration(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@overload
async def isEnumeration(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@external("isEnumeration")
def isEnumeration(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isEnumeration
          input TypeName cl;
          output Boolean b;
        end isEnumeration;"""
    return ...  # type: ignore


@overload
def isOperator(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@overload
async def isOperator(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@external("isOperator")
def isOperator(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isOperator
          input TypeName cl;
          output Boolean b;
        end isOperator;"""
    return ...  # type: ignore


@overload
def isOperatorRecord(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@overload
async def isOperatorRecord(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@external("isOperatorRecord")
def isOperatorRecord(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isOperatorRecord
          input TypeName cl;
          output Boolean b;
        end isOperatorRecord;"""
    return ...  # type: ignore


@overload
def isOperatorFunction(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@overload
async def isOperatorFunction(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> bool:
    ...


@external("isOperatorFunction")
def isOperatorFunction(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isOperatorFunction
          input TypeName cl;
          output Boolean b;
        end isOperatorFunction;"""
    return ...  # type: ignore


@overload
def isProtectedClass(
    self: SupportsInteractiveProperty[Synchronous],
    cl: Union[TypeName, str],
    c2: str,
) -> bool:
    ...


@overload
async def isProtectedClass(
    self: SupportsInteractiveProperty[Asynchronous],
    cl: Union[TypeName, str],
    c2: str,
) -> bool:
    ...


@external("isProtectedClass")
def isProtectedClass(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
    c2: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isProtectedClass
          input TypeName cl;
          input String c2;
          output Boolean b;
        end isProtectedClass;"""
    return ...  # type: ignore


@overload
def getBuiltinType(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> str:
    ...


@overload
async def getBuiltinType(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> str:
    ...


@external("getBuiltinType")
def getBuiltinType(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getBuiltinType
          input TypeName cl;
          output String name;
        end getBuiltinType;"""
    return ...  # type: ignore


@overload
def setInitXmlStartValue(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
    variableName: str,
    startValue: str,
    outputFile: Union[PathLike[str], str],
) -> Union[bool, None]:
    ...


@overload
async def setInitXmlStartValue(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
    variableName: str,
    startValue: str,
    outputFile: Union[PathLike[str], str],
) -> Union[bool, None]:
    ...


@external("setInitXmlStartValue")
def setInitXmlStartValue(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
    variableName: str,
    startValue: str,
    outputFile: Union[PathLike[str], str],
) -> Union[Union[bool, None], Coroutine[None, None, Union[bool, None]]]:
    """
    .. code-block:: modelica

        function setInitXmlStartValue
          input String fileName;
          input String variableName;
          input String startValue;
          input String outputFile;
          output Boolean success = false;
        end setInitXmlStartValue;"""
    return ...  # type: ignore


@overload
def ngspicetoModelica(
    self: SupportsInteractiveProperty[Synchronous],
    netlistfileName: Union[PathLike[str], str],
) -> Union[bool, None]:
    ...


@overload
async def ngspicetoModelica(
    self: SupportsInteractiveProperty[Asynchronous],
    netlistfileName: Union[PathLike[str], str],
) -> Union[bool, None]:
    ...


@external("ngspicetoModelica")
def ngspicetoModelica(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    netlistfileName: Union[PathLike[str], str],
) -> Union[Union[bool, None], Coroutine[None, None, Union[bool, None]]]:
    """
    .. code-block:: modelica

        function ngspicetoModelica
          input String netlistfileName;
          output Boolean success = false;
        end ngspicetoModelica;"""
    return ...  # type: ignore


@overload
def getInheritedClasses(
    self: SupportsInteractiveProperty[Synchronous], name: Union[TypeName, str]
) -> List[TypeName]:
    ...


@overload
async def getInheritedClasses(
    self: SupportsInteractiveProperty[Asynchronous], name: Union[TypeName, str]
) -> List[TypeName]:
    ...


@external("getInheritedClasses")
def getInheritedClasses(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    name: Union[TypeName, str],
) -> Union[List[TypeName], Coroutine[None, None, List[TypeName]]]:
    """
    .. code-block:: modelica

        function getInheritedClasses
          input TypeName name;
          output TypeName inheritedClasses[:];
        end getInheritedClasses;"""
    return ...  # type: ignore


@overload
def getComponentsTest(
    self: SupportsInteractiveProperty[Synchronous], name: Union[TypeName, str]
) -> List[Component]:
    ...


@overload
async def getComponentsTest(
    self: SupportsInteractiveProperty[Asynchronous], name: Union[TypeName, str]
) -> List[Component]:
    ...


@external("getComponentsTest")
def getComponentsTest(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    name: Union[TypeName, str],
) -> Union[List[Component], Coroutine[None, None, List[Component]]]:
    """
    .. code-block:: modelica

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
        end getComponentsTest;"""
    return ...  # type: ignore


@dataclass(frozen=True)
class Component(record):
    """
    .. code-block:: modelica

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
        end Component;"""

    __omc_class__ = TypeName(
        "OpenModelica.Scripting.getComponentsTest.Component"
    )
    className: str
    name: str
    comment: str
    isProtected: bool
    isFinal: bool
    isFlow: bool
    isStream: bool
    isReplaceable: bool
    variability: str
    innerOuter: str
    inputOutput: str
    dimensions: List[str]


@overload
def isExperiment(
    self: SupportsInteractiveProperty[Synchronous], name: Union[TypeName, str]
) -> bool:
    ...


@overload
async def isExperiment(
    self: SupportsInteractiveProperty[Asynchronous], name: Union[TypeName, str]
) -> bool:
    ...


@external("isExperiment")
def isExperiment(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    name: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function isExperiment
          input TypeName name;
          output Boolean res;
        end isExperiment;"""
    return ...  # type: ignore


class Getsimulationoptions(NamedTuple):
    startTime: float
    stopTime: float
    tolerance: float
    numberOfIntervals: int
    interval: float


@overload
def getSimulationOptions(
    self: SupportsInteractiveProperty[Synchronous],
    name: Union[TypeName, str],
    defaultStartTime: Union[float, None] = None,
    defaultStopTime: Union[float, None] = None,
    defaultTolerance: Union[float, None] = None,
    defaultNumberOfIntervals: Union[int, None] = None,
    defaultInterval: Union[float, None] = None,
) -> Getsimulationoptions:
    ...


@overload
async def getSimulationOptions(
    self: SupportsInteractiveProperty[Asynchronous],
    name: Union[TypeName, str],
    defaultStartTime: Union[float, None] = None,
    defaultStopTime: Union[float, None] = None,
    defaultTolerance: Union[float, None] = None,
    defaultNumberOfIntervals: Union[int, None] = None,
    defaultInterval: Union[float, None] = None,
) -> Getsimulationoptions:
    ...


@external("getSimulationOptions")
def getSimulationOptions(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    name: Union[TypeName, str],
    defaultStartTime: Union[float, None] = None,
    defaultStopTime: Union[float, None] = None,
    defaultTolerance: Union[float, None] = None,
    defaultNumberOfIntervals: Union[int, None] = None,
    defaultInterval: Union[float, None] = None,
) -> Union[Getsimulationoptions, Coroutine[None, None, Getsimulationoptions]]:
    """
    .. code-block:: modelica

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
        end getSimulationOptions;"""
    return ...  # type: ignore


@overload
def getAnnotationNamedModifiers(
    self: SupportsInteractiveProperty[Synchronous],
    name: Union[TypeName, str],
    vendorannotation: str,
) -> List[str]:
    ...


@overload
async def getAnnotationNamedModifiers(
    self: SupportsInteractiveProperty[Asynchronous],
    name: Union[TypeName, str],
    vendorannotation: str,
) -> List[str]:
    ...


@external("getAnnotationNamedModifiers")
def getAnnotationNamedModifiers(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    name: Union[TypeName, str],
    vendorannotation: str,
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function getAnnotationNamedModifiers
          input TypeName name;
          input String vendorannotation;
          output String[:] modifiernamelist;
        end getAnnotationNamedModifiers;"""
    return ...  # type: ignore


@overload
def getAnnotationModifierValue(
    self: SupportsInteractiveProperty[Synchronous],
    name: Union[TypeName, str],
    vendorannotation: str,
    modifiername: str,
) -> str:
    ...


@overload
async def getAnnotationModifierValue(
    self: SupportsInteractiveProperty[Asynchronous],
    name: Union[TypeName, str],
    vendorannotation: str,
    modifiername: str,
) -> str:
    ...


@external("getAnnotationModifierValue")
def getAnnotationModifierValue(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    name: Union[TypeName, str],
    vendorannotation: str,
    modifiername: str,
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getAnnotationModifierValue
          input TypeName name;
          input String vendorannotation;
          input String modifiername;
          output String modifiernamevalue;
        end getAnnotationModifierValue;"""
    return ...  # type: ignore


@overload
def classAnnotationExists(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    annotationName: Union[TypeName, str],
) -> bool:
    ...


@overload
async def classAnnotationExists(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    annotationName: Union[TypeName, str],
) -> bool:
    ...


@external("classAnnotationExists")
def classAnnotationExists(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    annotationName: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function classAnnotationExists
          input TypeName className;
          input TypeName annotationName;
          output Boolean exists;
        end classAnnotationExists;"""
    return ...  # type: ignore


@overload
def getBooleanClassAnnotation(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    annotationName: Union[TypeName, str],
) -> bool:
    ...


@overload
async def getBooleanClassAnnotation(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    annotationName: Union[TypeName, str],
) -> bool:
    ...


@external("getBooleanClassAnnotation")
def getBooleanClassAnnotation(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    annotationName: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function getBooleanClassAnnotation
          input TypeName className;
          input TypeName annotationName;
          output Boolean value;
        end getBooleanClassAnnotation;"""
    return ...  # type: ignore


@overload
def extendsFrom(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    baseClassName: Union[TypeName, str],
) -> bool:
    ...


@overload
async def extendsFrom(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    baseClassName: Union[TypeName, str],
) -> bool:
    ...


@external("extendsFrom")
def extendsFrom(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    baseClassName: Union[TypeName, str],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function extendsFrom
          input TypeName className;
          input TypeName baseClassName;
          output Boolean res;
        end extendsFrom;"""
    return ...  # type: ignore


@overload
def loadModelica3D(
    self: SupportsInteractiveProperty[Synchronous],
    version: Union[str, None] = None,
) -> bool:
    ...


@overload
async def loadModelica3D(
    self: SupportsInteractiveProperty[Asynchronous],
    version: Union[str, None] = None,
) -> bool:
    ...


@external("loadModelica3D")
def loadModelica3D(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    version: Union[str, None] = None,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function loadModelica3D
          input String version = "3.2.1";
          output Boolean status;
        end loadModelica3D;"""
    return ...  # type: ignore


@overload
def searchClassNames(
    self: SupportsInteractiveProperty[Synchronous],
    searchText: str,
    findInText: Union[bool, None] = None,
) -> List[TypeName]:
    ...


@overload
async def searchClassNames(
    self: SupportsInteractiveProperty[Asynchronous],
    searchText: str,
    findInText: Union[bool, None] = None,
) -> List[TypeName]:
    ...


@external("searchClassNames")
def searchClassNames(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    searchText: str,
    findInText: Union[bool, None] = None,
) -> Union[List[TypeName], Coroutine[None, None, List[TypeName]]]:
    """
    .. code-block:: modelica

        function searchClassNames
          input String searchText;
          input Boolean findInText = false;
          output TypeName classNames[:];
        end searchClassNames;"""
    return ...  # type: ignore


@overload
def getAvailableLibraries(
    self: SupportsInteractiveProperty[Synchronous],
) -> List[str]:
    ...


@overload
async def getAvailableLibraries(
    self: SupportsInteractiveProperty[Asynchronous],
) -> List[str]:
    ...


@external("getAvailableLibraries")
def getAvailableLibraries(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function getAvailableLibraries
          output String[:] libraries;
        end getAvailableLibraries;"""
    return ...  # type: ignore


@overload
def getUses(
    self: SupportsInteractiveProperty[Synchronous], pack: Union[TypeName, str]
) -> List[List[str]]:
    ...


@overload
async def getUses(
    self: SupportsInteractiveProperty[Asynchronous], pack: Union[TypeName, str]
) -> List[List[str]]:
    ...


@external("getUses")
def getUses(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    pack: Union[TypeName, str],
) -> Union[List[List[str]], Coroutine[None, None, List[List[str]]]]:
    """
    .. code-block:: modelica

        function getUses
          input TypeName pack;
          output String[:, :] uses;
        end getUses;"""
    return ...  # type: ignore


@overload
def getDerivedClassModifierNames(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
) -> List[str]:
    ...


@overload
async def getDerivedClassModifierNames(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
) -> List[str]:
    ...


@external("getDerivedClassModifierNames")
def getDerivedClassModifierNames(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function getDerivedClassModifierNames
          input TypeName className;
          output String[:] modifierNames;
        end getDerivedClassModifierNames;"""
    return ...  # type: ignore


@overload
def getDerivedClassModifierValue(
    self: SupportsInteractiveProperty[Synchronous],
    className: Union[TypeName, str],
    modifierName: Union[TypeName, str],
) -> str:
    ...


@overload
async def getDerivedClassModifierValue(
    self: SupportsInteractiveProperty[Asynchronous],
    className: Union[TypeName, str],
    modifierName: Union[TypeName, str],
) -> str:
    ...


@external("getDerivedClassModifierValue")
def getDerivedClassModifierValue(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    className: Union[TypeName, str],
    modifierName: Union[TypeName, str],
) -> Union[str, Coroutine[None, None, str]]:
    """
    .. code-block:: modelica

        function getDerivedClassModifierValue
          input TypeName className;
          input TypeName modifierName;
          output String modifierValue;
        end getDerivedClassModifierValue;"""
    return ...  # type: ignore


@overload
def generateEntryPoint(
    self: SupportsInteractiveProperty[Synchronous],
    fileName: Union[PathLike[str], str],
    entryPoint: Union[TypeName, str],
    url: Union[str, None] = None,
) -> None:
    ...


@overload
async def generateEntryPoint(
    self: SupportsInteractiveProperty[Asynchronous],
    fileName: Union[PathLike[str], str],
    entryPoint: Union[TypeName, str],
    url: Union[str, None] = None,
) -> None:
    ...


@external("generateEntryPoint")
def generateEntryPoint(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    fileName: Union[PathLike[str], str],
    entryPoint: Union[TypeName, str],
    url: Union[str, None] = None,
) -> Union[None, Coroutine[None, None, None]]:
    """
    .. code-block:: modelica

        function generateEntryPoint
          input String fileName;
          input TypeName entryPoint;
          input String url = "https://trac.openmodelica.org/OpenModelica/newticket";
        end generateEntryPoint;"""


@overload
def numProcessors(self: SupportsInteractiveProperty[Synchronous]) -> int:
    ...


@overload
async def numProcessors(
    self: SupportsInteractiveProperty[Asynchronous],
) -> int:
    ...


@external("numProcessors")
def numProcessors(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[int, Coroutine[None, None, int]]:
    """
    .. code-block:: modelica

        function numProcessors
          output Integer result;
        end numProcessors;"""
    return ...  # type: ignore


@overload
def runScriptParallel(
    self: SupportsInteractiveProperty[Synchronous],
    scripts: Sequence[str],
    numThreads: Union[int, None] = None,
    useThreads: Union[bool, None] = None,
) -> List[bool]:
    ...


@overload
async def runScriptParallel(
    self: SupportsInteractiveProperty[Asynchronous],
    scripts: Sequence[str],
    numThreads: Union[int, None] = None,
    useThreads: Union[bool, None] = None,
) -> List[bool]:
    ...


@external("runScriptParallel")
def runScriptParallel(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    scripts: Sequence[str],
    numThreads: Union[int, None] = None,
    useThreads: Union[bool, None] = None,
) -> Union[List[bool], Coroutine[None, None, List[bool]]]:
    """
    .. code-block:: modelica

        function runScriptParallel
          input String scripts[:];
          input Integer numThreads = numProcessors();
          input Boolean useThreads = false;
          output Boolean results[:];
        end runScriptParallel;"""
    return ...  # type: ignore


@overload
def exit(self: SupportsInteractiveProperty[Synchronous], status: int) -> None:
    ...


@overload
async def exit(
    self: SupportsInteractiveProperty[Asynchronous], status: int
) -> None:
    ...


@external("exit")
def exit(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    status: int,
) -> Union[None, Coroutine[None, None, None]]:
    """
    .. code-block:: modelica

        function exit
          input Integer status;
        end exit;"""


@overload
def threadWorkFailed(self: SupportsInteractiveProperty[Synchronous]) -> None:
    ...


@overload
async def threadWorkFailed(
    self: SupportsInteractiveProperty[Asynchronous],
) -> None:
    ...


@external("threadWorkFailed")
def threadWorkFailed(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[None, Coroutine[None, None, None]]:
    ...


@overload
def getMemorySize(self: SupportsInteractiveProperty[Synchronous]) -> float:
    ...


@overload
async def getMemorySize(
    self: SupportsInteractiveProperty[Asynchronous],
) -> float:
    ...


@external("getMemorySize")
def getMemorySize(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[float, Coroutine[None, None, float]]:
    """
    .. code-block:: modelica

        function getMemorySize
          output Real memory(unit = "MiB");
        end getMemorySize;"""
    return ...  # type: ignore


@overload
def GC_gcollect_and_unmap(
    self: SupportsInteractiveProperty[Synchronous],
) -> None:
    ...


@overload
async def GC_gcollect_and_unmap(
    self: SupportsInteractiveProperty[Asynchronous],
) -> None:
    ...


@external("GC_gcollect_and_unmap")
def GC_gcollect_and_unmap(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[None, Coroutine[None, None, None]]:
    ...


@overload
def GC_expand_hp(
    self: SupportsInteractiveProperty[Synchronous], size: int
) -> bool:
    ...


@overload
async def GC_expand_hp(
    self: SupportsInteractiveProperty[Asynchronous], size: int
) -> bool:
    ...


@external("GC_expand_hp")
def GC_expand_hp(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    size: int,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function GC_expand_hp
          input Integer size;
          output Boolean success;
        end GC_expand_hp;"""
    return ...  # type: ignore


@overload
def GC_set_max_heap_size(
    self: SupportsInteractiveProperty[Synchronous], size: int
) -> bool:
    ...


@overload
async def GC_set_max_heap_size(
    self: SupportsInteractiveProperty[Asynchronous], size: int
) -> bool:
    ...


@external("GC_set_max_heap_size")
def GC_set_max_heap_size(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    size: int,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function GC_set_max_heap_size
          input Integer size;
          output Boolean success;
        end GC_set_max_heap_size;"""
    return ...  # type: ignore


@dataclass(frozen=True)
class GC_PROFSTATS(record):
    """
    .. code-block:: modelica

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
        end GC_PROFSTATS;"""

    __omc_class__ = TypeName("OpenModelica.Scripting.GC_PROFSTATS")
    heapsize_full: int
    free_bytes_full: int
    unmapped_bytes: int
    bytes_allocd_since_gc: int
    allocd_bytes_before_gc: int
    non_gc_bytes: int
    gc_no: int
    markers_m1: int
    bytes_reclaimed_since_gc: int
    reclaimed_bytes_before_gc: int


@overload
def GC_get_prof_stats(
    self: SupportsInteractiveProperty[Synchronous],
) -> GC_PROFSTATS:
    ...


@overload
async def GC_get_prof_stats(
    self: SupportsInteractiveProperty[Asynchronous],
) -> GC_PROFSTATS:
    ...


@external("GC_get_prof_stats")
def GC_get_prof_stats(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[GC_PROFSTATS, Coroutine[None, None, GC_PROFSTATS]]:
    """
    .. code-block:: modelica

        function GC_get_prof_stats
          output GC_PROFSTATS gcStats;
        end GC_get_prof_stats;"""
    return ...  # type: ignore


@overload
def checkInterfaceOfPackages(
    self: SupportsInteractiveProperty[Synchronous],
    cl: Union[TypeName, str],
    dependencyMatrix: Sequence[Sequence[str]],
) -> bool:
    ...


@overload
async def checkInterfaceOfPackages(
    self: SupportsInteractiveProperty[Asynchronous],
    cl: Union[TypeName, str],
    dependencyMatrix: Sequence[Sequence[str]],
) -> bool:
    ...


@external("checkInterfaceOfPackages")
def checkInterfaceOfPackages(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
    dependencyMatrix: Sequence[Sequence[str]],
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function checkInterfaceOfPackages
          input TypeName cl;
          input String dependencyMatrix[:, :];
          output Boolean success;
        end checkInterfaceOfPackages;"""
    return ...  # type: ignore


@overload
def sortStrings(
    self: SupportsInteractiveProperty[Synchronous], arr: Sequence[str]
) -> List[str]:
    ...


@overload
async def sortStrings(
    self: SupportsInteractiveProperty[Asynchronous], arr: Sequence[str]
) -> List[str]:
    ...


@external("sortStrings")
def sortStrings(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    arr: Sequence[str],
) -> Union[List[str], Coroutine[None, None, List[str]]]:
    """
    .. code-block:: modelica

        function sortStrings
          input String arr[:];
          output String sorted[:];
        end sortStrings;"""
    return ...  # type: ignore


class Getclassinformation(NamedTuple):
    restriction: str
    comment: str
    partialPrefix: bool
    finalPrefix: bool
    encapsulatedPrefix: bool
    fileName: str
    fileReadOnly: bool
    lineNumberStart: int
    columnNumberStart: int
    lineNumberEnd: int
    columnNumberEnd: int
    dimensions: List[str]
    isProtectedClass: bool
    isDocumentationClass: bool
    version: str
    preferredView: str
    state: bool
    access: str


@overload
def getClassInformation(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> Getclassinformation:
    ...


@overload
async def getClassInformation(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> Getclassinformation:
    ...


@external("getClassInformation")
def getClassInformation(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[Getclassinformation, Coroutine[None, None, Getclassinformation]]:
    """
    .. code-block:: modelica

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
        end getClassInformation;"""
    return ...  # type: ignore


@overload
def getTransitions(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> List[List[str]]:
    ...


@overload
async def getTransitions(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> List[List[str]]:
    ...


@external("getTransitions")
def getTransitions(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[List[List[str]], Coroutine[None, None, List[List[str]]]]:
    """
    .. code-block:: modelica

        function getTransitions
          input TypeName cl;
          output String[:, :] transitions;
        end getTransitions;"""
    return ...  # type: ignore


@overload
def deleteTransition(
    self: SupportsInteractiveProperty[Synchronous],
    cl: Union[TypeName, str],
    from_: str,
    to: str,
    condition: str,
    immediate: bool,
    reset: bool,
    synchronize: bool,
    priority: int,
) -> bool:
    ...


@overload
async def deleteTransition(
    self: SupportsInteractiveProperty[Asynchronous],
    cl: Union[TypeName, str],
    from_: str,
    to: str,
    condition: str,
    immediate: bool,
    reset: bool,
    synchronize: bool,
    priority: int,
) -> bool:
    ...


@external("deleteTransition")
def deleteTransition(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
    from_: str,
    to: str,
    condition: str,
    immediate: bool,
    reset: bool,
    synchronize: bool,
    priority: int,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

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
        end deleteTransition;"""
    return ...  # type: ignore


@overload
def getInitialStates(
    self: SupportsInteractiveProperty[Synchronous], cl: Union[TypeName, str]
) -> List[List[str]]:
    ...


@overload
async def getInitialStates(
    self: SupportsInteractiveProperty[Asynchronous], cl: Union[TypeName, str]
) -> List[List[str]]:
    ...


@external("getInitialStates")
def getInitialStates(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
) -> Union[List[List[str]], Coroutine[None, None, List[List[str]]]]:
    """
    .. code-block:: modelica

        function getInitialStates
          input TypeName cl;
          output String[:, :] initialStates;
        end getInitialStates;"""
    return ...  # type: ignore


@overload
def deleteInitialState(
    self: SupportsInteractiveProperty[Synchronous],
    cl: Union[TypeName, str],
    state: str,
) -> bool:
    ...


@overload
async def deleteInitialState(
    self: SupportsInteractiveProperty[Asynchronous],
    cl: Union[TypeName, str],
    state: str,
) -> bool:
    ...


@external("deleteInitialState")
def deleteInitialState(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
    state: str,
) -> Union[bool, Coroutine[None, None, bool]]:
    """
    .. code-block:: modelica

        function deleteInitialState
          input TypeName cl;
          input String state;
          output Boolean bool;
        end deleteInitialState;"""
    return ...  # type: ignore


class Generatescriptingapi(NamedTuple):
    success: bool
    moFile: str
    qtFile: str
    qtHeader: str


@overload
def generateScriptingAPI(
    self: SupportsInteractiveProperty[Synchronous],
    cl: Union[TypeName, str],
    name: str,
) -> Generatescriptingapi:
    ...


@overload
async def generateScriptingAPI(
    self: SupportsInteractiveProperty[Asynchronous],
    cl: Union[TypeName, str],
    name: str,
) -> Generatescriptingapi:
    ...


@external("generateScriptingAPI")
def generateScriptingAPI(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ],
    cl: Union[TypeName, str],
    name: str,
) -> Union[Generatescriptingapi, Coroutine[None, None, Generatescriptingapi]]:
    """
    .. code-block:: modelica

        function generateScriptingAPI
          input TypeName cl;
          input String name;
          output Boolean success;
          output String moFile;
          output String qtFile;
          output String qtHeader;
        end generateScriptingAPI;"""
    return ...  # type: ignore


class Experimental(package[T_Calling]):
    __omc_class__ = TypeName("OpenModelica.Scripting.Experimental")
    relocateFunctions = experimental.relocateFunctions
