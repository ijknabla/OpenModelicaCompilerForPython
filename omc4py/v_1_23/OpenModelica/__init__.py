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

from . import AutoCompletion as autoCompletion
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
    parseEncryptedPackage = scripting.parseEncryptedPackage
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
    generateJuliaHeader = scripting.generateJuliaHeader
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
    getHomeDirectoryPath = scripting.getHomeDirectoryPath
    setCompilerFlags = scripting.setCompilerFlags
    enableNewInstantiation = scripting.enableNewInstantiation
    disableNewInstantiation = scripting.disableNewInstantiation
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
    generateCode = scripting.generateCode
    loadModel = scripting.loadModel
    deleteFile = scripting.deleteFile
    saveModel = scripting.saveModel
    saveTotalModel = scripting.saveTotalModel
    saveTotalModelDebug = scripting.saveTotalModelDebug
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
    getAllSubtypeOf = scripting.getAllSubtypeOf
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
    removeComponentModifiers = scripting.removeComponentModifiers
    getElementModifierNames = scripting.getElementModifierNames
    setComponentModifierValue = scripting.setComponentModifierValue
    getElementModifierValue = scripting.getElementModifierValue
    getElementModifierValues = scripting.getElementModifierValues
    removeElementModifiers = scripting.removeElementModifiers
    getElementAnnotation = scripting.getElementAnnotation
    getInstantiatedParametersAndValues = (
        scripting.getInstantiatedParametersAndValues
    )
    removeExtendsModifiers = scripting.removeExtendsModifiers
    updateConnectionAnnotation = scripting.updateConnectionAnnotation
    updateConnectionNames = scripting.updateConnectionNames
    getConnectionCount = scripting.getConnectionCount
    getNthConnection = scripting.getNthConnection
    getConnectionList = scripting.getConnectionList
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
    getMMfileTotalDependencies = scripting.getMMfileTotalDependencies
    getImportedNames = scripting.getImportedNames
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
    isReplaceable = scripting.isReplaceable
    isRedeclare = scripting.isRedeclare
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
    getAvailableLibraryVersions = scripting.getAvailableLibraryVersions
    installPackage = scripting.installPackage
    updatePackageIndex = scripting.updatePackageIndex
    upgradeInstalledPackages = scripting.upgradeInstalledPackages
    getAvailablePackageVersions = scripting.getAvailablePackageVersions
    getAvailablePackageConversionsTo = (
        scripting.getAvailablePackageConversionsTo
    )
    getAvailablePackageConversionsFrom = (
        scripting.getAvailablePackageConversionsFrom
    )
    getUses = scripting.getUses
    getConversionsFromVersions = scripting.getConversionsFromVersions
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
    runConversionScript = scripting.runConversionScript
    convertPackageToLibrary = scripting.convertPackageToLibrary
    getModelInstance = scripting.getModelInstance
    getModelInstanceIcon = scripting.getModelInstanceIcon
    modifierToJSON = scripting.modifierToJSON
    storeAST = scripting.storeAST
    restoreAST = scripting.restoreAST
    qualifyPath = scripting.qualifyPath
    oms_system = scripting.oms_system
    oms_causality = scripting.oms_causality
    oms_signal_type = scripting.oms_signal_type
    oms_solver = scripting.oms_solver
    oms_tlm_domain = scripting.oms_tlm_domain
    oms_tlm_interpolation = scripting.oms_tlm_interpolation
    oms_fault_type = scripting.oms_fault_type
    loadOMSimulator = scripting.loadOMSimulator
    unloadOMSimulator = scripting.unloadOMSimulator
    oms_addBus = scripting.oms_addBus
    oms_addConnection = scripting.oms_addConnection
    oms_addConnector = scripting.oms_addConnector
    oms_addConnectorToBus = scripting.oms_addConnectorToBus
    oms_addConnectorToTLMBus = scripting.oms_addConnectorToTLMBus
    oms_addDynamicValueIndicator = scripting.oms_addDynamicValueIndicator
    oms_addEventIndicator = scripting.oms_addEventIndicator
    oms_addExternalModel = scripting.oms_addExternalModel
    oms_addSignalsToResults = scripting.oms_addSignalsToResults
    oms_addStaticValueIndicator = scripting.oms_addStaticValueIndicator
    oms_addSubModel = scripting.oms_addSubModel
    oms_addSystem = scripting.oms_addSystem
    oms_addTimeIndicator = scripting.oms_addTimeIndicator
    oms_addTLMBus = scripting.oms_addTLMBus
    oms_addTLMConnection = scripting.oms_addTLMConnection
    oms_compareSimulationResults = scripting.oms_compareSimulationResults
    oms_copySystem = scripting.oms_copySystem
    oms_delete = scripting.oms_delete
    oms_deleteConnection = scripting.oms_deleteConnection
    oms_deleteConnectorFromBus = scripting.oms_deleteConnectorFromBus
    oms_deleteConnectorFromTLMBus = scripting.oms_deleteConnectorFromTLMBus
    oms_export = scripting.oms_export
    oms_exportDependencyGraphs = scripting.oms_exportDependencyGraphs
    oms_exportSnapshot = scripting.oms_exportSnapshot
    oms_extractFMIKind = scripting.oms_extractFMIKind
    oms_getBoolean = scripting.oms_getBoolean
    oms_getFixedStepSize = scripting.oms_getFixedStepSize
    oms_getInteger = scripting.oms_getInteger
    oms_getModelState = scripting.oms_getModelState
    oms_getReal = scripting.oms_getReal
    oms_getSolver = scripting.oms_getSolver
    oms_getStartTime = scripting.oms_getStartTime
    oms_getStopTime = scripting.oms_getStopTime
    oms_getSubModelPath = scripting.oms_getSubModelPath
    oms_getSystemType = scripting.oms_getSystemType
    oms_getTolerance = scripting.oms_getTolerance
    oms_getVariableStepSize = scripting.oms_getVariableStepSize
    oms_faultInjection = scripting.oms_faultInjection
    oms_importFile = scripting.oms_importFile
    oms_importSnapshot = scripting.oms_importSnapshot
    oms_initialize = scripting.oms_initialize
    oms_instantiate = scripting.oms_instantiate
    oms_list = scripting.oms_list
    oms_listUnconnectedConnectors = scripting.oms_listUnconnectedConnectors
    oms_loadSnapshot = scripting.oms_loadSnapshot
    oms_newModel = scripting.oms_newModel
    oms_removeSignalsFromResults = scripting.oms_removeSignalsFromResults
    oms_rename = scripting.oms_rename
    oms_reset = scripting.oms_reset
    oms_RunFile = scripting.oms_RunFile
    oms_setBoolean = scripting.oms_setBoolean
    oms_setCommandLineOption = scripting.oms_setCommandLineOption
    oms_setFixedStepSize = scripting.oms_setFixedStepSize
    oms_setInteger = scripting.oms_setInteger
    oms_setLogFile = scripting.oms_setLogFile
    oms_setLoggingInterval = scripting.oms_setLoggingInterval
    oms_setLoggingLevel = scripting.oms_setLoggingLevel
    oms_setReal = scripting.oms_setReal
    oms_setRealInputDerivative = scripting.oms_setRealInputDerivative
    oms_setResultFile = scripting.oms_setResultFile
    oms_setSignalFilter = scripting.oms_setSignalFilter
    oms_setSolver = scripting.oms_setSolver
    oms_setStartTime = scripting.oms_setStartTime
    oms_setStopTime = scripting.oms_setStopTime
    oms_setTempDirectory = scripting.oms_setTempDirectory
    oms_setTLMPositionAndOrientation = (
        scripting.oms_setTLMPositionAndOrientation
    )
    oms_setTLMSocketData = scripting.oms_setTLMSocketData
    oms_setTolerance = scripting.oms_setTolerance
    oms_setVariableStepSize = scripting.oms_setVariableStepSize
    oms_setWorkingDirectory = scripting.oms_setWorkingDirectory
    oms_simulate = scripting.oms_simulate
    oms_stepUntil = scripting.oms_stepUntil
    oms_terminate = scripting.oms_terminate
    oms_getVersion = scripting.oms_getVersion

    @property
    def Experimental(self) -> scripting.Experimental[T_Calling]:
        return scripting.Experimental(self.__omc_interactive__)


class UsersGuide(package[T_Calling]):
    __omc_class__ = TypeName("OpenModelica.UsersGuide")

    @property
    def ReleaseNotes(self) -> usersGuide.ReleaseNotes[T_Calling]:
        return usersGuide.ReleaseNotes(self.__omc_interactive__)


class AutoCompletion(package[T_Calling]):
    __omc_class__ = TypeName("OpenModelica.AutoCompletion")

    @property
    def Annotations(self) -> autoCompletion.Annotations[T_Calling]:
        return autoCompletion.Annotations(self.__omc_interactive__)
