from __future__ import annotations
from dataclasses import dataclass
from typing import List, Sequence, Union
from typing_extensions import Annotated, Literal
from ..enumeration import DiffFormat__v_1_13, ErrorKind__v_1_13, ErrorLevel__v_1_13, ExportKind__v_1_13, FileType__v_1_13, LinearSystemSolver__v_1_13, StandardStream__v_1_13
from ..modelica import alias, external, package, record
from ..openmodelica import TypeName, VariableName
from ..session import Session as BasicSession

@external('.OpenModelica.threadData.ThreadData')
@dataclass
class ThreadData(record):
    """record ThreadData
end ThreadData;"""

class getAvailableMatchingAlgorithms:
    allChoices: List[str]
    allComments: List[str]

class getAvailableIndexReductionMethods:
    allChoices: List[str]
    allComments: List[str]

class getAvailableTearingMethods:
    allChoices: List[str]
    allComments: List[str]

class getConfigFlagValidOptions:
    validOptions: List[str]
    mainDescription: str
    descriptions: List[str]

class stat:
    success: bool
    fileSize: float
    mtime: float

class regex:
    numMatches: int
    matchedSubstrings: List[str]

class countMessages:
    numMessages: int
    numErrors: int
    numWarnings: int

class dumpXMLDAE:
    success: bool
    xmlfileName: str

class convertUnits:
    unitsCompatible: bool
    scaleFactor: float
    offset: float

class solveLinearSystem:
    X: List[float]
    info: int

class buildEncryptedPackage:
    success: bool
    commandOutput: str

@external('.OpenModelica.Scripting.simulate.SimulationResult')
@dataclass
class SimulationResult(record):
    """record SimulationResult
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

class diffSimulationResults:
    success: bool
    failVars: List[str]

class getTimeStamp:
    timeStamp: float
    timeStampAsString: str

@external('.OpenModelica.Scripting.getComponentsTest.Component')
@dataclass
class Component(record):
    """record Component
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

class getSimulationOptions:
    startTime: float
    stopTime: float
    tolerance: float
    numberOfIntervals: int
    interval: float

class getClassInformation:
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

class generateScriptingAPI:
    success: bool
    moFile: str
    qtFile: str
    qtHeader: str

@external('.OpenModelica')
class OpenModelica(package):

    @external('.OpenModelica.threadData')
    @classmethod
    def threadData(_) -> ThreadData:
        """function threadData
  output ThreadData threadData;
end threadData;"""
        raise NotImplementedError()

    @external('.OpenModelica.Internal')
    class Internal(package):

        @external('.OpenModelica.Internal.ClockConstructor')
        @classmethod
        def ClockConstructor(_) -> None:
            raise NotImplementedError()

        @external('.OpenModelica.Internal.intervalInferred')
        @classmethod
        def intervalInferred(_) -> float:
            """function intervalInferred
  output Real interval;
end intervalInferred;"""
            raise NotImplementedError()

        @external('.OpenModelica.Internal.delay2')
        @classmethod
        def delay2(_, expr: float, delayTime: float) -> float:
            """impure function delay2
  input Real expr;
  parameter input Real delayTime;
  output Real value;
end delay2;"""
            raise NotImplementedError()

        @external('.OpenModelica.Internal.delay3')
        @classmethod
        def delay3(_, expr: float, delayTime: float, delayMax: float) -> float:
            """impure function delay3
  input Real expr, delayTime;
  parameter input Real delayMax;
  output Real value;
end delay3;"""
            raise NotImplementedError()

        @external('.OpenModelica.Internal.intAbs')
        @classmethod
        def intAbs(_, v: int) -> int:
            """function intAbs
  input Integer v;
  output Integer o;
end intAbs;"""
            raise NotImplementedError()

        @external('.OpenModelica.Internal.realAbs')
        @classmethod
        def realAbs(_, v: float) -> float:
            """function realAbs
  input Real v;
  output Real o;
end realAbs;"""
            raise NotImplementedError()

        @external('.OpenModelica.Internal.intDiv')
        @classmethod
        def intDiv(_, x: int, y: int) -> int:
            """function intDiv
  input Integer x;
  input Integer y;
  output Integer z;
end intDiv;"""
            raise NotImplementedError()

        @external('.OpenModelica.Internal.realDiv')
        @classmethod
        def realDiv(_, x: float, y: float) -> float:
            """function realDiv
  input Real x;
  input Real y;
  output Real z;
end realDiv;"""
            raise NotImplementedError()

        @external('.OpenModelica.Internal.intMod')
        @classmethod
        def intMod(_, x: int, y: int) -> int:
            """function intMod
  input Integer x;
  input Integer y;
  output Integer z;
end intMod;"""
            raise NotImplementedError()

        @external('.OpenModelica.Internal.realMod')
        @classmethod
        def realMod(_, x: float, y: float) -> float:
            """function realMod
  input Real x;
  input Real y;
  output Real z;
end realMod;"""
            raise NotImplementedError()

        @external('.OpenModelica.Internal.intRem')
        @classmethod
        def intRem(_, x: int, y: int) -> int:
            """function intRem
  input Integer x;
  input Integer y;
  output Integer z;
end intRem;"""
            raise NotImplementedError()

        @external('.OpenModelica.Internal.realRem')
        @classmethod
        def realRem(_, x: float, y: float) -> float:
            """function realRem
  input Real x;
  input Real y;
  output Real z;
end realRem;"""
            raise NotImplementedError()

        @external('.OpenModelica.Internal.Architecture')
        class Architecture(package):

            @external('.OpenModelica.Internal.Architecture.numBits')
            @classmethod
            def numBits(_) -> int:
                """function numBits
  output Integer numBit;
end numBits;"""
                raise NotImplementedError()

            @external('.OpenModelica.Internal.Architecture.integerMax')
            @classmethod
            def integerMax(_) -> int:
                """function integerMax
  output Integer max;
end integerMax;"""
                raise NotImplementedError()

    @external('.OpenModelica.Scripting')
    class Scripting(package):

        @external('.OpenModelica.Scripting.CheckSettingsResult')
        @dataclass
        class CheckSettingsResult(record):
            """record CheckSettingsResult
  String OPENMODELICAHOME, OPENMODELICALIBRARY, OMC_PATH, SYSTEM_PATH, OMDEV_PATH;
  Boolean OMC_FOUND;
  String MODELICAUSERCFLAGS, WORKING_DIRECTORY;
  Boolean CREATE_FILE_WORKS, REMOVE_FILE_WORKS;
  String OS, SYSTEM_INFO, SENDDATALIBS, C_COMPILER, C_COMPILER_VERSION;
  Boolean C_COMPILER_RESPONDING, HAVE_CORBA;
  String CONFIGURE_CMDLINE;
  annotation(
    preferredView = "text");
end CheckSettingsResult;"""
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
            SENDDATALIBS: str
            C_COMPILER: str
            C_COMPILER_VERSION: str
            C_COMPILER_RESPONDING: bool
            HAVE_CORBA: bool
            CONFIGURE_CMDLINE: str

        @external('.OpenModelica.Scripting.Internal')
        class Internal(package):

            @external('.OpenModelica.Scripting.Internal.Time')
            class Time(package):

                @external('.OpenModelica.Scripting.Internal.Time.readableTime')
                @classmethod
                def readableTime(_, sec: float) -> str:
                    """function readableTime
  input Real sec;
  output String str;
end readableTime;"""
                    raise NotImplementedError()

                @external('.OpenModelica.Scripting.Internal.Time.timerTick')
                @classmethod
                def timerTick(_, index: int) -> None:
                    """function timerTick
  input Integer index;
end timerTick;"""
                    raise NotImplementedError()

                @external('.OpenModelica.Scripting.Internal.Time.timerTock')
                @classmethod
                def timerTock(_, index: int) -> float:
                    """function timerTock
  input Integer index;
  output Real elapsed;
end timerTock;"""
                    raise NotImplementedError()

                @external('.OpenModelica.Scripting.Internal.Time.timerClear')
                @classmethod
                def timerClear(_, index: int) -> None:
                    """function timerClear
  input Integer index;
end timerClear;"""
                    raise NotImplementedError()
            FileType = FileType__v_1_13

            @external('.OpenModelica.Scripting.Internal.stat')
            @classmethod
            def stat(_, name: str) -> FileType__v_1_13:
                """function stat
  input String name;
  output FileType fileType;
end stat;"""
                raise NotImplementedError()

        @external('.OpenModelica.Scripting.checkSettings')
        @classmethod
        def checkSettings(_) -> OpenModelica.Scripting.CheckSettingsResult:
            """function checkSettings
  output CheckSettingsResult result;
end checkSettings;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.loadFile')
        @classmethod
        def loadFile(_, fileName: str, encoding: str=..., uses: bool=...) -> bool:
            """function loadFile
  input String fileName;
  input String encoding = "UTF-8";
  input Boolean uses = true;
  output Boolean success;
end loadFile;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.loadFiles')
        @classmethod
        def loadFiles(_, fileNames: Sequence[str], encoding: str=..., numThreads: int=...) -> bool:
            """function loadFiles
  input String[:] fileNames;
  input String encoding = "UTF-8";
  input Integer numThreads = OpenModelica.Scripting.numProcessors();
  output Boolean success;
end loadFiles;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.loadEncryptedPackage')
        @classmethod
        def loadEncryptedPackage(_, fileName: str, workdir: str=...) -> bool:
            """function loadEncryptedPackage
  input String fileName;
  input String workdir = "<default>" "The output directory for imported encrypted files. <default> will put the files to current working directory.";
  output Boolean success;
end loadEncryptedPackage;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.reloadClass')
        @classmethod
        def reloadClass(_, name: Union[TypeName, str], encoding: str=...) -> bool:
            """function reloadClass
  input TypeName name;
  input String encoding = "UTF-8";
  output Boolean success;
end reloadClass;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.loadString')
        @classmethod
        def loadString(_, data: str, filename: str=..., encoding: str=..., merge: bool=...) -> bool:
            """function loadString
  input String data;
  input String filename = "<interactive>";
  input String encoding = "UTF-8";
  input Boolean merge = false "if merge is true the parsed AST is merged with the existing AST, default to false which means that is replaced, not merged";
  output Boolean success;
end loadString;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.parseString')
        @classmethod
        def parseString(_, data: str, filename: str=...) -> List[TypeName]:
            """function parseString
  input String data;
  input String filename = "<interactive>";
  output TypeName names[:];
end parseString;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.parseFile')
        @classmethod
        def parseFile(_, filename: str, encoding: str=...) -> List[TypeName]:
            """function parseFile
  input String filename;
  input String encoding = "UTF-8";
  output TypeName names[:];
