from __future__ import annotations as _

from dataclasses import dataclass
from typing import Coroutine, Union, overload

from omc4py.modelica import external, package, record
from omc4py.openmodelica import TypeName
from omc4py.protocol import (
    Asynchronous,
    SupportsInteractiveProperty,
    Synchronous,
    T_Calling,
)

from . import Internal as internal
from . import Scripting as scripting
from . import UsersGuide as usersGuide


@overload
def threadData(self: SupportsInteractiveProperty[Synchronous]) -> ThreadData:
    ...


@overload
async def threadData(
    self: SupportsInteractiveProperty[Asynchronous],
) -> ThreadData:
    ...


@external("OpenModelica.threadData")
def threadData(
    self: Union[
        SupportsInteractiveProperty[Synchronous],
        SupportsInteractiveProperty[Asynchronous],
    ]
) -> Union[ThreadData, Coroutine[None, None, ThreadData]]:
    """
    .. code-block:: modelica

        function threadData
          output ThreadData threadData;
        end threadData;"""
    return ...  # type: ignore


@dataclass(frozen=True)
class ThreadData(record):
    """
    .. code-block:: modelica

        record ThreadData
        end ThreadData;"""

    __omc_class__ = TypeName("OpenModelica.threadData.ThreadData")


class Internal(package[T_Calling]):
    __omc_class__ = TypeName("OpenModelica.Internal")
    ClockConstructor = internal.ClockConstructor
    intervalInferred = internal.intervalInferred
    delay2 = internal.delay2
    delay3 = internal.delay3
    intAbs = internal.intAbs
    realAbs = internal.realAbs
    intDiv = internal.intDiv
    realDiv = internal.realDiv
    intMod = internal.intMod
    realMod = internal.realMod
    intRem = internal.intRem
    realRem = internal.realRem

    @property
    def Architecture(self) -> internal.Architecture[T_Calling]:
        return internal.Architecture(self.__omc_interactive__)


