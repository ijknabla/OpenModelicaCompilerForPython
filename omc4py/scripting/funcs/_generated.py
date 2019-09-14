
__license__ = '''
/*
 * This file is part of OpenModelica.
 *
 * Copyright (c) 1998-CurrentYear, Open Source Modelica Consortium (OSMC),
 * c/o Linköpings universitet, Department of Computer and Information Science,
 * SE-58183 Linköping, Sweden.
 *
 * All rights reserved.
 *
 * THIS PROGRAM IS PROVIDED UNDER THE TERMS OF GPL VERSION 3 LICENSE OR
 * THIS OSMC PUBLIC LICENSE (OSMC-PL) VERSION 1.2.
 * ANY USE, REPRODUCTION OR DISTRIBUTION OF THIS PROGRAM CONSTITUTES
 * RECIPIENT'S ACCEPTANCE OF THE OSMC PUBLIC LICENSE OR THE GPL VERSION 3,
 * ACCORDING TO RECIPIENTS CHOICE.
 *
 * The OpenModelica software and the Open Source Modelica
 * Consortium (OSMC) Public License (OSMC-PL) are obtained
 * from OSMC, either from the above address,
 * from the URLs: http://www.ida.liu.se/projects/OpenModelica or
 * http://www.openmodelica.org, and in the OpenModelica distribution.
 * GNU version 3 is obtained from: http://www.gnu.org/copyleft/gpl.html.
 *
 * This program is distributed WITHOUT ANY WARRANTY; without
 * even the implied warranty of  MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE, EXCEPT AS EXPRESSLY SET FORTH
 * IN THE BY RECIPIENT SELECTED SUBSIDIARY LICENSE CONDITIONS OF OSMC-PL.
 *
 * See the full OSMC Public License conditions for more details.
 *
 */
'''

__all__ = (
    "loadFile",
    "loadFiles",
    "loadEncryptedPackage",
    "reloadClass",
    "loadString",
    "parseString",
    "parseFile",
    "loadFileInteractiveQualified",
    "loadFileInteractive",
    "system",
    "system_parallel",
    "saveAll",
    "help",
    "clear",
    "clearProgram",
    "clearVariables",
    "generateHeader",
    "generateSeparateCode",
    "generateSeparateCodeDependencies",
    "generateSeparateCodeDependenciesMakefile",
    "getLinker",
    "setLinker",
    "getLinkerFlags",
    "setLinkerFlags",
    "getCompiler",
    "setCompiler",
    "setCFlags",
    "getCFlags",
    "getCXXCompiler",
    "setCXXCompiler",
    "verifyCompiler",
    "setCompilerPath",
    "getCompileCommand",
    "setCompileCommand",
    "setPlotCommand",
    "getSettings",
    "setTempDirectoryPath",
    "getTempDirectoryPath",
    "getEnvironmentVar",
    "setEnvironmentVar",
    "appendEnvironmentVar",
    "setInstallationDirectoryPath",
    "getInstallationDirectoryPath",
    "setModelicaPath",
    "getModelicaPath",
    "setCompilerFlags",
    "setDebugFlags",
    "clearDebugFlags",
    "setPreOptModules",
    "setCheapMatchingAlgorithm",
    "getMatchingAlgorithm",
    "getAvailableMatchingAlgorithms",
    "setMatchingAlgorithm",
    "getIndexReductionMethod",
    "getAvailableIndexReductionMethods",
    "setIndexReductionMethod",
    "setPostOptModules",
    "getTearingMethod",
    "getAvailableTearingMethods",
    "setTearingMethod",
    "setCommandLineOptions",
    "getCommandLineOptions",
    "getConfigFlagValidOptions",
    "clearCommandLineOptions",
    "getVersion",
    "regularFileExists",
    "directoryExists",
    "stat",
    "readFile",
    "writeFile",
    "compareFilesAndMove",
    "compareFiles",
    "alarm",
    "regex",
    "regexBool",
    "testsuiteFriendlyName",
    "readFileNoNumeric",
    "getErrorString",
    "getMessagesString",
    "countMessages",
    "clearMessages",
    "runScript",
    "echo",
    "getClassesInModelicaPath",
    "getAnnotationVersion",
    "setAnnotationVersion",
    "getNoSimplify",
    "setNoSimplify",
    "getVectorizationLimit",
    "setVectorizationLimit",
    "getDefaultOpenCLDevice",
    "setDefaultOpenCLDevice",
    "setShowAnnotations",
    "getShowAnnotations",
    "setOrderConnections",
    "getOrderConnections",
    "setLanguageStandard",
    "getLanguageStandard",
    "getAstAsCorbaString",
    "cd",
    "mkdir",
    "copy",
    "remove",
    "checkModel",
    "checkAllModelsRecursive",
    "typeOf",
    "instantiateModel",
    "buildOpenTURNSInterface",
    "runOpenTURNSPythonScript",
    "generateCode",
    "loadModel",
    "deleteFile",
    "saveModel",
    "saveTotalModel",
    "save",
    "translateGraphics",
    "dumpXMLDAE",
    "convertUnits",
    "getDerivedUnits",
    "listVariables",
    "strtok",
    "stringSplit",
    "stringReplace",
    "escapeXML",
    "listFile",
    "exportToFigaro",
    "inferBindings",
    "generateVerificationScenarios",
    "rewriteBlockCall",
    "realpath",
    "uriToFilename",
    "getLoadedLibraries",
    "importFMU",
    "importFMUModelDescription",
    "translateModelFMU",
    "buildModelFMU",
    "buildEncryptedPackage",
    "buildModel",
    "buildLabel",
    "reduceTerms",
    "moveClass",
    "moveClassToTop",
    "moveClassToBottom",
    "copyClass",
    "linearize",
    "optimize",
    "getSourceFile",
    "setSourceFile",
    "isShortDefinition",
    "setClassComment",
    "getClassNames",
    "getUsedClassNames",
    "getPackages",
    "basePlotFunction",
    "plot",
    "plotAll",
    "plotParametric",
    "readSimulationResult",
    "readSimulationResultSize",
    "readSimulationResultVars",
    "filterSimulationResults",
    "compareSimulationResults",
    "deltaSimulationResults",
    "diffSimulationResults",
    "diffSimulationResultsHtml",
    "checkTaskGraph",
    "checkCodeGraph",
    "val",
    "closeSimulationResultFile",
    "getParameterNames",
    "getParameterValue",
    "getComponentModifierNames",
    "getComponentModifierValue",
    "getComponentModifierValues",
    "getInstantiatedParametersAndValues",
    "removeComponentModifiers",
    "removeExtendsModifiers",
    "getConnectionCount",
    "getNthConnection",
    "getAlgorithmCount",
    "getNthAlgorithm",
    "getInitialAlgorithmCount",
    "getNthInitialAlgorithm",
    "getAlgorithmItemsCount",
    "getNthAlgorithmItem",
    "getInitialAlgorithmItemsCount",
    "getNthInitialAlgorithmItem",
    "getEquationCount",
    "getNthEquation",
    "getInitialEquationCount",
    "getNthInitialEquation",
    "getEquationItemsCount",
    "getNthEquationItem",
    "getInitialEquationItemsCount",
    "getNthInitialEquationItem",
    "getAnnotationCount",
    "getNthAnnotationString",
    "getImportCount",
    "getNthImport",
    "iconv",
    "getDocumentationAnnotation",
    "setDocumentationAnnotation",
    "getTimeStamp",
    "stringTypeName",
    "stringVariableName",
    "typeNameString",
    "typeNameStrings",
    "getClassComment",
    "dirname",
    "basename",
    "getClassRestriction",
    "isType",
    "isPackage",
    "isClass",
    "isRecord",
    "isBlock",
    "isFunction",
    "isPartial",
    "isModel",
    "isConnector",
    "isOptimization",
    "isEnumeration",
    "isOperator",
    "isOperatorRecord",
    "isOperatorFunction",
    "isProtectedClass",
    "getBuiltinType",
    "setInitXmlStartValue",
    "ngspicetoModelica",
    "getInheritedClasses",
    "isExperiment",
    "getSimulationOptions",
    "getAnnotationNamedModifiers",
    "getAnnotationModifierValue",
    "classAnnotationExists",
    "getBooleanClassAnnotation",
    "extendsFrom",
    "loadModelica3D",
    "searchClassNames",
    "getAvailableLibraries",
    "getUses",
    "getDerivedClassModifierNames",
    "getDerivedClassModifierValue",
    "generateEntryPoint",
    "numProcessors",
    "runScriptParallel",
    "exit",
    "threadWorkFailed",
    "getMemorySize",
    "GC_gcollect_and_unmap",
    "GC_expand_hp",
    "GC_set_max_heap_size",
    "checkInterfaceOfPackages",
    "sortStrings",
    "getClassInformation",
    "getTransitions",
    "deleteTransition",
    "getInitialStates",
    "deleteInitialState",
    "generateScriptingAPI",
    "saveTotalSCode",
)

from collections import namedtuple
from OMPython import OMCSessionBase
from ... import parsers
from ... import scripting


# def checkSettings(
#     omc: OMCSessionBase,
# ):
#     '''
# function checkSettings
#   output CheckSettingsResult result;
# end checkSettings;
#     '''
#     __kwrds = {}
# 
#     __answer = scripting.funcs._ask(omc, "checkSettings", **__kwrds)
#     try:
#         __value = parsers.parseOMCValue(__answer)
#     except parsers.NoMatch:
#         if __answer.lstrip().startswith("Error"):
#             raise scripting.exceptions.OMCError(__answer)
#         if not __answer or __answer.isspace():
#             return None
#         raise
# 
#     return scripting.types.CheckSettingsResult(__value)


def loadFile(
    omc: OMCSessionBase,
    fileName,
    encoding=None,
    uses=None,
):
    '''
function loadFile
  input String fileName;
  input String encoding = "UTF-8";
  input Boolean uses = true;
  output Boolean success;
end loadFile;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)
    if encoding is not None:
        __kwrds["encoding"] = scripting.types.String(encoding)
    if uses is not None:
        __kwrds["uses"] = scripting.types.Boolean(uses)

    __answer = scripting.funcs._ask(omc, "loadFile", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def loadFiles(
    omc: OMCSessionBase,
    fileNames,
    encoding=None,
    numThreads=None,
):
    '''
function loadFiles
  input String[:] fileNames;
  input String encoding = "UTF-8";
  input Integer numThreads = OpenModelica.Scripting.numProcessors();
  output Boolean success;
end loadFiles;
    '''
    __kwrds = {}
    __kwrds["fileNames"] = scripting.types.String[:](fileNames)
    if encoding is not None:
        __kwrds["encoding"] = scripting.types.String(encoding)
    if numThreads is not None:
        __kwrds["numThreads"] = scripting.types.Integer(numThreads)

    __answer = scripting.funcs._ask(omc, "loadFiles", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def loadEncryptedPackage(
    omc: OMCSessionBase,
    fileName,
    workdir=None,
):
    '''
function loadEncryptedPackage
  input String fileName;
  input String workdir = "<default>" "The output directory for imported encrypted files. <default> will put the files to current working directory.";
  output Boolean success;