end parseFile;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.loadFileInteractiveQualified')
        @classmethod
        def loadFileInteractiveQualified(_, filename: str, encoding: str=...) -> List[TypeName]:
            """function loadFileInteractiveQualified
  input String filename;
  input String encoding = "UTF-8";
  output TypeName names[:];
end loadFileInteractiveQualified;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.loadFileInteractive')
        @classmethod
        def loadFileInteractive(_, filename: str, encoding: str=...) -> List[TypeName]:
            """function loadFileInteractive
  input String filename;
  input String encoding = "UTF-8";
  output TypeName names[:];
end loadFileInteractive;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.system')
        @classmethod
        def system(_, callStr: str, outputFile: str=...) -> int:
            """impure function system
  input String callStr "String to call: sh -c $callStr";
  input String outputFile = "" "The output is redirected to this file (unless already done by callStr)";
  output Integer retval "Return value of the system call; usually 0 on success";
end system;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.system_parallel')
        @classmethod
        def system_parallel(_, callStr: Sequence[str], numThreads: int=...) -> List[int]:
            """impure function system_parallel
  input String callStr[:] "String to call: sh -c $callStr";
  input Integer numThreads = numProcessors();
  output Integer retval[:] "Return value of the system call; usually 0 on success";
end system_parallel;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.saveAll')
        @classmethod
        def saveAll(_, fileName: str) -> bool:
            """function saveAll
  input String fileName;
  output Boolean success;
end saveAll;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.help')
        @classmethod
        def help(_, topic: str=...) -> str:
            """function help
  input String topic = "topics";
  output String helpText;
end help;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.clear')
        @classmethod
        def clear(_) -> bool:
            """function clear
  output Boolean success;
end clear;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.clearProgram')
        @classmethod
        def clearProgram(_) -> bool:
            """function clearProgram
  output Boolean success;
end clearProgram;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.clearVariables')
        @classmethod
        def clearVariables(_) -> bool:
            """function clearVariables
  output Boolean success;
end clearVariables;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.generateHeader')
        @classmethod
        def generateHeader(_, fileName: str) -> bool:
            """function generateHeader
  input String fileName;
  output Boolean success;
end generateHeader;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.generateSeparateCode')
        @classmethod
        def generateSeparateCode(_, className: Union[TypeName, str], cleanCache: bool=...) -> bool:
            """function generateSeparateCode
  input TypeName className;
  input Boolean cleanCache = false "If true, the cache is reset between each generated package. This conserves memory at the cost of speed.";
  output Boolean success;
end generateSeparateCode;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.generateSeparateCodeDependencies')
        @classmethod
        def generateSeparateCodeDependencies(_, stampSuffix: str=...) -> List[str]:
            """function generateSeparateCodeDependencies
  input String stampSuffix = ".c" "Suffix to add to dependencies (often .c.stamp)";
  output String[:] dependencies;
end generateSeparateCodeDependencies;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.generateSeparateCodeDependenciesMakefile')
        @classmethod
        def generateSeparateCodeDependenciesMakefile(_, filename: str, directory: str=..., suffix: str=...) -> bool:
            """function generateSeparateCodeDependenciesMakefile
  input String filename "The file to write the makefile to";
  input String directory = "" "The relative path of the generated files";
  input String suffix = ".c" "Often .stamp since we do not update all the files";
  output Boolean success;
end generateSeparateCodeDependenciesMakefile;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getLinker')
        @classmethod
        def getLinker(_) -> str:
            """function getLinker
  output String linker;
end getLinker;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setLinker')
        @classmethod
        def setLinker(_, linker: str) -> bool:
            """function setLinker
  input String linker;
  output Boolean success;
end setLinker;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getLinkerFlags')
        @classmethod
        def getLinkerFlags(_) -> str:
            """function getLinkerFlags
  output String linkerFlags;
end getLinkerFlags;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setLinkerFlags')
        @classmethod
        def setLinkerFlags(_, linkerFlags: str) -> bool:
            """function setLinkerFlags
  input String linkerFlags;
  output Boolean success;
end setLinkerFlags;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getCompiler')
        @classmethod
        def getCompiler(_) -> str:
            """function getCompiler
  output String compiler;
end getCompiler;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setCompiler')
        @classmethod
        def setCompiler(_, compiler: str) -> bool:
            """function setCompiler
  input String compiler;
  output Boolean success;
end setCompiler;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setCFlags')
        @classmethod
        def setCFlags(_, inString: str) -> bool:
            """function setCFlags
  input String inString;
  output Boolean success;
end setCFlags;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getCFlags')
        @classmethod
        def getCFlags(_) -> str:
            """function getCFlags
  output String outString;
end getCFlags;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getCXXCompiler')
        @classmethod
        def getCXXCompiler(_) -> str:
            """function getCXXCompiler
  output String compiler;
end getCXXCompiler;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setCXXCompiler')
        @classmethod
        def setCXXCompiler(_, compiler: str) -> bool:
            """function setCXXCompiler
  input String compiler;
  output Boolean success;
end setCXXCompiler;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.verifyCompiler')
        @classmethod
        def verifyCompiler(_) -> bool:
            """function verifyCompiler
  output Boolean compilerWorks;
end verifyCompiler;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setCompilerPath')
        @classmethod
        def setCompilerPath(_, compilerPath: str) -> bool:
            """function setCompilerPath
  input String compilerPath;
  output Boolean success;
end setCompilerPath;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getCompileCommand')
        @classmethod
        def getCompileCommand(_) -> str:
            """function getCompileCommand
  output String compileCommand;
end getCompileCommand;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setCompileCommand')
        @classmethod
        def setCompileCommand(_, compileCommand: str) -> bool:
            """function setCompileCommand
  input String compileCommand;
  output Boolean success;
end setCompileCommand;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setPlotCommand')
        @classmethod
        def setPlotCommand(_, plotCommand: str) -> bool:
            """function setPlotCommand
  input String plotCommand;
  output Boolean success;
end setPlotCommand;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getSettings')
        @classmethod
        def getSettings(_) -> str:
            """function getSettings
  output String settings;
end getSettings;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setTempDirectoryPath')
        @classmethod
        def setTempDirectoryPath(_, tempDirectoryPath: str) -> bool:
            """function setTempDirectoryPath
  input String tempDirectoryPath;
  output Boolean success;
end setTempDirectoryPath;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getTempDirectoryPath')
        @classmethod
        def getTempDirectoryPath(_) -> str:
            """function getTempDirectoryPath
  output String tempDirectoryPath;
end getTempDirectoryPath;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getEnvironmentVar')
        @classmethod
        def getEnvironmentVar(_, var: str) -> str:
            """function getEnvironmentVar
  input String var;
  output String value "returns empty string on failure";
end getEnvironmentVar;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setEnvironmentVar')
        @classmethod
        def setEnvironmentVar(_, var: str, value: str) -> bool:
            """function setEnvironmentVar
  input String var;
  input String value;
  output Boolean success;
end setEnvironmentVar;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.appendEnvironmentVar')
        @classmethod
        def appendEnvironmentVar(_, var: str, value: str) -> str:
            """function appendEnvironmentVar
  input String var;
  input String value;
  output String result "returns \\"error\\" if the variable could not be appended";
end appendEnvironmentVar;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setInstallationDirectoryPath')
        @classmethod
        def setInstallationDirectoryPath(_, installationDirectoryPath: str) -> bool:
            """function setInstallationDirectoryPath
  input String installationDirectoryPath;
  output Boolean success;
end setInstallationDirectoryPath;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getInstallationDirectoryPath')
        @classmethod
        def getInstallationDirectoryPath(_) -> str:
            """function getInstallationDirectoryPath
  output String installationDirectoryPath;
end getInstallationDirectoryPath;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setModelicaPath')
        @classmethod
        def setModelicaPath(_, modelicaPath: str) -> bool:
            """function setModelicaPath
  input String modelicaPath;
  output Boolean success;
end setModelicaPath;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getModelicaPath')
        @classmethod
        def getModelicaPath(_) -> str:
            """function getModelicaPath
  output String modelicaPath;
end getModelicaPath;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setCompilerFlags')
        @classmethod
        def setCompilerFlags(_, compilerFlags: str) -> bool:
            """function setCompilerFlags
  input String compilerFlags;
  output Boolean success;
end setCompilerFlags;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setDebugFlags')
        @classmethod
        def setDebugFlags(_, debugFlags: str) -> bool:
            """function setDebugFlags
  input String debugFlags;
  output Boolean success;
end setDebugFlags;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.clearDebugFlags')
        @classmethod
        def clearDebugFlags(_) -> bool:
            """function clearDebugFlags
  output Boolean success;
end clearDebugFlags;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setPreOptModules')
        @classmethod
        def setPreOptModules(_, modules: str) -> bool:
            """function setPreOptModules
  input String modules;
  output Boolean success;
end setPreOptModules;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setCheapMatchingAlgorithm')
        @classmethod
        def setCheapMatchingAlgorithm(_, matchingAlgorithm: int) -> bool:
            """function setCheapMatchingAlgorithm
  input Integer matchingAlgorithm;
  output Boolean success;
end setCheapMatchingAlgorithm;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getMatchingAlgorithm')
        @classmethod
        def getMatchingAlgorithm(_) -> str:
            """function getMatchingAlgorithm
  output String selected;
end getMatchingAlgorithm;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getAvailableMatchingAlgorithms')
        @classmethod
        def getAvailableMatchingAlgorithms(_) -> getAvailableMatchingAlgorithms:
            """function getAvailableMatchingAlgorithms
  output String[:] allChoices;
  output String[:] allComments;
end getAvailableMatchingAlgorithms;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setMatchingAlgorithm')
        @classmethod
        def setMatchingAlgorithm(_, matchingAlgorithm: str) -> bool:
            """function setMatchingAlgorithm
  input String matchingAlgorithm;
  output Boolean success;
end setMatchingAlgorithm;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getIndexReductionMethod')
        @classmethod
        def getIndexReductionMethod(_) -> str:
            """function getIndexReductionMethod
  output String selected;
end getIndexReductionMethod;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getAvailableIndexReductionMethods')
        @classmethod
        def getAvailableIndexReductionMethods(_) -> getAvailableIndexReductionMethods:
            """function getAvailableIndexReductionMethods
  output String[:] allChoices;
  output String[:] allComments;
