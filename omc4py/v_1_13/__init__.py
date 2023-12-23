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
    setCompilerFlags = openModelica.scripting.setCompilerFlags
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
    buildOpenTURNSInterface = openModelica.scripting.buildOpenTURNSInterface
    runOpenTURNSPythonScript = openModelica.scripting.runOpenTURNSPythonScript
    generateCode = openModelica.scripting.generateCode
    loadModel = openModelica.scripting.loadModel
    deleteFile = openModelica.scripting.deleteFile
    saveModel = openModelica.scripting.saveModel
    saveTotalModel = openModelica.scripting.saveTotalModel
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
    getInstantiatedParametersAndValues = (
        openModelica.scripting.getInstantiatedParametersAndValues
    )
    removeComponentModifiers = openModelica.scripting.removeComponentModifiers
    removeExtendsModifiers = openModelica.scripting.removeExtendsModifiers
    getConnectionCount = openModelica.scripting.getConnectionCount
    getNthConnection = openModelica.scripting.getNthConnection
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
    getUses = openModelica.scripting.getUses
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


Session = GenericSession[Synchronous]
AsyncSession = GenericSession[Asynchronous]