end loadEncryptedPackage;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)
    if workdir is not None:
        __kwrds["workdir"] = scripting.types.String(workdir)

    __answer = scripting.funcs._ask(omc, "loadEncryptedPackage", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def reloadClass(
    omc: OMCSessionBase,
    name,
    encoding=None,
):
    '''
function reloadClass
  input TypeName name;
  input String encoding = "UTF-8";
  output Boolean success;
end reloadClass;
    '''
    __kwrds = {}
    __kwrds["name"] = scripting.types.TypeName(name)
    if encoding is not None:
        __kwrds["encoding"] = scripting.types.String(encoding)

    __answer = scripting.funcs._ask(omc, "reloadClass", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def loadString(
    omc: OMCSessionBase,
    data,
    filename=None,
    encoding=None,
    merge=None,
):
    '''
function loadString
  input String data;
  input String filename = "<interactive>";
  input String encoding = "UTF-8";
  input Boolean merge = false "if merge is true the parsed AST is merged with the existing AST, default to false which means that is replaced, not merged";
  output Boolean success;
end loadString;
    '''
    __kwrds = {}
    __kwrds["data"] = scripting.types.String(data)
    if filename is not None:
        __kwrds["filename"] = scripting.types.String(filename)
    if encoding is not None:
        __kwrds["encoding"] = scripting.types.String(encoding)
    if merge is not None:
        __kwrds["merge"] = scripting.types.Boolean(merge)

    __answer = scripting.funcs._ask(omc, "loadString", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def parseString(
    omc: OMCSessionBase,
    data,
    filename=None,
):
    '''
function parseString
  input String data;
  input String filename = "<interactive>";
  output TypeName names[:];
end parseString;
    '''
    __kwrds = {}
    __kwrds["data"] = scripting.types.String(data)
    if filename is not None:
        __kwrds["filename"] = scripting.types.String(filename)

    __answer = scripting.funcs._ask(omc, "parseString", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return scripting.types.TypeName[:](__value)


def parseFile(
    omc: OMCSessionBase,
    filename,
    encoding=None,
):
    '''
function parseFile
  input String filename;
  input String encoding = "UTF-8";
  output TypeName names[:];
end parseFile;
    '''
    __kwrds = {}
    __kwrds["filename"] = scripting.types.String(filename)
    if encoding is not None:
        __kwrds["encoding"] = scripting.types.String(encoding)

    __answer = scripting.funcs._ask(omc, "parseFile", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return scripting.types.TypeName[:](__value)


def loadFileInteractiveQualified(
    omc: OMCSessionBase,
    filename,
    encoding=None,
):
    '''
function loadFileInteractiveQualified
  input String filename;
  input String encoding = "UTF-8";
  output TypeName names[:];
end loadFileInteractiveQualified;
    '''
    __kwrds = {}
    __kwrds["filename"] = scripting.types.String(filename)
    if encoding is not None:
        __kwrds["encoding"] = scripting.types.String(encoding)

    __answer = scripting.funcs._ask(omc, "loadFileInteractiveQualified", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return scripting.types.TypeName[:](__value)


def loadFileInteractive(
    omc: OMCSessionBase,
    filename,
    encoding=None,
):
    '''
function loadFileInteractive
  input String filename;
  input String encoding = "UTF-8";
  output TypeName names[:];
end loadFileInteractive;
    '''
    __kwrds = {}
    __kwrds["filename"] = scripting.types.String(filename)
    if encoding is not None:
        __kwrds["encoding"] = scripting.types.String(encoding)

    __answer = scripting.funcs._ask(omc, "loadFileInteractive", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return scripting.types.TypeName[:](__value)


def system(
    omc: OMCSessionBase,
    callStr,
    outputFile=None,
):
    '''
impure function system
  input String callStr "String to call: sh -c $callStr";
  input String outputFile = "" "The output is redirected to this file (unless already done by callStr)";
  output Integer retval "Return value of the system call; usually 0 on success";
end system;
    '''
    __kwrds = {}
    __kwrds["callStr"] = scripting.types.String(callStr)
    if outputFile is not None:
        __kwrds["outputFile"] = scripting.types.String(outputFile)

    __answer = scripting.funcs._ask(omc, "system", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def system_parallel(
    omc: OMCSessionBase,
    callStr,
    numThreads=None,
):
    '''
impure function system_parallel
  input String callStr[:] "String to call: sh -c $callStr";
  input Integer numThreads = numProcessors();
  output Integer retval[:] "Return value of the system call; usually 0 on success";
end system_parallel;
    '''
    __kwrds = {}
    __kwrds["callStr"] = scripting.types.String[:](callStr)
    if numThreads is not None:
        __kwrds["numThreads"] = scripting.types.Integer(numThreads)

    __answer = scripting.funcs._ask(omc, "system_parallel", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def saveAll(
    omc: OMCSessionBase,
    fileName,
):
    '''
function saveAll
  input String fileName;
  output Boolean success;
end saveAll;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)

    __answer = scripting.funcs._ask(omc, "saveAll", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def help(
    omc: OMCSessionBase,
    topic=None,
):
    '''
function help
  input String topic = "topics";
  output String helpText;
end help;
    '''
    __kwrds = {}
    if topic is not None:
        __kwrds["topic"] = scripting.types.String(topic)

    __answer = scripting.funcs._ask(omc, "help", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def clear(
    omc: OMCSessionBase,
):
    '''
function clear
  output Boolean success;
end clear;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "clear", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def clearProgram(
    omc: OMCSessionBase,
):
    '''
function clearProgram
  output Boolean success;
end clearProgram;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "clearProgram", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def clearVariables(
    omc: OMCSessionBase,
):
    '''
function clearVariables
  output Boolean success;
end clearVariables;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "clearVariables", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def generateHeader(
    omc: OMCSessionBase,
    fileName,
):
    '''
function generateHeader
  input String fileName;
  output Boolean success;
end generateHeader;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)

    __answer = scripting.funcs._ask(omc, "generateHeader", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def generateSeparateCode(
    omc: OMCSessionBase,
    className,
    cleanCache=None,
):
    '''
function generateSeparateCode
  input TypeName className;
  input Boolean cleanCache = false "If true, the cache is reset between each generated package. This conserves memory at the cost of speed.";
  output Boolean success;
end generateSeparateCode;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    if cleanCache is not None:
        __kwrds["cleanCache"] = scripting.types.Boolean(cleanCache)

    __answer = scripting.funcs._ask(omc, "generateSeparateCode", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def generateSeparateCodeDependencies(
    omc: OMCSessionBase,
    stampSuffix=None,
):
    '''
function generateSeparateCodeDependencies
  input String stampSuffix = ".c" "Suffix to add to dependencies (often .c.stamp)";
  output String[:] dependencies;
end generateSeparateCodeDependencies;
    '''
    __kwrds = {}
    if stampSuffix is not None:
        __kwrds["stampSuffix"] = scripting.types.String(stampSuffix)

    __answer = scripting.funcs._ask(omc, "generateSeparateCodeDependencies", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def generateSeparateCodeDependenciesMakefile(
    omc: OMCSessionBase,
    filename,
    directory=None,
    suffix=None,
):
    '''
function generateSeparateCodeDependenciesMakefile
  input String filename "The file to write the makefile to";
  input String directory = "" "The relative path of the generated files";
  input String suffix = ".c" "Often .stamp since we do not update all the files";
  output Boolean success;
end generateSeparateCodeDependenciesMakefile;
    '''
    __kwrds = {}
    __kwrds["filename"] = scripting.types.String(filename)
    if directory is not None:
        __kwrds["directory"] = scripting.types.String(directory)
    if suffix is not None:
        __kwrds["suffix"] = scripting.types.String(suffix)

    __answer = scripting.funcs._ask(omc, "generateSeparateCodeDependenciesMakefile", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getLinker(
    omc: OMCSessionBase,
):
    '''
function getLinker
  output String linker;
end getLinker;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getLinker", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setLinker(
    omc: OMCSessionBase,
    linker,
):
    '''
function setLinker
  input String linker;
  output Boolean success;
end setLinker;
    '''
    __kwrds = {}
    __kwrds["linker"] = scripting.types.String(linker)

    __answer = scripting.funcs._ask(omc, "setLinker", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getLinkerFlags(
    omc: OMCSessionBase,
):
    '''
function getLinkerFlags
  output String linkerFlags;
end getLinkerFlags;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getLinkerFlags", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setLinkerFlags(
    omc: OMCSessionBase,
    linkerFlags,
):
    '''
function setLinkerFlags
  input String linkerFlags;
  output Boolean success;
end setLinkerFlags;
    '''
    __kwrds = {}
    __kwrds["linkerFlags"] = scripting.types.String(linkerFlags)

    __answer = scripting.funcs._ask(omc, "setLinkerFlags", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getCompiler(
    omc: OMCSessionBase,
):
    '''
function getCompiler
  output String compiler;
end getCompiler;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getCompiler", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setCompiler(
    omc: OMCSessionBase,
    compiler,
):
    '''
function setCompiler
  input String compiler;
  output Boolean success;
end setCompiler;
    '''
    __kwrds = {}
    __kwrds["compiler"] = scripting.types.String(compiler)

    __answer = scripting.funcs._ask(omc, "setCompiler", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setCFlags(
    omc: OMCSessionBase,
    inString,
):
    '''
function setCFlags
  input String inString;
  output Boolean success;
end setCFlags;
    '''
    __kwrds = {}
    __kwrds["inString"] = scripting.types.String(inString)

    __answer = scripting.funcs._ask(omc, "setCFlags", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getCFlags(
    omc: OMCSessionBase,
):
    '''
function getCFlags
  output String outString;
end getCFlags;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getCFlags", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getCXXCompiler(
    omc: OMCSessionBase,
):
    '''
function getCXXCompiler
  output String compiler;
end getCXXCompiler;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getCXXCompiler", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setCXXCompiler(
    omc: OMCSessionBase,
    compiler,
):
    '''
function setCXXCompiler
  input String compiler;
  output Boolean success;
end setCXXCompiler;
    '''
    __kwrds = {}
    __kwrds["compiler"] = scripting.types.String(compiler)

    __answer = scripting.funcs._ask(omc, "setCXXCompiler", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def verifyCompiler(
    omc: OMCSessionBase,
):
    '''
function verifyCompiler
  output Boolean compilerWorks;
end verifyCompiler;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "verifyCompiler", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setCompilerPath(
    omc: OMCSessionBase,
    compilerPath,
):
    '''
function setCompilerPath
  input String compilerPath;
  output Boolean success;
end setCompilerPath;
    '''
    __kwrds = {}
    __kwrds["compilerPath"] = scripting.types.String(compilerPath)

    __answer = scripting.funcs._ask(omc, "setCompilerPath", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getCompileCommand(
    omc: OMCSessionBase,
):
    '''
function getCompileCommand
  output String compileCommand;
end getCompileCommand;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getCompileCommand", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setCompileCommand(
    omc: OMCSessionBase,
    compileCommand,
):
    '''
function setCompileCommand
  input String compileCommand;
  output Boolean success;
end setCompileCommand;
    '''
    __kwrds = {}
    __kwrds["compileCommand"] = scripting.types.String(compileCommand)

    __answer = scripting.funcs._ask(omc, "setCompileCommand", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setPlotCommand(
    omc: OMCSessionBase,
    plotCommand,
):
    '''
function setPlotCommand
  input String plotCommand;
  output Boolean success;
end setPlotCommand;
    '''
    __kwrds = {}
    __kwrds["plotCommand"] = scripting.types.String(plotCommand)

    __answer = scripting.funcs._ask(omc, "setPlotCommand", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getSettings(
    omc: OMCSessionBase,
):
    '''
function getSettings
  output String settings;
end getSettings;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getSettings", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setTempDirectoryPath(
    omc: OMCSessionBase,
    tempDirectoryPath,
):
    '''
function setTempDirectoryPath
  input String tempDirectoryPath;
  output Boolean success;
end setTempDirectoryPath;
    '''
    __kwrds = {}
    __kwrds["tempDirectoryPath"] = scripting.types.String(tempDirectoryPath)

    __answer = scripting.funcs._ask(omc, "setTempDirectoryPath", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getTempDirectoryPath(
    omc: OMCSessionBase,
):
    '''
function getTempDirectoryPath
  output String tempDirectoryPath;
end getTempDirectoryPath;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getTempDirectoryPath", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getEnvironmentVar(
    omc: OMCSessionBase,
    var,
):
    '''
function getEnvironmentVar
  input String var;
  output String value "returns empty string on failure";
end getEnvironmentVar;
    '''
    __kwrds = {}
    __kwrds["var"] = scripting.types.String(var)

    __answer = scripting.funcs._ask(omc, "getEnvironmentVar", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setEnvironmentVar(
    omc: OMCSessionBase,
    var,
    value,
):
    '''
function setEnvironmentVar
  input String var;
  input String value;
  output Boolean success;
end setEnvironmentVar;
    '''
    __kwrds = {}
    __kwrds["var"] = scripting.types.String(var)
    __kwrds["value"] = scripting.types.String(value)

    __answer = scripting.funcs._ask(omc, "setEnvironmentVar", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def appendEnvironmentVar(
    omc: OMCSessionBase,
    var,
    value,
):
    '''
function appendEnvironmentVar
  input String var;
  input String value;
  output String result "returns \"error\" if the variable could not be appended";
end appendEnvironmentVar;
    '''
    __kwrds = {}
    __kwrds["var"] = scripting.types.String(var)
    __kwrds["value"] = scripting.types.String(value)

    __answer = scripting.funcs._ask(omc, "appendEnvironmentVar", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setInstallationDirectoryPath(
    omc: OMCSessionBase,
    installationDirectoryPath,
):
    '''
function setInstallationDirectoryPath
  input String installationDirectoryPath;
  output Boolean success;
end setInstallationDirectoryPath;
    '''
    __kwrds = {}
    __kwrds["installationDirectoryPath"] = scripting.types.String(installationDirectoryPath)

    __answer = scripting.funcs._ask(omc, "setInstallationDirectoryPath", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getInstallationDirectoryPath(
    omc: OMCSessionBase,
):
    '''
function getInstallationDirectoryPath
  output String installationDirectoryPath;
end getInstallationDirectoryPath;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getInstallationDirectoryPath", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setModelicaPath(
    omc: OMCSessionBase,
    modelicaPath,
):
    '''
function setModelicaPath
  input String modelicaPath;
  output Boolean success;
end setModelicaPath;
    '''
    __kwrds = {}
    __kwrds["modelicaPath"] = scripting.types.String(modelicaPath)

    __answer = scripting.funcs._ask(omc, "setModelicaPath", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getModelicaPath(
    omc: OMCSessionBase,
):
    '''
function getModelicaPath
  output String modelicaPath;
end getModelicaPath;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getModelicaPath", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setCompilerFlags(
    omc: OMCSessionBase,
    compilerFlags,
):
    '''
function setCompilerFlags
  input String compilerFlags;
  output Boolean success;
end setCompilerFlags;
    '''
    __kwrds = {}
    __kwrds["compilerFlags"] = scripting.types.String(compilerFlags)

    __answer = scripting.funcs._ask(omc, "setCompilerFlags", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setDebugFlags(
    omc: OMCSessionBase,
    debugFlags,
):
    '''
function setDebugFlags
  input String debugFlags;
  output Boolean success;
end setDebugFlags;
    '''
    __kwrds = {}
    __kwrds["debugFlags"] = scripting.types.String(debugFlags)

    __answer = scripting.funcs._ask(omc, "setDebugFlags", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def clearDebugFlags(
    omc: OMCSessionBase,
):
    '''
function clearDebugFlags
  output Boolean success;
end clearDebugFlags;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "clearDebugFlags", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setPreOptModules(
    omc: OMCSessionBase,
    modules,
):
    '''
function setPreOptModules
  input String modules;
  output Boolean success;
end setPreOptModules;
    '''
    __kwrds = {}
    __kwrds["modules"] = scripting.types.String(modules)

    __answer = scripting.funcs._ask(omc, "setPreOptModules", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setCheapMatchingAlgorithm(
    omc: OMCSessionBase,
    matchingAlgorithm,
):
    '''
function setCheapMatchingAlgorithm
  input Integer matchingAlgorithm;
  output Boolean success;
end setCheapMatchingAlgorithm;
    '''
    __kwrds = {}
    __kwrds["matchingAlgorithm"] = scripting.types.Integer(matchingAlgorithm)

    __answer = scripting.funcs._ask(omc, "setCheapMatchingAlgorithm", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getMatchingAlgorithm(
    omc: OMCSessionBase,
):
    '''
function getMatchingAlgorithm
  output String selected;
end getMatchingAlgorithm;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getMatchingAlgorithm", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


__getAvailableMatchingAlgorithms_output = namedtuple(
    "OMCOutput",
    "allChoices, allComments",
)


def getAvailableMatchingAlgorithms(
    omc: OMCSessionBase,
):
    '''
function getAvailableMatchingAlgorithms
  output String[:] allChoices;
  output String[:] allComments;
end getAvailableMatchingAlgorithms;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getAvailableMatchingAlgorithms", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __getAvailableMatchingAlgorithms_output(
        allChoices=__value[0],
        allComments=__value[1],
    )


def setMatchingAlgorithm(
    omc: OMCSessionBase,
    matchingAlgorithm,
):
    '''
function setMatchingAlgorithm
  input String matchingAlgorithm;
  output Boolean success;
end setMatchingAlgorithm;
    '''
    __kwrds = {}
    __kwrds["matchingAlgorithm"] = scripting.types.String(matchingAlgorithm)

    __answer = scripting.funcs._ask(omc, "setMatchingAlgorithm", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getIndexReductionMethod(
    omc: OMCSessionBase,
):
    '''
function getIndexReductionMethod
  output String selected;
end getIndexReductionMethod;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getIndexReductionMethod", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


__getAvailableIndexReductionMethods_output = namedtuple(
    "OMCOutput",
    "allChoices, allComments",
)


def getAvailableIndexReductionMethods(
    omc: OMCSessionBase,
):
    '''
function getAvailableIndexReductionMethods
  output String[:] allChoices;
  output String[:] allComments;
end getAvailableIndexReductionMethods;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getAvailableIndexReductionMethods", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __getAvailableIndexReductionMethods_output(
        allChoices=__value[0],
        allComments=__value[1],
    )


def setIndexReductionMethod(
    omc: OMCSessionBase,
    method,
):
    '''
function setIndexReductionMethod
  input String method;
  output Boolean success;
end setIndexReductionMethod;
    '''
    __kwrds = {}
    __kwrds["method"] = scripting.types.String(method)

    __answer = scripting.funcs._ask(omc, "setIndexReductionMethod", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setPostOptModules(
    omc: OMCSessionBase,
    modules,
):
    '''
function setPostOptModules
  input String modules;
  output Boolean success;
end setPostOptModules;
    '''
    __kwrds = {}
    __kwrds["modules"] = scripting.types.String(modules)

    __answer = scripting.funcs._ask(omc, "setPostOptModules", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getTearingMethod(
    omc: OMCSessionBase,
):
    '''
function getTearingMethod
  output String selected;
end getTearingMethod;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getTearingMethod", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


__getAvailableTearingMethods_output = namedtuple(
    "OMCOutput",
    "allChoices, allComments",
)


def getAvailableTearingMethods(
    omc: OMCSessionBase,
):
    '''
function getAvailableTearingMethods
  output String[:] allChoices;
  output String[:] allComments;
end getAvailableTearingMethods;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getAvailableTearingMethods", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __getAvailableTearingMethods_output(
        allChoices=__value[0],
        allComments=__value[1],
    )


def setTearingMethod(
    omc: OMCSessionBase,
    tearingMethod,
):
    '''
function setTearingMethod
  input String tearingMethod;
  output Boolean success;
end setTearingMethod;
    '''
    __kwrds = {}
    __kwrds["tearingMethod"] = scripting.types.String(tearingMethod)

    __answer = scripting.funcs._ask(omc, "setTearingMethod", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setCommandLineOptions(
    omc: OMCSessionBase,
    option,
):
    '''
function setCommandLineOptions
  input String option;
  output Boolean success;
end setCommandLineOptions;
    '''
    __kwrds = {}
    __kwrds["option"] = scripting.types.String(option)

    __answer = scripting.funcs._ask(omc, "setCommandLineOptions", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getCommandLineOptions(
    omc: OMCSessionBase,
):
    '''
function getCommandLineOptions
  output String[:] flags;
end getCommandLineOptions;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getCommandLineOptions", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


__getConfigFlagValidOptions_output = namedtuple(
    "OMCOutput",
    "validOptions, mainDescription, descriptions",
)


def getConfigFlagValidOptions(
    omc: OMCSessionBase,
    flag,
):
    '''
function getConfigFlagValidOptions
  input String flag;
  output String validOptions[:];
  output String mainDescription;
  output String descriptions[:];
end getConfigFlagValidOptions;
    '''
    __kwrds = {}
    __kwrds["flag"] = scripting.types.String(flag)

    __answer = scripting.funcs._ask(omc, "getConfigFlagValidOptions", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __getConfigFlagValidOptions_output(
        validOptions=__value[0],
        mainDescription=__value[1],
        descriptions=__value[2],
    )


def clearCommandLineOptions(
    omc: OMCSessionBase,
):
    '''
function clearCommandLineOptions
  output Boolean success;
end clearCommandLineOptions;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "clearCommandLineOptions", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getVersion(
    omc: OMCSessionBase,
    cl=None,
):
    '''
function getVersion
  input TypeName cl = $Code(OpenModelica);
  output String version;
end getVersion;
    '''
    __kwrds = {}
    if cl is not None:
        __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "getVersion", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def regularFileExists(
    omc: OMCSessionBase,
    fileName,
):
    '''
function regularFileExists
  input String fileName;
  output Boolean exists;
end regularFileExists;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)

    __answer = scripting.funcs._ask(omc, "regularFileExists", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def directoryExists(
    omc: OMCSessionBase,
    dirName,
):
    '''
function directoryExists
  input String dirName;
  output Boolean exists;
end directoryExists;
    '''
    __kwrds = {}
    __kwrds["dirName"] = scripting.types.String(dirName)

    __answer = scripting.funcs._ask(omc, "directoryExists", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


__stat_output = namedtuple(
    "OMCOutput",
    "success, fileSize, mtime",
)


def stat(
    omc: OMCSessionBase,
    fileName,
):
    '''
impure function stat
  input String fileName;
  output Boolean success;
  output Real fileSize;
  output Real mtime;
end stat;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)

    __answer = scripting.funcs._ask(omc, "stat", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __stat_output(
        success=__value[0],
        fileSize=__value[1],
        mtime=__value[2],
    )


def readFile(
    omc: OMCSessionBase,
    fileName,
):
    '''
impure function readFile
  input String fileName;
  output String contents;
end readFile;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)

    __answer = scripting.funcs._ask(omc, "readFile", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def writeFile(
    omc: OMCSessionBase,
    fileName,
    data,
    append=None,
):
    '''
impure function writeFile
  input String fileName;
  input String data;
  input Boolean append = false;
  output Boolean success;
end writeFile;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)
    __kwrds["data"] = scripting.types.String(data)
    if append is not None:
        __kwrds["append"] = scripting.types.Boolean(append)

    __answer = scripting.funcs._ask(omc, "writeFile", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def compareFilesAndMove(
    omc: OMCSessionBase,
    newFile,
    oldFile,
):
    '''
impure function compareFilesAndMove
  input String newFile;
  input String oldFile;
  output Boolean success;
end compareFilesAndMove;
    '''
    __kwrds = {}
    __kwrds["newFile"] = scripting.types.String(newFile)
    __kwrds["oldFile"] = scripting.types.String(oldFile)

    __answer = scripting.funcs._ask(omc, "compareFilesAndMove", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def compareFiles(
    omc: OMCSessionBase,
    file1,
    file2,
):
    '''
impure function compareFiles
  input String file1;
  input String file2;
  output Boolean isEqual;
end compareFiles;
    '''
    __kwrds = {}
    __kwrds["file1"] = scripting.types.String(file1)
    __kwrds["file2"] = scripting.types.String(file2)

    __answer = scripting.funcs._ask(omc, "compareFiles", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def alarm(
    omc: OMCSessionBase,
    seconds,
):
    '''
impure function alarm
  input Integer seconds;
  output Integer previousSeconds;
end alarm;
    '''
    __kwrds = {}
    __kwrds["seconds"] = scripting.types.Integer(seconds)

    __answer = scripting.funcs._ask(omc, "alarm", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


__regex_output = namedtuple(
    "OMCOutput",
    "numMatches, matchedSubstrings",
)


def regex(
    omc: OMCSessionBase,
    str,
    re,
    maxMatches=None,
    extended=None,
    caseInsensitive=None,
):
    '''
function regex
  input String str;
  input String re;
  input Integer maxMatches = 1 "The maximum number of matches that will be returned";
  input Boolean extended = true "Use POSIX extended or regular syntax";
  input Boolean caseInsensitive = false;
  output Integer numMatches "-1 is an error, 0 means no match, else returns a number 1..maxMatches";
  output String matchedSubstrings[maxMatches] "unmatched strings are returned as empty";
end regex;
    '''
    __kwrds = {}
    __kwrds["str"] = scripting.types.String(str)
    __kwrds["re"] = scripting.types.String(re)
    if maxMatches is not None:
        __kwrds["maxMatches"] = scripting.types.Integer(maxMatches)
    if extended is not None:
        __kwrds["extended"] = scripting.types.Boolean(extended)
    if caseInsensitive is not None:
        __kwrds["caseInsensitive"] = scripting.types.Boolean(caseInsensitive)

    __answer = scripting.funcs._ask(omc, "regex", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __regex_output(
        numMatches=__value[0],
        matchedSubstrings=__value[1],
    )


def regexBool(
    omc: OMCSessionBase,
    str,
    re,
    extended=None,
    caseInsensitive=None,
):
    '''
function regexBool
  input String str;
  input String re;
  input Boolean extended = true "Use POSIX extended or regular syntax";
  input Boolean caseInsensitive = false;
  output Boolean matches;
end regexBool;
    '''
    __kwrds = {}
    __kwrds["str"] = scripting.types.String(str)
    __kwrds["re"] = scripting.types.String(re)
    if extended is not None:
        __kwrds["extended"] = scripting.types.Boolean(extended)
    if caseInsensitive is not None:
        __kwrds["caseInsensitive"] = scripting.types.Boolean(caseInsensitive)

    __answer = scripting.funcs._ask(omc, "regexBool", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def testsuiteFriendlyName(
    omc: OMCSessionBase,
    path,
):
    '''
function testsuiteFriendlyName
  input String path;
  output String fixed;
end testsuiteFriendlyName;
    '''
    __kwrds = {}
    __kwrds["path"] = scripting.types.String(path)

    __answer = scripting.funcs._ask(omc, "testsuiteFriendlyName", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def readFileNoNumeric(
    omc: OMCSessionBase,
    fileName,
):
    '''
function readFileNoNumeric
  input String fileName;
  output String contents;
end readFileNoNumeric;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)

    __answer = scripting.funcs._ask(omc, "readFileNoNumeric", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getErrorString(
    omc: OMCSessionBase,
    warningsAsErrors=None,
):
    '''
impure function getErrorString
  input Boolean warningsAsErrors = false;
  output String errorString;
end getErrorString;
    '''
    __kwrds = {}
    if warningsAsErrors is not None:
        __kwrds["warningsAsErrors"] = scripting.types.Boolean(warningsAsErrors)

    __answer = scripting.funcs._ask(omc, "getErrorString", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getMessagesString(
    omc: OMCSessionBase,
):
    '''
function getMessagesString
  output String messagesString;
end getMessagesString;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getMessagesString", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


# def getMessagesStringInternal(
#     omc: OMCSessionBase,
#     unique=None,
# ):
#     '''
# function getMessagesStringInternal
#   input Boolean unique = true;
#   output ErrorMessage[:] messagesString;
# end getMessagesStringInternal;
#     '''
#     __kwrds = {}
#     if unique is not None:
#         __kwrds["unique"] = scripting.types.Boolean(unique)
# 
#     __answer = scripting.funcs._ask(omc, "getMessagesStringInternal", **__kwrds)
#     try:
#         __value = parsers.parseOMCValue(__answer)
#     except parsers.NoMatch:
#         if __answer.lstrip().startswith("Error"):
#             raise scripting.exceptions.OMCError(__answer)
#         if not __answer or __answer.isspace():
#             return None
#         raise
# 
#     return scripting.types.ErrorMessage[:](__value)


__countMessages_output = namedtuple(
    "OMCOutput",
    "numMessages, numErrors, numWarnings",
)


def countMessages(
    omc: OMCSessionBase,
):
    '''
function countMessages
  output Integer numMessages;
  output Integer numErrors;
  output Integer numWarnings;
end countMessages;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "countMessages", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __countMessages_output(
        numMessages=__value[0],
        numErrors=__value[1],
        numWarnings=__value[2],
    )


def clearMessages(
    omc: OMCSessionBase,
):
    '''
function clearMessages
  output Boolean success;
end clearMessages;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "clearMessages", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def runScript(
    omc: OMCSessionBase,
    fileName,
):
    '''
impure function runScript
  input String fileName "*.mos";
  output String result;
end runScript;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)

    __answer = scripting.funcs._ask(omc, "runScript", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def echo(
    omc: OMCSessionBase,
    setEcho,
):
    '''
function echo
  input Boolean setEcho;
  output Boolean newEcho;
end echo;
    '''
    __kwrds = {}
    __kwrds["setEcho"] = scripting.types.Boolean(setEcho)

    __answer = scripting.funcs._ask(omc, "echo", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getClassesInModelicaPath(
    omc: OMCSessionBase,
):
    '''
function getClassesInModelicaPath
  output String classesInModelicaPath;
end getClassesInModelicaPath;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getClassesInModelicaPath", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getAnnotationVersion(
    omc: OMCSessionBase,
):
    '''
function getAnnotationVersion
  output String annotationVersion;
end getAnnotationVersion;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getAnnotationVersion", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setAnnotationVersion(
    omc: OMCSessionBase,
    annotationVersion,
):
    '''
function setAnnotationVersion
  input String annotationVersion;
  output Boolean success;
end setAnnotationVersion;
    '''
    __kwrds = {}
    __kwrds["annotationVersion"] = scripting.types.String(annotationVersion)

    __answer = scripting.funcs._ask(omc, "setAnnotationVersion", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getNoSimplify(
    omc: OMCSessionBase,
):
    '''
function getNoSimplify
  output Boolean noSimplify;
end getNoSimplify;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getNoSimplify", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setNoSimplify(
    omc: OMCSessionBase,
    noSimplify,
):
    '''
function setNoSimplify
  input Boolean noSimplify;
  output Boolean success;
end setNoSimplify;
    '''
    __kwrds = {}
    __kwrds["noSimplify"] = scripting.types.Boolean(noSimplify)

    __answer = scripting.funcs._ask(omc, "setNoSimplify", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getVectorizationLimit(
    omc: OMCSessionBase,
):
    '''
function getVectorizationLimit
  output Integer vectorizationLimit;
end getVectorizationLimit;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getVectorizationLimit", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setVectorizationLimit(
    omc: OMCSessionBase,
    vectorizationLimit,
):
    '''
function setVectorizationLimit
  input Integer vectorizationLimit;
  output Boolean success;
end setVectorizationLimit;
    '''
    __kwrds = {}
    __kwrds["vectorizationLimit"] = scripting.types.Integer(vectorizationLimit)

    __answer = scripting.funcs._ask(omc, "setVectorizationLimit", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getDefaultOpenCLDevice(
    omc: OMCSessionBase,
):
    '''
function getDefaultOpenCLDevice
  output Integer defdevid;
end getDefaultOpenCLDevice;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getDefaultOpenCLDevice", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setDefaultOpenCLDevice(
    omc: OMCSessionBase,
    defdevid,
):
    '''
function setDefaultOpenCLDevice
  input Integer defdevid;
  output Boolean success;
end setDefaultOpenCLDevice;
    '''
    __kwrds = {}
    __kwrds["defdevid"] = scripting.types.Integer(defdevid)

    __answer = scripting.funcs._ask(omc, "setDefaultOpenCLDevice", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setShowAnnotations(
    omc: OMCSessionBase,
    show,
):
    '''
function setShowAnnotations
  input Boolean show;
  output Boolean success;
end setShowAnnotations;
    '''
    __kwrds = {}
    __kwrds["show"] = scripting.types.Boolean(show)

    __answer = scripting.funcs._ask(omc, "setShowAnnotations", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getShowAnnotations(
    omc: OMCSessionBase,
):
    '''
function getShowAnnotations
  output Boolean show;
end getShowAnnotations;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getShowAnnotations", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setOrderConnections(
    omc: OMCSessionBase,
    orderConnections,
):
    '''
function setOrderConnections
  input Boolean orderConnections;
  output Boolean success;
end setOrderConnections;
    '''
    __kwrds = {}
    __kwrds["orderConnections"] = scripting.types.Boolean(orderConnections)

    __answer = scripting.funcs._ask(omc, "setOrderConnections", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getOrderConnections(
    omc: OMCSessionBase,
):
    '''
function getOrderConnections
  output Boolean orderConnections;
end getOrderConnections;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getOrderConnections", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setLanguageStandard(
    omc: OMCSessionBase,
    inVersion,
):
    '''
function setLanguageStandard
  input String inVersion;
  output Boolean success;
end setLanguageStandard;
    '''
    __kwrds = {}
    __kwrds["inVersion"] = scripting.types.String(inVersion)

    __answer = scripting.funcs._ask(omc, "setLanguageStandard", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getLanguageStandard(
    omc: OMCSessionBase,
):
    '''
function getLanguageStandard
  output String outVersion;
end getLanguageStandard;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getLanguageStandard", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getAstAsCorbaString(
    omc: OMCSessionBase,
    fileName=None,
):
    '''
function getAstAsCorbaString
  input String fileName = "<interactive>";
  output String result "returns the string if fileName is interactive; else it returns ok or error depending on if writing the file succeeded";
end getAstAsCorbaString;
    '''
    __kwrds = {}
    if fileName is not None:
        __kwrds["fileName"] = scripting.types.String(fileName)

    __answer = scripting.funcs._ask(omc, "getAstAsCorbaString", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def cd(
    omc: OMCSessionBase,
    newWorkingDirectory=None,
):
    '''
function cd
  input String newWorkingDirectory = "";
  output String workingDirectory;
end cd;
    '''
    __kwrds = {}
    if newWorkingDirectory is not None:
        __kwrds["newWorkingDirectory"] = scripting.types.String(newWorkingDirectory)

    __answer = scripting.funcs._ask(omc, "cd", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def mkdir(
    omc: OMCSessionBase,
    newDirectory,
):
    '''
function mkdir
  input String newDirectory;
  output Boolean success;
end mkdir;
    '''
    __kwrds = {}
    __kwrds["newDirectory"] = scripting.types.String(newDirectory)

    __answer = scripting.funcs._ask(omc, "mkdir", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def copy(
    omc: OMCSessionBase,
    source,
    destination,
):
    '''
function copy
  input String source;
  input String destination;
  output Boolean success;
end copy;
    '''
    __kwrds = {}
    __kwrds["source"] = scripting.types.String(source)
    __kwrds["destination"] = scripting.types.String(destination)

    __answer = scripting.funcs._ask(omc, "copy", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def remove(
    omc: OMCSessionBase,
    path,
):
    '''
function remove
  input String path;
  output Boolean success "Returns true on success.";
end remove;
    '''
    __kwrds = {}
    __kwrds["path"] = scripting.types.String(path)

    __answer = scripting.funcs._ask(omc, "remove", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def checkModel(
    omc: OMCSessionBase,
    className,
):
    '''
function checkModel
  input TypeName className;
  output String result;
end checkModel;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)

    __answer = scripting.funcs._ask(omc, "checkModel", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def checkAllModelsRecursive(
    omc: OMCSessionBase,
    className,
    checkProtected=None,
):
    '''
function checkAllModelsRecursive
  input TypeName className;
  input Boolean checkProtected = false "Checks also protected classes if true";
  output String result;
end checkAllModelsRecursive;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    if checkProtected is not None:
        __kwrds["checkProtected"] = scripting.types.Boolean(checkProtected)

    __answer = scripting.funcs._ask(omc, "checkAllModelsRecursive", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def typeOf(
    omc: OMCSessionBase,
    variableName,
):
    '''
function typeOf
  input VariableName variableName;
  output String result;
end typeOf;
    '''
    __kwrds = {}
    __kwrds["variableName"] = scripting.types.VariableName(variableName)

    __answer = scripting.funcs._ask(omc, "typeOf", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def instantiateModel(
    omc: OMCSessionBase,
    className,
):
    '''
function instantiateModel
  input TypeName className;
  output String result;
end instantiateModel;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)

    __answer = scripting.funcs._ask(omc, "instantiateModel", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def buildOpenTURNSInterface(
    omc: OMCSessionBase,
    className,
    pythonTemplateFile,
    showFlatModelica=None,
):
    '''
function buildOpenTURNSInterface
  input TypeName className;
  input String pythonTemplateFile;
  input Boolean showFlatModelica = false;
  output String outPythonScript;
end buildOpenTURNSInterface;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    __kwrds["pythonTemplateFile"] = scripting.types.String(pythonTemplateFile)
    if showFlatModelica is not None:
        __kwrds["showFlatModelica"] = scripting.types.Boolean(showFlatModelica)

    __answer = scripting.funcs._ask(omc, "buildOpenTURNSInterface", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def runOpenTURNSPythonScript(
    omc: OMCSessionBase,
    pythonScriptFile,
):
    '''
function runOpenTURNSPythonScript
  input String pythonScriptFile;
  output String logOutputFile;
end runOpenTURNSPythonScript;
    '''
    __kwrds = {}
    __kwrds["pythonScriptFile"] = scripting.types.String(pythonScriptFile)

    __answer = scripting.funcs._ask(omc, "runOpenTURNSPythonScript", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def generateCode(
    omc: OMCSessionBase,
    className,
):
    '''
function generateCode
  input TypeName className;
  output Boolean success;
end generateCode;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)

    __answer = scripting.funcs._ask(omc, "generateCode", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def loadModel(
    omc: OMCSessionBase,
    className,
    priorityVersion=None,
    notify=None,
    languageStandard=None,
    requireExactVersion=None,
):
    '''
function loadModel
  input TypeName className;
  input String[:] priorityVersion = {"default"};
  input Boolean notify = false "Give a notification of the libraries and versions that were loaded";
  input String languageStandard = "" "Override the set language standard. Parse with the given setting, but do not change it permanently.";
  input Boolean requireExactVersion = false "If the version is required to be exact, if there is a uses Modelica(version=\"3.2\"), Modelica 3.2.1 will not match it.";
  output Boolean success;
end loadModel;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    if priorityVersion is not None:
        __kwrds["priorityVersion"] = scripting.types.String[:](priorityVersion)
    if notify is not None:
        __kwrds["notify"] = scripting.types.Boolean(notify)
    if languageStandard is not None:
        __kwrds["languageStandard"] = scripting.types.String(languageStandard)
    if requireExactVersion is not None:
        __kwrds["requireExactVersion"] = scripting.types.Boolean(requireExactVersion)

    __answer = scripting.funcs._ask(omc, "loadModel", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def deleteFile(
    omc: OMCSessionBase,
    fileName,
):
    '''
function deleteFile
  input String fileName;
  output Boolean success;
end deleteFile;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)

    __answer = scripting.funcs._ask(omc, "deleteFile", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def saveModel(
    omc: OMCSessionBase,
    fileName,
    className,
):
    '''
function saveModel
  input String fileName;
  input TypeName className;
  output Boolean success;
end saveModel;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)
    __kwrds["className"] = scripting.types.TypeName(className)

    __answer = scripting.funcs._ask(omc, "saveModel", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def saveTotalModel(
    omc: OMCSessionBase,
    fileName,
    className,
    stripAnnotations=None,
    stripComments=None,
):
    '''
function saveTotalModel
  input String fileName;
  input TypeName className;
  input Boolean stripAnnotations = false;
  input Boolean stripComments = false;
  output Boolean success;
end saveTotalModel;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)
    __kwrds["className"] = scripting.types.TypeName(className)
    if stripAnnotations is not None:
        __kwrds["stripAnnotations"] = scripting.types.Boolean(stripAnnotations)
    if stripComments is not None:
        __kwrds["stripComments"] = scripting.types.Boolean(stripComments)

    __answer = scripting.funcs._ask(omc, "saveTotalModel", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def save(
    omc: OMCSessionBase,
    className,
):
    '''
function save
  input TypeName className;
  output Boolean success;
end save;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)

    __answer = scripting.funcs._ask(omc, "save", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def translateGraphics(
    omc: OMCSessionBase,
    className,
):
    '''
function translateGraphics
  input TypeName className;
  output String result;
end translateGraphics;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)

    __answer = scripting.funcs._ask(omc, "translateGraphics", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


# def codeToString(
#     omc: OMCSessionBase,
#     className,
# ):
#     '''
# function codeToString
#   input $Code className;
#   output String string;
# end codeToString;
#     '''
#     __kwrds = {}
#     __kwrds["className"] = scripting.types.$Code(className)
# 
#     __answer = scripting.funcs._ask(omc, "codeToString", **__kwrds)
#     try:
#         __value = parsers.parseOMCValue(__answer)
#     except parsers.NoMatch:
#         if __answer.lstrip().startswith("Error"):
#             raise scripting.exceptions.OMCError(__answer)
#         if not __answer or __answer.isspace():
#             return None
#         raise
# 
#     return __value


__dumpXMLDAE_output = namedtuple(
    "OMCOutput",
    "success, xmlfileName",
)


def dumpXMLDAE(
    omc: OMCSessionBase,
    className,
    translationLevel=None,
    addOriginalIncidenceMatrix=None,
    addSolvingInfo=None,
    addMathMLCode=None,
    dumpResiduals=None,
    fileNamePrefix=None,
    rewriteRulesFile=None,
):
    '''
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
end dumpXMLDAE;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    if translationLevel is not None:
        __kwrds["translationLevel"] = scripting.types.String(translationLevel)
    if addOriginalIncidenceMatrix is not None:
        __kwrds["addOriginalIncidenceMatrix"] = scripting.types.Boolean(addOriginalIncidenceMatrix)
    if addSolvingInfo is not None:
        __kwrds["addSolvingInfo"] = scripting.types.Boolean(addSolvingInfo)
    if addMathMLCode is not None:
        __kwrds["addMathMLCode"] = scripting.types.Boolean(addMathMLCode)
    if dumpResiduals is not None:
        __kwrds["dumpResiduals"] = scripting.types.Boolean(dumpResiduals)
    if fileNamePrefix is not None:
        __kwrds["fileNamePrefix"] = scripting.types.String(fileNamePrefix)
    if rewriteRulesFile is not None:
        __kwrds["rewriteRulesFile"] = scripting.types.String(rewriteRulesFile)

    __answer = scripting.funcs._ask(omc, "dumpXMLDAE", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __dumpXMLDAE_output(
        success=__value[0],
        xmlfileName=__value[1],
    )


__convertUnits_output = namedtuple(
    "OMCOutput",
    "unitsCompatible, scaleFactor, offset",
)


def convertUnits(
    omc: OMCSessionBase,
    s1,
    s2,
):
    '''
function convertUnits
  input String s1;
  input String s2;
  output Boolean unitsCompatible;
  output Real scaleFactor;
  output Real offset;
end convertUnits;
    '''
    __kwrds = {}
    __kwrds["s1"] = scripting.types.String(s1)
    __kwrds["s2"] = scripting.types.String(s2)

    __answer = scripting.funcs._ask(omc, "convertUnits", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __convertUnits_output(
        unitsCompatible=__value[0],
        scaleFactor=__value[1],
        offset=__value[2],
    )


def getDerivedUnits(
    omc: OMCSessionBase,
    baseUnit,
):
    '''
function getDerivedUnits
  input String baseUnit;
  output String[:] derivedUnits;
end getDerivedUnits;
    '''
    __kwrds = {}
    __kwrds["baseUnit"] = scripting.types.String(baseUnit)

    __answer = scripting.funcs._ask(omc, "getDerivedUnits", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def listVariables(
    omc: OMCSessionBase,
):
    '''
function listVariables
  output TypeName variables[:];
end listVariables;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "listVariables", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return scripting.types.TypeName[:](__value)


def strtok(
    omc: OMCSessionBase,
    string,
    token,
):
    '''
function strtok
  input String string;
  input String token;
  output String[:] strings;
end strtok;
    '''
    __kwrds = {}
    __kwrds["string"] = scripting.types.String(string)
    __kwrds["token"] = scripting.types.String(token)

    __answer = scripting.funcs._ask(omc, "strtok", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def stringSplit(
    omc: OMCSessionBase,
    string,
    token,
):
    '''
function stringSplit
  input String string;
  input String token "single character only";
  output String[:] strings;
end stringSplit;
    '''
    __kwrds = {}
    __kwrds["string"] = scripting.types.String(string)
    __kwrds["token"] = scripting.types.String(token)

    __answer = scripting.funcs._ask(omc, "stringSplit", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def stringReplace(
    omc: OMCSessionBase,
    str,
    source,
    target,
):
    '''
function stringReplace
  input String str;
  input String source;
  input String target;
  output String res;
end stringReplace;
    '''
    __kwrds = {}
    __kwrds["str"] = scripting.types.String(str)
    __kwrds["source"] = scripting.types.String(source)
    __kwrds["target"] = scripting.types.String(target)

    __answer = scripting.funcs._ask(omc, "stringReplace", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def escapeXML(
    omc: OMCSessionBase,
    inStr,
):
    '''
function escapeXML
  input String inStr;
  output String outStr;
end escapeXML;
    '''
    __kwrds = {}
    __kwrds["inStr"] = scripting.types.String(inStr)

    __answer = scripting.funcs._ask(omc, "escapeXML", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


# def list(
#     omc: OMCSessionBase,
#     class_=None,
#     interfaceOnly=None,
#     shortOnly=None,
#     exportKind=None,
# ):
#     '''
# function list
#   input TypeName class_ = $Code(AllLoadedClasses);
#   input Boolean interfaceOnly = false;
#   input Boolean shortOnly = false "only short class definitions";
#   input ExportKind exportKind = ExportKind.Absyn;
#   output String contents;
# end list;
#     '''
#     __kwrds = {}
#     if class_ is not None:
#         __kwrds["class_"] = scripting.types.TypeName(class_)
#     if interfaceOnly is not None:
#         __kwrds["interfaceOnly"] = scripting.types.Boolean(interfaceOnly)
#     if shortOnly is not None:
#         __kwrds["shortOnly"] = scripting.types.Boolean(shortOnly)
#     if exportKind is not None:
#         __kwrds["exportKind"] = scripting.types.ExportKind(exportKind)
# 
#     __answer = scripting.funcs._ask(omc, "list", **__kwrds)
#     try:
#         __value = parsers.parseOMCValue(__answer)
#     except parsers.NoMatch:
#         if __answer.lstrip().startswith("Error"):
#             raise scripting.exceptions.OMCError(__answer)
#         if not __answer or __answer.isspace():
#             return None
#         raise
# 
#     return __value


def listFile(
    omc: OMCSessionBase,
    class_,
):
    '''
function listFile
  input TypeName class_;
  output String contents;
end listFile;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)

    __answer = scripting.funcs._ask(omc, "listFile", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


# def diffModelicaFileListings(
#     omc: OMCSessionBase,
#     before,
#     after,
#     diffFormat=None,
# ):
#     '''
# function diffModelicaFileListings
#   input String before, after;
#   input DiffFormat diffFormat = DiffFormat.color;
#   output String result;
# end diffModelicaFileListings;
#     '''
#     __kwrds = {}
#     __kwrds["before"] = scripting.types.String(before)
#     __kwrds["after"] = scripting.types.String(after)
#     if diffFormat is not None:
#         __kwrds["diffFormat"] = scripting.types.DiffFormat(diffFormat)
# 
#     __answer = scripting.funcs._ask(omc, "diffModelicaFileListings", **__kwrds)
#     try:
#         __value = parsers.parseOMCValue(__answer)
#     except parsers.NoMatch:
#         if __answer.lstrip().startswith("Error"):
#             raise scripting.exceptions.OMCError(__answer)
#         if not __answer or __answer.isspace():
#             return None
#         raise
# 
#     return __value


def exportToFigaro(
    omc: OMCSessionBase,
    path,
    database,
    mode,
    options,
    processor,
    directory=None,
):
    '''
function exportToFigaro
  input TypeName path;
  input String directory = cd();
  input String database;
  input String mode;
  input String options;
  input String processor;
  output Boolean success;
end exportToFigaro;
    '''
    __kwrds = {}
    __kwrds["path"] = scripting.types.TypeName(path)
    __kwrds["database"] = scripting.types.String(database)
    __kwrds["mode"] = scripting.types.String(mode)
    __kwrds["options"] = scripting.types.String(options)
    __kwrds["processor"] = scripting.types.String(processor)
    if directory is not None:
        __kwrds["directory"] = scripting.types.String(directory)

    __answer = scripting.funcs._ask(omc, "exportToFigaro", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def inferBindings(
    omc: OMCSessionBase,
    path,
):
    '''
function inferBindings
  input TypeName path;
  output Boolean success;
end inferBindings;
    '''
    __kwrds = {}
    __kwrds["path"] = scripting.types.TypeName(path)

    __answer = scripting.funcs._ask(omc, "inferBindings", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def generateVerificationScenarios(
    omc: OMCSessionBase,
    path,
):
    '''
function generateVerificationScenarios
  input TypeName path;
  output Boolean success;
end generateVerificationScenarios;
    '''
    __kwrds = {}
    __kwrds["path"] = scripting.types.TypeName(path)

    __answer = scripting.funcs._ask(omc, "generateVerificationScenarios", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def rewriteBlockCall(
    omc: OMCSessionBase,
    className,
    inDefs,
):
    '''
function rewriteBlockCall
  input TypeName className;
  input TypeName inDefs;
  output Boolean success;
end rewriteBlockCall;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    __kwrds["inDefs"] = scripting.types.TypeName(inDefs)

    __answer = scripting.funcs._ask(omc, "rewriteBlockCall", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def realpath(
    omc: OMCSessionBase,
    name,
):
    '''
function realpath
  input String name "Absolute or relative file or directory name";
  output String fullName "Full path of 'name'";
end realpath;
    '''
    __kwrds = {}
    __kwrds["name"] = scripting.types.String(name)

    __answer = scripting.funcs._ask(omc, "realpath", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def uriToFilename(
    omc: OMCSessionBase,
    uri,
):
    '''
function uriToFilename
  input String uri;
  output String filename = "";
end uriToFilename;
    '''
    __kwrds = {}
    __kwrds["uri"] = scripting.types.String(uri)

    __answer = scripting.funcs._ask(omc, "uriToFilename", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getLoadedLibraries(
    omc: OMCSessionBase,
):
    '''
function getLoadedLibraries
  output String[:, 2] libraries;
end getLoadedLibraries;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getLoadedLibraries", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


# __solveLinearSystem_output = namedtuple(
#     "OMCOutput",
#     "X, info",
# )
# 
# 
# def solveLinearSystem(
#     omc: OMCSessionBase,
#     A,
#     B,
#     solver=None,
#     isInt=None,
# ):
#     '''
# function solveLinearSystem
#   input Real[size(B, 1), size(B, 1)] A;
#   input Real[:] B;
#   input LinearSystemSolver solver = LinearSystemSolver.dgesv;
#   input Integer[:] isInt = {-1} "list of indices that are integers";
#   output Real[size(B, 1)] X;
#   output Integer info;
# end solveLinearSystem;
#     '''
#     __kwrds = {}
#     __kwrds["A"] = scripting.types.Real[:,:](A)
#     __kwrds["B"] = scripting.types.Real[:](B)
#     if solver is not None:
#         __kwrds["solver"] = scripting.types.LinearSystemSolver(solver)
#     if isInt is not None:
#         __kwrds["isInt"] = scripting.types.Integer[:](isInt)
# 
#     __answer = scripting.funcs._ask(omc, "solveLinearSystem", **__kwrds)
#     try:
#         __value = parsers.parseOMCValue(__answer)
#     except parsers.NoMatch:
#         if __answer.lstrip().startswith("Error"):
#             raise scripting.exceptions.OMCError(__answer)
#         if not __answer or __answer.isspace():
#             return None
#         raise
# 
#     return __solveLinearSystem_output(
#         X=__value[0],
#         info=__value[1],
#     )


# def reopenStandardStream(
#     omc: OMCSessionBase,
#     _stream,
#     filename,
# ):
#     '''
# function reopenStandardStream
#   input StandardStream _stream;
#   input String filename;
#   output Boolean success;
# end reopenStandardStream;
#     '''
#     __kwrds = {}
#     __kwrds["_stream"] = scripting.types.StandardStream(_stream)
#     __kwrds["filename"] = scripting.types.String(filename)
# 
#     __answer = scripting.funcs._ask(omc, "reopenStandardStream", **__kwrds)
#     try:
#         __value = parsers.parseOMCValue(__answer)
#     except parsers.NoMatch:
#         if __answer.lstrip().startswith("Error"):
#             raise scripting.exceptions.OMCError(__answer)
#         if not __answer or __answer.isspace():
#             return None
#         raise
# 
#     return __value


def importFMU(
    omc: OMCSessionBase,
    filename,
    workdir=None,
    loglevel=None,
    fullPath=None,
    debugLogging=None,
    generateInputConnectors=None,
    generateOutputConnectors=None,
):
    '''
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
    '''
    __kwrds = {}
    __kwrds["filename"] = scripting.types.String(filename)
    if workdir is not None:
        __kwrds["workdir"] = scripting.types.String(workdir)
    if loglevel is not None:
        __kwrds["loglevel"] = scripting.types.Integer(loglevel)
    if fullPath is not None:
        __kwrds["fullPath"] = scripting.types.Boolean(fullPath)
    if debugLogging is not None:
        __kwrds["debugLogging"] = scripting.types.Boolean(debugLogging)
    if generateInputConnectors is not None:
        __kwrds["generateInputConnectors"] = scripting.types.Boolean(generateInputConnectors)
    if generateOutputConnectors is not None:
        __kwrds["generateOutputConnectors"] = scripting.types.Boolean(generateOutputConnectors)

    __answer = scripting.funcs._ask(omc, "importFMU", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def importFMUModelDescription(
    omc: OMCSessionBase,
    filename,
    workdir=None,
    loglevel=None,
    fullPath=None,
    debugLogging=None,
    generateInputConnectors=None,
    generateOutputConnectors=None,
):
    '''
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
    '''
    __kwrds = {}
    __kwrds["filename"] = scripting.types.String(filename)
    if workdir is not None:
        __kwrds["workdir"] = scripting.types.String(workdir)
    if loglevel is not None:
        __kwrds["loglevel"] = scripting.types.Integer(loglevel)
    if fullPath is not None:
        __kwrds["fullPath"] = scripting.types.Boolean(fullPath)
    if debugLogging is not None:
        __kwrds["debugLogging"] = scripting.types.Boolean(debugLogging)
    if generateInputConnectors is not None:
        __kwrds["generateInputConnectors"] = scripting.types.Boolean(generateInputConnectors)
    if generateOutputConnectors is not None:
        __kwrds["generateOutputConnectors"] = scripting.types.Boolean(generateOutputConnectors)

    __answer = scripting.funcs._ask(omc, "importFMUModelDescription", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def translateModelFMU(
    omc: OMCSessionBase,
    className,
    version=None,
    fmuType=None,
    fileNamePrefix=None,
    includeResources=None,
):
    '''
function translateModelFMU
  input TypeName className "the class that should translated";
  input String version = "2.0" "FMU version, 1.0 or 2.0.";
  input String fmuType = "me" "FMU type, me (model exchange), cs (co-simulation), me_cs (both model exchange and co-simulation)";
  input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \"className\"";
  input Boolean includeResources = false "include Modelica based resources via loadResource or not";
  output String generatedFileName "Returns the full path of the generated FMU.";
end translateModelFMU;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    if version is not None:
        __kwrds["version"] = scripting.types.String(version)
    if fmuType is not None:
        __kwrds["fmuType"] = scripting.types.String(fmuType)
    if fileNamePrefix is not None:
        __kwrds["fileNamePrefix"] = scripting.types.String(fileNamePrefix)
    if includeResources is not None:
        __kwrds["includeResources"] = scripting.types.Boolean(includeResources)

    __answer = scripting.funcs._ask(omc, "translateModelFMU", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def buildModelFMU(
    omc: OMCSessionBase,
    className,
    version=None,
    fmuType=None,
    fileNamePrefix=None,
    platforms=None,
    includeResources=None,
):
    '''
function buildModelFMU
  input TypeName className "the class that should translated";
  input String version = "2.0" "FMU version, 1.0 or 2.0.";
  input String fmuType = "me" "FMU type, me (model exchange), cs (co-simulation), me_cs (both model exchange and co-simulation)";
  input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \"className\"";
  input String platforms[:] = {"static"} "The list of platforms to generate code for. \"dynamic\"=current platform, dynamically link the runtime. \"static\"=current platform, statically link everything. Else, use a host triple, e.g. \"x86_64-linux-gnu\" or \"x86_64-w64-mingw32\"";
  input Boolean includeResources = false "include Modelica based resources via loadResource or not";
  output String generatedFileName "Returns the full path of the generated FMU.";
end buildModelFMU;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    if version is not None:
        __kwrds["version"] = scripting.types.String(version)
    if fmuType is not None:
        __kwrds["fmuType"] = scripting.types.String(fmuType)
    if fileNamePrefix is not None:
        __kwrds["fileNamePrefix"] = scripting.types.String(fileNamePrefix)
    if platforms is not None:
        __kwrds["platforms"] = scripting.types.String[:](platforms)
    if includeResources is not None:
        __kwrds["includeResources"] = scripting.types.Boolean(includeResources)

    __answer = scripting.funcs._ask(omc, "buildModelFMU", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


__buildEncryptedPackage_output = namedtuple(
    "OMCOutput",
    "success, commandOutput",
)


def buildEncryptedPackage(
    omc: OMCSessionBase,
    className,
):
    '''
function buildEncryptedPackage
  input TypeName className "the class that should encrypted";
  output Boolean success;
  output String commandOutput "Output of the packagetool executable";
end buildEncryptedPackage;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)

    __answer = scripting.funcs._ask(omc, "buildEncryptedPackage", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __buildEncryptedPackage_output(
        success=__value[0],
        commandOutput=__value[1],
    )


# def simulate(
#     omc: OMCSessionBase,
#     className,
#     startTime=None,
#     stopTime=None,
#     numberOfIntervals=None,
#     tolerance=None,
#     method=None,
#     fileNamePrefix=None,
#     options=None,
#     outputFormat=None,
#     variableFilter=None,
#     cflags=None,
#     simflags=None,
# ):
#     '''
# function simulate
#   input TypeName className "the class that should simulated";
#   input Real startTime = "<default>" "the start time of the simulation. <default> = 0.0";
#   input Real stopTime = 1.0 "the stop time of the simulation. <default> = 1.0";
#   input Real numberOfIntervals = 500 "number of intervals in the result file. <default> = 500";
#   input Real tolerance = 1e-6 "tolerance used by the integration method. <default> = 1e-6";
#   input String method = "<default>" "integration method used for simulation. <default> = dassl";
#   input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \"\"";
#   input String options = "<default>" "options. <default> = \"\"";
#   input String outputFormat = "mat" "Format for the result file. <default> = \"mat\"";
#   input String variableFilter = ".*" "Filter for variables that should store in result file. <default> = \".*\"";
#   input String cflags = "<default>" "cflags. <default> = \"\"";
#   input String simflags = "<default>" "simflags. <default> = \"\"";
#   output SimulationResult simulationResults;
# 
#   record SimulationResult
#     String resultFile;
#     String simulationOptions;
#     String messages;
#     Real timeFrontend;
#     Real timeBackend;
#     Real timeSimCode;
#     Real timeTemplates;
#     Real timeCompile;
#     Real timeSimulation;
#     Real timeTotal;
#   end SimulationResult;
# end simulate;
#     '''
#     __kwrds = {}
#     __kwrds["className"] = scripting.types.TypeName(className)
#     if startTime is not None:
#         __kwrds["startTime"] = scripting.types.Real(startTime)
#     if stopTime is not None:
#         __kwrds["stopTime"] = scripting.types.Real(stopTime)
#     if numberOfIntervals is not None:
#         __kwrds["numberOfIntervals"] = scripting.types.Real(numberOfIntervals)
#     if tolerance is not None:
#         __kwrds["tolerance"] = scripting.types.Real(tolerance)
#     if method is not None:
#         __kwrds["method"] = scripting.types.String(method)
#     if fileNamePrefix is not None:
#         __kwrds["fileNamePrefix"] = scripting.types.String(fileNamePrefix)
#     if options is not None:
#         __kwrds["options"] = scripting.types.String(options)
#     if outputFormat is not None:
#         __kwrds["outputFormat"] = scripting.types.String(outputFormat)
#     if variableFilter is not None:
#         __kwrds["variableFilter"] = scripting.types.String(variableFilter)
#     if cflags is not None:
#         __kwrds["cflags"] = scripting.types.String(cflags)
#     if simflags is not None:
#         __kwrds["simflags"] = scripting.types.String(simflags)
# 
#     __answer = scripting.funcs._ask(omc, "simulate", **__kwrds)
#     try:
#         __value = parsers.parseOMCValue(__answer)
#     except parsers.NoMatch:
#         if __answer.lstrip().startswith("Error"):
#             raise scripting.exceptions.OMCError(__answer)
#         if not __answer or __answer.isspace():
#             return None
#         raise
# 
#     return scripting.types.SimulationResult(__value)


def buildModel(
    omc: OMCSessionBase,
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
    '''
function buildModel
  input TypeName className "the class that should be built";
  input Real startTime = "<default>" "the start time of the simulation. <default> = 0.0";
  input Real stopTime = 1.0 "the stop time of the simulation. <default> = 1.0";
  input Real numberOfIntervals = 500 "number of intervals in the result file. <default> = 500";
  input Real tolerance = 1e-6 "tolerance used by the integration method. <default> = 1e-6";
  input String method = "<default>" "integration method used for simulation. <default> = dassl";
  input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \"\"";
  input String options = "<default>" "options. <default> = \"\"";
  input String outputFormat = "mat" "Format for the result file. <default> = \"mat\"";
  input String variableFilter = ".*" "Filter for variables that should store in result file. <default> = \".*\"";
  input String cflags = "<default>" "cflags. <default> = \"\"";
  input String simflags = "<default>" "simflags. <default> = \"\"";
  output String[2] buildModelResults;
end buildModel;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    if startTime is not None:
        __kwrds["startTime"] = scripting.types.Real(startTime)
    if stopTime is not None:
        __kwrds["stopTime"] = scripting.types.Real(stopTime)
    if numberOfIntervals is not None:
        __kwrds["numberOfIntervals"] = scripting.types.Real(numberOfIntervals)
    if tolerance is not None:
        __kwrds["tolerance"] = scripting.types.Real(tolerance)
    if method is not None:
        __kwrds["method"] = scripting.types.String(method)
    if fileNamePrefix is not None:
        __kwrds["fileNamePrefix"] = scripting.types.String(fileNamePrefix)
    if options is not None:
        __kwrds["options"] = scripting.types.String(options)
    if outputFormat is not None:
        __kwrds["outputFormat"] = scripting.types.String(outputFormat)
    if variableFilter is not None:
        __kwrds["variableFilter"] = scripting.types.String(variableFilter)
    if cflags is not None:
        __kwrds["cflags"] = scripting.types.String(cflags)
    if simflags is not None:
        __kwrds["simflags"] = scripting.types.String(simflags)

    __answer = scripting.funcs._ask(omc, "buildModel", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def buildLabel(
    omc: OMCSessionBase,
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
    '''
function buildLabel
  input TypeName className "the class that should be built";
  input Real startTime = 0.0 "the start time of the simulation. <default> = 0.0";
  input Real stopTime = 1.0 "the stop time of the simulation. <default> = 1.0";
  input Integer numberOfIntervals = 500 "number of intervals in the result file. <default> = 500";
  input Real tolerance = 1e-6 "tolerance used by the integration method. <default> = 1e-6";
  input String method = "dassl" "integration method used for simulation. <default> = dassl";
  input String fileNamePrefix = "" "fileNamePrefix. <default> = \"\"";
  input String options = "" "options. <default> = \"\"";
  input String outputFormat = "mat" "Format for the result file. <default> = \"mat\"";
  input String variableFilter = ".*" "Filter for variables that should store in result file. <default> = \".*\"";
  input String cflags = "" "cflags. <default> = \"\"";
  input String simflags = "" "simflags. <default> = \"\"";
  output String[2] buildModelResults;
end buildLabel;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    if startTime is not None:
        __kwrds["startTime"] = scripting.types.Real(startTime)
    if stopTime is not None:
        __kwrds["stopTime"] = scripting.types.Real(stopTime)
    if numberOfIntervals is not None:
        __kwrds["numberOfIntervals"] = scripting.types.Integer(numberOfIntervals)
    if tolerance is not None:
        __kwrds["tolerance"] = scripting.types.Real(tolerance)
    if method is not None:
        __kwrds["method"] = scripting.types.String(method)
    if fileNamePrefix is not None:
        __kwrds["fileNamePrefix"] = scripting.types.String(fileNamePrefix)
    if options is not None:
        __kwrds["options"] = scripting.types.String(options)
    if outputFormat is not None:
        __kwrds["outputFormat"] = scripting.types.String(outputFormat)
    if variableFilter is not None:
        __kwrds["variableFilter"] = scripting.types.String(variableFilter)
    if cflags is not None:
        __kwrds["cflags"] = scripting.types.String(cflags)
    if simflags is not None:
        __kwrds["simflags"] = scripting.types.String(simflags)

    __answer = scripting.funcs._ask(omc, "buildLabel", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def reduceTerms(
    omc: OMCSessionBase,
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
    '''
function reduceTerms
  input TypeName className "the class that should be built";
  input Real startTime = 0.0 "the start time of the simulation. <default> = 0.0";
  input Real stopTime = 1.0 "the stop time of the simulation. <default> = 1.0";
  input Integer numberOfIntervals = 500 "number of intervals in the result file. <default> = 500";
  input Real tolerance = 1e-6 "tolerance used by the integration method. <default> = 1e-6";
  input String method = "dassl" "integration method used for simulation. <default> = dassl";
  input String fileNamePrefix = "" "fileNamePrefix. <default> = \"\"";
  input String options = "" "options. <default> = \"\"";
  input String outputFormat = "mat" "Format for the result file. <default> = \"mat\"";
  input String variableFilter = ".*" "Filter for variables that should store in result file. <default> = \".*\"";
  input String cflags = "" "cflags. <default> = \"\"";
  input String simflags = "" "simflags. <default> = \"\"";
  input String labelstoCancel = "";
  output String[2] buildModelResults;
end reduceTerms;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    if startTime is not None:
        __kwrds["startTime"] = scripting.types.Real(startTime)
    if stopTime is not None:
        __kwrds["stopTime"] = scripting.types.Real(stopTime)
    if numberOfIntervals is not None:
        __kwrds["numberOfIntervals"] = scripting.types.Integer(numberOfIntervals)
    if tolerance is not None:
        __kwrds["tolerance"] = scripting.types.Real(tolerance)
    if method is not None:
        __kwrds["method"] = scripting.types.String(method)
    if fileNamePrefix is not None:
        __kwrds["fileNamePrefix"] = scripting.types.String(fileNamePrefix)
    if options is not None:
        __kwrds["options"] = scripting.types.String(options)
    if outputFormat is not None:
        __kwrds["outputFormat"] = scripting.types.String(outputFormat)
    if variableFilter is not None:
        __kwrds["variableFilter"] = scripting.types.String(variableFilter)
    if cflags is not None:
        __kwrds["cflags"] = scripting.types.String(cflags)
    if simflags is not None:
        __kwrds["simflags"] = scripting.types.String(simflags)
    if labelstoCancel is not None:
        __kwrds["labelstoCancel"] = scripting.types.String(labelstoCancel)

    __answer = scripting.funcs._ask(omc, "reduceTerms", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def moveClass(
    omc: OMCSessionBase,
    className,
    offset,
):
    '''
function moveClass
  input TypeName className "the class that should be moved";
  input Integer offset "Offset in the class list.";
  output Boolean result;
end moveClass;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    __kwrds["offset"] = scripting.types.Integer(offset)

    __answer = scripting.funcs._ask(omc, "moveClass", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def moveClassToTop(
    omc: OMCSessionBase,
    className,
):
    '''
function moveClassToTop
  input TypeName className;
  output Boolean result;
end moveClassToTop;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)

    __answer = scripting.funcs._ask(omc, "moveClassToTop", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def moveClassToBottom(
    omc: OMCSessionBase,
    className,
):
    '''
function moveClassToBottom
  input TypeName className;
  output Boolean result;
end moveClassToBottom;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)

    __answer = scripting.funcs._ask(omc, "moveClassToBottom", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def copyClass(
    omc: OMCSessionBase,
    className,
    newClassName,
    withIn=None,
):
    '''
function copyClass
  input TypeName className "the class that should be copied";
  input String newClassName "the name for new class";
  input TypeName withIn = $Code(TopLevel) "the with in path for new class";
  output Boolean result;
end copyClass;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    __kwrds["newClassName"] = scripting.types.String(newClassName)
    if withIn is not None:
        __kwrds["withIn"] = scripting.types.TypeName(withIn)

    __answer = scripting.funcs._ask(omc, "copyClass", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def linearize(
    omc: OMCSessionBase,
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
    '''
function linearize
  input TypeName className "the class that should simulated";
  input Real startTime = "<default>" "the start time of the simulation. <default> = 0.0";
  input Real stopTime = 1.0 "the stop time of the simulation. <default> = 1.0";
  input Real numberOfIntervals = 500 "number of intervals in the result file. <default> = 500";
  input Real stepSize = 0.002 "step size that is used for the result file. <default> = 0.002";
  input Real tolerance = 1e-6 "tolerance used by the integration method. <default> = 1e-6";
  input String method = "<default>" "integration method used for simulation. <default> = dassl";
  input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \"\"";
  input Boolean storeInTemp = false "storeInTemp. <default> = false";
  input Boolean noClean = false "noClean. <default> = false";
  input String options = "<default>" "options. <default> = \"\"";
  input String outputFormat = "mat" "Format for the result file. <default> = \"mat\"";
  input String variableFilter = ".*" "Filter for variables that should store in result file. <default> = \".*\"";
  input String cflags = "<default>" "cflags. <default> = \"\"";
  input String simflags = "<default>" "simflags. <default> = \"\"";
  output String linearizationResult;
end linearize;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    if startTime is not None:
        __kwrds["startTime"] = scripting.types.Real(startTime)
    if stopTime is not None:
        __kwrds["stopTime"] = scripting.types.Real(stopTime)
    if numberOfIntervals is not None:
        __kwrds["numberOfIntervals"] = scripting.types.Real(numberOfIntervals)
    if stepSize is not None:
        __kwrds["stepSize"] = scripting.types.Real(stepSize)
    if tolerance is not None:
        __kwrds["tolerance"] = scripting.types.Real(tolerance)
    if method is not None:
        __kwrds["method"] = scripting.types.String(method)
    if fileNamePrefix is not None:
        __kwrds["fileNamePrefix"] = scripting.types.String(fileNamePrefix)
    if storeInTemp is not None:
        __kwrds["storeInTemp"] = scripting.types.Boolean(storeInTemp)
    if noClean is not None:
        __kwrds["noClean"] = scripting.types.Boolean(noClean)
    if options is not None:
        __kwrds["options"] = scripting.types.String(options)
    if outputFormat is not None:
        __kwrds["outputFormat"] = scripting.types.String(outputFormat)
    if variableFilter is not None:
        __kwrds["variableFilter"] = scripting.types.String(variableFilter)
    if cflags is not None:
        __kwrds["cflags"] = scripting.types.String(cflags)
    if simflags is not None:
        __kwrds["simflags"] = scripting.types.String(simflags)

    __answer = scripting.funcs._ask(omc, "linearize", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def optimize(
    omc: OMCSessionBase,
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
    '''
function optimize
  input TypeName className "the class that should simulated";
  input Real startTime = "<default>" "the start time of the simulation. <default> = 0.0";
  input Real stopTime = 1.0 "the stop time of the simulation. <default> = 1.0";
  input Real numberOfIntervals = 500 "number of intervals in the result file. <default> = 500";
  input Real stepSize = 0.002 "step size that is used for the result file. <default> = 0.002";
  input Real tolerance = 1e-6 "tolerance used by the integration method. <default> = 1e-6";
  input String method = DAE.SCONST("optimization") "optimize a modelica/optimica model.";
  input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \"\"";
  input Boolean storeInTemp = false "storeInTemp. <default> = false";
  input Boolean noClean = false "noClean. <default> = false";
  input String options = "<default>" "options. <default> = \"\"";
  input String outputFormat = "mat" "Format for the result file. <default> = \"mat\"";
  input String variableFilter = ".*" "Filter for variables that should store in result file. <default> = \".*\"";
  input String cflags = "<default>" "cflags. <default> = \"\"";
  input String simflags = "<default>" "simflags. <default> = \"\"";
  output String optimizationResults;
end optimize;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    if startTime is not None:
        __kwrds["startTime"] = scripting.types.Real(startTime)
    if stopTime is not None:
        __kwrds["stopTime"] = scripting.types.Real(stopTime)
    if numberOfIntervals is not None:
        __kwrds["numberOfIntervals"] = scripting.types.Real(numberOfIntervals)
    if stepSize is not None:
        __kwrds["stepSize"] = scripting.types.Real(stepSize)
    if tolerance is not None:
        __kwrds["tolerance"] = scripting.types.Real(tolerance)
    if method is not None:
        __kwrds["method"] = scripting.types.String(method)
    if fileNamePrefix is not None:
        __kwrds["fileNamePrefix"] = scripting.types.String(fileNamePrefix)
    if storeInTemp is not None:
        __kwrds["storeInTemp"] = scripting.types.Boolean(storeInTemp)
    if noClean is not None:
        __kwrds["noClean"] = scripting.types.Boolean(noClean)
    if options is not None:
        __kwrds["options"] = scripting.types.String(options)
    if outputFormat is not None:
        __kwrds["outputFormat"] = scripting.types.String(outputFormat)
    if variableFilter is not None:
        __kwrds["variableFilter"] = scripting.types.String(variableFilter)
    if cflags is not None:
        __kwrds["cflags"] = scripting.types.String(cflags)
    if simflags is not None:
        __kwrds["simflags"] = scripting.types.String(simflags)

    __answer = scripting.funcs._ask(omc, "optimize", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getSourceFile(
    omc: OMCSessionBase,
    class_,
):
    '''
function getSourceFile
  input TypeName class_;
  output String filename "empty on failure";
end getSourceFile;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)

    __answer = scripting.funcs._ask(omc, "getSourceFile", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setSourceFile(
    omc: OMCSessionBase,
    class_,
    filename,
):
    '''
function setSourceFile
  input TypeName class_;
  input String filename;
  output Boolean success;
end setSourceFile;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["filename"] = scripting.types.String(filename)

    __answer = scripting.funcs._ask(omc, "setSourceFile", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def isShortDefinition(
    omc: OMCSessionBase,
    class_,
):
    '''
function isShortDefinition
  input TypeName class_;
  output Boolean isShortCls;
end isShortDefinition;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)

    __answer = scripting.funcs._ask(omc, "isShortDefinition", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setClassComment(
    omc: OMCSessionBase,
    class_,
    filename,
):
    '''
function setClassComment
  input TypeName class_;
  input String filename;
  output Boolean success;
end setClassComment;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["filename"] = scripting.types.String(filename)

    __answer = scripting.funcs._ask(omc, "setClassComment", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getClassNames(
    omc: OMCSessionBase,
    class_=None,
    recursive=None,
    qualified=None,
    sort=None,
    builtin=None,
    showProtected=None,
    includeConstants=None,
):
    '''
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
    '''
    __kwrds = {}
    if class_ is not None:
        __kwrds["class_"] = scripting.types.TypeName(class_)
    if recursive is not None:
        __kwrds["recursive"] = scripting.types.Boolean(recursive)
    if qualified is not None:
        __kwrds["qualified"] = scripting.types.Boolean(qualified)
    if sort is not None:
        __kwrds["sort"] = scripting.types.Boolean(sort)
    if builtin is not None:
        __kwrds["builtin"] = scripting.types.Boolean(builtin)
    if showProtected is not None:
        __kwrds["showProtected"] = scripting.types.Boolean(showProtected)
    if includeConstants is not None:
        __kwrds["includeConstants"] = scripting.types.Boolean(includeConstants)

    __answer = scripting.funcs._ask(omc, "getClassNames", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return scripting.types.TypeName[:](__value)


def getUsedClassNames(
    omc: OMCSessionBase,
    className,
):
    '''
function getUsedClassNames
  input TypeName className;
  output TypeName classNames[:];
end getUsedClassNames;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)

    __answer = scripting.funcs._ask(omc, "getUsedClassNames", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return scripting.types.TypeName[:](__value)


def getPackages(
    omc: OMCSessionBase,
    class_=None,
):
    '''
function getPackages
  input TypeName class_ = $Code(AllLoadedClasses);
  output TypeName classNames[:];
end getPackages;
    '''
    __kwrds = {}
    if class_ is not None:
        __kwrds["class_"] = scripting.types.TypeName(class_)

    __answer = scripting.funcs._ask(omc, "getPackages", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return scripting.types.TypeName[:](__value)


def basePlotFunction(
    omc: OMCSessionBase,
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
    '''
partial function basePlotFunction
  input String fileName = "<default>" "The filename containing the variables. <default> will read the last simulation result";
  input String interpolation = "linear" "
      Determines if the simulation data should be interpolated to allow drawing of continuous lines in the diagram.
      \"linear\" results in linear interpolation between data points, \"constant\" keeps the value of the last known
      data point until a new one is found and \"none\" results in a diagram where only known data points are plotted.";
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
    '''
    __kwrds = {}
    if fileName is not None:
        __kwrds["fileName"] = scripting.types.String(fileName)
    if interpolation is not None:
        __kwrds["interpolation"] = scripting.types.String(interpolation)
    if title is not None:
        __kwrds["title"] = scripting.types.String(title)
    if legend is not None:
        __kwrds["legend"] = scripting.types.Boolean(legend)
    if grid is not None:
        __kwrds["grid"] = scripting.types.Boolean(grid)
    if logX is not None:
        __kwrds["logX"] = scripting.types.Boolean(logX)
    if logY is not None:
        __kwrds["logY"] = scripting.types.Boolean(logY)
    if xLabel is not None:
        __kwrds["xLabel"] = scripting.types.String(xLabel)
    if yLabel is not None:
        __kwrds["yLabel"] = scripting.types.String(yLabel)
    if points is not None:
        __kwrds["points"] = scripting.types.Boolean(points)
    if xRange is not None:
        __kwrds["xRange"] = scripting.types.Real[2](xRange)
    if yRange is not None:
        __kwrds["yRange"] = scripting.types.Real[2](yRange)

    __answer = scripting.funcs._ask(omc, "basePlotFunction", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def plot(
    omc: OMCSessionBase,
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
    '''
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
    '''
    __kwrds = {}
    __kwrds["vars"] = scripting.types.VariableNames(vars)
    if externalWindow is not None:
        __kwrds["externalWindow"] = scripting.types.Boolean(externalWindow)
    if fileName is not None:
        __kwrds["fileName"] = scripting.types.String(fileName)
    if title is not None:
        __kwrds["title"] = scripting.types.String(title)
    if grid is not None:
        __kwrds["grid"] = scripting.types.String(grid)
    if logX is not None:
        __kwrds["logX"] = scripting.types.Boolean(logX)
    if logY is not None:
        __kwrds["logY"] = scripting.types.Boolean(logY)
    if xLabel is not None:
        __kwrds["xLabel"] = scripting.types.String(xLabel)
    if yLabel is not None:
        __kwrds["yLabel"] = scripting.types.String(yLabel)
    if xRange is not None:
        __kwrds["xRange"] = scripting.types.Real[2](xRange)
    if yRange is not None:
        __kwrds["yRange"] = scripting.types.Real[2](yRange)
    if curveWidth is not None:
        __kwrds["curveWidth"] = scripting.types.Real(curveWidth)
    if curveStyle is not None:
        __kwrds["curveStyle"] = scripting.types.Integer(curveStyle)
    if legendPosition is not None:
        __kwrds["legendPosition"] = scripting.types.String(legendPosition)
    if footer is not None:
        __kwrds["footer"] = scripting.types.String(footer)
    if autoScale is not None:
        __kwrds["autoScale"] = scripting.types.Boolean(autoScale)
    if forceOMPlot is not None:
        __kwrds["forceOMPlot"] = scripting.types.Boolean(forceOMPlot)

    __answer = scripting.funcs._ask(omc, "plot", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def plotAll(
    omc: OMCSessionBase,
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
    '''
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
    '''
    __kwrds = {}
    if externalWindow is not None:
        __kwrds["externalWindow"] = scripting.types.Boolean(externalWindow)
    if fileName is not None:
        __kwrds["fileName"] = scripting.types.String(fileName)
    if title is not None:
        __kwrds["title"] = scripting.types.String(title)
    if grid is not None:
        __kwrds["grid"] = scripting.types.String(grid)
    if logX is not None:
        __kwrds["logX"] = scripting.types.Boolean(logX)
    if logY is not None:
        __kwrds["logY"] = scripting.types.Boolean(logY)
    if xLabel is not None:
        __kwrds["xLabel"] = scripting.types.String(xLabel)
    if yLabel is not None:
        __kwrds["yLabel"] = scripting.types.String(yLabel)
    if xRange is not None:
        __kwrds["xRange"] = scripting.types.Real[2](xRange)
    if yRange is not None:
        __kwrds["yRange"] = scripting.types.Real[2](yRange)
    if curveWidth is not None:
        __kwrds["curveWidth"] = scripting.types.Real(curveWidth)
    if curveStyle is not None:
        __kwrds["curveStyle"] = scripting.types.Integer(curveStyle)
    if legendPosition is not None:
        __kwrds["legendPosition"] = scripting.types.String(legendPosition)
    if footer is not None:
        __kwrds["footer"] = scripting.types.String(footer)
    if autoScale is not None:
        __kwrds["autoScale"] = scripting.types.Boolean(autoScale)
    if forceOMPlot is not None:
        __kwrds["forceOMPlot"] = scripting.types.Boolean(forceOMPlot)

    __answer = scripting.funcs._ask(omc, "plotAll", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def plotParametric(
    omc: OMCSessionBase,
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
    '''
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
    '''
    __kwrds = {}
    __kwrds["xVariable"] = scripting.types.VariableName(xVariable)
    __kwrds["yVariable"] = scripting.types.VariableName(yVariable)
    if externalWindow is not None:
        __kwrds["externalWindow"] = scripting.types.Boolean(externalWindow)
    if fileName is not None:
        __kwrds["fileName"] = scripting.types.String(fileName)
    if title is not None:
        __kwrds["title"] = scripting.types.String(title)
    if grid is not None:
        __kwrds["grid"] = scripting.types.String(grid)
    if logX is not None:
        __kwrds["logX"] = scripting.types.Boolean(logX)
    if logY is not None:
        __kwrds["logY"] = scripting.types.Boolean(logY)
    if xLabel is not None:
        __kwrds["xLabel"] = scripting.types.String(xLabel)
    if yLabel is not None:
        __kwrds["yLabel"] = scripting.types.String(yLabel)
    if xRange is not None:
        __kwrds["xRange"] = scripting.types.Real[2](xRange)
    if yRange is not None:
        __kwrds["yRange"] = scripting.types.Real[2](yRange)
    if curveWidth is not None:
        __kwrds["curveWidth"] = scripting.types.Real(curveWidth)
    if curveStyle is not None:
        __kwrds["curveStyle"] = scripting.types.Integer(curveStyle)
    if legendPosition is not None:
        __kwrds["legendPosition"] = scripting.types.String(legendPosition)
    if footer is not None:
        __kwrds["footer"] = scripting.types.String(footer)
    if autoScale is not None:
        __kwrds["autoScale"] = scripting.types.Boolean(autoScale)
    if forceOMPlot is not None:
        __kwrds["forceOMPlot"] = scripting.types.Boolean(forceOMPlot)

    __answer = scripting.funcs._ask(omc, "plotParametric", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def readSimulationResult(
    omc: OMCSessionBase,
    filename,
    variables,
    size=None,
):
    '''
function readSimulationResult
  input String filename;
  input VariableNames variables;
  input Integer size = 0 "0=read any size... If the size is not the same as the result-file, this function fails";
  output Real result[:, :];
end readSimulationResult;
    '''
    __kwrds = {}
    __kwrds["filename"] = scripting.types.String(filename)
    __kwrds["variables"] = scripting.types.VariableNames(variables)
    if size is not None:
        __kwrds["size"] = scripting.types.Integer(size)

    __answer = scripting.funcs._ask(omc, "readSimulationResult", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def readSimulationResultSize(
    omc: OMCSessionBase,
    fileName,
):
    '''
function readSimulationResultSize
  input String fileName;
  output Integer sz;
end readSimulationResultSize;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)

    __answer = scripting.funcs._ask(omc, "readSimulationResultSize", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def readSimulationResultVars(
    omc: OMCSessionBase,
    fileName,
    readParameters=None,
    openmodelicaStyle=None,
):
    '''
function readSimulationResultVars
  input String fileName;
  input Boolean readParameters = true;
  input Boolean openmodelicaStyle = false;
  output String[:] vars;
end readSimulationResultVars;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)
    if readParameters is not None:
        __kwrds["readParameters"] = scripting.types.Boolean(readParameters)
    if openmodelicaStyle is not None:
        __kwrds["openmodelicaStyle"] = scripting.types.Boolean(openmodelicaStyle)

    __answer = scripting.funcs._ask(omc, "readSimulationResultVars", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def filterSimulationResults(
    omc: OMCSessionBase,
    inFile,
    outFile,
    vars,
    numberOfIntervals=None,
    removeDescription=None,
):
    '''
function filterSimulationResults
  input String inFile;
  input String outFile;
  input String[:] vars;
  input Integer numberOfIntervals = 0 "0=Do not resample";
  input Boolean removeDescription = false;
  output Boolean success;
end filterSimulationResults;
    '''
    __kwrds = {}
    __kwrds["inFile"] = scripting.types.String(inFile)
    __kwrds["outFile"] = scripting.types.String(outFile)
    __kwrds["vars"] = scripting.types.String[:](vars)
    if numberOfIntervals is not None:
        __kwrds["numberOfIntervals"] = scripting.types.Integer(numberOfIntervals)
    if removeDescription is not None:
        __kwrds["removeDescription"] = scripting.types.Boolean(removeDescription)

    __answer = scripting.funcs._ask(omc, "filterSimulationResults", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def compareSimulationResults(
    omc: OMCSessionBase,
    filename,
    reffilename,
    logfilename,
    relTol=None,
    absTol=None,
    vars=None,
):
    '''
function compareSimulationResults
  input String filename;
  input String reffilename;
  input String logfilename;
  input Real relTol = 0.01;
  input Real absTol = 0.0001;
  input String[:] vars = fill("", 0);
  output String[:] result;
end compareSimulationResults;
    '''
    __kwrds = {}
    __kwrds["filename"] = scripting.types.String(filename)
    __kwrds["reffilename"] = scripting.types.String(reffilename)
    __kwrds["logfilename"] = scripting.types.String(logfilename)
    if relTol is not None:
        __kwrds["relTol"] = scripting.types.Real(relTol)
    if absTol is not None:
        __kwrds["absTol"] = scripting.types.Real(absTol)
    if vars is not None:
        __kwrds["vars"] = scripting.types.String[:](vars)

    __answer = scripting.funcs._ask(omc, "compareSimulationResults", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def deltaSimulationResults(
    omc: OMCSessionBase,
    filename,
    reffilename,
    method,
    vars=None,
):
    '''
function deltaSimulationResults
  input String filename;
  input String reffilename;
  input String method "method to compute then error. choose 1norm, 2norm, maxerr";
  input String[:] vars = fill("", 0);
  output Real result;
end deltaSimulationResults;
    '''
    __kwrds = {}
    __kwrds["filename"] = scripting.types.String(filename)
    __kwrds["reffilename"] = scripting.types.String(reffilename)
    __kwrds["method"] = scripting.types.String(method)
    if vars is not None:
        __kwrds["vars"] = scripting.types.String[:](vars)

    __answer = scripting.funcs._ask(omc, "deltaSimulationResults", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


__diffSimulationResults_output = namedtuple(
    "OMCOutput",
    "success, failVars",
)


def diffSimulationResults(
    omc: OMCSessionBase,
    actualFile,
    expectedFile,
    diffPrefix,
    relTol=None,
    relTolDiffMinMax=None,
    rangeDelta=None,
    vars=None,
    keepEqualResults=None,
):
    '''
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
    '''
    __kwrds = {}
    __kwrds["actualFile"] = scripting.types.String(actualFile)
    __kwrds["expectedFile"] = scripting.types.String(expectedFile)
    __kwrds["diffPrefix"] = scripting.types.String(diffPrefix)
    if relTol is not None:
        __kwrds["relTol"] = scripting.types.Real(relTol)
    if relTolDiffMinMax is not None:
        __kwrds["relTolDiffMinMax"] = scripting.types.Real(relTolDiffMinMax)
    if rangeDelta is not None:
        __kwrds["rangeDelta"] = scripting.types.Real(rangeDelta)
    if vars is not None:
        __kwrds["vars"] = scripting.types.String[:](vars)
    if keepEqualResults is not None:
        __kwrds["keepEqualResults"] = scripting.types.Boolean(keepEqualResults)

    __answer = scripting.funcs._ask(omc, "diffSimulationResults", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __diffSimulationResults_output(
        success=__value[0],
        failVars=__value[1],
    )


def diffSimulationResultsHtml(
    omc: OMCSessionBase,
    var,
    actualFile,
    expectedFile,
    relTol=None,
    relTolDiffMinMax=None,
    rangeDelta=None,
):
    '''
function diffSimulationResultsHtml
  input String var;
  input String actualFile;
  input String expectedFile;
  input Real relTol = 1e-3 "y tolerance";
  input Real relTolDiffMinMax = 1e-4 "y tolerance based on the difference between the maximum and minimum of the signal";
  input Real rangeDelta = 0.002 "x tolerance";
  output String html;
end diffSimulationResultsHtml;
    '''
    __kwrds = {}
    __kwrds["var"] = scripting.types.String(var)
    __kwrds["actualFile"] = scripting.types.String(actualFile)
    __kwrds["expectedFile"] = scripting.types.String(expectedFile)
    if relTol is not None:
        __kwrds["relTol"] = scripting.types.Real(relTol)
    if relTolDiffMinMax is not None:
        __kwrds["relTolDiffMinMax"] = scripting.types.Real(relTolDiffMinMax)
    if rangeDelta is not None:
        __kwrds["rangeDelta"] = scripting.types.Real(rangeDelta)

    __answer = scripting.funcs._ask(omc, "diffSimulationResultsHtml", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def checkTaskGraph(
    omc: OMCSessionBase,
    filename,
    reffilename,
):
    '''
function checkTaskGraph
  input String filename;
  input String reffilename;
  output String[:] result;
end checkTaskGraph;
    '''
    __kwrds = {}
    __kwrds["filename"] = scripting.types.String(filename)
    __kwrds["reffilename"] = scripting.types.String(reffilename)

    __answer = scripting.funcs._ask(omc, "checkTaskGraph", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def checkCodeGraph(
    omc: OMCSessionBase,
    graphfile,
    codefile,
):
    '''
function checkCodeGraph
  input String graphfile;
  input String codefile;
  output String[:] result;
end checkCodeGraph;
    '''
    __kwrds = {}
    __kwrds["graphfile"] = scripting.types.String(graphfile)
    __kwrds["codefile"] = scripting.types.String(codefile)

    __answer = scripting.funcs._ask(omc, "checkCodeGraph", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def val(
    omc: OMCSessionBase,
    var,
    timePoint=None,
    fileName=None,
):
    '''
function val
  input VariableName var;
  input Real timePoint = 0.0;
  input String fileName = "<default>" "The contents of the currentSimulationResult variable";
  output Real valAtTime;
end val;
    '''
    __kwrds = {}
    __kwrds["var"] = scripting.types.VariableName(var)
    if timePoint is not None:
        __kwrds["timePoint"] = scripting.types.Real(timePoint)
    if fileName is not None:
        __kwrds["fileName"] = scripting.types.String(fileName)

    __answer = scripting.funcs._ask(omc, "val", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def closeSimulationResultFile(
    omc: OMCSessionBase,
):
    '''
function closeSimulationResultFile
  output Boolean success;
end closeSimulationResultFile;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "closeSimulationResultFile", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


# def addClassAnnotation(
#     omc: OMCSessionBase,
#     class_,
#     annotate,
# ):
#     '''
# function addClassAnnotation
#   input TypeName class_;
#   input ExpressionOrModification annotate;
#   output Boolean bool;
# end addClassAnnotation;
#     '''
#     __kwrds = {}
#     __kwrds["class_"] = scripting.types.TypeName(class_)
#     __kwrds["annotate"] = scripting.types.ExpressionOrModification(annotate)
# 
#     __answer = scripting.funcs._ask(omc, "addClassAnnotation", **__kwrds)
#     try:
#         __value = parsers.parseOMCValue(__answer)
#     except parsers.NoMatch:
#         if __answer.lstrip().startswith("Error"):
#             raise scripting.exceptions.OMCError(__answer)
#         if not __answer or __answer.isspace():
#             return None
#         raise
# 
#     return __value


def getParameterNames(
    omc: OMCSessionBase,
    class_,
):
    '''
function getParameterNames
  input TypeName class_;
  output String[:] parameters;
end getParameterNames;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)

    __answer = scripting.funcs._ask(omc, "getParameterNames", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getParameterValue(
    omc: OMCSessionBase,
    class_,
    parameterName,
):
    '''
function getParameterValue
  input TypeName class_;
  input String parameterName;
  output String parameterValue;
end getParameterValue;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["parameterName"] = scripting.types.String(parameterName)

    __answer = scripting.funcs._ask(omc, "getParameterValue", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getComponentModifierNames(
    omc: OMCSessionBase,
    class_,
    componentName,
):
    '''
function getComponentModifierNames
  input TypeName class_;
  input String componentName;
  output String[:] modifiers;
end getComponentModifierNames;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["componentName"] = scripting.types.String(componentName)

    __answer = scripting.funcs._ask(omc, "getComponentModifierNames", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getComponentModifierValue(
    omc: OMCSessionBase,
    class_,
    modifier,
):
    '''
function getComponentModifierValue
  input TypeName class_;
  input TypeName modifier;
  output String value;
end getComponentModifierValue;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["modifier"] = scripting.types.TypeName(modifier)

    __answer = scripting.funcs._ask(omc, "getComponentModifierValue", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getComponentModifierValues(
    omc: OMCSessionBase,
    class_,
    modifier,
):
    '''
function getComponentModifierValues
  input TypeName class_;
  input TypeName modifier;
  output String value;
end getComponentModifierValues;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["modifier"] = scripting.types.TypeName(modifier)

    __answer = scripting.funcs._ask(omc, "getComponentModifierValues", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getInstantiatedParametersAndValues(
    omc: OMCSessionBase,
    cls,
):
    '''
function getInstantiatedParametersAndValues
  input TypeName cls;
  output String[:] values;
end getInstantiatedParametersAndValues;
    '''
    __kwrds = {}
    __kwrds["cls"] = scripting.types.TypeName(cls)

    __answer = scripting.funcs._ask(omc, "getInstantiatedParametersAndValues", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def removeComponentModifiers(
    omc: OMCSessionBase,
    class_,
    componentName,
    keepRedeclares=None,
):
    '''
function removeComponentModifiers
  input TypeName class_;
  input String componentName;
  input Boolean keepRedeclares = false;
  output Boolean success;
end removeComponentModifiers;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["componentName"] = scripting.types.String(componentName)
    if keepRedeclares is not None:
        __kwrds["keepRedeclares"] = scripting.types.Boolean(keepRedeclares)

    __answer = scripting.funcs._ask(omc, "removeComponentModifiers", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def removeExtendsModifiers(
    omc: OMCSessionBase,
    className,
    baseClassName,
    keepRedeclares=None,
):
    '''
function removeExtendsModifiers
  input TypeName className;
  input TypeName baseClassName;
  input Boolean keepRedeclares = false;
  output Boolean success;
end removeExtendsModifiers;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    __kwrds["baseClassName"] = scripting.types.TypeName(baseClassName)
    if keepRedeclares is not None:
        __kwrds["keepRedeclares"] = scripting.types.Boolean(keepRedeclares)

    __answer = scripting.funcs._ask(omc, "removeExtendsModifiers", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getConnectionCount(
    omc: OMCSessionBase,
    className,
):
    '''
function getConnectionCount
  input TypeName className;
  output Integer count;
end getConnectionCount;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)

    __answer = scripting.funcs._ask(omc, "getConnectionCount", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getNthConnection(
    omc: OMCSessionBase,
    className,
    index,
):
    '''
function getNthConnection
  input TypeName className;
  input Integer index;
  output String[:] result;
end getNthConnection;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    __kwrds["index"] = scripting.types.Integer(index)

    __answer = scripting.funcs._ask(omc, "getNthConnection", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getAlgorithmCount(
    omc: OMCSessionBase,
    class_,
):
    '''
function getAlgorithmCount
  input TypeName class_;
  output Integer count;
end getAlgorithmCount;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)

    __answer = scripting.funcs._ask(omc, "getAlgorithmCount", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getNthAlgorithm(
    omc: OMCSessionBase,
    class_,
    index,
):
    '''
function getNthAlgorithm
  input TypeName class_;
  input Integer index;
  output String result;
end getNthAlgorithm;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["index"] = scripting.types.Integer(index)

    __answer = scripting.funcs._ask(omc, "getNthAlgorithm", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getInitialAlgorithmCount(
    omc: OMCSessionBase,
    class_,
):
    '''
function getInitialAlgorithmCount
  input TypeName class_;
  output Integer count;
end getInitialAlgorithmCount;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)

    __answer = scripting.funcs._ask(omc, "getInitialAlgorithmCount", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getNthInitialAlgorithm(
    omc: OMCSessionBase,
    class_,
    index,
):
    '''
function getNthInitialAlgorithm
  input TypeName class_;
  input Integer index;
  output String result;
end getNthInitialAlgorithm;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["index"] = scripting.types.Integer(index)

    __answer = scripting.funcs._ask(omc, "getNthInitialAlgorithm", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getAlgorithmItemsCount(
    omc: OMCSessionBase,
    class_,
):
    '''
function getAlgorithmItemsCount
  input TypeName class_;
  output Integer count;
end getAlgorithmItemsCount;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)

    __answer = scripting.funcs._ask(omc, "getAlgorithmItemsCount", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getNthAlgorithmItem(
    omc: OMCSessionBase,
    class_,
    index,
):
    '''
function getNthAlgorithmItem
  input TypeName class_;
  input Integer index;
  output String result;
end getNthAlgorithmItem;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["index"] = scripting.types.Integer(index)

    __answer = scripting.funcs._ask(omc, "getNthAlgorithmItem", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getInitialAlgorithmItemsCount(
    omc: OMCSessionBase,
    class_,
):
    '''
function getInitialAlgorithmItemsCount
  input TypeName class_;
  output Integer count;
end getInitialAlgorithmItemsCount;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)

    __answer = scripting.funcs._ask(omc, "getInitialAlgorithmItemsCount", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getNthInitialAlgorithmItem(
    omc: OMCSessionBase,
    class_,
    index,
):
    '''
function getNthInitialAlgorithmItem
  input TypeName class_;
  input Integer index;
  output String result;
end getNthInitialAlgorithmItem;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["index"] = scripting.types.Integer(index)

    __answer = scripting.funcs._ask(omc, "getNthInitialAlgorithmItem", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getEquationCount(
    omc: OMCSessionBase,
    class_,
):
    '''
function getEquationCount
  input TypeName class_;
  output Integer count;
end getEquationCount;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)

    __answer = scripting.funcs._ask(omc, "getEquationCount", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getNthEquation(
    omc: OMCSessionBase,
    class_,
    index,
):
    '''
function getNthEquation
  input TypeName class_;
  input Integer index;
  output String result;
end getNthEquation;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["index"] = scripting.types.Integer(index)

    __answer = scripting.funcs._ask(omc, "getNthEquation", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getInitialEquationCount(
    omc: OMCSessionBase,
    class_,
):
    '''
function getInitialEquationCount
  input TypeName class_;
  output Integer count;
end getInitialEquationCount;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)

    __answer = scripting.funcs._ask(omc, "getInitialEquationCount", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getNthInitialEquation(
    omc: OMCSessionBase,
    class_,
    index,
):
    '''
function getNthInitialEquation
  input TypeName class_;
  input Integer index;
  output String result;
end getNthInitialEquation;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["index"] = scripting.types.Integer(index)

    __answer = scripting.funcs._ask(omc, "getNthInitialEquation", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getEquationItemsCount(
    omc: OMCSessionBase,
    class_,
):
    '''
function getEquationItemsCount
  input TypeName class_;
  output Integer count;
end getEquationItemsCount;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)

    __answer = scripting.funcs._ask(omc, "getEquationItemsCount", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getNthEquationItem(
    omc: OMCSessionBase,
    class_,
    index,
):
    '''
function getNthEquationItem
  input TypeName class_;
  input Integer index;
  output String result;
end getNthEquationItem;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["index"] = scripting.types.Integer(index)

    __answer = scripting.funcs._ask(omc, "getNthEquationItem", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getInitialEquationItemsCount(
    omc: OMCSessionBase,
    class_,
):
    '''
function getInitialEquationItemsCount
  input TypeName class_;
  output Integer count;
end getInitialEquationItemsCount;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)

    __answer = scripting.funcs._ask(omc, "getInitialEquationItemsCount", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getNthInitialEquationItem(
    omc: OMCSessionBase,
    class_,
    index,
):
    '''
function getNthInitialEquationItem
  input TypeName class_;
  input Integer index;
  output String result;
end getNthInitialEquationItem;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["index"] = scripting.types.Integer(index)

    __answer = scripting.funcs._ask(omc, "getNthInitialEquationItem", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getAnnotationCount(
    omc: OMCSessionBase,
    class_,
):
    '''
function getAnnotationCount
  input TypeName class_;
  output Integer count;
end getAnnotationCount;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)

    __answer = scripting.funcs._ask(omc, "getAnnotationCount", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getNthAnnotationString(
    omc: OMCSessionBase,
    class_,
    index,
):
    '''
function getNthAnnotationString
  input TypeName class_;
  input Integer index;
  output String result;
end getNthAnnotationString;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["index"] = scripting.types.Integer(index)

    __answer = scripting.funcs._ask(omc, "getNthAnnotationString", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getImportCount(
    omc: OMCSessionBase,
    class_,
):
    '''
function getImportCount
  input TypeName class_;
  output Integer count;
end getImportCount;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)

    __answer = scripting.funcs._ask(omc, "getImportCount", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getNthImport(
    omc: OMCSessionBase,
    class_,
    index,
):
    '''
function getNthImport
  input TypeName class_;
  input Integer index;
  output String out[3] "{\"Path\",\"Id\",\"Kind\"}";
end getNthImport;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    __kwrds["index"] = scripting.types.Integer(index)

    __answer = scripting.funcs._ask(omc, "getNthImport", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def iconv(
    omc: OMCSessionBase,
    string,
    from_,
    to=None,
):
    '''
function iconv
  input String string;
  input String from;
  input String to = "UTF-8";
  output String result;
end iconv;
    '''
    __kwrds = {}
    __kwrds["string"] = scripting.types.String(string)
    __kwrds["from"] = scripting.types.String(from_)
    if to is not None:
        __kwrds["to"] = scripting.types.String(to)

    __answer = scripting.funcs._ask(omc, "iconv", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getDocumentationAnnotation(
    omc: OMCSessionBase,
    cl,
):
    '''
function getDocumentationAnnotation
  input TypeName cl;
  output String out[3] "{info,revision,infoHeader} TODO: Should be changed to have 2 outputs instead of an array of 2 Strings...";
end getDocumentationAnnotation;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "getDocumentationAnnotation", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setDocumentationAnnotation(
    omc: OMCSessionBase,
    class_,
    info=None,
    revisions=None,
):
    '''
function setDocumentationAnnotation
  input TypeName class_;
  input String info = "";
  input String revisions = "";
  output Boolean bool;
end setDocumentationAnnotation;
    '''
    __kwrds = {}
    __kwrds["class_"] = scripting.types.TypeName(class_)
    if info is not None:
        __kwrds["info"] = scripting.types.String(info)
    if revisions is not None:
        __kwrds["revisions"] = scripting.types.String(revisions)

    __answer = scripting.funcs._ask(omc, "setDocumentationAnnotation", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


__getTimeStamp_output = namedtuple(
    "OMCOutput",
    "timeStamp, timeStampAsString",
)


def getTimeStamp(
    omc: OMCSessionBase,
    cl,
):
    '''
function getTimeStamp
  input TypeName cl;
  output Real timeStamp;
  output String timeStampAsString;
end getTimeStamp;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "getTimeStamp", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __getTimeStamp_output(
        timeStamp=__value[0],
        timeStampAsString=__value[1],
    )


def stringTypeName(
    omc: OMCSessionBase,
    str,
):
    '''
function stringTypeName
  input String str;
  output TypeName cl;
end stringTypeName;
    '''
    __kwrds = {}
    __kwrds["str"] = scripting.types.String(str)

    __answer = scripting.funcs._ask(omc, "stringTypeName", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return scripting.types.TypeName(__value)


def stringVariableName(
    omc: OMCSessionBase,
    str,
):
    '''
function stringVariableName
  input String str;
  output VariableName cl;
end stringVariableName;
    '''
    __kwrds = {}
    __kwrds["str"] = scripting.types.String(str)

    __answer = scripting.funcs._ask(omc, "stringVariableName", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def typeNameString(
    omc: OMCSessionBase,
    cl,
):
    '''
function typeNameString
  input TypeName cl;
  output String out;
end typeNameString;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "typeNameString", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def typeNameStrings(
    omc: OMCSessionBase,
    cl,
):
    '''
function typeNameStrings
  input TypeName cl;
  output String out[:];
end typeNameStrings;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "typeNameStrings", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getClassComment(
    omc: OMCSessionBase,
    cl,
):
    '''
function getClassComment
  input TypeName cl;
  output String comment;
end getClassComment;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "getClassComment", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def dirname(
    omc: OMCSessionBase,
    path,
):
    '''
function dirname
  input String path;
  output String dirname;
end dirname;
    '''
    __kwrds = {}
    __kwrds["path"] = scripting.types.String(path)

    __answer = scripting.funcs._ask(omc, "dirname", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def basename(
    omc: OMCSessionBase,
    path,
):
    '''
function basename
  input String path;
  output String basename;
end basename;
    '''
    __kwrds = {}
    __kwrds["path"] = scripting.types.String(path)

    __answer = scripting.funcs._ask(omc, "basename", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getClassRestriction(
    omc: OMCSessionBase,
    cl,
):
    '''
function getClassRestriction
  input TypeName cl;
  output String restriction;
end getClassRestriction;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "getClassRestriction", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def isType(
    omc: OMCSessionBase,
    cl,
):
    '''
function isType
  input TypeName cl;
  output Boolean b;
end isType;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "isType", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def isPackage(
    omc: OMCSessionBase,
    cl,
):
    '''
function isPackage
  input TypeName cl;
  output Boolean b;
end isPackage;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "isPackage", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def isClass(
    omc: OMCSessionBase,
    cl,
):
    '''
function isClass
  input TypeName cl;
  output Boolean b;
end isClass;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "isClass", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def isRecord(
    omc: OMCSessionBase,
    cl,
):
    '''
function isRecord
  input TypeName cl;
  output Boolean b;
end isRecord;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "isRecord", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def isBlock(
    omc: OMCSessionBase,
    cl,
):
    '''
function isBlock
  input TypeName cl;
  output Boolean b;
end isBlock;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "isBlock", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def isFunction(
    omc: OMCSessionBase,
    cl,
):
    '''
function isFunction
  input TypeName cl;
  output Boolean b;
end isFunction;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "isFunction", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def isPartial(
    omc: OMCSessionBase,
    cl,
):
    '''
function isPartial
  input TypeName cl;
  output Boolean b;
end isPartial;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "isPartial", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def isModel(
    omc: OMCSessionBase,
    cl,
):
    '''
function isModel
  input TypeName cl;
  output Boolean b;
end isModel;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "isModel", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def isConnector(
    omc: OMCSessionBase,
    cl,
):
    '''
function isConnector
  input TypeName cl;
  output Boolean b;
end isConnector;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "isConnector", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def isOptimization(
    omc: OMCSessionBase,
    cl,
):
    '''
function isOptimization
  input TypeName cl;
  output Boolean b;
end isOptimization;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "isOptimization", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def isEnumeration(
    omc: OMCSessionBase,
    cl,
):
    '''
function isEnumeration
  input TypeName cl;
  output Boolean b;
end isEnumeration;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "isEnumeration", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def isOperator(
    omc: OMCSessionBase,
    cl,
):
    '''
function isOperator
  input TypeName cl;
  output Boolean b;
end isOperator;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "isOperator", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def isOperatorRecord(
    omc: OMCSessionBase,
    cl,
):
    '''
function isOperatorRecord
  input TypeName cl;
  output Boolean b;
end isOperatorRecord;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "isOperatorRecord", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def isOperatorFunction(
    omc: OMCSessionBase,
    cl,
):
    '''
function isOperatorFunction
  input TypeName cl;
  output Boolean b;
end isOperatorFunction;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "isOperatorFunction", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def isProtectedClass(
    omc: OMCSessionBase,
    cl,
    c2,
):
    '''
function isProtectedClass
  input TypeName cl;
  input String c2;
  output Boolean b;
end isProtectedClass;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)
    __kwrds["c2"] = scripting.types.String(c2)

    __answer = scripting.funcs._ask(omc, "isProtectedClass", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getBuiltinType(
    omc: OMCSessionBase,
    cl,
):
    '''
function getBuiltinType
  input TypeName cl;
  output String name;
end getBuiltinType;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "getBuiltinType", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def setInitXmlStartValue(
    omc: OMCSessionBase,
    fileName,
    variableName,
    startValue,
    outputFile,
):
    '''
function setInitXmlStartValue
  input String fileName;
  input String variableName;
  input String startValue;
  input String outputFile;
  output Boolean success = false;
end setInitXmlStartValue;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)
    __kwrds["variableName"] = scripting.types.String(variableName)
    __kwrds["startValue"] = scripting.types.String(startValue)
    __kwrds["outputFile"] = scripting.types.String(outputFile)

    __answer = scripting.funcs._ask(omc, "setInitXmlStartValue", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def ngspicetoModelica(
    omc: OMCSessionBase,
    netlistfileName,
):
    '''
function ngspicetoModelica
  input String netlistfileName;
  output Boolean success = false;
end ngspicetoModelica;
    '''
    __kwrds = {}
    __kwrds["netlistfileName"] = scripting.types.String(netlistfileName)

    __answer = scripting.funcs._ask(omc, "ngspicetoModelica", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getInheritedClasses(
    omc: OMCSessionBase,
    name,
):
    '''
function getInheritedClasses
  input TypeName name;
  output TypeName inheritedClasses[:];
end getInheritedClasses;
    '''
    __kwrds = {}
    __kwrds["name"] = scripting.types.TypeName(name)

    __answer = scripting.funcs._ask(omc, "getInheritedClasses", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return scripting.types.TypeName[:](__value)


# def getComponentsTest(
#     omc: OMCSessionBase,
#     name,
# ):
#     '''
# function getComponentsTest
#   input TypeName name;
#   output Component[:] components;
# 
#   record Component
#     String className;
#     // when building record the constructor. Records are allowed to contain only components of basic types, arrays of basic types or other records.
#     String name;
#     String comment;
#     Boolean isProtected;
#     Boolean isFinal;
#     Boolean isFlow;
#     Boolean isStream;
#     Boolean isReplaceable;
#     String variability "'constant', 'parameter', 'discrete', ''";
#     String innerOuter "'inner', 'outer', ''";
#     String inputOutput "'input', 'output', ''";
#     String dimensions[:];
#   end Component;
# end getComponentsTest;
#     '''
#     __kwrds = {}
#     __kwrds["name"] = scripting.types.TypeName(name)
# 
#     __answer = scripting.funcs._ask(omc, "getComponentsTest", **__kwrds)
#     try:
#         __value = parsers.parseOMCValue(__answer)
#     except parsers.NoMatch:
#         if __answer.lstrip().startswith("Error"):
#             raise scripting.exceptions.OMCError(__answer)
#         if not __answer or __answer.isspace():
#             return None
#         raise
# 
#     return scripting.types.Component[:](__value)


def isExperiment(
    omc: OMCSessionBase,
    name,
):
    '''
function isExperiment
  input TypeName name;
  output Boolean res;
end isExperiment;
    '''
    __kwrds = {}
    __kwrds["name"] = scripting.types.TypeName(name)

    __answer = scripting.funcs._ask(omc, "isExperiment", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


__getSimulationOptions_output = namedtuple(
    "OMCOutput",
    "startTime, stopTime, tolerance, numberOfIntervals, interval",
)


def getSimulationOptions(
    omc: OMCSessionBase,
    name,
    defaultStartTime=None,
    defaultStopTime=None,
    defaultTolerance=None,
    defaultNumberOfIntervals=None,
    defaultInterval=None,
):
    '''
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
    '''
    __kwrds = {}
    __kwrds["name"] = scripting.types.TypeName(name)
    if defaultStartTime is not None:
        __kwrds["defaultStartTime"] = scripting.types.Real(defaultStartTime)
    if defaultStopTime is not None:
        __kwrds["defaultStopTime"] = scripting.types.Real(defaultStopTime)
    if defaultTolerance is not None:
        __kwrds["defaultTolerance"] = scripting.types.Real(defaultTolerance)
    if defaultNumberOfIntervals is not None:
        __kwrds["defaultNumberOfIntervals"] = scripting.types.Integer(defaultNumberOfIntervals)
    if defaultInterval is not None:
        __kwrds["defaultInterval"] = scripting.types.Real(defaultInterval)

    __answer = scripting.funcs._ask(omc, "getSimulationOptions", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __getSimulationOptions_output(
        startTime=__value[0],
        stopTime=__value[1],
        tolerance=__value[2],
        numberOfIntervals=__value[3],
        interval=__value[4],
    )


def getAnnotationNamedModifiers(
    omc: OMCSessionBase,
    name,
    vendorannotation,
):
    '''
function getAnnotationNamedModifiers
  input TypeName name;
  input String vendorannotation;
  output String[:] modifiernamelist;
end getAnnotationNamedModifiers;
    '''
    __kwrds = {}
    __kwrds["name"] = scripting.types.TypeName(name)
    __kwrds["vendorannotation"] = scripting.types.String(vendorannotation)

    __answer = scripting.funcs._ask(omc, "getAnnotationNamedModifiers", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getAnnotationModifierValue(
    omc: OMCSessionBase,
    name,
    vendorannotation,
    modifiername,
):
    '''
function getAnnotationModifierValue
  input TypeName name;
  input String vendorannotation;
  input String modifiername;
  output String modifiernamevalue;
end getAnnotationModifierValue;
    '''
    __kwrds = {}
    __kwrds["name"] = scripting.types.TypeName(name)
    __kwrds["vendorannotation"] = scripting.types.String(vendorannotation)
    __kwrds["modifiername"] = scripting.types.String(modifiername)

    __answer = scripting.funcs._ask(omc, "getAnnotationModifierValue", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def classAnnotationExists(
    omc: OMCSessionBase,
    className,
    annotationName,
):
    '''
function classAnnotationExists
  input TypeName className;
  input TypeName annotationName;
  output Boolean exists;
end classAnnotationExists;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    __kwrds["annotationName"] = scripting.types.TypeName(annotationName)

    __answer = scripting.funcs._ask(omc, "classAnnotationExists", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getBooleanClassAnnotation(
    omc: OMCSessionBase,
    className,
    annotationName,
):
    '''
function getBooleanClassAnnotation
  input TypeName className;
  input TypeName annotationName;
  output Boolean value;
end getBooleanClassAnnotation;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    __kwrds["annotationName"] = scripting.types.TypeName(annotationName)

    __answer = scripting.funcs._ask(omc, "getBooleanClassAnnotation", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def extendsFrom(
    omc: OMCSessionBase,
    className,
    baseClassName,
):
    '''
function extendsFrom
  input TypeName className;
  input TypeName baseClassName;
  output Boolean res;
end extendsFrom;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    __kwrds["baseClassName"] = scripting.types.TypeName(baseClassName)

    __answer = scripting.funcs._ask(omc, "extendsFrom", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def loadModelica3D(
    omc: OMCSessionBase,
    version=None,
):
    '''
function loadModelica3D
  input String version = "3.2.1";
  output Boolean status;
end loadModelica3D;
    '''
    __kwrds = {}
    if version is not None:
        __kwrds["version"] = scripting.types.String(version)

    __answer = scripting.funcs._ask(omc, "loadModelica3D", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def searchClassNames(
    omc: OMCSessionBase,
    searchText,
    findInText=None,
):
    '''
function searchClassNames
  input String searchText;
  input Boolean findInText = false;
  output TypeName classNames[:];
end searchClassNames;
    '''
    __kwrds = {}
    __kwrds["searchText"] = scripting.types.String(searchText)
    if findInText is not None:
        __kwrds["findInText"] = scripting.types.Boolean(findInText)

    __answer = scripting.funcs._ask(omc, "searchClassNames", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return scripting.types.TypeName[:](__value)


def getAvailableLibraries(
    omc: OMCSessionBase,
):
    '''
function getAvailableLibraries
  output String[:] libraries;
end getAvailableLibraries;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getAvailableLibraries", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getUses(
    omc: OMCSessionBase,
    pack,
):
    '''
function getUses
  input TypeName pack;
  output String[:, :] uses;
end getUses;
    '''
    __kwrds = {}
    __kwrds["pack"] = scripting.types.TypeName(pack)

    __answer = scripting.funcs._ask(omc, "getUses", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getDerivedClassModifierNames(
    omc: OMCSessionBase,
    className,
):
    '''
function getDerivedClassModifierNames
  input TypeName className;
  output String[:] modifierNames;
end getDerivedClassModifierNames;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)

    __answer = scripting.funcs._ask(omc, "getDerivedClassModifierNames", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def getDerivedClassModifierValue(
    omc: OMCSessionBase,
    className,
    modifierName,
):
    '''
function getDerivedClassModifierValue
  input TypeName className;
  input TypeName modifierName;
  output String modifierValue;
end getDerivedClassModifierValue;
    '''
    __kwrds = {}
    __kwrds["className"] = scripting.types.TypeName(className)
    __kwrds["modifierName"] = scripting.types.TypeName(modifierName)

    __answer = scripting.funcs._ask(omc, "getDerivedClassModifierValue", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def generateEntryPoint(
    omc: OMCSessionBase,
    fileName,
    entryPoint,
    url=None,
):
    '''
function generateEntryPoint
  input String fileName;
  input TypeName entryPoint;
  input String url = "https://trac.openmodelica.org/OpenModelica/newticket";
end generateEntryPoint;
    '''
    __kwrds = {}
    __kwrds["fileName"] = scripting.types.String(fileName)
    __kwrds["entryPoint"] = scripting.types.TypeName(entryPoint)
    if url is not None:
        __kwrds["url"] = scripting.types.String(url)

    __answer = scripting.funcs._ask(omc, "generateEntryPoint", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return


def numProcessors(
    omc: OMCSessionBase,
):
    '''
function numProcessors
  output Integer result;
end numProcessors;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "numProcessors", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def runScriptParallel(
    omc: OMCSessionBase,
    scripts,
    numThreads=None,
    useThreads=None,
):
    '''
function runScriptParallel
  input String scripts[:];
  input Integer numThreads = numProcessors();
  input Boolean useThreads = false;
  output Boolean results[:];
end runScriptParallel;
    '''
    __kwrds = {}
    __kwrds["scripts"] = scripting.types.String[:](scripts)
    if numThreads is not None:
        __kwrds["numThreads"] = scripting.types.Integer(numThreads)
    if useThreads is not None:
        __kwrds["useThreads"] = scripting.types.Boolean(useThreads)

    __answer = scripting.funcs._ask(omc, "runScriptParallel", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def exit(
    omc: OMCSessionBase,
    status,
):
    '''
function exit
  input Integer status;
end exit;
    '''
    __kwrds = {}
    __kwrds["status"] = scripting.types.Integer(status)

    __answer = scripting.funcs._ask(omc, "exit", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return


def threadWorkFailed(
    omc: OMCSessionBase,
):
    '''
function threadWorkFailed

  external "builtin" ;
  annotation(
    Documentation(info = "<html>
<p>(Experimental) Exits the current (<a href=\"modelica://OpenModelica.Scripting.runScriptParallel\">worker thread</a>) signalling a failure.</p>
</html>"));
end threadWorkFailed;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "threadWorkFailed", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return


def getMemorySize(
    omc: OMCSessionBase,
):
    '''
function getMemorySize
  output Real memory(unit = "MiB");
end getMemorySize;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "getMemorySize", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def GC_gcollect_and_unmap(
    omc: OMCSessionBase,
):
    '''
function GC_gcollect_and_unmap

  external "builtin" ;
  annotation(
    Documentation(info = "<html>
<p>Forces GC to collect and unmap memory (we use it before we start and wait for memory-intensive tasks in child processes).</p>
</html>"));
end GC_gcollect_and_unmap;
    '''
    __kwrds = {}

    __answer = scripting.funcs._ask(omc, "GC_gcollect_and_unmap", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return


def GC_expand_hp(
    omc: OMCSessionBase,
    size,
):
    '''
function GC_expand_hp
  input Integer size;
  output Boolean success;
end GC_expand_hp;
    '''
    __kwrds = {}
    __kwrds["size"] = scripting.types.Integer(size)

    __answer = scripting.funcs._ask(omc, "GC_expand_hp", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def GC_set_max_heap_size(
    omc: OMCSessionBase,
    size,
):
    '''
function GC_set_max_heap_size
  input Integer size;
  output Boolean success;
end GC_set_max_heap_size;
    '''
    __kwrds = {}
    __kwrds["size"] = scripting.types.Integer(size)

    __answer = scripting.funcs._ask(omc, "GC_set_max_heap_size", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


# def GC_get_prof_stats(
#     omc: OMCSessionBase,
# ):
#     '''
# function GC_get_prof_stats
#   output GC_PROFSTATS gcStats;
# end GC_get_prof_stats;
#     '''
#     __kwrds = {}
# 
#     __answer = scripting.funcs._ask(omc, "GC_get_prof_stats", **__kwrds)
#     try:
#         __value = parsers.parseOMCValue(__answer)
#     except parsers.NoMatch:
#         if __answer.lstrip().startswith("Error"):
#             raise scripting.exceptions.OMCError(__answer)
#         if not __answer or __answer.isspace():
#             return None
#         raise
# 
#     return scripting.types.GC_PROFSTATS(__value)


def checkInterfaceOfPackages(
    omc: OMCSessionBase,
    cl,
    dependencyMatrix,
):
    '''
function checkInterfaceOfPackages
  input TypeName cl;
  input String dependencyMatrix[:, :];
  output Boolean success;
end checkInterfaceOfPackages;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)
    __kwrds["dependencyMatrix"] = scripting.types.String[:,:](dependencyMatrix)

    __answer = scripting.funcs._ask(omc, "checkInterfaceOfPackages", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


def sortStrings(
    omc: OMCSessionBase,
    arr,
):
    '''
function sortStrings
  input String arr[:];
  output String sorted[:];
end sortStrings;
    '''
    __kwrds = {}
    __kwrds["arr"] = scripting.types.String[:](arr)

    __answer = scripting.funcs._ask(omc, "sortStrings", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


__getClassInformation_output = namedtuple(
    "OMCOutput",
    "restriction, comment, partialPrefix, finalPrefix, encapsulatedPrefix, fileName, fileReadOnly, lineNumberStart, columnNumberStart, lineNumberEnd, columnNumberEnd, dimensions, isProtectedClass, isDocumentationClass, version, preferredView, state, access",
)


def getClassInformation(
    omc: OMCSessionBase,
    cl,
):
    '''
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
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "getClassInformation", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __getClassInformation_output(
        restriction=__value[0],
        comment=__value[1],
        partialPrefix=__value[2],
        finalPrefix=__value[3],
        encapsulatedPrefix=__value[4],
        fileName=__value[5],
        fileReadOnly=__value[6],
        lineNumberStart=__value[7],
        columnNumberStart=__value[8],
        lineNumberEnd=__value[9],
        columnNumberEnd=__value[10],
        dimensions=__value[11],
        isProtectedClass=__value[12],
        isDocumentationClass=__value[13],
        version=__value[14],
        preferredView=__value[15],
        state=__value[16],
        access=__value[17],
    )


def getTransitions(
    omc: OMCSessionBase,
    cl,
):
    '''
function getTransitions
  input TypeName cl;
  output String[:, :] transitions;
end getTransitions;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "getTransitions", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


# def addTransition(
#     omc: OMCSessionBase,
#     cl,
#     from_,
#     to,
#     condition,
#     annotate,
#     immediate=None,
#     reset=None,
#     synchronize=None,
#     priority=None,
# ):
#     '''
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
#     '''
#     __kwrds = {}
#     __kwrds["cl"] = scripting.types.TypeName(cl)
#     __kwrds["from"] = scripting.types.String(from_)
#     __kwrds["to"] = scripting.types.String(to)
#     __kwrds["condition"] = scripting.types.String(condition)
#     __kwrds["annotate"] = scripting.types.ExpressionOrModification(annotate)
#     if immediate is not None:
#         __kwrds["immediate"] = scripting.types.Boolean(immediate)
#     if reset is not None:
#         __kwrds["reset"] = scripting.types.Boolean(reset)
#     if synchronize is not None:
#         __kwrds["synchronize"] = scripting.types.Boolean(synchronize)
#     if priority is not None:
#         __kwrds["priority"] = scripting.types.Integer(priority)
# 
#     __answer = scripting.funcs._ask(omc, "addTransition", **__kwrds)
#     try:
#         __value = parsers.parseOMCValue(__answer)
#     except parsers.NoMatch:
#         if __answer.lstrip().startswith("Error"):
#             raise scripting.exceptions.OMCError(__answer)
#         if not __answer or __answer.isspace():
#             return None
#         raise
# 
#     return __value


def deleteTransition(
    omc: OMCSessionBase,
    cl,
    from_,
    to,
    condition,
    immediate,
    reset,
    synchronize,
    priority,
):
    '''
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
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)
    __kwrds["from"] = scripting.types.String(from_)
    __kwrds["to"] = scripting.types.String(to)
    __kwrds["condition"] = scripting.types.String(condition)
    __kwrds["immediate"] = scripting.types.Boolean(immediate)
    __kwrds["reset"] = scripting.types.Boolean(reset)
    __kwrds["synchronize"] = scripting.types.Boolean(synchronize)
    __kwrds["priority"] = scripting.types.Integer(priority)

    __answer = scripting.funcs._ask(omc, "deleteTransition", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


# def updateTransition(
#     omc: OMCSessionBase,
#     cl,
#     from_,
#     to,
#     oldCondition,
#     oldImmediate,
#     oldReset,
#     oldSynchronize,
#     oldPriority,
#     newCondition,
#     newImmediate,
#     newReset,
#     newSynchronize,
#     newPriority,
#     annotate,
# ):
#     '''
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
#     '''
#     __kwrds = {}
#     __kwrds["cl"] = scripting.types.TypeName(cl)
#     __kwrds["from"] = scripting.types.String(from_)
#     __kwrds["to"] = scripting.types.String(to)
#     __kwrds["oldCondition"] = scripting.types.String(oldCondition)
#     __kwrds["oldImmediate"] = scripting.types.Boolean(oldImmediate)
#     __kwrds["oldReset"] = scripting.types.Boolean(oldReset)
#     __kwrds["oldSynchronize"] = scripting.types.Boolean(oldSynchronize)
#     __kwrds["oldPriority"] = scripting.types.Integer(oldPriority)
#     __kwrds["newCondition"] = scripting.types.String(newCondition)
#     __kwrds["newImmediate"] = scripting.types.Boolean(newImmediate)
#     __kwrds["newReset"] = scripting.types.Boolean(newReset)
#     __kwrds["newSynchronize"] = scripting.types.Boolean(newSynchronize)
#     __kwrds["newPriority"] = scripting.types.Integer(newPriority)
#     __kwrds["annotate"] = scripting.types.ExpressionOrModification(annotate)
# 
#     __answer = scripting.funcs._ask(omc, "updateTransition", **__kwrds)
#     try:
#         __value = parsers.parseOMCValue(__answer)
#     except parsers.NoMatch:
#         if __answer.lstrip().startswith("Error"):
#             raise scripting.exceptions.OMCError(__answer)
#         if not __answer or __answer.isspace():
#             return None
#         raise
# 
#     return __value


def getInitialStates(
    omc: OMCSessionBase,
    cl,
):
    '''
function getInitialStates
  input TypeName cl;
  output String[:, :] initialStates;
end getInitialStates;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)

    __answer = scripting.funcs._ask(omc, "getInitialStates", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


# def addInitialState(
#     omc: OMCSessionBase,
#     cl,
#     state,
#     annotate,
# ):
#     '''
# function addInitialState
#   input TypeName cl;
#   input String state;
#   input ExpressionOrModification annotate;
#   output Boolean bool;
# end addInitialState;
#     '''
#     __kwrds = {}
#     __kwrds["cl"] = scripting.types.TypeName(cl)
#     __kwrds["state"] = scripting.types.String(state)
#     __kwrds["annotate"] = scripting.types.ExpressionOrModification(annotate)
# 
#     __answer = scripting.funcs._ask(omc, "addInitialState", **__kwrds)
#     try:
#         __value = parsers.parseOMCValue(__answer)
#     except parsers.NoMatch:
#         if __answer.lstrip().startswith("Error"):
#             raise scripting.exceptions.OMCError(__answer)
#         if not __answer or __answer.isspace():
#             return None
#         raise
# 
#     return __value


def deleteInitialState(
    omc: OMCSessionBase,
    cl,
    state,
):
    '''
function deleteInitialState
  input TypeName cl;
  input String state;
  output Boolean bool;
end deleteInitialState;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)
    __kwrds["state"] = scripting.types.String(state)

    __answer = scripting.funcs._ask(omc, "deleteInitialState", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __value


# def updateInitialState(
#     omc: OMCSessionBase,
#     cl,
#     state,
#     annotate,
# ):
#     '''
# function updateInitialState
#   input TypeName cl;
#   input String state;
#   input ExpressionOrModification annotate;
#   output Boolean bool;
# end updateInitialState;
#     '''
#     __kwrds = {}
#     __kwrds["cl"] = scripting.types.TypeName(cl)
#     __kwrds["state"] = scripting.types.String(state)
#     __kwrds["annotate"] = scripting.types.ExpressionOrModification(annotate)
# 
#     __answer = scripting.funcs._ask(omc, "updateInitialState", **__kwrds)
#     try:
#         __value = parsers.parseOMCValue(__answer)
#     except parsers.NoMatch:
#         if __answer.lstrip().startswith("Error"):
#             raise scripting.exceptions.OMCError(__answer)
#         if not __answer or __answer.isspace():
#             return None
#         raise
# 
#     return __value


__generateScriptingAPI_output = namedtuple(
    "OMCOutput",
    "success, moFile, qtFile, qtHeader",
)


def generateScriptingAPI(
    omc: OMCSessionBase,
    cl,
    name,
):
    '''
function generateScriptingAPI
  input TypeName cl;
  input String name;
  output Boolean success;
  output String moFile;
  output String qtFile;
  output String qtHeader;
end generateScriptingAPI;
    '''
    __kwrds = {}
    __kwrds["cl"] = scripting.types.TypeName(cl)
    __kwrds["name"] = scripting.types.String(name)

    __answer = scripting.funcs._ask(omc, "generateScriptingAPI", **__kwrds)
    try:
        __value = parsers.parseOMCValue(__answer)
    except parsers.NoMatch:
        if __answer.lstrip().startswith("Error"):
            raise scripting.exceptions.OMCError(__answer)
        if not __answer or __answer.isspace():
            return None
        raise

    return __generateScriptingAPI_output(
        success=__value[0],
        moFile=__value[1],
        qtFile=__value[2],
        qtHeader=__value[3],
    )


saveTotalSCode = saveTotalModel