end getAvailableIndexReductionMethods;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setIndexReductionMethod')
        @classmethod
        def setIndexReductionMethod(_, method: str) -> bool:
            """function setIndexReductionMethod
  input String method;
  output Boolean success;
end setIndexReductionMethod;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setPostOptModules')
        @classmethod
        def setPostOptModules(_, modules: str) -> bool:
            """function setPostOptModules
  input String modules;
  output Boolean success;
end setPostOptModules;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getTearingMethod')
        @classmethod
        def getTearingMethod(_) -> str:
            """function getTearingMethod
  output String selected;
end getTearingMethod;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getAvailableTearingMethods')
        @classmethod
        def getAvailableTearingMethods(_) -> getAvailableTearingMethods:
            """function getAvailableTearingMethods
  output String[:] allChoices;
  output String[:] allComments;
end getAvailableTearingMethods;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setTearingMethod')
        @classmethod
        def setTearingMethod(_, tearingMethod: str) -> bool:
            """function setTearingMethod
  input String tearingMethod;
  output Boolean success;
end setTearingMethod;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setCommandLineOptions')
        @classmethod
        def setCommandLineOptions(_, option: str) -> bool:
            """function setCommandLineOptions
  input String option;
  output Boolean success;
end setCommandLineOptions;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getCommandLineOptions')
        @classmethod
        def getCommandLineOptions(_) -> List[str]:
            """function getCommandLineOptions
  output String[:] flags;
end getCommandLineOptions;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getConfigFlagValidOptions')
        @classmethod
        def getConfigFlagValidOptions(_, flag: str) -> getConfigFlagValidOptions:
            """function getConfigFlagValidOptions
  input String flag;
  output String validOptions[:];
  output String mainDescription;
  output String descriptions[:];
end getConfigFlagValidOptions;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.clearCommandLineOptions')
        @classmethod
        def clearCommandLineOptions(_) -> bool:
            """function clearCommandLineOptions
  output Boolean success;
end clearCommandLineOptions;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getVersion')
        @classmethod
        def getVersion(_, cl: Union[TypeName, str]=...) -> str:
            """function getVersion
  input TypeName cl = $Code(OpenModelica);
  output String version;
end getVersion;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.regularFileExists')
        @classmethod
        def regularFileExists(_, fileName: str) -> bool:
            """function regularFileExists
  input String fileName;
  output Boolean exists;
end regularFileExists;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.directoryExists')
        @classmethod
        def directoryExists(_, dirName: str) -> bool:
            """function directoryExists
  input String dirName;
  output Boolean exists;
end directoryExists;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.stat')
        @classmethod
        def stat(_, fileName: str) -> stat:
            """impure function stat
  input String fileName;
  output Boolean success;
  output Real fileSize;
  output Real mtime;
end stat;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.readFile')
        @classmethod
        def readFile(_, fileName: str) -> str:
            """impure function readFile
  input String fileName;
  output String contents;
end readFile;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.writeFile')
        @classmethod
        def writeFile(_, fileName: str, data: str, append: bool=...) -> bool:
            """impure function writeFile
  input String fileName;
  input String data;
  input Boolean append = false;
  output Boolean success;
end writeFile;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.compareFilesAndMove')
        @classmethod
        def compareFilesAndMove(_, newFile: str, oldFile: str) -> bool:
            """impure function compareFilesAndMove
  input String newFile;
  input String oldFile;
  output Boolean success;
end compareFilesAndMove;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.compareFiles')
        @classmethod
        def compareFiles(_, file1: str, file2: str) -> bool:
            """impure function compareFiles
  input String file1;
  input String file2;
  output Boolean isEqual;
end compareFiles;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.alarm')
        @classmethod
        def alarm(_, seconds: int) -> int:
            """impure function alarm
  input Integer seconds;
  output Integer previousSeconds;
end alarm;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.regex')
        @classmethod
        def regex(_, str: str, re: str, maxMatches: int=..., extended: bool=..., caseInsensitive: bool=...) -> regex:
            """function regex
  input String str;
  input String re;
  input Integer maxMatches = 1 "The maximum number of matches that will be returned";
  input Boolean extended = true "Use POSIX extended or regular syntax";
  input Boolean caseInsensitive = false;
  output Integer numMatches "-1 is an error, 0 means no match, else returns a number 1..maxMatches";
  output String matchedSubstrings[maxMatches] "unmatched strings are returned as empty";
end regex;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.regexBool')
        @classmethod
        def regexBool(_, str: str, re: str, extended: bool=..., caseInsensitive: bool=...) -> bool:
            """function regexBool
  input String str;
  input String re;
  input Boolean extended = true "Use POSIX extended or regular syntax";
  input Boolean caseInsensitive = false;
  output Boolean matches;
end regexBool;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.testsuiteFriendlyName')
        @classmethod
        def testsuiteFriendlyName(_, path: str) -> str:
            """function testsuiteFriendlyName
  input String path;
  output String fixed;
end testsuiteFriendlyName;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.readFileNoNumeric')
        @classmethod
        def readFileNoNumeric(_, fileName: str) -> str:
            """function readFileNoNumeric
  input String fileName;
  output String contents;
end readFileNoNumeric;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getErrorString')
        @classmethod
        def getErrorString(_, warningsAsErrors: bool=...) -> str:
            """impure function getErrorString
  input Boolean warningsAsErrors = false;
  output String errorString;
end getErrorString;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getMessagesString')
        @classmethod
        def getMessagesString(_) -> str:
            """function getMessagesString
  output String messagesString;
end getMessagesString;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.SourceInfo')
        @dataclass
        class SourceInfo(record):
            """record SourceInfo
  String fileName;
  Boolean readonly;
  Integer lineStart;
  Integer columnStart;
  Integer lineEnd;
  Integer columnEnd;
  annotation(
    preferredView = "text");
end SourceInfo;"""
            fileName: str
            readonly: bool
            lineStart: int
            columnStart: int
            lineEnd: int
            columnEnd: int
        ErrorKind = ErrorKind__v_1_13
        ErrorLevel = ErrorLevel__v_1_13

        @external('.OpenModelica.Scripting.ErrorMessage')
        @dataclass
        class ErrorMessage(record):
            """record ErrorMessage
  SourceInfo info;
  String message "After applying the individual arguments";
  ErrorKind kind;
  ErrorLevel level;
  Integer id "Internal ID of the error (just ignore this)";
  annotation(
    preferredView = "text");
end ErrorMessage;"""
            info: OpenModelica.Scripting.SourceInfo
            message: str
            kind: ErrorKind__v_1_13
            level: ErrorLevel__v_1_13
            id: int

        @external('.OpenModelica.Scripting.getMessagesStringInternal')
        @classmethod
        def getMessagesStringInternal(_, unique: bool=...) -> List[OpenModelica.Scripting.ErrorMessage]:
            """function getMessagesStringInternal
  input Boolean unique = true;
  output ErrorMessage[:] messagesString;
end getMessagesStringInternal;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.countMessages')
        @classmethod
        def countMessages(_) -> countMessages:
            """function countMessages
  output Integer numMessages;
  output Integer numErrors;
  output Integer numWarnings;
end countMessages;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.clearMessages')
        @classmethod
        def clearMessages(_) -> bool:
            """function clearMessages
  output Boolean success;
end clearMessages;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.runScript')
        @classmethod
        def runScript(_, fileName: str) -> str:
            """impure function runScript
  input String fileName "*.mos";
  output String result;
end runScript;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.echo')
        @classmethod
        def echo(_, setEcho: bool) -> bool:
            """function echo
  input Boolean setEcho;
  output Boolean newEcho;
end echo;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getClassesInModelicaPath')
        @classmethod
        def getClassesInModelicaPath(_) -> str:
            """function getClassesInModelicaPath
  output String classesInModelicaPath;
end getClassesInModelicaPath;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getAnnotationVersion')
        @classmethod
        def getAnnotationVersion(_) -> str:
            """function getAnnotationVersion
  output String annotationVersion;
end getAnnotationVersion;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setAnnotationVersion')
        @classmethod
        def setAnnotationVersion(_, annotationVersion: str) -> bool:
            """function setAnnotationVersion
  input String annotationVersion;
  output Boolean success;
end setAnnotationVersion;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getNoSimplify')
        @classmethod
        def getNoSimplify(_) -> bool:
            """function getNoSimplify
  output Boolean noSimplify;
end getNoSimplify;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setNoSimplify')
        @classmethod
        def setNoSimplify(_, noSimplify: bool) -> bool:
            """function setNoSimplify
  input Boolean noSimplify;
  output Boolean success;
end setNoSimplify;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getVectorizationLimit')
        @classmethod
        def getVectorizationLimit(_) -> int:
            """function getVectorizationLimit
  output Integer vectorizationLimit;
end getVectorizationLimit;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setVectorizationLimit')
        @classmethod
        def setVectorizationLimit(_, vectorizationLimit: int) -> bool:
            """function setVectorizationLimit
  input Integer vectorizationLimit;
  output Boolean success;
end setVectorizationLimit;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getDefaultOpenCLDevice')
        @classmethod
        def getDefaultOpenCLDevice(_) -> int:
            """function getDefaultOpenCLDevice
  output Integer defdevid;
end getDefaultOpenCLDevice;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setDefaultOpenCLDevice')
        @classmethod
        def setDefaultOpenCLDevice(_, defdevid: int) -> bool:
            """function setDefaultOpenCLDevice
  input Integer defdevid;
  output Boolean success;
end setDefaultOpenCLDevice;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setShowAnnotations')
        @classmethod
        def setShowAnnotations(_, show: bool) -> bool:
            """function setShowAnnotations
  input Boolean show;
  output Boolean success;
end setShowAnnotations;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getShowAnnotations')
        @classmethod
        def getShowAnnotations(_) -> bool:
            """function getShowAnnotations
  output Boolean show;
end getShowAnnotations;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setOrderConnections')
        @classmethod
        def setOrderConnections(_, orderConnections: bool) -> bool:
            """function setOrderConnections
  input Boolean orderConnections;
  output Boolean success;
end setOrderConnections;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getOrderConnections')
        @classmethod
        def getOrderConnections(_) -> bool:
            """function getOrderConnections
  output Boolean orderConnections;
end getOrderConnections;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setLanguageStandard')
        @classmethod
        def setLanguageStandard(_, inVersion: str) -> bool:
            """function setLanguageStandard
  input String inVersion;
  output Boolean success;
end setLanguageStandard;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getLanguageStandard')
        @classmethod
        def getLanguageStandard(_) -> str:
            """function getLanguageStandard
  output String outVersion;