class Scripting(package[T_Calling]):
    __omc_class__ = TypeName("OpenModelica.Scripting")
    CheckSettingsResult = scripting.CheckSettingsResult

    @property
    def Internal(self) -> scripting.Internal[T_Calling]:
        return scripting.Internal(self.__omc_interactive__)

    checkSettings = scripting.checkSettings
    loadFile = scripting.loadFile
    loadFiles = scripting.loadFiles
    loadEncryptedPackage = scripting.loadEncryptedPackage
    reloadClass = scripting.reloadClass
    loadString = scripting.loadString
    parseString = scripting.parseString
    parseFile = scripting.parseFile
    loadFileInteractiveQualified = scripting.loadFileInteractiveQualified
    loadFileInteractive = scripting.loadFileInteractive
    system = scripting.system
    system_parallel = scripting.system_parallel
    saveAll = scripting.saveAll
    help = scripting.help
    clear = scripting.clear
    clearProgram = scripting.clearProgram
    clearVariables = scripting.clearVariables
    generateHeader = scripting.generateHeader
    generateSeparateCode = scripting.generateSeparateCode
    generateSeparateCodeDependencies = (
        scripting.generateSeparateCodeDependencies
    )
    generateSeparateCodeDependenciesMakefile = (
        scripting.generateSeparateCodeDependenciesMakefile
    )
    getLinker = scripting.getLinker
    setLinker = scripting.setLinker
    getLinkerFlags = scripting.getLinkerFlags
    setLinkerFlags = scripting.setLinkerFlags
    getCompiler = scripting.getCompiler
    setCompiler = scripting.setCompiler
    setCFlags = scripting.setCFlags
    getCFlags = scripting.getCFlags
    getCXXCompiler = scripting.getCXXCompiler
    setCXXCompiler = scripting.setCXXCompiler
    verifyCompiler = scripting.verifyCompiler
    setCompilerPath = scripting.setCompilerPath
    getCompileCommand = scripting.getCompileCommand
    setCompileCommand = scripting.setCompileCommand
    setPlotCommand = scripting.setPlotCommand
    getSettings = scripting.getSettings
    setTempDirectoryPath = scripting.setTempDirectoryPath
    getTempDirectoryPath = scripting.getTempDirectoryPath
    getEnvironmentVar = scripting.getEnvironmentVar
    setEnvironmentVar = scripting.setEnvironmentVar
    appendEnvironmentVar = scripting.appendEnvironmentVar
    setInstallationDirectoryPath = scripting.setInstallationDirectoryPath
    getInstallationDirectoryPath = scripting.getInstallationDirectoryPath
    setModelicaPath = scripting.setModelicaPath
    getModelicaPath = scripting.getModelicaPath
    setCompilerFlags = scripting.setCompilerFlags
    setDebugFlags = scripting.setDebugFlags
    clearDebugFlags = scripting.clearDebugFlags
    setPreOptModules = scripting.setPreOptModules
    setCheapMatchingAlgorithm = scripting.setCheapMatchingAlgorithm
    getMatchingAlgorithm = scripting.getMatchingAlgorithm
    getAvailableMatchingAlgorithms = scripting.getAvailableMatchingAlgorithms
    setMatchingAlgorithm = scripting.setMatchingAlgorithm
    getIndexReductionMethod = scripting.getIndexReductionMethod
    getAvailableIndexReductionMethods = (
        scripting.getAvailableIndexReductionMethods
    )
    setIndexReductionMethod = scripting.setIndexReductionMethod
    setPostOptModules = scripting.setPostOptModules
    getTearingMethod = scripting.getTearingMethod
    getAvailableTearingMethods = scripting.getAvailableTearingMethods
    setTearingMethod = scripting.setTearingMethod
    setCommandLineOptions = scripting.setCommandLineOptions
    getCommandLineOptions = scripting.getCommandLineOptions
    getConfigFlagValidOptions = scripting.getConfigFlagValidOptions
    clearCommandLineOptions = scripting.clearCommandLineOptions
    getVersion = scripting.getVersion
    regularFileExists = scripting.regularFileExists
    directoryExists = scripting.directoryExists
    stat = scripting.stat
    readFile = scripting.readFile
    writeFile = scripting.writeFile
    compareFilesAndMove = scripting.compareFilesAndMove
    compareFiles = scripting.compareFiles
    alarm = scripting.alarm
    regex = scripting.regex
    regexBool = scripting.regexBool
    testsuiteFriendlyName = scripting.testsuiteFriendlyName
    readFileNoNumeric = scripting.readFileNoNumeric
    getErrorString = scripting.getErrorString
    getMessagesString = scripting.getMessagesString
    SourceInfo = scripting.SourceInfo
    ErrorKind = scripting.ErrorKind
    ErrorLevel = scripting.ErrorLevel
    ErrorMessage = scripting.ErrorMessage
    getMessagesStringInternal = scripting.getMessagesStringInternal
    countMessages = scripting.countMessages
    clearMessages = scripting.clearMessages
    runScript = scripting.runScript
    echo = scripting.echo
    getClassesInModelicaPath = scripting.getClassesInModelicaPath
    getAnnotationVersion = scripting.getAnnotationVersion
    setAnnotationVersion = scripting.setAnnotationVersion
    getNoSimplify = scripting.getNoSimplify
    setNoSimplify = scripting.setNoSimplify
    getVectorizationLimit = scripting.getVectorizationLimit
    setVectorizationLimit = scripting.setVectorizationLimit
    getDefaultOpenCLDevice = scripting.getDefaultOpenCLDevice
    setDefaultOpenCLDevice = scripting.setDefaultOpenCLDevice
    setShowAnnotations = scripting.setShowAnnotations
    getShowAnnotations = scripting.getShowAnnotations
    setOrderConnections = scripting.setOrderConnections
    getOrderConnections = scripting.getOrderConnections
    setLanguageStandard = scripting.setLanguageStandard
    getLanguageStandard = scripting.getLanguageStandard
    getAstAsCorbaString = scripting.getAstAsCorbaString
    cd = scripting.cd
    mkdir = scripting.mkdir
    copy = scripting.copy
    remove = scripting.remove
    checkModel = scripting.checkModel
    checkAllModelsRecursive = scripting.checkAllModelsRecursive
    typeOf = scripting.typeOf
    instantiateModel = scripting.instantiateModel
    buildOpenTURNSInterface = scripting.buildOpenTURNSInterface
    runOpenTURNSPythonScript = scripting.runOpenTURNSPythonScript
    generateCode = scripting.generateCode
    loadModel = scripting.loadModel
    deleteFile = scripting.deleteFile
    saveModel = scripting.saveModel
    saveTotalModel = scripting.saveTotalModel
    save = scripting.save
    saveTotalSCode = scripting.saveTotalSCode
    translateGraphics = scripting.translateGraphics
    dumpXMLDAE = scripting.dumpXMLDAE
    convertUnits = scripting.convertUnits
    getDerivedUnits = scripting.getDerivedUnits
    listVariables = scripting.listVariables
    strtok = scripting.strtok
    stringSplit = scripting.stringSplit
    stringReplace = scripting.stringReplace
    escapeXML = scripting.escapeXML
    ExportKind = scripting.ExportKind
    list = scripting.list
    listFile = scripting.listFile
    DiffFormat = scripting.DiffFormat
    diffModelicaFileListings = scripting.diffModelicaFileListings
    exportToFigaro = scripting.exportToFigaro
    inferBindings = scripting.inferBindings
    generateVerificationScenarios = scripting.generateVerificationScenarios
    rewriteBlockCall = scripting.rewriteBlockCall
    realpath = scripting.realpath
    uriToFilename = scripting.uriToFilename
    getLoadedLibraries = scripting.getLoadedLibraries
    LinearSystemSolver = scripting.LinearSystemSolver
    solveLinearSystem = scripting.solveLinearSystem
    StandardStream = scripting.StandardStream
    reopenStandardStream = scripting.reopenStandardStream
    importFMU = scripting.importFMU
    importFMUModelDescription = scripting.importFMUModelDescription
    translateModelFMU = scripting.translateModelFMU
    buildModelFMU = scripting.buildModelFMU
    buildEncryptedPackage = scripting.buildEncryptedPackage
    simulate = scripting.simulate
    SimulationResult = scripting.SimulationResult
    buildModel = scripting.buildModel
    buildLabel = scripting.buildLabel
    reduceTerms = scripting.reduceTerms
    moveClass = scripting.moveClass
    moveClassToTop = scripting.moveClassToTop
    moveClassToBottom = scripting.moveClassToBottom
    copyClass = scripting.copyClass
    linearize = scripting.linearize
    optimize = scripting.optimize
    getSourceFile = scripting.getSourceFile
    setSourceFile = scripting.setSourceFile
    isShortDefinition = scripting.isShortDefinition
    setClassComment = scripting.setClassComment
    getClassNames = scripting.getClassNames
    getUsedClassNames = scripting.getUsedClassNames
    getPackages = scripting.getPackages
    basePlotFunction = scripting.basePlotFunction
    plot = scripting.plot
    plotAll = scripting.plotAll
    plotParametric = scripting.plotParametric
    readSimulationResult = scripting.readSimulationResult
    readSimulationResultSize = scripting.readSimulationResultSize
    readSimulationResultVars = scripting.readSimulationResultVars
    filterSimulationResults = scripting.filterSimulationResults
    compareSimulationResults = scripting.compareSimulationResults
    deltaSimulationResults = scripting.deltaSimulationResults
    diffSimulationResults = scripting.diffSimulationResults
    diffSimulationResultsHtml = scripting.diffSimulationResultsHtml
    checkTaskGraph = scripting.checkTaskGraph
    checkCodeGraph = scripting.checkCodeGraph
    val = scripting.val
    closeSimulationResultFile = scripting.closeSimulationResultFile
    getParameterNames = scripting.getParameterNames
    getParameterValue = scripting.getParameterValue
    getComponentModifierNames = scripting.getComponentModifierNames
    getComponentModifierValue = scripting.getComponentModifierValue
    getComponentModifierValues = scripting.getComponentModifierValues
    getInstantiatedParametersAndValues = (
        scripting.getInstantiatedParametersAndValues
    )
    removeComponentModifiers = scripting.removeComponentModifiers
    removeExtendsModifiers = scripting.removeExtendsModifiers
    getConnectionCount = scripting.getConnectionCount
    getNthConnection = scripting.getNthConnection
    getAlgorithmCount = scripting.getAlgorithmCount
    getNthAlgorithm = scripting.getNthAlgorithm
    getInitialAlgorithmCount = scripting.getInitialAlgorithmCount
    getNthInitialAlgorithm = scripting.getNthInitialAlgorithm
    getAlgorithmItemsCount = scripting.getAlgorithmItemsCount
    getNthAlgorithmItem = scripting.getNthAlgorithmItem
    getInitialAlgorithmItemsCount = scripting.getInitialAlgorithmItemsCount
    getNthInitialAlgorithmItem = scripting.getNthInitialAlgorithmItem
    getEquationCount = scripting.getEquationCount
    getNthEquation = scripting.getNthEquation
    getInitialEquationCount = scripting.getInitialEquationCount
    getNthInitialEquation = scripting.getNthInitialEquation
    getEquationItemsCount = scripting.getEquationItemsCount
    getNthEquationItem = scripting.getNthEquationItem
    getInitialEquationItemsCount = scripting.getInitialEquationItemsCount
    getNthInitialEquationItem = scripting.getNthInitialEquationItem
    getAnnotationCount = scripting.getAnnotationCount
    getNthAnnotationString = scripting.getNthAnnotationString
    getImportCount = scripting.getImportCount
    getNthImport = scripting.getNthImport
    iconv = scripting.iconv
    getDocumentationAnnotation = scripting.getDocumentationAnnotation
    setDocumentationAnnotation = scripting.setDocumentationAnnotation
    getTimeStamp = scripting.getTimeStamp
    stringTypeName = scripting.stringTypeName
    stringVariableName = scripting.stringVariableName
    typeNameString = scripting.typeNameString
    typeNameStrings = scripting.typeNameStrings
    getClassComment = scripting.getClassComment
    dirname = scripting.dirname
    basename = scripting.basename
    getClassRestriction = scripting.getClassRestriction
    isType = scripting.isType
    isPackage = scripting.isPackage
    isClass = scripting.isClass
    isRecord = scripting.isRecord
    isBlock = scripting.isBlock
    isFunction = scripting.isFunction
    isPartial = scripting.isPartial
    isModel = scripting.isModel
    isConnector = scripting.isConnector
    isOptimization = scripting.isOptimization
    isEnumeration = scripting.isEnumeration
    isOperator = scripting.isOperator
    isOperatorRecord = scripting.isOperatorRecord
    isOperatorFunction = scripting.isOperatorFunction
    isProtectedClass = scripting.isProtectedClass
    getBuiltinType = scripting.getBuiltinType
    setInitXmlStartValue = scripting.setInitXmlStartValue
    ngspicetoModelica = scripting.ngspicetoModelica
    getInheritedClasses = scripting.getInheritedClasses
    getComponentsTest = scripting.getComponentsTest
    Component = scripting.Component
    isExperiment = scripting.isExperiment
    getSimulationOptions = scripting.getSimulationOptions
    getAnnotationNamedModifiers = scripting.getAnnotationNamedModifiers
    getAnnotationModifierValue = scripting.getAnnotationModifierValue
    classAnnotationExists = scripting.classAnnotationExists
    getBooleanClassAnnotation = scripting.getBooleanClassAnnotation
    extendsFrom = scripting.extendsFrom
    loadModelica3D = scripting.loadModelica3D
    searchClassNames = scripting.searchClassNames
    getAvailableLibraries = scripting.getAvailableLibraries
    getUses = scripting.getUses
    getDerivedClassModifierNames = scripting.getDerivedClassModifierNames
    getDerivedClassModifierValue = scripting.getDerivedClassModifierValue
    generateEntryPoint = scripting.generateEntryPoint
    numProcessors = scripting.numProcessors
    runScriptParallel = scripting.runScriptParallel
    exit = scripting.exit
    threadWorkFailed = scripting.threadWorkFailed
    getMemorySize = scripting.getMemorySize
    GC_gcollect_and_unmap = scripting.GC_gcollect_and_unmap
    GC_expand_hp = scripting.GC_expand_hp
    GC_set_max_heap_size = scripting.GC_set_max_heap_size
    GC_PROFSTATS = scripting.GC_PROFSTATS
    GC_get_prof_stats = scripting.GC_get_prof_stats
    checkInterfaceOfPackages = scripting.checkInterfaceOfPackages
    sortStrings = scripting.sortStrings
    getClassInformation = scripting.getClassInformation
    getTransitions = scripting.getTransitions
    deleteTransition = scripting.deleteTransition
    getInitialStates = scripting.getInitialStates
    deleteInitialState = scripting.deleteInitialState
    generateScriptingAPI = scripting.generateScriptingAPI

    @property
    def Experimental(self) -> scripting.Experimental[T_Calling]:
        return scripting.Experimental(self.__omc_interactive__)


class UsersGuide(package[T_Calling]):
    __omc_class__ = TypeName("OpenModelica.UsersGuide")

    @property
    def ReleaseNotes(self) -> usersGuide.ReleaseNotes[T_Calling]:
        return usersGuide.ReleaseNotes(self.__omc_interactive__)
