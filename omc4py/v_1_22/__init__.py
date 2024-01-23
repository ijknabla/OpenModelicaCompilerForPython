from __future__ import annotations as _

from typing import TYPE_CHECKING

from omc4py.modelica import package
from omc4py.openmodelica import TypeName
from omc4py.protocol import Asynchronous, Synchronous, T_Calling
from omc4py.session import BasicSession

from . import OpenModelica as openModelica


class OpenModelica(package[T_Calling]):
    __omc_class__ = TypeName("OpenModelica")
    threadData = openModelica.threadData
    ThreadData = openModelica.ThreadData

    @property
    def Internal(self) -> openModelica.Internal[T_Calling]:
        return openModelica.Internal(self.__omc_interactive__)

    @property
    def Scripting(self) -> openModelica.Scripting[T_Calling]:
        return openModelica.Scripting(self.__omc_interactive__)

    @property
    def UsersGuide(self) -> openModelica.UsersGuide[T_Calling]:
        return openModelica.UsersGuide(self.__omc_interactive__)

    @property
    def AutoCompletion(self) -> openModelica.AutoCompletion[T_Calling]:
        return openModelica.AutoCompletion(self.__omc_interactive__)


class GenericSession(BasicSession[T_Calling]):
    if TYPE_CHECKING:

        @property
        def synchronous(self) -> GenericSession[Synchronous]:
            return ...  # type: ignore

        @property
        def asynchronous(self) -> GenericSession[Asynchronous]:
            return ...  # type: ignore

    @property
    def OpenModelica(self) -> OpenModelica[T_Calling]:
        return OpenModelica(self.__omc_interactive__)

    checkSettings = openModelica.scripting.checkSettings
    loadFile = openModelica.scripting.loadFile
    loadFiles = openModelica.scripting.loadFiles
    parseEncryptedPackage = openModelica.scripting.parseEncryptedPackage
    loadEncryptedPackage = openModelica.scripting.loadEncryptedPackage
    reloadClass = openModelica.scripting.reloadClass
    loadString = openModelica.scripting.loadString
    parseString = openModelica.scripting.parseString
    parseFile = openModelica.scripting.parseFile
    loadFileInteractiveQualified = (
        openModelica.scripting.loadFileInteractiveQualified
    )
    loadFileInteractive = openModelica.scripting.loadFileInteractive
    system = openModelica.scripting.system
    system_parallel = openModelica.scripting.system_parallel
    saveAll = openModelica.scripting.saveAll
    help = openModelica.scripting.help
    clear = openModelica.scripting.clear
    clearProgram = openModelica.scripting.clearProgram
    clearVariables = openModelica.scripting.clearVariables
    generateHeader = openModelica.scripting.generateHeader
    generateJuliaHeader = openModelica.scripting.generateJuliaHeader
    generateSeparateCode = openModelica.scripting.generateSeparateCode
    generateSeparateCodeDependencies = (
        openModelica.scripting.generateSeparateCodeDependencies
    )
    generateSeparateCodeDependenciesMakefile = (
        openModelica.scripting.generateSeparateCodeDependenciesMakefile
    )
    getLinker = openModelica.scripting.getLinker
    setLinker = openModelica.scripting.setLinker
    getLinkerFlags = openModelica.scripting.getLinkerFlags
    setLinkerFlags = openModelica.scripting.setLinkerFlags
    getCompiler = openModelica.scripting.getCompiler
    setCompiler = openModelica.scripting.setCompiler
    setCFlags = openModelica.scripting.setCFlags
    getCFlags = openModelica.scripting.getCFlags
    getCXXCompiler = openModelica.scripting.getCXXCompiler
    setCXXCompiler = openModelica.scripting.setCXXCompiler
    verifyCompiler = openModelica.scripting.verifyCompiler
    setCompilerPath = openModelica.scripting.setCompilerPath
    getCompileCommand = openModelica.scripting.getCompileCommand
    setCompileCommand = openModelica.scripting.setCompileCommand
    setPlotCommand = openModelica.scripting.setPlotCommand
    getSettings = openModelica.scripting.getSettings
    setTempDirectoryPath = openModelica.scripting.setTempDirectoryPath
    getTempDirectoryPath = openModelica.scripting.getTempDirectoryPath
    getEnvironmentVar = openModelica.scripting.getEnvironmentVar
    setEnvironmentVar = openModelica.scripting.setEnvironmentVar
    appendEnvironmentVar = openModelica.scripting.appendEnvironmentVar
    setInstallationDirectoryPath = (
        openModelica.scripting.setInstallationDirectoryPath
    )
    getInstallationDirectoryPath = (
        openModelica.scripting.getInstallationDirectoryPath
    )
    setModelicaPath = openModelica.scripting.setModelicaPath
    getModelicaPath = openModelica.scripting.getModelicaPath
    getHomeDirectoryPath = openModelica.scripting.getHomeDirectoryPath
    setCompilerFlags = openModelica.scripting.setCompilerFlags
    enableNewInstantiation = openModelica.scripting.enableNewInstantiation
    disableNewInstantiation = openModelica.scripting.disableNewInstantiation
    setDebugFlags = openModelica.scripting.setDebugFlags
    clearDebugFlags = openModelica.scripting.clearDebugFlags
    setPreOptModules = openModelica.scripting.setPreOptModules
    setCheapMatchingAlgorithm = (
        openModelica.scripting.setCheapMatchingAlgorithm
    )
    getMatchingAlgorithm = openModelica.scripting.getMatchingAlgorithm
    getAvailableMatchingAlgorithms = (
        openModelica.scripting.getAvailableMatchingAlgorithms
    )
    setMatchingAlgorithm = openModelica.scripting.setMatchingAlgorithm
    getIndexReductionMethod = openModelica.scripting.getIndexReductionMethod
    getAvailableIndexReductionMethods = (
        openModelica.scripting.getAvailableIndexReductionMethods
    )
    setIndexReductionMethod = openModelica.scripting.setIndexReductionMethod
    setPostOptModules = openModelica.scripting.setPostOptModules
    getTearingMethod = openModelica.scripting.getTearingMethod
    getAvailableTearingMethods = (
        openModelica.scripting.getAvailableTearingMethods
    )
    setTearingMethod = openModelica.scripting.setTearingMethod
    setCommandLineOptions = openModelica.scripting.setCommandLineOptions
    getCommandLineOptions = openModelica.scripting.getCommandLineOptions
    getConfigFlagValidOptions = (
        openModelica.scripting.getConfigFlagValidOptions
    )
    clearCommandLineOptions = openModelica.scripting.clearCommandLineOptions
    getVersion = openModelica.scripting.getVersion
    regularFileExists = openModelica.scripting.regularFileExists
    directoryExists = openModelica.scripting.directoryExists
    stat = openModelica.scripting.stat
    readFile = openModelica.scripting.readFile
    writeFile = openModelica.scripting.writeFile
    compareFilesAndMove = openModelica.scripting.compareFilesAndMove
    compareFiles = openModelica.scripting.compareFiles
    alarm = openModelica.scripting.alarm
    regex = openModelica.scripting.regex
    regexBool = openModelica.scripting.regexBool
    testsuiteFriendlyName = openModelica.scripting.testsuiteFriendlyName
    readFileNoNumeric = openModelica.scripting.readFileNoNumeric
    getErrorString = openModelica.scripting.getErrorString
    getMessagesString = openModelica.scripting.getMessagesString
    getMessagesStringInternal = (
        openModelica.scripting.getMessagesStringInternal
    )
    countMessages = openModelica.scripting.countMessages
    clearMessages = openModelica.scripting.clearMessages
    runScript = openModelica.scripting.runScript
    echo = openModelica.scripting.echo
    getClassesInModelicaPath = openModelica.scripting.getClassesInModelicaPath
    getAnnotationVersion = openModelica.scripting.getAnnotationVersion
    setAnnotationVersion = openModelica.scripting.setAnnotationVersion
    getNoSimplify = openModelica.scripting.getNoSimplify
    setNoSimplify = openModelica.scripting.setNoSimplify
    getVectorizationLimit = openModelica.scripting.getVectorizationLimit
    setVectorizationLimit = openModelica.scripting.setVectorizationLimit
    getDefaultOpenCLDevice = openModelica.scripting.getDefaultOpenCLDevice
    setDefaultOpenCLDevice = openModelica.scripting.setDefaultOpenCLDevice
    setShowAnnotations = openModelica.scripting.setShowAnnotations
    getShowAnnotations = openModelica.scripting.getShowAnnotations
    setOrderConnections = openModelica.scripting.setOrderConnections
    getOrderConnections = openModelica.scripting.getOrderConnections
    setLanguageStandard = openModelica.scripting.setLanguageStandard
    getLanguageStandard = openModelica.scripting.getLanguageStandard
    getAstAsCorbaString = openModelica.scripting.getAstAsCorbaString
    cd = openModelica.scripting.cd
    mkdir = openModelica.scripting.mkdir
    copy = openModelica.scripting.copy
    remove = openModelica.scripting.remove
    checkModel = openModelica.scripting.checkModel
    checkAllModelsRecursive = openModelica.scripting.checkAllModelsRecursive
    typeOf = openModelica.scripting.typeOf
    instantiateModel = openModelica.scripting.instantiateModel
    generateCode = openModelica.scripting.generateCode
    loadModel = openModelica.scripting.loadModel
    deleteFile = openModelica.scripting.deleteFile
    saveModel = openModelica.scripting.saveModel
    saveTotalModel = openModelica.scripting.saveTotalModel
    saveTotalModelDebug = openModelica.scripting.saveTotalModelDebug
    save = openModelica.scripting.save
    saveTotalSCode = openModelica.scripting.saveTotalSCode
    translateGraphics = openModelica.scripting.translateGraphics
    dumpXMLDAE = openModelica.scripting.dumpXMLDAE
    convertUnits = openModelica.scripting.convertUnits
    getDerivedUnits = openModelica.scripting.getDerivedUnits
    listVariables = openModelica.scripting.listVariables
    strtok = openModelica.scripting.strtok
    stringSplit = openModelica.scripting.stringSplit
    stringReplace = openModelica.scripting.stringReplace
    escapeXML = openModelica.scripting.escapeXML
    list = openModelica.scripting.list
    listFile = openModelica.scripting.listFile
    diffModelicaFileListings = openModelica.scripting.diffModelicaFileListings
    exportToFigaro = openModelica.scripting.exportToFigaro
    inferBindings = openModelica.scripting.inferBindings
    generateVerificationScenarios = (
        openModelica.scripting.generateVerificationScenarios
    )
    rewriteBlockCall = openModelica.scripting.rewriteBlockCall
    realpath = openModelica.scripting.realpath
    uriToFilename = openModelica.scripting.uriToFilename
    getLoadedLibraries = openModelica.scripting.getLoadedLibraries
    solveLinearSystem = openModelica.scripting.solveLinearSystem
    reopenStandardStream = openModelica.scripting.reopenStandardStream
    importFMU = openModelica.scripting.importFMU
    importFMUModelDescription = (
        openModelica.scripting.importFMUModelDescription
    )
    translateModelFMU = openModelica.scripting.translateModelFMU
    buildModelFMU = openModelica.scripting.buildModelFMU
    buildEncryptedPackage = openModelica.scripting.buildEncryptedPackage
    simulate = openModelica.scripting.simulate
    buildModel = openModelica.scripting.buildModel
    buildLabel = openModelica.scripting.buildLabel
    reduceTerms = openModelica.scripting.reduceTerms
    moveClass = openModelica.scripting.moveClass
    moveClassToTop = openModelica.scripting.moveClassToTop
    moveClassToBottom = openModelica.scripting.moveClassToBottom
    copyClass = openModelica.scripting.copyClass
    linearize = openModelica.scripting.linearize
    optimize = openModelica.scripting.optimize
    getSourceFile = openModelica.scripting.getSourceFile
    setSourceFile = openModelica.scripting.setSourceFile
    isShortDefinition = openModelica.scripting.isShortDefinition
    setClassComment = openModelica.scripting.setClassComment
    getClassNames = openModelica.scripting.getClassNames
    getUsedClassNames = openModelica.scripting.getUsedClassNames
    getPackages = openModelica.scripting.getPackages
    getAllSubtypeOf = openModelica.scripting.getAllSubtypeOf
    basePlotFunction = openModelica.scripting.basePlotFunction
    plot = openModelica.scripting.plot
    plotAll = openModelica.scripting.plotAll
    plotParametric = openModelica.scripting.plotParametric
    readSimulationResult = openModelica.scripting.readSimulationResult
    readSimulationResultSize = openModelica.scripting.readSimulationResultSize
    readSimulationResultVars = openModelica.scripting.readSimulationResultVars
    filterSimulationResults = openModelica.scripting.filterSimulationResults
    compareSimulationResults = openModelica.scripting.compareSimulationResults
    deltaSimulationResults = openModelica.scripting.deltaSimulationResults
    diffSimulationResults = openModelica.scripting.diffSimulationResults
    diffSimulationResultsHtml = (
        openModelica.scripting.diffSimulationResultsHtml
    )
    checkTaskGraph = openModelica.scripting.checkTaskGraph
    checkCodeGraph = openModelica.scripting.checkCodeGraph
    val = openModelica.scripting.val
    closeSimulationResultFile = (
        openModelica.scripting.closeSimulationResultFile
    )
    getParameterNames = openModelica.scripting.getParameterNames
    getParameterValue = openModelica.scripting.getParameterValue
    getComponentModifierNames = (
        openModelica.scripting.getComponentModifierNames
    )
    getComponentModifierValue = (
        openModelica.scripting.getComponentModifierValue
    )
    getComponentModifierValues = (
        openModelica.scripting.getComponentModifierValues
    )
    removeComponentModifiers = openModelica.scripting.removeComponentModifiers
    getElementModifierNames = openModelica.scripting.getElementModifierNames
    setComponentModifierValue = (
        openModelica.scripting.setComponentModifierValue
    )
    getElementModifierValue = openModelica.scripting.getElementModifierValue
    getElementModifierValues = openModelica.scripting.getElementModifierValues
    removeElementModifiers = openModelica.scripting.removeElementModifiers
    getElementAnnotation = openModelica.scripting.getElementAnnotation
    getInstantiatedParametersAndValues = (
        openModelica.scripting.getInstantiatedParametersAndValues
    )
    removeExtendsModifiers = openModelica.scripting.removeExtendsModifiers
    updateConnectionAnnotation = (
        openModelica.scripting.updateConnectionAnnotation
    )
    updateConnectionNames = openModelica.scripting.updateConnectionNames
    getConnectionCount = openModelica.scripting.getConnectionCount
    getNthConnection = openModelica.scripting.getNthConnection
    getConnectionList = openModelica.scripting.getConnectionList
    getAlgorithmCount = openModelica.scripting.getAlgorithmCount
    getNthAlgorithm = openModelica.scripting.getNthAlgorithm
    getInitialAlgorithmCount = openModelica.scripting.getInitialAlgorithmCount
    getNthInitialAlgorithm = openModelica.scripting.getNthInitialAlgorithm
    getAlgorithmItemsCount = openModelica.scripting.getAlgorithmItemsCount
    getNthAlgorithmItem = openModelica.scripting.getNthAlgorithmItem
    getInitialAlgorithmItemsCount = (
        openModelica.scripting.getInitialAlgorithmItemsCount
    )
    getNthInitialAlgorithmItem = (
        openModelica.scripting.getNthInitialAlgorithmItem
    )
    getEquationCount = openModelica.scripting.getEquationCount
    getNthEquation = openModelica.scripting.getNthEquation
    getInitialEquationCount = openModelica.scripting.getInitialEquationCount
    getNthInitialEquation = openModelica.scripting.getNthInitialEquation
    getEquationItemsCount = openModelica.scripting.getEquationItemsCount
    getNthEquationItem = openModelica.scripting.getNthEquationItem
    getInitialEquationItemsCount = (
        openModelica.scripting.getInitialEquationItemsCount
    )
    getNthInitialEquationItem = (
        openModelica.scripting.getNthInitialEquationItem
    )
    getAnnotationCount = openModelica.scripting.getAnnotationCount
    getNthAnnotationString = openModelica.scripting.getNthAnnotationString
    getImportCount = openModelica.scripting.getImportCount
    getMMfileTotalDependencies = (
        openModelica.scripting.getMMfileTotalDependencies
    )
    getImportedNames = openModelica.scripting.getImportedNames
    getNthImport = openModelica.scripting.getNthImport
    iconv = openModelica.scripting.iconv
    getDocumentationAnnotation = (
        openModelica.scripting.getDocumentationAnnotation
    )
    setDocumentationAnnotation = (
        openModelica.scripting.setDocumentationAnnotation
    )
    getTimeStamp = openModelica.scripting.getTimeStamp
    stringTypeName = openModelica.scripting.stringTypeName
    stringVariableName = openModelica.scripting.stringVariableName
    typeNameString = openModelica.scripting.typeNameString
    typeNameStrings = openModelica.scripting.typeNameStrings
    getClassComment = openModelica.scripting.getClassComment
    dirname = openModelica.scripting.dirname
    basename = openModelica.scripting.basename
    getClassRestriction = openModelica.scripting.getClassRestriction
    isType = openModelica.scripting.isType
    isPackage = openModelica.scripting.isPackage
    isClass = openModelica.scripting.isClass
    isRecord = openModelica.scripting.isRecord
    isBlock = openModelica.scripting.isBlock
    isFunction = openModelica.scripting.isFunction
    isPartial = openModelica.scripting.isPartial
    isReplaceable = openModelica.scripting.isReplaceable
    isRedeclare = openModelica.scripting.isRedeclare
    isModel = openModelica.scripting.isModel
    isConnector = openModelica.scripting.isConnector
    isOptimization = openModelica.scripting.isOptimization
    isEnumeration = openModelica.scripting.isEnumeration
    isOperator = openModelica.scripting.isOperator
    isOperatorRecord = openModelica.scripting.isOperatorRecord
    isOperatorFunction = openModelica.scripting.isOperatorFunction
    isProtectedClass = openModelica.scripting.isProtectedClass
    getBuiltinType = openModelica.scripting.getBuiltinType
    setInitXmlStartValue = openModelica.scripting.setInitXmlStartValue
    ngspicetoModelica = openModelica.scripting.ngspicetoModelica
    getInheritedClasses = openModelica.scripting.getInheritedClasses
    getComponentsTest = openModelica.scripting.getComponentsTest
    isExperiment = openModelica.scripting.isExperiment
    getSimulationOptions = openModelica.scripting.getSimulationOptions
    getAnnotationNamedModifiers = (
        openModelica.scripting.getAnnotationNamedModifiers
    )
    getAnnotationModifierValue = (
        openModelica.scripting.getAnnotationModifierValue
    )
    classAnnotationExists = openModelica.scripting.classAnnotationExists
    getBooleanClassAnnotation = (
        openModelica.scripting.getBooleanClassAnnotation
    )
    extendsFrom = openModelica.scripting.extendsFrom
    loadModelica3D = openModelica.scripting.loadModelica3D
    searchClassNames = openModelica.scripting.searchClassNames
    getAvailableLibraries = openModelica.scripting.getAvailableLibraries
    getAvailableLibraryVersions = (
        openModelica.scripting.getAvailableLibraryVersions
    )
    installPackage = openModelica.scripting.installPackage
    updatePackageIndex = openModelica.scripting.updatePackageIndex
    upgradeInstalledPackages = openModelica.scripting.upgradeInstalledPackages
    getAvailablePackageVersions = (
        openModelica.scripting.getAvailablePackageVersions
    )
    getAvailablePackageConversionsTo = (
        openModelica.scripting.getAvailablePackageConversionsTo
    )
    getAvailablePackageConversionsFrom = (
        openModelica.scripting.getAvailablePackageConversionsFrom
    )
    getUses = openModelica.scripting.getUses
    getConversionsFromVersions = (
        openModelica.scripting.getConversionsFromVersions
    )
    getDerivedClassModifierNames = (
        openModelica.scripting.getDerivedClassModifierNames
    )
    getDerivedClassModifierValue = (
        openModelica.scripting.getDerivedClassModifierValue
    )
    generateEntryPoint = openModelica.scripting.generateEntryPoint
    numProcessors = openModelica.scripting.numProcessors
    runScriptParallel = openModelica.scripting.runScriptParallel
    exit = openModelica.scripting.exit
    threadWorkFailed = openModelica.scripting.threadWorkFailed
    getMemorySize = openModelica.scripting.getMemorySize
    GC_gcollect_and_unmap = openModelica.scripting.GC_gcollect_and_unmap
    GC_expand_hp = openModelica.scripting.GC_expand_hp
    GC_set_max_heap_size = openModelica.scripting.GC_set_max_heap_size
    GC_get_prof_stats = openModelica.scripting.GC_get_prof_stats
    checkInterfaceOfPackages = openModelica.scripting.checkInterfaceOfPackages
    sortStrings = openModelica.scripting.sortStrings
    getClassInformation = openModelica.scripting.getClassInformation
    getTransitions = openModelica.scripting.getTransitions
    deleteTransition = openModelica.scripting.deleteTransition
    getInitialStates = openModelica.scripting.getInitialStates
    deleteInitialState = openModelica.scripting.deleteInitialState
    generateScriptingAPI = openModelica.scripting.generateScriptingAPI
    runConversionScript = openModelica.scripting.runConversionScript
    convertPackageToLibrary = openModelica.scripting.convertPackageToLibrary
    getModelInstance = openModelica.scripting.getModelInstance
    getModelInstanceAnnotation = (
        openModelica.scripting.getModelInstanceAnnotation
    )
    modifierToJSON = openModelica.scripting.modifierToJSON
    storeAST = openModelica.scripting.storeAST
    restoreAST = openModelica.scripting.restoreAST
    qualifyPath = openModelica.scripting.qualifyPath
    loadOMSimulator = openModelica.scripting.loadOMSimulator
    unloadOMSimulator = openModelica.scripting.unloadOMSimulator
    oms_addBus = openModelica.scripting.oms_addBus
    oms_addConnection = openModelica.scripting.oms_addConnection
    oms_addConnector = openModelica.scripting.oms_addConnector
    oms_addConnectorToBus = openModelica.scripting.oms_addConnectorToBus
    oms_addConnectorToTLMBus = openModelica.scripting.oms_addConnectorToTLMBus
    oms_addDynamicValueIndicator = (
        openModelica.scripting.oms_addDynamicValueIndicator
    )
    oms_addEventIndicator = openModelica.scripting.oms_addEventIndicator
    oms_addExternalModel = openModelica.scripting.oms_addExternalModel
    oms_addSignalsToResults = openModelica.scripting.oms_addSignalsToResults
    oms_addStaticValueIndicator = (
        openModelica.scripting.oms_addStaticValueIndicator
    )
    oms_addSubModel = openModelica.scripting.oms_addSubModel
    oms_addSystem = openModelica.scripting.oms_addSystem
    oms_addTimeIndicator = openModelica.scripting.oms_addTimeIndicator
    oms_addTLMBus = openModelica.scripting.oms_addTLMBus
    oms_addTLMConnection = openModelica.scripting.oms_addTLMConnection
    oms_compareSimulationResults = (
        openModelica.scripting.oms_compareSimulationResults
    )
    oms_copySystem = openModelica.scripting.oms_copySystem
    oms_delete = openModelica.scripting.oms_delete
    oms_deleteConnection = openModelica.scripting.oms_deleteConnection
    oms_deleteConnectorFromBus = (
        openModelica.scripting.oms_deleteConnectorFromBus
    )
    oms_deleteConnectorFromTLMBus = (
        openModelica.scripting.oms_deleteConnectorFromTLMBus
    )
    oms_export = openModelica.scripting.oms_export
    oms_exportDependencyGraphs = (
        openModelica.scripting.oms_exportDependencyGraphs
    )
    oms_exportSnapshot = openModelica.scripting.oms_exportSnapshot
    oms_extractFMIKind = openModelica.scripting.oms_extractFMIKind
    oms_getBoolean = openModelica.scripting.oms_getBoolean
    oms_getFixedStepSize = openModelica.scripting.oms_getFixedStepSize
    oms_getInteger = openModelica.scripting.oms_getInteger
    oms_getModelState = openModelica.scripting.oms_getModelState
    oms_getReal = openModelica.scripting.oms_getReal
    oms_getSolver = openModelica.scripting.oms_getSolver
    oms_getStartTime = openModelica.scripting.oms_getStartTime
    oms_getStopTime = openModelica.scripting.oms_getStopTime
    oms_getSubModelPath = openModelica.scripting.oms_getSubModelPath
    oms_getSystemType = openModelica.scripting.oms_getSystemType
    oms_getTolerance = openModelica.scripting.oms_getTolerance
    oms_getVariableStepSize = openModelica.scripting.oms_getVariableStepSize
    oms_faultInjection = openModelica.scripting.oms_faultInjection
    oms_importFile = openModelica.scripting.oms_importFile
    oms_importSnapshot = openModelica.scripting.oms_importSnapshot
    oms_initialize = openModelica.scripting.oms_initialize
    oms_instantiate = openModelica.scripting.oms_instantiate
    oms_list = openModelica.scripting.oms_list
    oms_listUnconnectedConnectors = (
        openModelica.scripting.oms_listUnconnectedConnectors
    )
    oms_loadSnapshot = openModelica.scripting.oms_loadSnapshot
    oms_newModel = openModelica.scripting.oms_newModel
    oms_removeSignalsFromResults = (
        openModelica.scripting.oms_removeSignalsFromResults
    )
    oms_rename = openModelica.scripting.oms_rename
    oms_reset = openModelica.scripting.oms_reset
    oms_RunFile = openModelica.scripting.oms_RunFile
    oms_setBoolean = openModelica.scripting.oms_setBoolean
    oms_setCommandLineOption = openModelica.scripting.oms_setCommandLineOption
    oms_setFixedStepSize = openModelica.scripting.oms_setFixedStepSize
    oms_setInteger = openModelica.scripting.oms_setInteger
    oms_setLogFile = openModelica.scripting.oms_setLogFile
    oms_setLoggingInterval = openModelica.scripting.oms_setLoggingInterval
    oms_setLoggingLevel = openModelica.scripting.oms_setLoggingLevel
    oms_setReal = openModelica.scripting.oms_setReal
    oms_setRealInputDerivative = (
        openModelica.scripting.oms_setRealInputDerivative
    )
    oms_setResultFile = openModelica.scripting.oms_setResultFile
    oms_setSignalFilter = openModelica.scripting.oms_setSignalFilter
    oms_setSolver = openModelica.scripting.oms_setSolver
    oms_setStartTime = openModelica.scripting.oms_setStartTime
    oms_setStopTime = openModelica.scripting.oms_setStopTime
    oms_setTempDirectory = openModelica.scripting.oms_setTempDirectory
    oms_setTLMPositionAndOrientation = (
        openModelica.scripting.oms_setTLMPositionAndOrientation
    )
    oms_setTLMSocketData = openModelica.scripting.oms_setTLMSocketData
    oms_setTolerance = openModelica.scripting.oms_setTolerance
    oms_setVariableStepSize = openModelica.scripting.oms_setVariableStepSize
    oms_setWorkingDirectory = openModelica.scripting.oms_setWorkingDirectory
    oms_simulate = openModelica.scripting.oms_simulate
    oms_stepUntil = openModelica.scripting.oms_stepUntil
    oms_terminate = openModelica.scripting.oms_terminate
    oms_getVersion = openModelica.scripting.oms_getVersion


Session = GenericSession[Synchronous]
AsyncSession = GenericSession[Asynchronous]