end getLanguageStandard;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getAstAsCorbaString')
        @classmethod
        def getAstAsCorbaString(_, fileName: str=...) -> str:
            """function getAstAsCorbaString
  input String fileName = "<interactive>";
  output String result "returns the string if fileName is interactive; else it returns ok or error depending on if writing the file succeeded";
end getAstAsCorbaString;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.cd')
        @classmethod
        def cd(_, newWorkingDirectory: str=...) -> str:
            """function cd
  input String newWorkingDirectory = "";
  output String workingDirectory;
end cd;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.mkdir')
        @classmethod
        def mkdir(_, newDirectory: str) -> bool:
            """function mkdir
  input String newDirectory;
  output Boolean success;
end mkdir;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.copy')
        @classmethod
        def copy(_, source: str, destination: str) -> bool:
            """function copy
  input String source;
  input String destination;
  output Boolean success;
end copy;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.remove')
        @classmethod
        def remove(_, path: str) -> bool:
            """function remove
  input String path;
  output Boolean success "Returns true on success.";
end remove;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.checkModel')
        @classmethod
        def checkModel(_, className: Union[TypeName, str]) -> str:
            """function checkModel
  input TypeName className;
  output String result;
end checkModel;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.checkAllModelsRecursive')
        @classmethod
        def checkAllModelsRecursive(_, className: Union[TypeName, str], checkProtected: bool=...) -> str:
            """function checkAllModelsRecursive
  input TypeName className;
  input Boolean checkProtected = false "Checks also protected classes if true";
  output String result;
end checkAllModelsRecursive;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.typeOf')
        @classmethod
        def typeOf(_, variableName: Union[VariableName, str]) -> str:
            """function typeOf
  input VariableName variableName;
  output String result;
end typeOf;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.instantiateModel')
        @classmethod
        def instantiateModel(_, className: Union[TypeName, str]) -> str:
            """function instantiateModel
  input TypeName className;
  output String result;
end instantiateModel;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.buildOpenTURNSInterface')
        @classmethod
        def buildOpenTURNSInterface(_, className: Union[TypeName, str], pythonTemplateFile: str, showFlatModelica: bool=...) -> str:
            """function buildOpenTURNSInterface
  input TypeName className;
  input String pythonTemplateFile;
  input Boolean showFlatModelica = false;
  output String outPythonScript;
end buildOpenTURNSInterface;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.runOpenTURNSPythonScript')
        @classmethod
        def runOpenTURNSPythonScript(_, pythonScriptFile: str) -> str:
            """function runOpenTURNSPythonScript
  input String pythonScriptFile;
  output String logOutputFile;
end runOpenTURNSPythonScript;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.generateCode')
        @classmethod
        def generateCode(_, className: Union[TypeName, str]) -> bool:
            """function generateCode
  input TypeName className;
  output Boolean success;
end generateCode;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.loadModel')
        @classmethod
        def loadModel(_, className: Union[TypeName, str], priorityVersion: Sequence[str]=..., notify: bool=..., languageStandard: str=..., requireExactVersion: bool=...) -> bool:
            """function loadModel
  input TypeName className;
  input String[:] priorityVersion = {"default"};
  input Boolean notify = false "Give a notification of the libraries and versions that were loaded";
  input String languageStandard = "" "Override the set language standard. Parse with the given setting, but do not change it permanently.";
  input Boolean requireExactVersion = false "If the version is required to be exact, if there is a uses Modelica(version=\\"3.2\\"), Modelica 3.2.1 will not match it.";
  output Boolean success;
end loadModel;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.deleteFile')
        @classmethod
        def deleteFile(_, fileName: str) -> bool:
            """function deleteFile
  input String fileName;
  output Boolean success;
end deleteFile;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.saveModel')
        @classmethod
        def saveModel(_, fileName: str, className: Union[TypeName, str]) -> bool:
            """function saveModel
  input String fileName;
  input TypeName className;
  output Boolean success;
end saveModel;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.saveTotalModel')
        @classmethod
        def saveTotalModel(_, fileName: str, className: Union[TypeName, str], stripAnnotations: bool=..., stripComments: bool=...) -> bool:
            """function saveTotalModel
  input String fileName;
  input TypeName className;
  input Boolean stripAnnotations = false;
  input Boolean stripComments = false;
  output Boolean success;
end saveTotalModel;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.save')
        @classmethod
        def save(_, className: Union[TypeName, str]) -> bool:
            """function save
  input TypeName className;
  output Boolean success;
end save;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.saveTotalSCode')
        @classmethod
        def saveTotalSCode(_) -> None:
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.translateGraphics')
        @classmethod
        def translateGraphics(_, className: Union[TypeName, str]) -> str:
            """function translateGraphics
  input TypeName className;
  output String result;
end translateGraphics;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.dumpXMLDAE')
        @classmethod
        def dumpXMLDAE(_, className: Union[TypeName, str], translationLevel: str=..., addOriginalIncidenceMatrix: bool=..., addSolvingInfo: bool=..., addMathMLCode: bool=..., dumpResiduals: bool=..., fileNamePrefix: str=..., rewriteRulesFile: str=...) -> dumpXMLDAE:
            """function dumpXMLDAE
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
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.convertUnits')
        @classmethod
        def convertUnits(_, s1: str, s2: str) -> convertUnits:
            """function convertUnits
  input String s1;
  input String s2;
  output Boolean unitsCompatible;
  output Real scaleFactor;
  output Real offset;
end convertUnits;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getDerivedUnits')
        @classmethod
        def getDerivedUnits(_, baseUnit: str) -> List[str]:
            """function getDerivedUnits
  input String baseUnit;
  output String[:] derivedUnits;
end getDerivedUnits;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.listVariables')
        @classmethod
        def listVariables(_) -> List[TypeName]:
            """function listVariables
  output TypeName variables[:];
end listVariables;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.strtok')
        @classmethod
        def strtok(_, string: str, token: str) -> List[str]:
            """function strtok
  input String string;
  input String token;
  output String[:] strings;
end strtok;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.stringSplit')
        @classmethod
        def stringSplit(_, string: str, token: str) -> List[str]:
            """function stringSplit
  input String string;
  input String token "single character only";
  output String[:] strings;
end stringSplit;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.stringReplace')
        @classmethod
        def stringReplace(_, str: str, source: str, target: str) -> str:
            """function stringReplace
  input String str;
  input String source;
  input String target;
  output String res;
end stringReplace;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.escapeXML')
        @classmethod
        def escapeXML(_, inStr: str) -> str:
            """function escapeXML
  input String inStr;
  output String outStr;
end escapeXML;"""
            raise NotImplementedError()
        ExportKind = ExportKind__v_1_13

        @external('.OpenModelica.Scripting.list')
        @classmethod
        def list(_, class_: Union[TypeName, str]=..., interfaceOnly: bool=..., shortOnly: bool=..., exportKind: Union[ExportKind__v_1_13, Literal['Absyn', 1, 'SCode', 2, 'MetaModelicaInterface', 3, 'Internal', 4]]=...) -> str:
            """function list
  input TypeName class_ = $Code(AllLoadedClasses);
  input Boolean interfaceOnly = false;
  input Boolean shortOnly = false "only short class definitions";
  input ExportKind exportKind = ExportKind.Absyn;
  output String contents;
end list;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.listFile')
        @classmethod
        def listFile(_, class_: Union[TypeName, str]) -> str:
            """function listFile
  input TypeName class_;
  output String contents;
end listFile;"""
            raise NotImplementedError()
        DiffFormat = DiffFormat__v_1_13

        @external('.OpenModelica.Scripting.diffModelicaFileListings')
        @classmethod
        def diffModelicaFileListings(_, before: str, after: str, diffFormat: Union[DiffFormat__v_1_13, Literal['plain', 1, 'color', 2, 'xml', 3]]=...) -> str:
            """function diffModelicaFileListings
  input String before, after;
  input DiffFormat diffFormat = DiffFormat.color;
  output String result;
end diffModelicaFileListings;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.exportToFigaro')
        @classmethod
        def exportToFigaro(_, path: Union[TypeName, str], database: str, mode: str, options: str, processor: str, directory: str=...) -> bool:
            """function exportToFigaro
  input TypeName path;
  input String directory = cd();
  input String database;
  input String mode;
  input String options;
  input String processor;
  output Boolean success;
end exportToFigaro;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.inferBindings')
        @classmethod
        def inferBindings(_, path: Union[TypeName, str]) -> bool:
            """function inferBindings
  input TypeName path;
  output Boolean success;
end inferBindings;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.generateVerificationScenarios')
        @classmethod
        def generateVerificationScenarios(_, path: Union[TypeName, str]) -> bool:
            """function generateVerificationScenarios
  input TypeName path;
  output Boolean success;
end generateVerificationScenarios;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.rewriteBlockCall')
        @classmethod
        def rewriteBlockCall(_, className: Union[TypeName, str], inDefs: Union[TypeName, str]) -> bool:
            """function rewriteBlockCall
  input TypeName className;
  input TypeName inDefs;
  output Boolean success;
end rewriteBlockCall;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.realpath')
        @classmethod
        def realpath(_, name: str) -> str:
            """function realpath
  input String name "Absolute or relative file or directory name";
  output String fullName "Full path of 'name'";
end realpath;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.uriToFilename')
        @classmethod
        def uriToFilename(_, uri: str) -> str:
            """function uriToFilename
  input String uri;
  output String filename = "";
end uriToFilename;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getLoadedLibraries')
        @classmethod
        def getLoadedLibraries(_) -> List[List[str]]:
            """function getLoadedLibraries
  output String[:, 2] libraries;
end getLoadedLibraries;"""
            raise NotImplementedError()
        LinearSystemSolver = LinearSystemSolver__v_1_13

        @external('.OpenModelica.Scripting.solveLinearSystem')
        @classmethod
        def solveLinearSystem(_, A: Sequence[Sequence[float]], B: Sequence[float], solver: Union[LinearSystemSolver__v_1_13, Literal['dgesv', 1, 'lpsolve55', 2]]=..., isInt: Sequence[int]=...) -> solveLinearSystem:
            """function solveLinearSystem
  input Real[size(B, 1), size(B, 1)] A;
  input Real[:] B;
  input LinearSystemSolver solver = LinearSystemSolver.dgesv;
  input Integer[:] isInt = {-1} "list of indices that are integers";
  output Real[size(B, 1)] X;
  output Integer info;
end solveLinearSystem;"""
            raise NotImplementedError()
        StandardStream = StandardStream__v_1_13

        @external('.OpenModelica.Scripting.reopenStandardStream')
        @classmethod
        def reopenStandardStream(_, _stream: Union[StandardStream__v_1_13, Literal['stdin', 1, 'stdout', 2, 'stderr', 3]], filename: str) -> bool:
            """function reopenStandardStream
  input StandardStream _stream;
  input String filename;
  output Boolean success;
end reopenStandardStream;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.importFMU')
        @classmethod
        def importFMU(_, filename: str, workdir: str=..., loglevel: int=..., fullPath: bool=..., debugLogging: bool=..., generateInputConnectors: bool=..., generateOutputConnectors: bool=...) -> str:
            """function importFMU
  input String filename "the fmu file name";
  input String workdir = "<default>" "The output directory for imported FMU files. <default> will put the files to current working directory.";
  input Integer loglevel = 3 "loglevel_nothing=0;loglevel_fatal=1;loglevel_error=2;loglevel_warning=3;loglevel_info=4;loglevel_verbose=5;loglevel_debug=6";
  input Boolean fullPath = false "When true the full output path is returned otherwise only the file name.";
  input Boolean debugLogging = false "When true the FMU's debug output is printed.";
  input Boolean generateInputConnectors = true "When true creates the input connector pins.";
  input Boolean generateOutputConnectors = true "When true creates the output connector pins.";
  output String generatedFileName "Returns the full path of the generated file.";
end importFMU;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.importFMUModelDescription')
        @classmethod
        def importFMUModelDescription(_, filename: str, workdir: str=..., loglevel: int=..., fullPath: bool=..., debugLogging: bool=..., generateInputConnectors: bool=..., generateOutputConnectors: bool=...) -> str:
            """function importFMUModelDescription
  input String filename "the fmu file name";
  input String workdir = "<default>" "The output directory for imported FMU files. <default> will put the files to current working directory.";
  input Integer loglevel = 3 "loglevel_nothing=0;loglevel_fatal=1;loglevel_error=2;loglevel_warning=3;loglevel_info=4;loglevel_verbose=5;loglevel_debug=6";
  input Boolean fullPath = false "When true the full output path is returned otherwise only the file name.";
  input Boolean debugLogging = false "When true the FMU's debug output is printed.";
  input Boolean generateInputConnectors = true "When true creates the input connector pins.";
  input Boolean generateOutputConnectors = true "When true creates the output connector pins.";
  output String generatedFileName "Returns the full path of the generated file.";
end importFMUModelDescription;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.translateModelFMU')
        @classmethod
        def translateModelFMU(_, className: Union[TypeName, str], version: str=..., fmuType: str=..., fileNamePrefix: str=..., includeResources: bool=...) -> str:
            """function translateModelFMU
  input TypeName className "the class that should translated";
  input String version = "2.0" "FMU version, 1.0 or 2.0.";
  input String fmuType = "me" "FMU type, me (model exchange), cs (co-simulation), me_cs (both model exchange and co-simulation)";
  input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \\"className\\"";
  input Boolean includeResources = false "include Modelica based resources via loadResource or not";
  output String generatedFileName "Returns the full path of the generated FMU.";
end translateModelFMU;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.buildModelFMU')
        @classmethod
        def buildModelFMU(_, className: Union[TypeName, str], version: str=..., fmuType: str=..., fileNamePrefix: str=..., platforms: Sequence[str]=..., includeResources: bool=...) -> str:
            """function buildModelFMU
  input TypeName className "the class that should translated";
  input String version = "2.0" "FMU version, 1.0 or 2.0.";
  input String fmuType = "me" "FMU type, me (model exchange), cs (co-simulation), me_cs (both model exchange and co-simulation)";
  input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \\"className\\"";
  input String platforms[:] = {"static"} "The list of platforms to generate code for. \\"dynamic\\"=current platform, dynamically link the runtime. \\"static\\"=current platform, statically link everything. Else, use a host triple, e.g. \\"x86_64-linux-gnu\\" or \\"x86_64-w64-mingw32\\"";
  input Boolean includeResources = false "include Modelica based resources via loadResource or not";
  output String generatedFileName "Returns the full path of the generated FMU.";
end buildModelFMU;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.buildEncryptedPackage')
        @classmethod
        def buildEncryptedPackage(_, className: Union[TypeName, str]) -> buildEncryptedPackage:
            """function buildEncryptedPackage
  input TypeName className "the class that should encrypted";
  output Boolean success;
  output String commandOutput "Output of the packagetool executable";
end buildEncryptedPackage;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.simulate')
        @classmethod
        def simulate(_, className: Union[TypeName, str], startTime: float=..., stopTime: float=..., numberOfIntervals: float=..., tolerance: float=..., method: str=..., fileNamePrefix: str=..., options: str=..., outputFormat: str=..., variableFilter: str=..., cflags: str=..., simflags: str=...) -> SimulationResult:
            """function simulate
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
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.buildModel')
        @classmethod
        def buildModel(_, className: Union[TypeName, str], startTime: float=..., stopTime: float=..., numberOfIntervals: float=..., tolerance: float=..., method: str=..., fileNamePrefix: str=..., options: str=..., outputFormat: str=..., variableFilter: str=..., cflags: str=..., simflags: str=...) -> List[str]:
            """function buildModel
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
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.buildLabel')
        @classmethod
        def buildLabel(_, className: Union[TypeName, str], startTime: float=..., stopTime: float=..., numberOfIntervals: int=..., tolerance: float=..., method: str=..., fileNamePrefix: str=..., options: str=..., outputFormat: str=..., variableFilter: str=..., cflags: str=..., simflags: str=...) -> List[str]:
            """function buildLabel
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
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.reduceTerms')
        @classmethod
        def reduceTerms(_, className: Union[TypeName, str], startTime: float=..., stopTime: float=..., numberOfIntervals: int=..., tolerance: float=..., method: str=..., fileNamePrefix: str=..., options: str=..., outputFormat: str=..., variableFilter: str=..., cflags: str=..., simflags: str=..., labelstoCancel: str=...) -> List[str]:
            """function reduceTerms
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
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.moveClass')
        @classmethod
        def moveClass(_, className: Union[TypeName, str], offset: int) -> bool:
            """function moveClass
  input TypeName className "the class that should be moved";
  input Integer offset "Offset in the class list.";
  output Boolean result;
end moveClass;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.moveClassToTop')
        @classmethod
        def moveClassToTop(_, className: Union[TypeName, str]) -> bool:
            """function moveClassToTop
  input TypeName className;
  output Boolean result;
end moveClassToTop;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.moveClassToBottom')
        @classmethod
        def moveClassToBottom(_, className: Union[TypeName, str]) -> bool:
            """function moveClassToBottom
  input TypeName className;
  output Boolean result;
end moveClassToBottom;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.copyClass')
        @classmethod
        def copyClass(_, className: Union[TypeName, str], newClassName: str, withIn: Union[TypeName, str]=...) -> bool:
            """function copyClass
  input TypeName className "the class that should be copied";
  input String newClassName "the name for new class";
  input TypeName withIn = $Code(TopLevel) "the with in path for new class";
  output Boolean result;
end copyClass;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.linearize')
        @classmethod
        def linearize(_, className: Union[TypeName, str], startTime: float=..., stopTime: float=..., numberOfIntervals: float=..., stepSize: float=..., tolerance: float=..., method: str=..., fileNamePrefix: str=..., storeInTemp: bool=..., noClean: bool=..., options: str=..., outputFormat: str=..., variableFilter: str=..., cflags: str=..., simflags: str=...) -> str:
            """function linearize
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
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.optimize')
        @classmethod
        def optimize(_, className: Union[TypeName, str], startTime: float=..., stopTime: float=..., numberOfIntervals: float=..., stepSize: float=..., tolerance: float=..., method: str=..., fileNamePrefix: str=..., storeInTemp: bool=..., noClean: bool=..., options: str=..., outputFormat: str=..., variableFilter: str=..., cflags: str=..., simflags: str=...) -> str:
            """function optimize
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
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getSourceFile')
        @classmethod
        def getSourceFile(_, class_: Union[TypeName, str]) -> str:
            """function getSourceFile
  input TypeName class_;
  output String filename "empty on failure";
end getSourceFile;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setSourceFile')
        @classmethod
        def setSourceFile(_, class_: Union[TypeName, str], filename: str) -> bool:
            """function setSourceFile
  input TypeName class_;
  input String filename;
  output Boolean success;
end setSourceFile;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isShortDefinition')
        @classmethod
        def isShortDefinition(_, class_: Union[TypeName, str]) -> bool:
            """function isShortDefinition
  input TypeName class_;
  output Boolean isShortCls;
end isShortDefinition;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setClassComment')
        @classmethod
        def setClassComment(_, class_: Union[TypeName, str], filename: str) -> bool:
            """function setClassComment
  input TypeName class_;
  input String filename;
  output Boolean success;
end setClassComment;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getClassNames')
        @classmethod
        def getClassNames(_, class_: Union[TypeName, str]=..., recursive: bool=..., qualified: bool=..., sort: bool=..., builtin: bool=..., showProtected: bool=..., includeConstants: bool=...) -> List[TypeName]:
            """function getClassNames
  input TypeName class_ = $Code(AllLoadedClasses);
  input Boolean recursive = false;
  input Boolean qualified = false;
  input Boolean sort = false;
  input Boolean builtin = false "List also builtin classes if true";
  input Boolean showProtected = false "List also protected classes if true";
  input Boolean includeConstants = false "List also constants in the class if true";
  output TypeName classNames[:];
end getClassNames;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getUsedClassNames')
        @classmethod
        def getUsedClassNames(_, className: Union[TypeName, str]) -> List[TypeName]:
            """function getUsedClassNames
  input TypeName className;
  output TypeName classNames[:];
end getUsedClassNames;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getPackages')
        @classmethod
        def getPackages(_, class_: Union[TypeName, str]=...) -> List[TypeName]:
            """function getPackages
  input TypeName class_ = $Code(AllLoadedClasses);
  output TypeName classNames[:];
end getPackages;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.basePlotFunction')
        @classmethod
        def basePlotFunction(_, fileName: str=..., interpolation: str=..., title: str=..., legend: bool=..., grid: bool=..., logX: bool=..., logY: bool=..., xLabel: str=..., yLabel: str=..., points: bool=..., xRange: Sequence[float]=..., yRange: Sequence[float]=...) -> bool:
            """partial function basePlotFunction
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
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.plot')
        @classmethod
        def plot(_, vars: Sequence[Union[VariableName, str]], externalWindow: bool=..., fileName: str=..., title: str=..., grid: str=..., logX: bool=..., logY: bool=..., xLabel: str=..., yLabel: str=..., xRange: Sequence[float]=..., yRange: Sequence[float]=..., curveWidth: float=..., curveStyle: int=..., legendPosition: str=..., footer: str=..., autoScale: bool=..., forceOMPlot: bool=...) -> bool:
            """function plot
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
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.plotAll')
        @classmethod
        def plotAll(_, externalWindow: bool=..., fileName: str=..., title: str=..., grid: str=..., logX: bool=..., logY: bool=..., xLabel: str=..., yLabel: str=..., xRange: Sequence[float]=..., yRange: Sequence[float]=..., curveWidth: float=..., curveStyle: int=..., legendPosition: str=..., footer: str=..., autoScale: bool=..., forceOMPlot: bool=...) -> bool:
            """function plotAll
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
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.plotParametric')
        @classmethod
        def plotParametric(_, xVariable: Union[VariableName, str], yVariable: Union[VariableName, str], externalWindow: bool=..., fileName: str=..., title: str=..., grid: str=..., logX: bool=..., logY: bool=..., xLabel: str=..., yLabel: str=..., xRange: Sequence[float]=..., yRange: Sequence[float]=..., curveWidth: float=..., curveStyle: int=..., legendPosition: str=..., footer: str=..., autoScale: bool=..., forceOMPlot: bool=...) -> bool:
            """function plotParametric
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
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.readSimulationResult')
        @classmethod
        def readSimulationResult(_, filename: str, variables: Sequence[Union[VariableName, str]], size: int=...) -> List[List[float]]:
            """function readSimulationResult
  input String filename;
  input VariableNames variables;
  input Integer size = 0 "0=read any size... If the size is not the same as the result-file, this function fails";
  output Real result[:, :];
end readSimulationResult;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.readSimulationResultSize')
        @classmethod
        def readSimulationResultSize(_, fileName: str) -> int:
            """function readSimulationResultSize
  input String fileName;
  output Integer sz;
end readSimulationResultSize;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.readSimulationResultVars')
        @classmethod
        def readSimulationResultVars(_, fileName: str, readParameters: bool=..., openmodelicaStyle: bool=...) -> List[str]:
            """function readSimulationResultVars
  input String fileName;
  input Boolean readParameters = true;
  input Boolean openmodelicaStyle = false;
  output String[:] vars;
end readSimulationResultVars;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.filterSimulationResults')
        @classmethod
        def filterSimulationResults(_, inFile: str, outFile: str, vars: Sequence[str], numberOfIntervals: int=..., removeDescription: bool=...) -> bool:
            """function filterSimulationResults
  input String inFile;
  input String outFile;
  input String[:] vars;
  input Integer numberOfIntervals = 0 "0=Do not resample";
  input Boolean removeDescription = false;
  output Boolean success;
end filterSimulationResults;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.compareSimulationResults')
        @classmethod
        def compareSimulationResults(_, filename: str, reffilename: str, logfilename: str, relTol: float=..., absTol: float=..., vars: Sequence[str]=...) -> List[str]:
            """function compareSimulationResults
  input String filename;
  input String reffilename;
  input String logfilename;
  input Real relTol = 0.01;
  input Real absTol = 0.0001;
  input String[:] vars = fill("", 0);
  output String[:] result;
end compareSimulationResults;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.deltaSimulationResults')
        @classmethod
        def deltaSimulationResults(_, filename: str, reffilename: str, method: str, vars: Sequence[str]=...) -> float:
            """function deltaSimulationResults
  input String filename;
  input String reffilename;
  input String method "method to compute then error. choose 1norm, 2norm, maxerr";
  input String[:] vars = fill("", 0);
  output Real result;
end deltaSimulationResults;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.diffSimulationResults')
        @classmethod
        def diffSimulationResults(_, actualFile: str, expectedFile: str, diffPrefix: str, relTol: float=..., relTolDiffMinMax: float=..., rangeDelta: float=..., vars: Sequence[str]=..., keepEqualResults: bool=...) -> diffSimulationResults:
            """function diffSimulationResults
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
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.diffSimulationResultsHtml')
        @classmethod
        def diffSimulationResultsHtml(_, var: str, actualFile: str, expectedFile: str, relTol: float=..., relTolDiffMinMax: float=..., rangeDelta: float=...) -> str:
            """function diffSimulationResultsHtml
  input String var;
  input String actualFile;
  input String expectedFile;
  input Real relTol = 1e-3 "y tolerance";
  input Real relTolDiffMinMax = 1e-4 "y tolerance based on the difference between the maximum and minimum of the signal";
  input Real rangeDelta = 0.002 "x tolerance";
  output String html;
end diffSimulationResultsHtml;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.checkTaskGraph')
        @classmethod
        def checkTaskGraph(_, filename: str, reffilename: str) -> List[str]:
            """function checkTaskGraph
  input String filename;
  input String reffilename;
  output String[:] result;
end checkTaskGraph;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.checkCodeGraph')
        @classmethod
        def checkCodeGraph(_, graphfile: str, codefile: str) -> List[str]:
            """function checkCodeGraph
  input String graphfile;
  input String codefile;
  output String[:] result;
end checkCodeGraph;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.val')
        @classmethod
        def val(_, var: Union[VariableName, str], timePoint: float=..., fileName: str=...) -> float:
            """function val
  input VariableName var;
  input Real timePoint = 0.0;
  input String fileName = "<default>" "The contents of the currentSimulationResult variable";
  output Real valAtTime;
end val;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.closeSimulationResultFile')
        @classmethod
        def closeSimulationResultFile(_) -> bool:
            """function closeSimulationResultFile
  output Boolean success;
end closeSimulationResultFile;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getParameterNames')
        @classmethod
        def getParameterNames(_, class_: Union[TypeName, str]) -> List[str]:
            """function getParameterNames
  input TypeName class_;
  output String[:] parameters;
end getParameterNames;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getParameterValue')
        @classmethod
        def getParameterValue(_, class_: Union[TypeName, str], parameterName: str) -> str:
            """function getParameterValue
  input TypeName class_;
  input String parameterName;
  output String parameterValue;
end getParameterValue;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getComponentModifierNames')
        @classmethod
        def getComponentModifierNames(_, class_: Union[TypeName, str], componentName: str) -> List[str]:
            """function getComponentModifierNames
  input TypeName class_;
  input String componentName;
  output String[:] modifiers;
end getComponentModifierNames;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getComponentModifierValue')
        @classmethod
        def getComponentModifierValue(_, class_: Union[TypeName, str], modifier: Union[TypeName, str]) -> str:
            """function getComponentModifierValue
  input TypeName class_;
  input TypeName modifier;
  output String value;
end getComponentModifierValue;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getComponentModifierValues')
        @classmethod
        def getComponentModifierValues(_, class_: Union[TypeName, str], modifier: Union[TypeName, str]) -> str:
            """function getComponentModifierValues
  input TypeName class_;
  input TypeName modifier;
  output String value;
end getComponentModifierValues;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getInstantiatedParametersAndValues')
        @classmethod
        def getInstantiatedParametersAndValues(_, cls: Union[TypeName, str]) -> List[str]:
            """function getInstantiatedParametersAndValues
  input TypeName cls;
  output String[:] values;
end getInstantiatedParametersAndValues;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.removeComponentModifiers')
        @classmethod
        def removeComponentModifiers(_, class_: Union[TypeName, str], componentName: str, keepRedeclares: bool=...) -> bool:
            """function removeComponentModifiers
  input TypeName class_;
  input String componentName;
  input Boolean keepRedeclares = false;
  output Boolean success;
end removeComponentModifiers;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.removeExtendsModifiers')
        @classmethod
        def removeExtendsModifiers(_, className: Union[TypeName, str], baseClassName: Union[TypeName, str], keepRedeclares: bool=...) -> bool:
            """function removeExtendsModifiers
  input TypeName className;
  input TypeName baseClassName;
  input Boolean keepRedeclares = false;
  output Boolean success;
end removeExtendsModifiers;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getConnectionCount')
        @classmethod
        def getConnectionCount(_, className: Union[TypeName, str]) -> int:
            """function getConnectionCount
  input TypeName className;
  output Integer count;
end getConnectionCount;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getNthConnection')
        @classmethod
        def getNthConnection(_, className: Union[TypeName, str], index: int) -> List[str]:
            """function getNthConnection
  input TypeName className;
  input Integer index;
  output String[:] result;
end getNthConnection;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getAlgorithmCount')
        @classmethod
        def getAlgorithmCount(_, class_: Union[TypeName, str]) -> int:
            """function getAlgorithmCount
  input TypeName class_;
  output Integer count;
end getAlgorithmCount;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getNthAlgorithm')
        @classmethod
        def getNthAlgorithm(_, class_: Union[TypeName, str], index: int) -> str:
            """function getNthAlgorithm
  input TypeName class_;
  input Integer index;
  output String result;
end getNthAlgorithm;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getInitialAlgorithmCount')
        @classmethod
        def getInitialAlgorithmCount(_, class_: Union[TypeName, str]) -> int:
            """function getInitialAlgorithmCount
  input TypeName class_;
  output Integer count;
end getInitialAlgorithmCount;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getNthInitialAlgorithm')
        @classmethod
        def getNthInitialAlgorithm(_, class_: Union[TypeName, str], index: int) -> str:
            """function getNthInitialAlgorithm
  input TypeName class_;
  input Integer index;
  output String result;
end getNthInitialAlgorithm;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getAlgorithmItemsCount')
        @classmethod
        def getAlgorithmItemsCount(_, class_: Union[TypeName, str]) -> int:
            """function getAlgorithmItemsCount
  input TypeName class_;
  output Integer count;
end getAlgorithmItemsCount;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getNthAlgorithmItem')
        @classmethod
        def getNthAlgorithmItem(_, class_: Union[TypeName, str], index: int) -> str:
            """function getNthAlgorithmItem
  input TypeName class_;
  input Integer index;
  output String result;
end getNthAlgorithmItem;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getInitialAlgorithmItemsCount')
        @classmethod
        def getInitialAlgorithmItemsCount(_, class_: Union[TypeName, str]) -> int:
            """function getInitialAlgorithmItemsCount
  input TypeName class_;
  output Integer count;
end getInitialAlgorithmItemsCount;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getNthInitialAlgorithmItem')
        @classmethod
        def getNthInitialAlgorithmItem(_, class_: Union[TypeName, str], index: int) -> str:
            """function getNthInitialAlgorithmItem
  input TypeName class_;
  input Integer index;
  output String result;
end getNthInitialAlgorithmItem;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getEquationCount')
        @classmethod
        def getEquationCount(_, class_: Union[TypeName, str]) -> int:
            """function getEquationCount
  input TypeName class_;
  output Integer count;
end getEquationCount;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getNthEquation')
        @classmethod
        def getNthEquation(_, class_: Union[TypeName, str], index: int) -> str:
            """function getNthEquation
  input TypeName class_;
  input Integer index;
  output String result;
end getNthEquation;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getInitialEquationCount')
        @classmethod
        def getInitialEquationCount(_, class_: Union[TypeName, str]) -> int:
            """function getInitialEquationCount
  input TypeName class_;
  output Integer count;
end getInitialEquationCount;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getNthInitialEquation')
        @classmethod
        def getNthInitialEquation(_, class_: Union[TypeName, str], index: int) -> str:
            """function getNthInitialEquation
  input TypeName class_;
  input Integer index;
  output String result;
end getNthInitialEquation;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getEquationItemsCount')
        @classmethod
        def getEquationItemsCount(_, class_: Union[TypeName, str]) -> int:
            """function getEquationItemsCount
  input TypeName class_;
  output Integer count;
end getEquationItemsCount;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getNthEquationItem')
        @classmethod
        def getNthEquationItem(_, class_: Union[TypeName, str], index: int) -> str:
            """function getNthEquationItem
  input TypeName class_;
  input Integer index;
  output String result;
end getNthEquationItem;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getInitialEquationItemsCount')
        @classmethod
        def getInitialEquationItemsCount(_, class_: Union[TypeName, str]) -> int:
            """function getInitialEquationItemsCount
  input TypeName class_;
  output Integer count;
end getInitialEquationItemsCount;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getNthInitialEquationItem')
        @classmethod
        def getNthInitialEquationItem(_, class_: Union[TypeName, str], index: int) -> str:
            """function getNthInitialEquationItem
  input TypeName class_;
  input Integer index;
  output String result;
end getNthInitialEquationItem;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getAnnotationCount')
        @classmethod
        def getAnnotationCount(_, class_: Union[TypeName, str]) -> int:
            """function getAnnotationCount
  input TypeName class_;
  output Integer count;
end getAnnotationCount;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getNthAnnotationString')
        @classmethod
        def getNthAnnotationString(_, class_: Union[TypeName, str], index: int) -> str:
            """function getNthAnnotationString
  input TypeName class_;
  input Integer index;
  output String result;
end getNthAnnotationString;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getImportCount')
        @classmethod
        def getImportCount(_, class_: Union[TypeName, str]) -> int:
            """function getImportCount
  input TypeName class_;
  output Integer count;
end getImportCount;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getNthImport')
        @classmethod
        def getNthImport(_, class_: Union[TypeName, str], index: int) -> List[str]:
            """function getNthImport
  input TypeName class_;
  input Integer index;
  output String out[3] "{\\"Path\\",\\"Id\\",\\"Kind\\"}";
end getNthImport;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.iconv')
        @classmethod
        def iconv(_, string: str, from_: Annotated[str, alias[Literal['from']]], to: str=...) -> str:
            """function iconv
  input String string;
  input String from;
  input String to = "UTF-8";
  output String result;
end iconv;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getDocumentationAnnotation')
        @classmethod
        def getDocumentationAnnotation(_, cl: Union[TypeName, str]) -> List[str]:
            """function getDocumentationAnnotation
  input TypeName cl;
  output String out[3] "{info,revision,infoHeader} TODO: Should be changed to have 2 outputs instead of an array of 2 Strings...";
end getDocumentationAnnotation;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setDocumentationAnnotation')
        @classmethod
        def setDocumentationAnnotation(_, class_: Union[TypeName, str], info: str=..., revisions: str=...) -> bool:
            """function setDocumentationAnnotation
  input TypeName class_;
  input String info = "";
  input String revisions = "";
  output Boolean bool;
end setDocumentationAnnotation;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getTimeStamp')
        @classmethod
        def getTimeStamp(_, cl: Union[TypeName, str]) -> getTimeStamp:
            """function getTimeStamp
  input TypeName cl;
  output Real timeStamp;
  output String timeStampAsString;
end getTimeStamp;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.stringTypeName')
        @classmethod
        def stringTypeName(_, str: str) -> TypeName:
            """function stringTypeName
  input String str;
  output TypeName cl;
end stringTypeName;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.stringVariableName')
        @classmethod
        def stringVariableName(_, str: str) -> VariableName:
            """function stringVariableName
  input String str;
  output VariableName cl;
end stringVariableName;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.typeNameString')
        @classmethod
        def typeNameString(_, cl: Union[TypeName, str]) -> str:
            """function typeNameString
  input TypeName cl;
  output String out;
end typeNameString;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.typeNameStrings')
        @classmethod
        def typeNameStrings(_, cl: Union[TypeName, str]) -> List[str]:
            """function typeNameStrings
  input TypeName cl;
  output String out[:];
end typeNameStrings;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getClassComment')
        @classmethod
        def getClassComment(_, cl: Union[TypeName, str]) -> str:
            """function getClassComment
  input TypeName cl;
  output String comment;
end getClassComment;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.dirname')
        @classmethod
        def dirname(_, path: str) -> str:
            """function dirname
  input String path;
  output String dirname;
end dirname;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.basename')
        @classmethod
        def basename(_, path: str) -> str:
            """function basename
  input String path;
  output String basename;
end basename;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getClassRestriction')
        @classmethod
        def getClassRestriction(_, cl: Union[TypeName, str]) -> str:
            """function getClassRestriction
  input TypeName cl;
  output String restriction;
end getClassRestriction;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isType')
        @classmethod
        def isType(_, cl: Union[TypeName, str]) -> bool:
            """function isType
  input TypeName cl;
  output Boolean b;
end isType;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isPackage')
        @classmethod
        def isPackage(_, cl: Union[TypeName, str]) -> bool:
            """function isPackage
  input TypeName cl;
  output Boolean b;
end isPackage;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isClass')
        @classmethod
        def isClass(_, cl: Union[TypeName, str]) -> bool:
            """function isClass
  input TypeName cl;
  output Boolean b;
end isClass;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isRecord')
        @classmethod
        def isRecord(_, cl: Union[TypeName, str]) -> bool:
            """function isRecord
  input TypeName cl;
  output Boolean b;
end isRecord;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isBlock')
        @classmethod
        def isBlock(_, cl: Union[TypeName, str]) -> bool:
            """function isBlock
  input TypeName cl;
  output Boolean b;
end isBlock;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isFunction')
        @classmethod
        def isFunction(_, cl: Union[TypeName, str]) -> bool:
            """function isFunction
  input TypeName cl;
  output Boolean b;
end isFunction;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isPartial')
        @classmethod
        def isPartial(_, cl: Union[TypeName, str]) -> bool:
            """function isPartial
  input TypeName cl;
  output Boolean b;
end isPartial;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isModel')
        @classmethod
        def isModel(_, cl: Union[TypeName, str]) -> bool:
            """function isModel
  input TypeName cl;
  output Boolean b;
end isModel;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isConnector')
        @classmethod
        def isConnector(_, cl: Union[TypeName, str]) -> bool:
            """function isConnector
  input TypeName cl;
  output Boolean b;
end isConnector;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isOptimization')
        @classmethod
        def isOptimization(_, cl: Union[TypeName, str]) -> bool:
            """function isOptimization
  input TypeName cl;
  output Boolean b;
end isOptimization;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isEnumeration')
        @classmethod
        def isEnumeration(_, cl: Union[TypeName, str]) -> bool:
            """function isEnumeration
  input TypeName cl;
  output Boolean b;
end isEnumeration;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isOperator')
        @classmethod
        def isOperator(_, cl: Union[TypeName, str]) -> bool:
            """function isOperator
  input TypeName cl;
  output Boolean b;
end isOperator;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isOperatorRecord')
        @classmethod
        def isOperatorRecord(_, cl: Union[TypeName, str]) -> bool:
            """function isOperatorRecord
  input TypeName cl;
  output Boolean b;
end isOperatorRecord;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isOperatorFunction')
        @classmethod
        def isOperatorFunction(_, cl: Union[TypeName, str]) -> bool:
            """function isOperatorFunction
  input TypeName cl;
  output Boolean b;
end isOperatorFunction;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isProtectedClass')
        @classmethod
        def isProtectedClass(_, cl: Union[TypeName, str], c2: str) -> bool:
            """function isProtectedClass
  input TypeName cl;
  input String c2;
  output Boolean b;
end isProtectedClass;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getBuiltinType')
        @classmethod
        def getBuiltinType(_, cl: Union[TypeName, str]) -> str:
            """function getBuiltinType
  input TypeName cl;
  output String name;
end getBuiltinType;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.setInitXmlStartValue')
        @classmethod
        def setInitXmlStartValue(_, fileName: str, variableName: str, startValue: str, outputFile: str) -> bool:
            """function setInitXmlStartValue
  input String fileName;
  input String variableName;
  input String startValue;
  input String outputFile;
  output Boolean success = false;
end setInitXmlStartValue;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.ngspicetoModelica')
        @classmethod
        def ngspicetoModelica(_, netlistfileName: str) -> bool:
            """function ngspicetoModelica
  input String netlistfileName;
  output Boolean success = false;
end ngspicetoModelica;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getInheritedClasses')
        @classmethod
        def getInheritedClasses(_, name: Union[TypeName, str]) -> List[TypeName]:
            """function getInheritedClasses
  input TypeName name;
  output TypeName inheritedClasses[:];
end getInheritedClasses;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getComponentsTest')
        @classmethod
        def getComponentsTest(_, name: Union[TypeName, str]) -> List[Component]:
            """function getComponentsTest
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
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.isExperiment')
        @classmethod
        def isExperiment(_, name: Union[TypeName, str]) -> bool:
            """function isExperiment
  input TypeName name;
  output Boolean res;
end isExperiment;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getSimulationOptions')
        @classmethod
        def getSimulationOptions(_, name: Union[TypeName, str], defaultStartTime: float=..., defaultStopTime: float=..., defaultTolerance: float=..., defaultNumberOfIntervals: int=..., defaultInterval: float=...) -> getSimulationOptions:
            """function getSimulationOptions
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
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getAnnotationNamedModifiers')
        @classmethod
        def getAnnotationNamedModifiers(_, name: Union[TypeName, str], vendorannotation: str) -> List[str]:
            """function getAnnotationNamedModifiers
  input TypeName name;
  input String vendorannotation;
  output String[:] modifiernamelist;
end getAnnotationNamedModifiers;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getAnnotationModifierValue')
        @classmethod
        def getAnnotationModifierValue(_, name: Union[TypeName, str], vendorannotation: str, modifiername: str) -> str:
            """function getAnnotationModifierValue
  input TypeName name;
  input String vendorannotation;
  input String modifiername;
  output String modifiernamevalue;
end getAnnotationModifierValue;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.classAnnotationExists')
        @classmethod
        def classAnnotationExists(_, className: Union[TypeName, str], annotationName: Union[TypeName, str]) -> bool:
            """function classAnnotationExists
  input TypeName className;
  input TypeName annotationName;
  output Boolean exists;
end classAnnotationExists;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getBooleanClassAnnotation')
        @classmethod
        def getBooleanClassAnnotation(_, className: Union[TypeName, str], annotationName: Union[TypeName, str]) -> bool:
            """function getBooleanClassAnnotation
  input TypeName className;
  input TypeName annotationName;
  output Boolean value;
end getBooleanClassAnnotation;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.extendsFrom')
        @classmethod
        def extendsFrom(_, className: Union[TypeName, str], baseClassName: Union[TypeName, str]) -> bool:
            """function extendsFrom
  input TypeName className;
  input TypeName baseClassName;
  output Boolean res;
end extendsFrom;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.loadModelica3D')
        @classmethod
        def loadModelica3D(_, version: str=...) -> bool:
            """function loadModelica3D
  input String version = "3.2.1";
  output Boolean status;
end loadModelica3D;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.searchClassNames')
        @classmethod
        def searchClassNames(_, searchText: str, findInText: bool=...) -> List[TypeName]:
            """function searchClassNames
  input String searchText;
  input Boolean findInText = false;
  output TypeName classNames[:];
end searchClassNames;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getAvailableLibraries')
        @classmethod
        def getAvailableLibraries(_) -> List[str]:
            """function getAvailableLibraries
  output String[:] libraries;
end getAvailableLibraries;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getUses')
        @classmethod
        def getUses(_, pack: Union[TypeName, str]) -> List[List[str]]:
            """function getUses
  input TypeName pack;
  output String[:, :] uses;
end getUses;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getDerivedClassModifierNames')
        @classmethod
        def getDerivedClassModifierNames(_, className: Union[TypeName, str]) -> List[str]:
            """function getDerivedClassModifierNames
  input TypeName className;
  output String[:] modifierNames;
end getDerivedClassModifierNames;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getDerivedClassModifierValue')
        @classmethod
        def getDerivedClassModifierValue(_, className: Union[TypeName, str], modifierName: Union[TypeName, str]) -> str:
            """function getDerivedClassModifierValue
  input TypeName className;
  input TypeName modifierName;
  output String modifierValue;
end getDerivedClassModifierValue;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.generateEntryPoint')
        @classmethod
        def generateEntryPoint(_, fileName: str, entryPoint: Union[TypeName, str], url: str=...) -> None:
            """function generateEntryPoint
  input String fileName;
  input TypeName entryPoint;
  input String url = "https://trac.openmodelica.org/OpenModelica/newticket";
end generateEntryPoint;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.numProcessors')
        @classmethod
        def numProcessors(_) -> int:
            """function numProcessors
  output Integer result;
end numProcessors;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.runScriptParallel')
        @classmethod
        def runScriptParallel(_, scripts: Sequence[str], numThreads: int=..., useThreads: bool=...) -> List[bool]:
            """function runScriptParallel
  input String scripts[:];
  input Integer numThreads = numProcessors();
  input Boolean useThreads = false;
  output Boolean results[:];
end runScriptParallel;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.exit')
        @classmethod
        def exit(_, status: int) -> None:
            """function exit
  input Integer status;
end exit;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.threadWorkFailed')
        @classmethod
        def threadWorkFailed(_) -> None:
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getMemorySize')
        @classmethod
        def getMemorySize(_) -> float:
            """function getMemorySize
  output Real memory(unit = "MiB");
end getMemorySize;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.GC_gcollect_and_unmap')
        @classmethod
        def GC_gcollect_and_unmap(_) -> None:
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.GC_expand_hp')
        @classmethod
        def GC_expand_hp(_, size: int) -> bool:
            """function GC_expand_hp
  input Integer size;
  output Boolean success;
end GC_expand_hp;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.GC_set_max_heap_size')
        @classmethod
        def GC_set_max_heap_size(_, size: int) -> bool:
            """function GC_set_max_heap_size
  input Integer size;
  output Boolean success;
end GC_set_max_heap_size;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.GC_PROFSTATS')
        @dataclass
        class GC_PROFSTATS(record):
            """record GC_PROFSTATS
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

        @external('.OpenModelica.Scripting.GC_get_prof_stats')
        @classmethod
        def GC_get_prof_stats(_) -> OpenModelica.Scripting.GC_PROFSTATS:
            """function GC_get_prof_stats
  output GC_PROFSTATS gcStats;
end GC_get_prof_stats;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.checkInterfaceOfPackages')
        @classmethod
        def checkInterfaceOfPackages(_, cl: Union[TypeName, str], dependencyMatrix: Sequence[Sequence[str]]) -> bool:
            """function checkInterfaceOfPackages
  input TypeName cl;
  input String dependencyMatrix[:, :];
  output Boolean success;
end checkInterfaceOfPackages;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.sortStrings')
        @classmethod
        def sortStrings(_, arr: Sequence[str]) -> List[str]:
            """function sortStrings
  input String arr[:];
  output String sorted[:];
end sortStrings;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getClassInformation')
        @classmethod
        def getClassInformation(_, cl: Union[TypeName, str]) -> getClassInformation:
            """function getClassInformation
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
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getTransitions')
        @classmethod
        def getTransitions(_, cl: Union[TypeName, str]) -> List[List[str]]:
            """function getTransitions
  input TypeName cl;
  output String[:, :] transitions;
end getTransitions;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.deleteTransition')
        @classmethod
        def deleteTransition(_, cl: Union[TypeName, str], from_: Annotated[str, alias[Literal['from']]], to: str, condition: str, immediate: bool, reset: bool, synchronize: bool, priority: int) -> bool:
            """function deleteTransition
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
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.getInitialStates')
        @classmethod
        def getInitialStates(_, cl: Union[TypeName, str]) -> List[List[str]]:
            """function getInitialStates
  input TypeName cl;
  output String[:, :] initialStates;
end getInitialStates;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.deleteInitialState')
        @classmethod
        def deleteInitialState(_, cl: Union[TypeName, str], state: str) -> bool:
            """function deleteInitialState
  input TypeName cl;
  input String state;
  output Boolean bool;
end deleteInitialState;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.generateScriptingAPI')
        @classmethod
        def generateScriptingAPI(_, cl: Union[TypeName, str], name: str) -> generateScriptingAPI:
            """function generateScriptingAPI
  input TypeName cl;
  input String name;
  output Boolean success;
  output String moFile;
  output String qtFile;
  output String qtHeader;
end generateScriptingAPI;"""
            raise NotImplementedError()

        @external('.OpenModelica.Scripting.Experimental')
        class Experimental(package):

            @external('.OpenModelica.Scripting.Experimental.relocateFunctions')
            @classmethod
            def relocateFunctions(_, fileName: str, names: Sequence[Sequence[str]]) -> bool:
                """function relocateFunctions
  input String fileName;
  input String names[:, 2];
  output Boolean success;
end relocateFunctions;"""
                raise NotImplementedError()

class Session(BasicSession):
    OpenModelica = OpenModelica
    checkSettings = OpenModelica.Scripting.checkSettings
    loadFile = OpenModelica.Scripting.loadFile
    loadFiles = OpenModelica.Scripting.loadFiles
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
    dumpXMLDAE = OpenModelica.Scripting.dumpXMLDAE
    convertUnits = OpenModelica.Scripting.convertUnits
    getDerivedUnits = OpenModelica.Scripting.getDerivedUnits
    listVariables = OpenModelica.Scripting.listVariables
    strtok = OpenModelica.Scripting.strtok
    stringSplit = OpenModelica.Scripting.stringSplit
    stringReplace = OpenModelica.Scripting.stringReplace
    escapeXML = OpenModelica.Scripting.escapeXML
    list = OpenModelica.Scripting.list
    listFile = OpenModelica.Scripting.listFile
    diffModelicaFileListings = OpenModelica.Scripting.diffModelicaFileListings
    exportToFigaro = OpenModelica.Scripting.exportToFigaro
    inferBindings = OpenModelica.Scripting.inferBindings
    generateVerificationScenarios = OpenModelica.Scripting.generateVerificationScenarios
    rewriteBlockCall = OpenModelica.Scripting.rewriteBlockCall
    realpath = OpenModelica.Scripting.realpath
    uriToFilename = OpenModelica.Scripting.uriToFilename
    getLoadedLibraries = OpenModelica.Scripting.getLoadedLibraries
    solveLinearSystem = OpenModelica.Scripting.solveLinearSystem
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
    getParameterNames = OpenModelica.Scripting.getParameterNames
    getParameterValue = OpenModelica.Scripting.getParameterValue
    getComponentModifierNames = OpenModelica.Scripting.getComponentModifierNames
    getComponentModifierValue = OpenModelica.Scripting.getComponentModifierValue
    getComponentModifierValues = OpenModelica.Scripting.getComponentModifierValues
    getInstantiatedParametersAndValues = OpenModelica.Scripting.getInstantiatedParametersAndValues
    removeComponentModifiers = OpenModelica.Scripting.removeComponentModifiers
    removeExtendsModifiers = OpenModelica.Scripting.removeExtendsModifiers
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
    getUses = OpenModelica.Scripting.getUses
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
    GC_get_prof_stats = OpenModelica.Scripting.GC_get_prof_stats
    checkInterfaceOfPackages = OpenModelica.Scripting.checkInterfaceOfPackages
    sortStrings = OpenModelica.Scripting.sortStrings
    getClassInformation = OpenModelica.Scripting.getClassInformation
    getTransitions = OpenModelica.Scripting.getTransitions
    deleteTransition = OpenModelica.Scripting.deleteTransition
    getInitialStates = OpenModelica.Scripting.getInitialStates
    deleteInitialState = OpenModelica.Scripting.deleteInitialState
    generateScriptingAPI = OpenModelica.Scripting.generateScriptingAPI
