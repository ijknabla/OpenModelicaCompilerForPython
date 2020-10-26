

# type: ignore
# flake8: noqa

import functools as functools__
import numpy as numpy__
from omc4py.primitive_types import (
    TypeName,
    VariableName,
)
from omc4py.types import OMCEnumeration as OMCEnumeration__
from omc4py.session import OMCSessionBase as OMCSessionBase__
from omc4py.session import OMCSession__open as OMCSession__open__
from omc4py.session import OMCSession__call as OMCSession__call__
from omc4py.session import cast_value as cast_value__
from omc4py.session import OMCSession__close as close_session
from omc4py.session.types import OMCRecord as OMCRecord__


class FileType(
    OMCEnumeration__
):
    __className__ = TypeName('OpenModelica.Scripting.Internal.FileType')

    NoFile = 1
    RegularFile = 2
    Directory = 3
    SpecialFile = 4


class ErrorKind(
    OMCEnumeration__
):
    __className__ = TypeName('OpenModelica.Scripting.ErrorKind')

    syntax = 1
    grammar = 2
    translation = 3
    symbolic = 4
    runtime = 5
    scripting = 6


class ErrorLevel(
    OMCEnumeration__
):
    __className__ = TypeName('OpenModelica.Scripting.ErrorLevel')

    notification = 1
    warning = 2
    error = 3


class ExportKind(
    OMCEnumeration__
):
    __className__ = TypeName('OpenModelica.Scripting.ExportKind')

    Absyn = 1
    SCode = 2
    MetaModelicaInterface = 3
    Internal = 4


class DiffFormat(
    OMCEnumeration__
):
    __className__ = TypeName('OpenModelica.Scripting.DiffFormat')

    plain = 1
    color = 2
    xml = 3


class LinearSystemSolver(
    OMCEnumeration__
):
    __className__ = TypeName('OpenModelica.Scripting.LinearSystemSolver')

    dgesv = 1
    lpsolve55 = 2


class StandardStream(
    OMCEnumeration__
):
    __className__ = TypeName('OpenModelica.Scripting.StandardStream')

    stdin = 1
    stdout = 2
    stderr = 3


class CheckSettingsResult(
    OMCRecord__,
):
    __recordName__ = TypeName('OpenModelica.Scripting.CheckSettingsResult')
    __fields__ = {
        'OPENMODELICAHOME': functools__.partial(
            cast_value__,
            name='OPENMODELICAHOME',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'OPENMODELICALIBRARY': functools__.partial(
            cast_value__,
            name='OPENMODELICALIBRARY',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'OMC_PATH': functools__.partial(
            cast_value__,
            name='OMC_PATH',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'SYSTEM_PATH': functools__.partial(
            cast_value__,
            name='SYSTEM_PATH',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'OMDEV_PATH': functools__.partial(
            cast_value__,
            name='OMDEV_PATH',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'OMC_FOUND': functools__.partial(
            cast_value__,
            name='OMC_FOUND',
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        ),
        'MODELICAUSERCFLAGS': functools__.partial(
            cast_value__,
            name='MODELICAUSERCFLAGS',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'WORKING_DIRECTORY': functools__.partial(
            cast_value__,
            name='WORKING_DIRECTORY',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'CREATE_FILE_WORKS': functools__.partial(
            cast_value__,
            name='CREATE_FILE_WORKS',
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        ),
        'REMOVE_FILE_WORKS': functools__.partial(
            cast_value__,
            name='REMOVE_FILE_WORKS',
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        ),
        'OS': functools__.partial(
            cast_value__,
            name='OS',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'SYSTEM_INFO': functools__.partial(
            cast_value__,
            name='SYSTEM_INFO',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'SENDDATALIBS': functools__.partial(
            cast_value__,
            name='SENDDATALIBS',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'C_COMPILER': functools__.partial(
            cast_value__,
            name='C_COMPILER',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'C_COMPILER_VERSION': functools__.partial(
            cast_value__,
            name='C_COMPILER_VERSION',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'C_COMPILER_RESPONDING': functools__.partial(
            cast_value__,
            name='C_COMPILER_RESPONDING',
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        ),
        'HAVE_CORBA': functools__.partial(
            cast_value__,
            name='HAVE_CORBA',
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        ),
        'CONFIGURE_CMDLINE': functools__.partial(
            cast_value__,
            name='CONFIGURE_CMDLINE',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
    }


class SourceInfo(
    OMCRecord__,
):
    __recordName__ = TypeName('OpenModelica.Scripting.SourceInfo')
    __fields__ = {
        'fileName': functools__.partial(
            cast_value__,
            name='fileName',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'readonly': functools__.partial(
            cast_value__,
            name='readonly',
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        ),
        'lineStart': functools__.partial(
            cast_value__,
            name='lineStart',
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        ),
        'columnStart': functools__.partial(
            cast_value__,
            name='columnStart',
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        ),
        'lineEnd': functools__.partial(
            cast_value__,
            name='lineEnd',
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        ),
        'columnEnd': functools__.partial(
            cast_value__,
            name='columnEnd',
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        ),
    }


class ErrorMessage(
    OMCRecord__,
):
    __recordName__ = TypeName('OpenModelica.Scripting.ErrorMessage')
    __fields__ = {
        'info': functools__.partial(
            cast_value__,
            name='info',
            optional=False,
            class_=SourceInfo,
            class_restrictions=SourceInfo,
            sizes=(),
        ),
        'message': functools__.partial(
            cast_value__,
            name='message',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'kind': functools__.partial(
            cast_value__,
            name='kind',
            optional=False,
            class_=ErrorKind,
            class_restrictions=ErrorKind,
            sizes=(),
        ),
        'level': functools__.partial(
            cast_value__,
            name='level',
            optional=False,
            class_=ErrorLevel,
            class_restrictions=ErrorLevel,
            sizes=(),
        ),
        'id': functools__.partial(
            cast_value__,
            name='id',
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        ),
    }


class SimulationResult(
    OMCRecord__,
):
    __recordName__ = TypeName('OpenModelica.Scripting.simulate.SimulationResult')
    __fields__ = {
        'resultFile': functools__.partial(
            cast_value__,
            name='resultFile',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'simulationOptions': functools__.partial(
            cast_value__,
            name='simulationOptions',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'messages': functools__.partial(
            cast_value__,
            name='messages',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'timeFrontend': functools__.partial(
            cast_value__,
            name='timeFrontend',
            optional=False,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        ),
        'timeBackend': functools__.partial(
            cast_value__,
            name='timeBackend',
            optional=False,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        ),
        'timeSimCode': functools__.partial(
            cast_value__,
            name='timeSimCode',
            optional=False,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        ),
        'timeTemplates': functools__.partial(
            cast_value__,
            name='timeTemplates',
            optional=False,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        ),
        'timeCompile': functools__.partial(
            cast_value__,
            name='timeCompile',
            optional=False,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        ),
        'timeSimulation': functools__.partial(
            cast_value__,
            name='timeSimulation',
            optional=False,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        ),
        'timeTotal': functools__.partial(
            cast_value__,
            name='timeTotal',
            optional=False,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        ),
    }


class Component(
    OMCRecord__,
):
    __recordName__ = TypeName('OpenModelica.Scripting.getComponentsTest.Component')
    __fields__ = {
        'className': functools__.partial(
            cast_value__,
            name='className',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'name': functools__.partial(
            cast_value__,
            name='name',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'comment': functools__.partial(
            cast_value__,
            name='comment',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'isProtected': functools__.partial(
            cast_value__,
            name='isProtected',
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        ),
        'isFinal': functools__.partial(
            cast_value__,
            name='isFinal',
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        ),
        'isFlow': functools__.partial(
            cast_value__,
            name='isFlow',
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        ),
        'isStream': functools__.partial(
            cast_value__,
            name='isStream',
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        ),
        'isReplaceable': functools__.partial(
            cast_value__,
            name='isReplaceable',
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        ),
        'variability': functools__.partial(
            cast_value__,
            name='variability',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'innerOuter': functools__.partial(
            cast_value__,
            name='innerOuter',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'inputOutput': functools__.partial(
            cast_value__,
            name='inputOutput',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        ),
        'dimensions': functools__.partial(
            cast_value__,
            name='dimensions',
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(None,),
        ),
    }


class GC_PROFSTATS(
    OMCRecord__,
):
    __recordName__ = TypeName('OpenModelica.Scripting.GC_PROFSTATS')
    __fields__ = {
        'heapsize_full': functools__.partial(
            cast_value__,
            name='heapsize_full',
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        ),
        'free_bytes_full': functools__.partial(
            cast_value__,
            name='free_bytes_full',
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        ),
        'unmapped_bytes': functools__.partial(
            cast_value__,
            name='unmapped_bytes',
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        ),
        'bytes_allocd_since_gc': functools__.partial(
            cast_value__,
            name='bytes_allocd_since_gc',
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        ),
        'allocd_bytes_before_gc': functools__.partial(
            cast_value__,
            name='allocd_bytes_before_gc',
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        ),
        'non_gc_bytes': functools__.partial(
            cast_value__,
            name='non_gc_bytes',
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        ),
        'gc_no': functools__.partial(
            cast_value__,
            name='gc_no',
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        ),
        'markers_m1': functools__.partial(
            cast_value__,
            name='markers_m1',
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        ),
        'bytes_reclaimed_since_gc': functools__.partial(
            cast_value__,
            name='bytes_reclaimed_since_gc',
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        ),
        'reclaimed_bytes_before_gc': functools__.partial(
            cast_value__,
            name='reclaimed_bytes_before_gc',
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        ),
    }



class OMCSession(
    OMCSessionBase__,
):
    def checkSettings(
        self,
    ):
        """
```modelica
function checkSettings
  output CheckSettingsResult result;
end checkSettings;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'checkSettings',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def loadFile(
        self,
        fileName,
        encoding=None,
        uses=None,
    ):
        """
```modelica
function loadFile
  input String fileName;
  input String encoding = "UTF-8";
  input Boolean uses = true;
  output Boolean success;
end loadFile;
```
        """
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        encoding__internal__ = cast_value__(
            name='encoding', value=encoding,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        uses__internal__ = cast_value__(
            name='uses', value=uses,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
        ]
        __kwrds = {
            'encoding': encoding__internal__,
            'uses': uses__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'loadFile',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def loadFiles(
        self,
        fileNames,
        encoding=None,
        numThreads=None,
    ):
        """
```modelica
function loadFiles
  input String[:] fileNames;
  input String encoding = "UTF-8";
  input Integer numThreads = OpenModelica.Scripting.numProcessors();
  output Boolean success;
end loadFiles;
```
        """
        # Argument check
        fileNames__internal__ = cast_value__(
            name='fileNames', value=fileNames,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(None,),
        )
        encoding__internal__ = cast_value__(
            name='encoding', value=encoding,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        numThreads__internal__ = cast_value__(
            name='numThreads', value=numThreads,
            optional=True,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileNames__internal__,
        ]
        __kwrds = {
            'encoding': encoding__internal__,
            'numThreads': numThreads__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'loadFiles',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def loadEncryptedPackage(
        self,
        fileName,
        workdir=None,
    ):
        """
```modelica
function loadEncryptedPackage
  input String fileName;
  input String workdir = "<default>" "The output directory for imported encrypted files. <default> will put the files to current working directory.";
  output Boolean success;
end loadEncryptedPackage;
```
        """
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        workdir__internal__ = cast_value__(
            name='workdir', value=workdir,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
        ]
        __kwrds = {
            'workdir': workdir__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'loadEncryptedPackage',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def reloadClass(
        self,
        name,
        encoding=None,
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
        # Argument check
        name__internal__ = cast_value__(
            name='name', value=name,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        encoding__internal__ = cast_value__(
            name='encoding', value=encoding,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            name__internal__,
        ]
        __kwrds = {
            'encoding': encoding__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'reloadClass',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def loadString(
        self,
        data,
        filename=None,
        encoding=None,
        merge=None,
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
        # Argument check
        data__internal__ = cast_value__(
            name='data', value=data,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        filename__internal__ = cast_value__(
            name='filename', value=filename,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        encoding__internal__ = cast_value__(
            name='encoding', value=encoding,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        merge__internal__ = cast_value__(
            name='merge', value=merge,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            data__internal__,
        ]
        __kwrds = {
            'filename': filename__internal__,
            'encoding': encoding__internal__,
            'merge': merge__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'loadString',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def parseString(
        self,
        data,
        filename=None,
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
        # Argument check
        data__internal__ = cast_value__(
            name='data', value=data,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        filename__internal__ = cast_value__(
            name='filename', value=filename,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            data__internal__,
        ]
        __kwrds = {
            'filename': filename__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'parseString',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def parseFile(
        self,
        filename,
        encoding=None,
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
        # Argument check
        filename__internal__ = cast_value__(
            name='filename', value=filename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        encoding__internal__ = cast_value__(
            name='encoding', value=encoding,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            filename__internal__,
        ]
        __kwrds = {
            'encoding': encoding__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'parseFile',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def loadFileInteractiveQualified(
        self,
        filename,
        encoding=None,
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
        # Argument check
        filename__internal__ = cast_value__(
            name='filename', value=filename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        encoding__internal__ = cast_value__(
            name='encoding', value=encoding,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            filename__internal__,
        ]
        __kwrds = {
            'encoding': encoding__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'loadFileInteractiveQualified',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def loadFileInteractive(
        self,
        filename,
        encoding=None,
    ):
        """
```modelica
function loadFileInteractive
  input String filename;
  input String encoding = "UTF-8";
  output TypeName names[:];
end loadFileInteractive;
```
        """
        # Argument check
        filename__internal__ = cast_value__(
            name='filename', value=filename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        encoding__internal__ = cast_value__(
            name='encoding', value=encoding,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            filename__internal__,
        ]
        __kwrds = {
            'encoding': encoding__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'loadFileInteractive',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def system(
        self,
        callStr,
        outputFile=None,
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
        # Argument check
        callStr__internal__ = cast_value__(
            name='callStr', value=callStr,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        outputFile__internal__ = cast_value__(
            name='outputFile', value=outputFile,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            callStr__internal__,
        ]
        __kwrds = {
            'outputFile': outputFile__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'system',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def system_parallel(
        self,
        callStr,
        numThreads=None,
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
        # Argument check
        callStr__internal__ = cast_value__(
            name='callStr', value=callStr,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(None,),
        )
        numThreads__internal__ = cast_value__(
            name='numThreads', value=numThreads,
            optional=True,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            callStr__internal__,
        ]
        __kwrds = {
            'numThreads': numThreads__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'system_parallel',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def saveAll(
        self,
        fileName,
    ):
        """
```modelica
function saveAll
  input String fileName;
  output Boolean success;
end saveAll;
```
        """
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'saveAll',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def help(
        self,
        topic=None,
    ):
        """
```modelica
function help
  input String topic = "topics";
  output String helpText;
end help;
```
        """
        # Argument check
        topic__internal__ = cast_value__(
            name='topic', value=topic,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
            'topic': topic__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'help',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def clear(
        self,
    ):
        """
```modelica
function clear
  output Boolean success;
end clear;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'clear',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def clearProgram(
        self,
    ):
        """
```modelica
function clearProgram
  output Boolean success;
end clearProgram;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'clearProgram',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def clearVariables(
        self,
    ):
        """
```modelica
function clearVariables
  output Boolean success;
end clearVariables;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'clearVariables',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def generateHeader(
        self,
        fileName,
    ):
        """
```modelica
function generateHeader
  input String fileName;
  output Boolean success;
end generateHeader;
```
        """
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'generateHeader',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def generateSeparateCode(
        self,
        className,
        cleanCache=None,
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
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        cleanCache__internal__ = cast_value__(
            name='cleanCache', value=cleanCache,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
            'cleanCache': cleanCache__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'generateSeparateCode',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def generateSeparateCodeDependencies(
        self,
        stampSuffix=None,
    ):
        """
```modelica
function generateSeparateCodeDependencies
  input String stampSuffix = ".c" "Suffix to add to dependencies (often .c.stamp)";
  output String[:] dependencies;
end generateSeparateCodeDependencies;
```
        """
        # Argument check
        stampSuffix__internal__ = cast_value__(
            name='stampSuffix', value=stampSuffix,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
            'stampSuffix': stampSuffix__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'generateSeparateCodeDependencies',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def generateSeparateCodeDependenciesMakefile(
        self,
        filename,
        directory=None,
        suffix=None,
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
        # Argument check
        filename__internal__ = cast_value__(
            name='filename', value=filename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        directory__internal__ = cast_value__(
            name='directory', value=directory,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        suffix__internal__ = cast_value__(
            name='suffix', value=suffix,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            filename__internal__,
        ]
        __kwrds = {
            'directory': directory__internal__,
            'suffix': suffix__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'generateSeparateCodeDependenciesMakefile',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getLinker(
        self,
    ):
        """
```modelica
function getLinker
  output String linker;
end getLinker;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getLinker',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setLinker(
        self,
        linker,
    ):
        """
```modelica
function setLinker
  input String linker;
  output Boolean success;
end setLinker;
```
        """
        # Argument check
        linker__internal__ = cast_value__(
            name='linker', value=linker,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            linker__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setLinker',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getLinkerFlags(
        self,
    ):
        """
```modelica
function getLinkerFlags
  output String linkerFlags;
end getLinkerFlags;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getLinkerFlags',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setLinkerFlags(
        self,
        linkerFlags,
    ):
        """
```modelica
function setLinkerFlags
  input String linkerFlags;
  output Boolean success;
end setLinkerFlags;
```
        """
        # Argument check
        linkerFlags__internal__ = cast_value__(
            name='linkerFlags', value=linkerFlags,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            linkerFlags__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setLinkerFlags',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getCompiler(
        self,
    ):
        """
```modelica
function getCompiler
  output String compiler;
end getCompiler;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getCompiler',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setCompiler(
        self,
        compiler,
    ):
        """
```modelica
function setCompiler
  input String compiler;
  output Boolean success;
end setCompiler;
```
        """
        # Argument check
        compiler__internal__ = cast_value__(
            name='compiler', value=compiler,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            compiler__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setCompiler',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setCFlags(
        self,
        inString,
    ):
        """
```modelica
function setCFlags
  input String inString;
  output Boolean success;
end setCFlags;
```
        """
        # Argument check
        inString__internal__ = cast_value__(
            name='inString', value=inString,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            inString__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setCFlags',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getCFlags(
        self,
    ):
        """
```modelica
function getCFlags
  output String outString;
end getCFlags;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getCFlags',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getCXXCompiler(
        self,
    ):
        """
```modelica
function getCXXCompiler
  output String compiler;
end getCXXCompiler;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getCXXCompiler',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setCXXCompiler(
        self,
        compiler,
    ):
        """
```modelica
function setCXXCompiler
  input String compiler;
  output Boolean success;
end setCXXCompiler;
```
        """
        # Argument check
        compiler__internal__ = cast_value__(
            name='compiler', value=compiler,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            compiler__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setCXXCompiler',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def verifyCompiler(
        self,
    ):
        """
```modelica
function verifyCompiler
  output Boolean compilerWorks;
end verifyCompiler;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'verifyCompiler',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setCompilerPath(
        self,
        compilerPath,
    ):
        """
```modelica
function setCompilerPath
  input String compilerPath;
  output Boolean success;
end setCompilerPath;
```
        """
        # Argument check
        compilerPath__internal__ = cast_value__(
            name='compilerPath', value=compilerPath,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            compilerPath__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setCompilerPath',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getCompileCommand(
        self,
    ):
        """
```modelica
function getCompileCommand
  output String compileCommand;
end getCompileCommand;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getCompileCommand',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setCompileCommand(
        self,
        compileCommand,
    ):
        """
```modelica
function setCompileCommand
  input String compileCommand;
  output Boolean success;
end setCompileCommand;
```
        """
        # Argument check
        compileCommand__internal__ = cast_value__(
            name='compileCommand', value=compileCommand,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            compileCommand__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setCompileCommand',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setPlotCommand(
        self,
        plotCommand,
    ):
        """
```modelica
function setPlotCommand
  input String plotCommand;
  output Boolean success;
end setPlotCommand;
```
        """
        # Argument check
        plotCommand__internal__ = cast_value__(
            name='plotCommand', value=plotCommand,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            plotCommand__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setPlotCommand',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getSettings(
        self,
    ):
        """
```modelica
function getSettings
  output String settings;
end getSettings;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getSettings',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setTempDirectoryPath(
        self,
        tempDirectoryPath,
    ):
        """
```modelica
function setTempDirectoryPath
  input String tempDirectoryPath;
  output Boolean success;
end setTempDirectoryPath;
```
        """
        # Argument check
        tempDirectoryPath__internal__ = cast_value__(
            name='tempDirectoryPath', value=tempDirectoryPath,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            tempDirectoryPath__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setTempDirectoryPath',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getTempDirectoryPath(
        self,
    ):
        """
```modelica
function getTempDirectoryPath
  output String tempDirectoryPath;
end getTempDirectoryPath;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getTempDirectoryPath',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getEnvironmentVar(
        self,
        var,
    ):
        """
```modelica
function getEnvironmentVar
  input String var;
  output String value "returns empty string on failure";
end getEnvironmentVar;
```
        """
        # Argument check
        var__internal__ = cast_value__(
            name='var', value=var,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            var__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getEnvironmentVar',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setEnvironmentVar(
        self,
        var,
        value,
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
        # Argument check
        var__internal__ = cast_value__(
            name='var', value=var,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        value__internal__ = cast_value__(
            name='value', value=value,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            var__internal__,
            value__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setEnvironmentVar',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def appendEnvironmentVar(
        self,
        var,
        value,
    ):
        """
```modelica
function appendEnvironmentVar
  input String var;
  input String value;
  output String result "returns \"error\" if the variable could not be appended";
end appendEnvironmentVar;
```
        """
        # Argument check
        var__internal__ = cast_value__(
            name='var', value=var,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        value__internal__ = cast_value__(
            name='value', value=value,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            var__internal__,
            value__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'appendEnvironmentVar',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setInstallationDirectoryPath(
        self,
        installationDirectoryPath,
    ):
        """
```modelica
function setInstallationDirectoryPath
  input String installationDirectoryPath;
  output Boolean success;
end setInstallationDirectoryPath;
```
        """
        # Argument check
        installationDirectoryPath__internal__ = cast_value__(
            name='installationDirectoryPath', value=installationDirectoryPath,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            installationDirectoryPath__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setInstallationDirectoryPath',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getInstallationDirectoryPath(
        self,
    ):
        """
```modelica
function getInstallationDirectoryPath
  output String installationDirectoryPath;
end getInstallationDirectoryPath;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getInstallationDirectoryPath',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setModelicaPath(
        self,
        modelicaPath,
    ):
        """
```modelica
function setModelicaPath
  input String modelicaPath;
  output Boolean success;
end setModelicaPath;
```
        """
        # Argument check
        modelicaPath__internal__ = cast_value__(
            name='modelicaPath', value=modelicaPath,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            modelicaPath__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setModelicaPath',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getModelicaPath(
        self,
    ):
        """
```modelica
function getModelicaPath
  output String modelicaPath;
end getModelicaPath;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getModelicaPath',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setCompilerFlags(
        self,
        compilerFlags,
    ):
        """
```modelica
function setCompilerFlags
  input String compilerFlags;
  output Boolean success;
end setCompilerFlags;
```
        """
        # Argument check
        compilerFlags__internal__ = cast_value__(
            name='compilerFlags', value=compilerFlags,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            compilerFlags__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setCompilerFlags',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setDebugFlags(
        self,
        debugFlags,
    ):
        """
```modelica
function setDebugFlags
  input String debugFlags;
  output Boolean success;
end setDebugFlags;
```
        """
        # Argument check
        debugFlags__internal__ = cast_value__(
            name='debugFlags', value=debugFlags,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            debugFlags__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setDebugFlags',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def clearDebugFlags(
        self,
    ):
        """
```modelica
function clearDebugFlags
  output Boolean success;
end clearDebugFlags;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'clearDebugFlags',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setPreOptModules(
        self,
        modules,
    ):
        """
```modelica
function setPreOptModules
  input String modules;
  output Boolean success;
end setPreOptModules;
```
        """
        # Argument check
        modules__internal__ = cast_value__(
            name='modules', value=modules,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            modules__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setPreOptModules',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setCheapMatchingAlgorithm(
        self,
        matchingAlgorithm,
    ):
        """
```modelica
function setCheapMatchingAlgorithm
  input Integer matchingAlgorithm;
  output Boolean success;
end setCheapMatchingAlgorithm;
```
        """
        # Argument check
        matchingAlgorithm__internal__ = cast_value__(
            name='matchingAlgorithm', value=matchingAlgorithm,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            matchingAlgorithm__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setCheapMatchingAlgorithm',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getMatchingAlgorithm(
        self,
    ):
        """
```modelica
function getMatchingAlgorithm
  output String selected;
end getMatchingAlgorithm;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getMatchingAlgorithm',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getAvailableMatchingAlgorithms(
        self,
    ):
        """
```modelica
function getAvailableMatchingAlgorithms
  output String[:] allChoices;
  output String[:] allComments;
end getAvailableMatchingAlgorithms;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getAvailableMatchingAlgorithms',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setMatchingAlgorithm(
        self,
        matchingAlgorithm,
    ):
        """
```modelica
function setMatchingAlgorithm
  input String matchingAlgorithm;
  output Boolean success;
end setMatchingAlgorithm;
```
        """
        # Argument check
        matchingAlgorithm__internal__ = cast_value__(
            name='matchingAlgorithm', value=matchingAlgorithm,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            matchingAlgorithm__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setMatchingAlgorithm',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getIndexReductionMethod(
        self,
    ):
        """
```modelica
function getIndexReductionMethod
  output String selected;
end getIndexReductionMethod;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getIndexReductionMethod',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getAvailableIndexReductionMethods(
        self,
    ):
        """
```modelica
function getAvailableIndexReductionMethods
  output String[:] allChoices;
  output String[:] allComments;
end getAvailableIndexReductionMethods;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getAvailableIndexReductionMethods',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setIndexReductionMethod(
        self,
        method,
    ):
        """
```modelica
function setIndexReductionMethod
  input String method;
  output Boolean success;
end setIndexReductionMethod;
```
        """
        # Argument check
        method__internal__ = cast_value__(
            name='method', value=method,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            method__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setIndexReductionMethod',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setPostOptModules(
        self,
        modules,
    ):
        """
```modelica
function setPostOptModules
  input String modules;
  output Boolean success;
end setPostOptModules;
```
        """
        # Argument check
        modules__internal__ = cast_value__(
            name='modules', value=modules,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            modules__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setPostOptModules',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getTearingMethod(
        self,
    ):
        """
```modelica
function getTearingMethod
  output String selected;
end getTearingMethod;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getTearingMethod',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getAvailableTearingMethods(
        self,
    ):
        """
```modelica
function getAvailableTearingMethods
  output String[:] allChoices;
  output String[:] allComments;
end getAvailableTearingMethods;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getAvailableTearingMethods',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setTearingMethod(
        self,
        tearingMethod,
    ):
        """
```modelica
function setTearingMethod
  input String tearingMethod;
  output Boolean success;
end setTearingMethod;
```
        """
        # Argument check
        tearingMethod__internal__ = cast_value__(
            name='tearingMethod', value=tearingMethod,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            tearingMethod__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setTearingMethod',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setCommandLineOptions(
        self,
        option,
    ):
        """
```modelica
function setCommandLineOptions
  input String option;
  output Boolean success;
end setCommandLineOptions;
```
        """
        # Argument check
        option__internal__ = cast_value__(
            name='option', value=option,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            option__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setCommandLineOptions',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getCommandLineOptions(
        self,
    ):
        """
```modelica
function getCommandLineOptions
  output String[:] flags;
end getCommandLineOptions;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getCommandLineOptions',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getConfigFlagValidOptions(
        self,
        flag,
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
        # Argument check
        flag__internal__ = cast_value__(
            name='flag', value=flag,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            flag__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getConfigFlagValidOptions',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def clearCommandLineOptions(
        self,
    ):
        """
```modelica
function clearCommandLineOptions
  output Boolean success;
end clearCommandLineOptions;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'clearCommandLineOptions',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getVersion(
        self,
        cl=None,
    ):
        """
```modelica
function getVersion
  input TypeName cl = $Code(OpenModelica);
  output String version;
end getVersion;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=True,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
            'cl': cl__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getVersion',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def regularFileExists(
        self,
        fileName,
    ):
        """
```modelica
function regularFileExists
  input String fileName;
  output Boolean exists;
end regularFileExists;
```
        """
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'regularFileExists',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def directoryExists(
        self,
        dirName,
    ):
        """
```modelica
function directoryExists
  input String dirName;
  output Boolean exists;
end directoryExists;
```
        """
        # Argument check
        dirName__internal__ = cast_value__(
            name='dirName', value=dirName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            dirName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'directoryExists',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def stat(
        self,
        fileName,
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
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'stat',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def readFile(
        self,
        fileName,
    ):
        """
```modelica
impure function readFile
  input String fileName;
  output String contents;
end readFile;
```
        """
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'readFile',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def writeFile(
        self,
        fileName,
        data,
        append=None,
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
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        data__internal__ = cast_value__(
            name='data', value=data,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        append__internal__ = cast_value__(
            name='append', value=append,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
            data__internal__,
        ]
        __kwrds = {
            'append': append__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'writeFile',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def compareFilesAndMove(
        self,
        newFile,
        oldFile,
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
        # Argument check
        newFile__internal__ = cast_value__(
            name='newFile', value=newFile,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        oldFile__internal__ = cast_value__(
            name='oldFile', value=oldFile,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            newFile__internal__,
            oldFile__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'compareFilesAndMove',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def compareFiles(
        self,
        file1,
        file2,
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
        # Argument check
        file1__internal__ = cast_value__(
            name='file1', value=file1,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        file2__internal__ = cast_value__(
            name='file2', value=file2,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            file1__internal__,
            file2__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'compareFiles',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def alarm(
        self,
        seconds,
    ):
        """
```modelica
impure function alarm
  input Integer seconds;
  output Integer previousSeconds;
end alarm;
```
        """
        # Argument check
        seconds__internal__ = cast_value__(
            name='seconds', value=seconds,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            seconds__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'alarm',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def regex(
        self,
        str,
        re,
        maxMatches=None,
        extended=None,
        caseInsensitive=None,
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
        # Argument check
        str__internal__ = cast_value__(
            name='str', value=str,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        re__internal__ = cast_value__(
            name='re', value=re,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        maxMatches__internal__ = cast_value__(
            name='maxMatches', value=maxMatches,
            optional=True,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )
        extended__internal__ = cast_value__(
            name='extended', value=extended,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        caseInsensitive__internal__ = cast_value__(
            name='caseInsensitive', value=caseInsensitive,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            str__internal__,
            re__internal__,
        ]
        __kwrds = {
            'maxMatches': maxMatches__internal__,
            'extended': extended__internal__,
            'caseInsensitive': caseInsensitive__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'regex',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def regexBool(
        self,
        str,
        re,
        extended=None,
        caseInsensitive=None,
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
        # Argument check
        str__internal__ = cast_value__(
            name='str', value=str,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        re__internal__ = cast_value__(
            name='re', value=re,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        extended__internal__ = cast_value__(
            name='extended', value=extended,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        caseInsensitive__internal__ = cast_value__(
            name='caseInsensitive', value=caseInsensitive,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            str__internal__,
            re__internal__,
        ]
        __kwrds = {
            'extended': extended__internal__,
            'caseInsensitive': caseInsensitive__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'regexBool',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def testsuiteFriendlyName(
        self,
        path,
    ):
        """
```modelica
function testsuiteFriendlyName
  input String path;
  output String fixed;
end testsuiteFriendlyName;
```
        """
        # Argument check
        path__internal__ = cast_value__(
            name='path', value=path,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            path__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'testsuiteFriendlyName',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def readFileNoNumeric(
        self,
        fileName,
    ):
        """
```modelica
function readFileNoNumeric
  input String fileName;
  output String contents;
end readFileNoNumeric;
```
        """
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'readFileNoNumeric',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getErrorString(
        self,
        warningsAsErrors=None,
    ):
        """
```modelica
impure function getErrorString
  input Boolean warningsAsErrors = false;
  output String errorString;
end getErrorString;
```
        """
        # Argument check
        warningsAsErrors__internal__ = cast_value__(
            name='warningsAsErrors', value=warningsAsErrors,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
            'warningsAsErrors': warningsAsErrors__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getErrorString',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getMessagesString(
        self,
    ):
        """
```modelica
function getMessagesString
  output String messagesString;
end getMessagesString;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getMessagesString',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getMessagesStringInternal(
        self,
        unique=None,
    ):
        """
```modelica
function getMessagesStringInternal
  input Boolean unique = true;
  output ErrorMessage[:] messagesString;
end getMessagesStringInternal;
```
        """
        # Argument check
        unique__internal__ = cast_value__(
            name='unique', value=unique,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
            'unique': unique__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getMessagesStringInternal',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def countMessages(
        self,
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
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'countMessages',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def clearMessages(
        self,
    ):
        """
```modelica
function clearMessages
  output Boolean success;
end clearMessages;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'clearMessages',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def runScript(
        self,
        fileName,
    ):
        """
```modelica
impure function runScript
  input String fileName "*.mos";
  output String result;
end runScript;
```
        """
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'runScript',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def echo(
        self,
        setEcho,
    ):
        """
```modelica
function echo
  input Boolean setEcho;
  output Boolean newEcho;
end echo;
```
        """
        # Argument check
        setEcho__internal__ = cast_value__(
            name='setEcho', value=setEcho,
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            setEcho__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'echo',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getClassesInModelicaPath(
        self,
    ):
        """
```modelica
function getClassesInModelicaPath
  output String classesInModelicaPath;
end getClassesInModelicaPath;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getClassesInModelicaPath',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getAnnotationVersion(
        self,
    ):
        """
```modelica
function getAnnotationVersion
  output String annotationVersion;
end getAnnotationVersion;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getAnnotationVersion',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setAnnotationVersion(
        self,
        annotationVersion,
    ):
        """
```modelica
function setAnnotationVersion
  input String annotationVersion;
  output Boolean success;
end setAnnotationVersion;
```
        """
        # Argument check
        annotationVersion__internal__ = cast_value__(
            name='annotationVersion', value=annotationVersion,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            annotationVersion__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setAnnotationVersion',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getNoSimplify(
        self,
    ):
        """
```modelica
function getNoSimplify
  output Boolean noSimplify;
end getNoSimplify;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getNoSimplify',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setNoSimplify(
        self,
        noSimplify,
    ):
        """
```modelica
function setNoSimplify
  input Boolean noSimplify;
  output Boolean success;
end setNoSimplify;
```
        """
        # Argument check
        noSimplify__internal__ = cast_value__(
            name='noSimplify', value=noSimplify,
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            noSimplify__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setNoSimplify',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getVectorizationLimit(
        self,
    ):
        """
```modelica
function getVectorizationLimit
  output Integer vectorizationLimit;
end getVectorizationLimit;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getVectorizationLimit',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setVectorizationLimit(
        self,
        vectorizationLimit,
    ):
        """
```modelica
function setVectorizationLimit
  input Integer vectorizationLimit;
  output Boolean success;
end setVectorizationLimit;
```
        """
        # Argument check
        vectorizationLimit__internal__ = cast_value__(
            name='vectorizationLimit', value=vectorizationLimit,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            vectorizationLimit__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setVectorizationLimit',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getDefaultOpenCLDevice(
        self,
    ):
        """
```modelica
function getDefaultOpenCLDevice
  output Integer defdevid;
end getDefaultOpenCLDevice;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getDefaultOpenCLDevice',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setDefaultOpenCLDevice(
        self,
        defdevid,
    ):
        """
```modelica
function setDefaultOpenCLDevice
  input Integer defdevid;
  output Boolean success;
end setDefaultOpenCLDevice;
```
        """
        # Argument check
        defdevid__internal__ = cast_value__(
            name='defdevid', value=defdevid,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            defdevid__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setDefaultOpenCLDevice',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setShowAnnotations(
        self,
        show,
    ):
        """
```modelica
function setShowAnnotations
  input Boolean show;
  output Boolean success;
end setShowAnnotations;
```
        """
        # Argument check
        show__internal__ = cast_value__(
            name='show', value=show,
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            show__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setShowAnnotations',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getShowAnnotations(
        self,
    ):
        """
```modelica
function getShowAnnotations
  output Boolean show;
end getShowAnnotations;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getShowAnnotations',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setOrderConnections(
        self,
        orderConnections,
    ):
        """
```modelica
function setOrderConnections
  input Boolean orderConnections;
  output Boolean success;
end setOrderConnections;
```
        """
        # Argument check
        orderConnections__internal__ = cast_value__(
            name='orderConnections', value=orderConnections,
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            orderConnections__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setOrderConnections',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getOrderConnections(
        self,
    ):
        """
```modelica
function getOrderConnections
  output Boolean orderConnections;
end getOrderConnections;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getOrderConnections',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setLanguageStandard(
        self,
        inVersion,
    ):
        """
```modelica
function setLanguageStandard
  input String inVersion;
  output Boolean success;
end setLanguageStandard;
```
        """
        # Argument check
        inVersion__internal__ = cast_value__(
            name='inVersion', value=inVersion,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            inVersion__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setLanguageStandard',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getLanguageStandard(
        self,
    ):
        """
```modelica
function getLanguageStandard
  output String outVersion;
end getLanguageStandard;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getLanguageStandard',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getAstAsCorbaString(
        self,
        fileName=None,
    ):
        """
```modelica
function getAstAsCorbaString
  input String fileName = "<interactive>";
  output String result "returns the string if fileName is interactive; else it returns ok or error depending on if writing the file succeeded";
end getAstAsCorbaString;
```
        """
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
            'fileName': fileName__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getAstAsCorbaString',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def cd(
        self,
        newWorkingDirectory=None,
    ):
        """
```modelica
function cd
  input String newWorkingDirectory = "";
  output String workingDirectory;
end cd;
```
        """
        # Argument check
        newWorkingDirectory__internal__ = cast_value__(
            name='newWorkingDirectory', value=newWorkingDirectory,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
            'newWorkingDirectory': newWorkingDirectory__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'cd',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def mkdir(
        self,
        newDirectory,
    ):
        """
```modelica
function mkdir
  input String newDirectory;
  output Boolean success;
end mkdir;
```
        """
        # Argument check
        newDirectory__internal__ = cast_value__(
            name='newDirectory', value=newDirectory,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            newDirectory__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'mkdir',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def copy(
        self,
        source,
        destination,
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
        # Argument check
        source__internal__ = cast_value__(
            name='source', value=source,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        destination__internal__ = cast_value__(
            name='destination', value=destination,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            source__internal__,
            destination__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'copy',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def remove(
        self,
        path,
    ):
        """
```modelica
function remove
  input String path;
  output Boolean success "Returns true on success.";
end remove;
```
        """
        # Argument check
        path__internal__ = cast_value__(
            name='path', value=path,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            path__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'remove',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def checkModel(
        self,
        className,
    ):
        """
```modelica
function checkModel
  input TypeName className;
  output String result;
end checkModel;
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'checkModel',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def checkAllModelsRecursive(
        self,
        className,
        checkProtected=None,
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
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        checkProtected__internal__ = cast_value__(
            name='checkProtected', value=checkProtected,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
            'checkProtected': checkProtected__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'checkAllModelsRecursive',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def typeOf(
        self,
        variableName,
    ):
        """
```modelica
function typeOf
  input VariableName variableName;
  output String result;
end typeOf;
```
        """
        # Argument check
        variableName__internal__ = cast_value__(
            name='variableName', value=variableName,
            optional=False,
            class_=VariableName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            variableName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'typeOf',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def instantiateModel(
        self,
        className,
    ):
        """
```modelica
function instantiateModel
  input TypeName className;
  output String result;
end instantiateModel;
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'instantiateModel',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def buildOpenTURNSInterface(
        self,
        className,
        pythonTemplateFile,
        showFlatModelica=None,
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
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        pythonTemplateFile__internal__ = cast_value__(
            name='pythonTemplateFile', value=pythonTemplateFile,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        showFlatModelica__internal__ = cast_value__(
            name='showFlatModelica', value=showFlatModelica,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
            pythonTemplateFile__internal__,
        ]
        __kwrds = {
            'showFlatModelica': showFlatModelica__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'buildOpenTURNSInterface',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def runOpenTURNSPythonScript(
        self,
        pythonScriptFile,
    ):
        """
```modelica
function runOpenTURNSPythonScript
  input String pythonScriptFile;
  output String logOutputFile;
end runOpenTURNSPythonScript;
```
        """
        # Argument check
        pythonScriptFile__internal__ = cast_value__(
            name='pythonScriptFile', value=pythonScriptFile,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            pythonScriptFile__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'runOpenTURNSPythonScript',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def generateCode(
        self,
        className,
    ):
        """
```modelica
function generateCode
  input TypeName className;
  output Boolean success;
end generateCode;
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'generateCode',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def loadModel(
        self,
        className,
        priorityVersion=None,
        notify=None,
        languageStandard=None,
        requireExactVersion=None,
    ):
        """
```modelica
function loadModel
  input TypeName className;
  input String[:] priorityVersion = {"default"};
  input Boolean notify = false "Give a notification of the libraries and versions that were loaded";
  input String languageStandard = "" "Override the set language standard. Parse with the given setting, but do not change it permanently.";
  input Boolean requireExactVersion = false "If the version is required to be exact, if there is a uses Modelica(version=\"3.2\"), Modelica 3.2.1 will not match it.";
  output Boolean success;
end loadModel;
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        priorityVersion__internal__ = cast_value__(
            name='priorityVersion', value=priorityVersion,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(None,),
        )
        notify__internal__ = cast_value__(
            name='notify', value=notify,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        languageStandard__internal__ = cast_value__(
            name='languageStandard', value=languageStandard,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        requireExactVersion__internal__ = cast_value__(
            name='requireExactVersion', value=requireExactVersion,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
            'priorityVersion': priorityVersion__internal__,
            'notify': notify__internal__,
            'languageStandard': languageStandard__internal__,
            'requireExactVersion': requireExactVersion__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'loadModel',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def deleteFile(
        self,
        fileName,
    ):
        """
```modelica
function deleteFile
  input String fileName;
  output Boolean success;
end deleteFile;
```
        """
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'deleteFile',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def saveModel(
        self,
        fileName,
        className,
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
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
            className__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'saveModel',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def saveTotalModel(
        self,
        fileName,
        className,
        stripAnnotations=None,
        stripComments=None,
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
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        stripAnnotations__internal__ = cast_value__(
            name='stripAnnotations', value=stripAnnotations,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        stripComments__internal__ = cast_value__(
            name='stripComments', value=stripComments,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
            className__internal__,
        ]
        __kwrds = {
            'stripAnnotations': stripAnnotations__internal__,
            'stripComments': stripComments__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'saveTotalModel',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def save(
        self,
        className,
    ):
        """
```modelica
function save
  input TypeName className;
  output Boolean success;
end save;
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'save',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    saveTotalSCode = saveTotalModel

    def translateGraphics(
        self,
        className,
    ):
        """
```modelica
function translateGraphics
  input TypeName className;
  output String result;
end translateGraphics;
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'translateGraphics',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def dumpXMLDAE(
        self,
        className,
        translationLevel=None,
        addOriginalIncidenceMatrix=None,
        addSolvingInfo=None,
        addMathMLCode=None,
        dumpResiduals=None,
        fileNamePrefix=None,
        rewriteRulesFile=None,
    ):
        """
```modelica
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
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        translationLevel__internal__ = cast_value__(
            name='translationLevel', value=translationLevel,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        addOriginalIncidenceMatrix__internal__ = cast_value__(
            name='addOriginalIncidenceMatrix', value=addOriginalIncidenceMatrix,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        addSolvingInfo__internal__ = cast_value__(
            name='addSolvingInfo', value=addSolvingInfo,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        addMathMLCode__internal__ = cast_value__(
            name='addMathMLCode', value=addMathMLCode,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        dumpResiduals__internal__ = cast_value__(
            name='dumpResiduals', value=dumpResiduals,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        fileNamePrefix__internal__ = cast_value__(
            name='fileNamePrefix', value=fileNamePrefix,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        rewriteRulesFile__internal__ = cast_value__(
            name='rewriteRulesFile', value=rewriteRulesFile,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
            'translationLevel': translationLevel__internal__,
            'addOriginalIncidenceMatrix': addOriginalIncidenceMatrix__internal__,
            'addSolvingInfo': addSolvingInfo__internal__,
            'addMathMLCode': addMathMLCode__internal__,
            'dumpResiduals': dumpResiduals__internal__,
            'fileNamePrefix': fileNamePrefix__internal__,
            'rewriteRulesFile': rewriteRulesFile__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'dumpXMLDAE',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def convertUnits(
        self,
        s1,
        s2,
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
        # Argument check
        s1__internal__ = cast_value__(
            name='s1', value=s1,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        s2__internal__ = cast_value__(
            name='s2', value=s2,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            s1__internal__,
            s2__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'convertUnits',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getDerivedUnits(
        self,
        baseUnit,
    ):
        """
```modelica
function getDerivedUnits
  input String baseUnit;
  output String[:] derivedUnits;
end getDerivedUnits;
```
        """
        # Argument check
        baseUnit__internal__ = cast_value__(
            name='baseUnit', value=baseUnit,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            baseUnit__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getDerivedUnits',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def listVariables(
        self,
    ):
        """
```modelica
function listVariables
  output TypeName variables[:];
end listVariables;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'listVariables',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def strtok(
        self,
        string,
        token,
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
        # Argument check
        string__internal__ = cast_value__(
            name='string', value=string,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        token__internal__ = cast_value__(
            name='token', value=token,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            string__internal__,
            token__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'strtok',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def stringSplit(
        self,
        string,
        token,
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
        # Argument check
        string__internal__ = cast_value__(
            name='string', value=string,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        token__internal__ = cast_value__(
            name='token', value=token,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            string__internal__,
            token__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'stringSplit',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def stringReplace(
        self,
        str,
        source,
        target,
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
        # Argument check
        str__internal__ = cast_value__(
            name='str', value=str,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        source__internal__ = cast_value__(
            name='source', value=source,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        target__internal__ = cast_value__(
            name='target', value=target,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            str__internal__,
            source__internal__,
            target__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'stringReplace',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def escapeXML(
        self,
        inStr,
    ):
        """
```modelica
function escapeXML
  input String inStr;
  output String outStr;
end escapeXML;
```
        """
        # Argument check
        inStr__internal__ = cast_value__(
            name='inStr', value=inStr,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            inStr__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'escapeXML',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def list(
        self,
        class_=None,
        interfaceOnly=None,
        shortOnly=None,
        exportKind=None,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=True,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        interfaceOnly__internal__ = cast_value__(
            name='interfaceOnly', value=interfaceOnly,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        shortOnly__internal__ = cast_value__(
            name='shortOnly', value=shortOnly,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        exportKind__internal__ = cast_value__(
            name='exportKind', value=exportKind,
            optional=True,
            class_=ExportKind,
            class_restrictions=ExportKind,
            sizes=(),
        )

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
            'class_': class___internal__,
            'interfaceOnly': interfaceOnly__internal__,
            'shortOnly': shortOnly__internal__,
            'exportKind': exportKind__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'list',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def listFile(
        self,
        class_,
    ):
        """
```modelica
function listFile
  input TypeName class_;
  output String contents;
end listFile;
```
        """
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'listFile',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def diffModelicaFileListings(
        self,
        before,
        after,
        diffFormat=None,
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
        # Argument check
        before__internal__ = cast_value__(
            name='before', value=before,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        after__internal__ = cast_value__(
            name='after', value=after,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        diffFormat__internal__ = cast_value__(
            name='diffFormat', value=diffFormat,
            optional=True,
            class_=DiffFormat,
            class_restrictions=DiffFormat,
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            before__internal__,
            after__internal__,
        ]
        __kwrds = {
            'diffFormat': diffFormat__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'diffModelicaFileListings',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def exportToFigaro(
        self,
        path,
        database,
        mode,
        options,
        processor,
        directory=None,
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
        # Argument check
        path__internal__ = cast_value__(
            name='path', value=path,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        directory__internal__ = cast_value__(
            name='directory', value=directory,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        database__internal__ = cast_value__(
            name='database', value=database,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        mode__internal__ = cast_value__(
            name='mode', value=mode,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        options__internal__ = cast_value__(
            name='options', value=options,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        processor__internal__ = cast_value__(
            name='processor', value=processor,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            path__internal__,
        ]
        __kwrds = {
            'directory': directory__internal__,
            'database': database__internal__,
            'mode': mode__internal__,
            'options': options__internal__,
            'processor': processor__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'exportToFigaro',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def inferBindings(
        self,
        path,
    ):
        """
```modelica
function inferBindings
  input TypeName path;
  output Boolean success;
end inferBindings;
```
        """
        # Argument check
        path__internal__ = cast_value__(
            name='path', value=path,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            path__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'inferBindings',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def generateVerificationScenarios(
        self,
        path,
    ):
        """
```modelica
function generateVerificationScenarios
  input TypeName path;
  output Boolean success;
end generateVerificationScenarios;
```
        """
        # Argument check
        path__internal__ = cast_value__(
            name='path', value=path,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            path__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'generateVerificationScenarios',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def rewriteBlockCall(
        self,
        className,
        inDefs,
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
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        inDefs__internal__ = cast_value__(
            name='inDefs', value=inDefs,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
            inDefs__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'rewriteBlockCall',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def realpath(
        self,
        name,
    ):
        """
```modelica
function realpath
  input String name "Absolute or relative file or directory name";
  output String fullName "Full path of 'name'";
end realpath;
```
        """
        # Argument check
        name__internal__ = cast_value__(
            name='name', value=name,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            name__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'realpath',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def uriToFilename(
        self,
        uri,
    ):
        """
```modelica
function uriToFilename
  input String uri;
  output String filename = "";
end uriToFilename;
```
        """
        # Argument check
        uri__internal__ = cast_value__(
            name='uri', value=uri,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            uri__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'uriToFilename',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getLoadedLibraries(
        self,
    ):
        """
```modelica
function getLoadedLibraries
  output String[:, 2] libraries;
end getLoadedLibraries;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getLoadedLibraries',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def solveLinearSystem(
        self,
        A,
        B,
        solver=None,
        isInt=None,
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
        # Argument check
        A__internal__ = cast_value__(
            name='A', value=A,
            optional=False,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(None, None),
        )
        B__internal__ = cast_value__(
            name='B', value=B,
            optional=False,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(None,),
        )
        solver__internal__ = cast_value__(
            name='solver', value=solver,
            optional=True,
            class_=LinearSystemSolver,
            class_restrictions=LinearSystemSolver,
            sizes=(),
        )
        isInt__internal__ = cast_value__(
            name='isInt', value=isInt,
            optional=True,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(None,),
        )

        # Pack positional arguments
        __args = [
            A__internal__,
            B__internal__,
        ]
        __kwrds = {
            'solver': solver__internal__,
            'isInt': isInt__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'solveLinearSystem',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def reopenStandardStream(
        self,
        _stream,
        filename,
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
        # Argument check
        _stream__internal__ = cast_value__(
            name='_stream', value=_stream,
            optional=False,
            class_=StandardStream,
            class_restrictions=StandardStream,
            sizes=(),
        )
        filename__internal__ = cast_value__(
            name='filename', value=filename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            _stream__internal__,
            filename__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'reopenStandardStream',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def importFMU(
        self,
        filename,
        workdir=None,
        loglevel=None,
        fullPath=None,
        debugLogging=None,
        generateInputConnectors=None,
        generateOutputConnectors=None,
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
        # Argument check
        filename__internal__ = cast_value__(
            name='filename', value=filename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        workdir__internal__ = cast_value__(
            name='workdir', value=workdir,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        loglevel__internal__ = cast_value__(
            name='loglevel', value=loglevel,
            optional=True,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )
        fullPath__internal__ = cast_value__(
            name='fullPath', value=fullPath,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        debugLogging__internal__ = cast_value__(
            name='debugLogging', value=debugLogging,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        generateInputConnectors__internal__ = cast_value__(
            name='generateInputConnectors', value=generateInputConnectors,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        generateOutputConnectors__internal__ = cast_value__(
            name='generateOutputConnectors', value=generateOutputConnectors,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            filename__internal__,
        ]
        __kwrds = {
            'workdir': workdir__internal__,
            'loglevel': loglevel__internal__,
            'fullPath': fullPath__internal__,
            'debugLogging': debugLogging__internal__,
            'generateInputConnectors': generateInputConnectors__internal__,
            'generateOutputConnectors': generateOutputConnectors__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'importFMU',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def importFMUModelDescription(
        self,
        filename,
        workdir=None,
        loglevel=None,
        fullPath=None,
        debugLogging=None,
        generateInputConnectors=None,
        generateOutputConnectors=None,
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
        # Argument check
        filename__internal__ = cast_value__(
            name='filename', value=filename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        workdir__internal__ = cast_value__(
            name='workdir', value=workdir,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        loglevel__internal__ = cast_value__(
            name='loglevel', value=loglevel,
            optional=True,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )
        fullPath__internal__ = cast_value__(
            name='fullPath', value=fullPath,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        debugLogging__internal__ = cast_value__(
            name='debugLogging', value=debugLogging,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        generateInputConnectors__internal__ = cast_value__(
            name='generateInputConnectors', value=generateInputConnectors,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        generateOutputConnectors__internal__ = cast_value__(
            name='generateOutputConnectors', value=generateOutputConnectors,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            filename__internal__,
        ]
        __kwrds = {
            'workdir': workdir__internal__,
            'loglevel': loglevel__internal__,
            'fullPath': fullPath__internal__,
            'debugLogging': debugLogging__internal__,
            'generateInputConnectors': generateInputConnectors__internal__,
            'generateOutputConnectors': generateOutputConnectors__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'importFMUModelDescription',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def translateModelFMU(
        self,
        className,
        version=None,
        fmuType=None,
        fileNamePrefix=None,
        includeResources=None,
    ):
        """
```modelica
function translateModelFMU
  input TypeName className "the class that should translated";
  input String version = "2.0" "FMU version, 1.0 or 2.0.";
  input String fmuType = "me" "FMU type, me (model exchange), cs (co-simulation), me_cs (both model exchange and co-simulation)";
  input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \"className\"";
  input Boolean includeResources = false "include Modelica based resources via loadResource or not";
  output String generatedFileName "Returns the full path of the generated FMU.";
end translateModelFMU;
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        version__internal__ = cast_value__(
            name='version', value=version,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        fmuType__internal__ = cast_value__(
            name='fmuType', value=fmuType,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        fileNamePrefix__internal__ = cast_value__(
            name='fileNamePrefix', value=fileNamePrefix,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        includeResources__internal__ = cast_value__(
            name='includeResources', value=includeResources,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
            'version': version__internal__,
            'fmuType': fmuType__internal__,
            'fileNamePrefix': fileNamePrefix__internal__,
            'includeResources': includeResources__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'translateModelFMU',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def buildModelFMU(
        self,
        className,
        version=None,
        fmuType=None,
        fileNamePrefix=None,
        platforms=None,
        includeResources=None,
    ):
        """
```modelica
function buildModelFMU
  input TypeName className "the class that should translated";
  input String version = "2.0" "FMU version, 1.0 or 2.0.";
  input String fmuType = "me" "FMU type, me (model exchange), cs (co-simulation), me_cs (both model exchange and co-simulation)";
  input String fileNamePrefix = "<default>" "fileNamePrefix. <default> = \"className\"";
  input String platforms[:] = {"static"} "The list of platforms to generate code for. \"dynamic\"=current platform, dynamically link the runtime. \"static\"=current platform, statically link everything. Else, use a host triple, e.g. \"x86_64-linux-gnu\" or \"x86_64-w64-mingw32\"";
  input Boolean includeResources = false "include Modelica based resources via loadResource or not";
  output String generatedFileName "Returns the full path of the generated FMU.";
end buildModelFMU;
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        version__internal__ = cast_value__(
            name='version', value=version,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        fmuType__internal__ = cast_value__(
            name='fmuType', value=fmuType,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        fileNamePrefix__internal__ = cast_value__(
            name='fileNamePrefix', value=fileNamePrefix,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        platforms__internal__ = cast_value__(
            name='platforms', value=platforms,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(None,),
        )
        includeResources__internal__ = cast_value__(
            name='includeResources', value=includeResources,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
            'version': version__internal__,
            'fmuType': fmuType__internal__,
            'fileNamePrefix': fileNamePrefix__internal__,
            'platforms': platforms__internal__,
            'includeResources': includeResources__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'buildModelFMU',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def buildEncryptedPackage(
        self,
        className,
    ):
        """
```modelica
function buildEncryptedPackage
  input TypeName className "the class that should encrypted";
  output Boolean success;
  output String commandOutput "Output of the packagetool executable";
end buildEncryptedPackage;
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'buildEncryptedPackage',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def simulate(
        self,
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
        """
```modelica
function simulate
  input TypeName className "the class that should simulated";
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
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        startTime__internal__ = cast_value__(
            name='startTime', value=startTime,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        stopTime__internal__ = cast_value__(
            name='stopTime', value=stopTime,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        numberOfIntervals__internal__ = cast_value__(
            name='numberOfIntervals', value=numberOfIntervals,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        tolerance__internal__ = cast_value__(
            name='tolerance', value=tolerance,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        method__internal__ = cast_value__(
            name='method', value=method,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        fileNamePrefix__internal__ = cast_value__(
            name='fileNamePrefix', value=fileNamePrefix,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        options__internal__ = cast_value__(
            name='options', value=options,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        outputFormat__internal__ = cast_value__(
            name='outputFormat', value=outputFormat,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        variableFilter__internal__ = cast_value__(
            name='variableFilter', value=variableFilter,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        cflags__internal__ = cast_value__(
            name='cflags', value=cflags,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        simflags__internal__ = cast_value__(
            name='simflags', value=simflags,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
            'startTime': startTime__internal__,
            'stopTime': stopTime__internal__,
            'numberOfIntervals': numberOfIntervals__internal__,
            'tolerance': tolerance__internal__,
            'method': method__internal__,
            'fileNamePrefix': fileNamePrefix__internal__,
            'options': options__internal__,
            'outputFormat': outputFormat__internal__,
            'variableFilter': variableFilter__internal__,
            'cflags': cflags__internal__,
            'simflags': simflags__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'simulate',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def buildModel(
        self,
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
        """
```modelica
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
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        startTime__internal__ = cast_value__(
            name='startTime', value=startTime,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        stopTime__internal__ = cast_value__(
            name='stopTime', value=stopTime,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        numberOfIntervals__internal__ = cast_value__(
            name='numberOfIntervals', value=numberOfIntervals,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        tolerance__internal__ = cast_value__(
            name='tolerance', value=tolerance,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        method__internal__ = cast_value__(
            name='method', value=method,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        fileNamePrefix__internal__ = cast_value__(
            name='fileNamePrefix', value=fileNamePrefix,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        options__internal__ = cast_value__(
            name='options', value=options,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        outputFormat__internal__ = cast_value__(
            name='outputFormat', value=outputFormat,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        variableFilter__internal__ = cast_value__(
            name='variableFilter', value=variableFilter,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        cflags__internal__ = cast_value__(
            name='cflags', value=cflags,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        simflags__internal__ = cast_value__(
            name='simflags', value=simflags,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
            'startTime': startTime__internal__,
            'stopTime': stopTime__internal__,
            'numberOfIntervals': numberOfIntervals__internal__,
            'tolerance': tolerance__internal__,
            'method': method__internal__,
            'fileNamePrefix': fileNamePrefix__internal__,
            'options': options__internal__,
            'outputFormat': outputFormat__internal__,
            'variableFilter': variableFilter__internal__,
            'cflags': cflags__internal__,
            'simflags': simflags__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'buildModel',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def buildLabel(
        self,
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
        """
```modelica
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
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        startTime__internal__ = cast_value__(
            name='startTime', value=startTime,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        stopTime__internal__ = cast_value__(
            name='stopTime', value=stopTime,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        numberOfIntervals__internal__ = cast_value__(
            name='numberOfIntervals', value=numberOfIntervals,
            optional=True,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )
        tolerance__internal__ = cast_value__(
            name='tolerance', value=tolerance,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        method__internal__ = cast_value__(
            name='method', value=method,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        fileNamePrefix__internal__ = cast_value__(
            name='fileNamePrefix', value=fileNamePrefix,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        options__internal__ = cast_value__(
            name='options', value=options,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        outputFormat__internal__ = cast_value__(
            name='outputFormat', value=outputFormat,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        variableFilter__internal__ = cast_value__(
            name='variableFilter', value=variableFilter,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        cflags__internal__ = cast_value__(
            name='cflags', value=cflags,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        simflags__internal__ = cast_value__(
            name='simflags', value=simflags,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
            'startTime': startTime__internal__,
            'stopTime': stopTime__internal__,
            'numberOfIntervals': numberOfIntervals__internal__,
            'tolerance': tolerance__internal__,
            'method': method__internal__,
            'fileNamePrefix': fileNamePrefix__internal__,
            'options': options__internal__,
            'outputFormat': outputFormat__internal__,
            'variableFilter': variableFilter__internal__,
            'cflags': cflags__internal__,
            'simflags': simflags__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'buildLabel',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def reduceTerms(
        self,
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
        """
```modelica
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
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        startTime__internal__ = cast_value__(
            name='startTime', value=startTime,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        stopTime__internal__ = cast_value__(
            name='stopTime', value=stopTime,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        numberOfIntervals__internal__ = cast_value__(
            name='numberOfIntervals', value=numberOfIntervals,
            optional=True,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )
        tolerance__internal__ = cast_value__(
            name='tolerance', value=tolerance,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        method__internal__ = cast_value__(
            name='method', value=method,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        fileNamePrefix__internal__ = cast_value__(
            name='fileNamePrefix', value=fileNamePrefix,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        options__internal__ = cast_value__(
            name='options', value=options,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        outputFormat__internal__ = cast_value__(
            name='outputFormat', value=outputFormat,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        variableFilter__internal__ = cast_value__(
            name='variableFilter', value=variableFilter,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        cflags__internal__ = cast_value__(
            name='cflags', value=cflags,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        simflags__internal__ = cast_value__(
            name='simflags', value=simflags,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        labelstoCancel__internal__ = cast_value__(
            name='labelstoCancel', value=labelstoCancel,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
            'startTime': startTime__internal__,
            'stopTime': stopTime__internal__,
            'numberOfIntervals': numberOfIntervals__internal__,
            'tolerance': tolerance__internal__,
            'method': method__internal__,
            'fileNamePrefix': fileNamePrefix__internal__,
            'options': options__internal__,
            'outputFormat': outputFormat__internal__,
            'variableFilter': variableFilter__internal__,
            'cflags': cflags__internal__,
            'simflags': simflags__internal__,
            'labelstoCancel': labelstoCancel__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'reduceTerms',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def moveClass(
        self,
        className,
        offset,
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
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        offset__internal__ = cast_value__(
            name='offset', value=offset,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
            offset__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'moveClass',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def moveClassToTop(
        self,
        className,
    ):
        """
```modelica
function moveClassToTop
  input TypeName className;
  output Boolean result;
end moveClassToTop;
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'moveClassToTop',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def moveClassToBottom(
        self,
        className,
    ):
        """
```modelica
function moveClassToBottom
  input TypeName className;
  output Boolean result;
end moveClassToBottom;
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'moveClassToBottom',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def copyClass(
        self,
        className,
        newClassName,
        withIn=None,
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
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        newClassName__internal__ = cast_value__(
            name='newClassName', value=newClassName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        withIn__internal__ = cast_value__(
            name='withIn', value=withIn,
            optional=True,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
            newClassName__internal__,
        ]
        __kwrds = {
            'withIn': withIn__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'copyClass',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def linearize(
        self,
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
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        startTime__internal__ = cast_value__(
            name='startTime', value=startTime,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        stopTime__internal__ = cast_value__(
            name='stopTime', value=stopTime,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        numberOfIntervals__internal__ = cast_value__(
            name='numberOfIntervals', value=numberOfIntervals,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        stepSize__internal__ = cast_value__(
            name='stepSize', value=stepSize,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        tolerance__internal__ = cast_value__(
            name='tolerance', value=tolerance,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        method__internal__ = cast_value__(
            name='method', value=method,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        fileNamePrefix__internal__ = cast_value__(
            name='fileNamePrefix', value=fileNamePrefix,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        storeInTemp__internal__ = cast_value__(
            name='storeInTemp', value=storeInTemp,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        noClean__internal__ = cast_value__(
            name='noClean', value=noClean,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        options__internal__ = cast_value__(
            name='options', value=options,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        outputFormat__internal__ = cast_value__(
            name='outputFormat', value=outputFormat,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        variableFilter__internal__ = cast_value__(
            name='variableFilter', value=variableFilter,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        cflags__internal__ = cast_value__(
            name='cflags', value=cflags,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        simflags__internal__ = cast_value__(
            name='simflags', value=simflags,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
            'startTime': startTime__internal__,
            'stopTime': stopTime__internal__,
            'numberOfIntervals': numberOfIntervals__internal__,
            'stepSize': stepSize__internal__,
            'tolerance': tolerance__internal__,
            'method': method__internal__,
            'fileNamePrefix': fileNamePrefix__internal__,
            'storeInTemp': storeInTemp__internal__,
            'noClean': noClean__internal__,
            'options': options__internal__,
            'outputFormat': outputFormat__internal__,
            'variableFilter': variableFilter__internal__,
            'cflags': cflags__internal__,
            'simflags': simflags__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'linearize',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def optimize(
        self,
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
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        startTime__internal__ = cast_value__(
            name='startTime', value=startTime,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        stopTime__internal__ = cast_value__(
            name='stopTime', value=stopTime,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        numberOfIntervals__internal__ = cast_value__(
            name='numberOfIntervals', value=numberOfIntervals,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        stepSize__internal__ = cast_value__(
            name='stepSize', value=stepSize,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        tolerance__internal__ = cast_value__(
            name='tolerance', value=tolerance,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        method__internal__ = cast_value__(
            name='method', value=method,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        fileNamePrefix__internal__ = cast_value__(
            name='fileNamePrefix', value=fileNamePrefix,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        storeInTemp__internal__ = cast_value__(
            name='storeInTemp', value=storeInTemp,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        noClean__internal__ = cast_value__(
            name='noClean', value=noClean,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        options__internal__ = cast_value__(
            name='options', value=options,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        outputFormat__internal__ = cast_value__(
            name='outputFormat', value=outputFormat,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        variableFilter__internal__ = cast_value__(
            name='variableFilter', value=variableFilter,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        cflags__internal__ = cast_value__(
            name='cflags', value=cflags,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        simflags__internal__ = cast_value__(
            name='simflags', value=simflags,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
            'startTime': startTime__internal__,
            'stopTime': stopTime__internal__,
            'numberOfIntervals': numberOfIntervals__internal__,
            'stepSize': stepSize__internal__,
            'tolerance': tolerance__internal__,
            'method': method__internal__,
            'fileNamePrefix': fileNamePrefix__internal__,
            'storeInTemp': storeInTemp__internal__,
            'noClean': noClean__internal__,
            'options': options__internal__,
            'outputFormat': outputFormat__internal__,
            'variableFilter': variableFilter__internal__,
            'cflags': cflags__internal__,
            'simflags': simflags__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'optimize',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getSourceFile(
        self,
        class_,
    ):
        """
```modelica
function getSourceFile
  input TypeName class_;
  output String filename "empty on failure";
end getSourceFile;
```
        """
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getSourceFile',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setSourceFile(
        self,
        class_,
        filename,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        filename__internal__ = cast_value__(
            name='filename', value=filename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            filename__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setSourceFile',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isShortDefinition(
        self,
        class_,
    ):
        """
```modelica
function isShortDefinition
  input TypeName class_;
  output Boolean isShortCls;
end isShortDefinition;
```
        """
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isShortDefinition',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setClassComment(
        self,
        class_,
        filename,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        filename__internal__ = cast_value__(
            name='filename', value=filename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            filename__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setClassComment',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getClassNames(
        self,
        class_=None,
        recursive=None,
        qualified=None,
        sort=None,
        builtin=None,
        showProtected=None,
        includeConstants=None,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=True,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        recursive__internal__ = cast_value__(
            name='recursive', value=recursive,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        qualified__internal__ = cast_value__(
            name='qualified', value=qualified,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        sort__internal__ = cast_value__(
            name='sort', value=sort,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        builtin__internal__ = cast_value__(
            name='builtin', value=builtin,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        showProtected__internal__ = cast_value__(
            name='showProtected', value=showProtected,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        includeConstants__internal__ = cast_value__(
            name='includeConstants', value=includeConstants,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
            'class_': class___internal__,
            'recursive': recursive__internal__,
            'qualified': qualified__internal__,
            'sort': sort__internal__,
            'builtin': builtin__internal__,
            'showProtected': showProtected__internal__,
            'includeConstants': includeConstants__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getClassNames',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getUsedClassNames(
        self,
        className,
    ):
        """
```modelica
function getUsedClassNames
  input TypeName className;
  output TypeName classNames[:];
end getUsedClassNames;
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getUsedClassNames',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getPackages(
        self,
        class_=None,
    ):
        """
```modelica
function getPackages
  input TypeName class_ = $Code(AllLoadedClasses);
  output TypeName classNames[:];
end getPackages;
```
        """
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=True,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
            'class_': class___internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getPackages',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def basePlotFunction(
        self,
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
        """
```modelica
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
```
        """
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        interpolation__internal__ = cast_value__(
            name='interpolation', value=interpolation,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        title__internal__ = cast_value__(
            name='title', value=title,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        legend__internal__ = cast_value__(
            name='legend', value=legend,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        grid__internal__ = cast_value__(
            name='grid', value=grid,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        logX__internal__ = cast_value__(
            name='logX', value=logX,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        logY__internal__ = cast_value__(
            name='logY', value=logY,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        xLabel__internal__ = cast_value__(
            name='xLabel', value=xLabel,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        yLabel__internal__ = cast_value__(
            name='yLabel', value=yLabel,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        points__internal__ = cast_value__(
            name='points', value=points,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        xRange__internal__ = cast_value__(
            name='xRange', value=xRange,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(2,),
        )
        yRange__internal__ = cast_value__(
            name='yRange', value=yRange,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(2,),
        )

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
            'fileName': fileName__internal__,
            'interpolation': interpolation__internal__,
            'title': title__internal__,
            'legend': legend__internal__,
            'grid': grid__internal__,
            'logX': logX__internal__,
            'logY': logY__internal__,
            'xLabel': xLabel__internal__,
            'yLabel': yLabel__internal__,
            'points': points__internal__,
            'xRange': xRange__internal__,
            'yRange': yRange__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'basePlotFunction',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def plot(
        self,
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
        # Argument check
        vars__internal__ = cast_value__(
            name='vars', value=vars,
            optional=False,
            class_=VariableName,
            class_restrictions=(),
            sizes=(None,),
        )
        externalWindow__internal__ = cast_value__(
            name='externalWindow', value=externalWindow,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        title__internal__ = cast_value__(
            name='title', value=title,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        grid__internal__ = cast_value__(
            name='grid', value=grid,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        logX__internal__ = cast_value__(
            name='logX', value=logX,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        logY__internal__ = cast_value__(
            name='logY', value=logY,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        xLabel__internal__ = cast_value__(
            name='xLabel', value=xLabel,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        yLabel__internal__ = cast_value__(
            name='yLabel', value=yLabel,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        xRange__internal__ = cast_value__(
            name='xRange', value=xRange,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(2,),
        )
        yRange__internal__ = cast_value__(
            name='yRange', value=yRange,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(2,),
        )
        curveWidth__internal__ = cast_value__(
            name='curveWidth', value=curveWidth,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        curveStyle__internal__ = cast_value__(
            name='curveStyle', value=curveStyle,
            optional=True,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )
        legendPosition__internal__ = cast_value__(
            name='legendPosition', value=legendPosition,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        footer__internal__ = cast_value__(
            name='footer', value=footer,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        autoScale__internal__ = cast_value__(
            name='autoScale', value=autoScale,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        forceOMPlot__internal__ = cast_value__(
            name='forceOMPlot', value=forceOMPlot,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            vars__internal__,
        ]
        __kwrds = {
            'externalWindow': externalWindow__internal__,
            'fileName': fileName__internal__,
            'title': title__internal__,
            'grid': grid__internal__,
            'logX': logX__internal__,
            'logY': logY__internal__,
            'xLabel': xLabel__internal__,
            'yLabel': yLabel__internal__,
            'xRange': xRange__internal__,
            'yRange': yRange__internal__,
            'curveWidth': curveWidth__internal__,
            'curveStyle': curveStyle__internal__,
            'legendPosition': legendPosition__internal__,
            'footer': footer__internal__,
            'autoScale': autoScale__internal__,
            'forceOMPlot': forceOMPlot__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'plot',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def plotAll(
        self,
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
        # Argument check
        externalWindow__internal__ = cast_value__(
            name='externalWindow', value=externalWindow,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        title__internal__ = cast_value__(
            name='title', value=title,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        grid__internal__ = cast_value__(
            name='grid', value=grid,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        logX__internal__ = cast_value__(
            name='logX', value=logX,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        logY__internal__ = cast_value__(
            name='logY', value=logY,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        xLabel__internal__ = cast_value__(
            name='xLabel', value=xLabel,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        yLabel__internal__ = cast_value__(
            name='yLabel', value=yLabel,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        xRange__internal__ = cast_value__(
            name='xRange', value=xRange,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(2,),
        )
        yRange__internal__ = cast_value__(
            name='yRange', value=yRange,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(2,),
        )
        curveWidth__internal__ = cast_value__(
            name='curveWidth', value=curveWidth,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        curveStyle__internal__ = cast_value__(
            name='curveStyle', value=curveStyle,
            optional=True,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )
        legendPosition__internal__ = cast_value__(
            name='legendPosition', value=legendPosition,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        footer__internal__ = cast_value__(
            name='footer', value=footer,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        autoScale__internal__ = cast_value__(
            name='autoScale', value=autoScale,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        forceOMPlot__internal__ = cast_value__(
            name='forceOMPlot', value=forceOMPlot,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
            'externalWindow': externalWindow__internal__,
            'fileName': fileName__internal__,
            'title': title__internal__,
            'grid': grid__internal__,
            'logX': logX__internal__,
            'logY': logY__internal__,
            'xLabel': xLabel__internal__,
            'yLabel': yLabel__internal__,
            'xRange': xRange__internal__,
            'yRange': yRange__internal__,
            'curveWidth': curveWidth__internal__,
            'curveStyle': curveStyle__internal__,
            'legendPosition': legendPosition__internal__,
            'footer': footer__internal__,
            'autoScale': autoScale__internal__,
            'forceOMPlot': forceOMPlot__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'plotAll',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def plotParametric(
        self,
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
        # Argument check
        xVariable__internal__ = cast_value__(
            name='xVariable', value=xVariable,
            optional=False,
            class_=VariableName,
            class_restrictions=(),
            sizes=(),
        )
        yVariable__internal__ = cast_value__(
            name='yVariable', value=yVariable,
            optional=False,
            class_=VariableName,
            class_restrictions=(),
            sizes=(),
        )
        externalWindow__internal__ = cast_value__(
            name='externalWindow', value=externalWindow,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        title__internal__ = cast_value__(
            name='title', value=title,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        grid__internal__ = cast_value__(
            name='grid', value=grid,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        logX__internal__ = cast_value__(
            name='logX', value=logX,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        logY__internal__ = cast_value__(
            name='logY', value=logY,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        xLabel__internal__ = cast_value__(
            name='xLabel', value=xLabel,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        yLabel__internal__ = cast_value__(
            name='yLabel', value=yLabel,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        xRange__internal__ = cast_value__(
            name='xRange', value=xRange,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(2,),
        )
        yRange__internal__ = cast_value__(
            name='yRange', value=yRange,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(2,),
        )
        curveWidth__internal__ = cast_value__(
            name='curveWidth', value=curveWidth,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        curveStyle__internal__ = cast_value__(
            name='curveStyle', value=curveStyle,
            optional=True,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )
        legendPosition__internal__ = cast_value__(
            name='legendPosition', value=legendPosition,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        footer__internal__ = cast_value__(
            name='footer', value=footer,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        autoScale__internal__ = cast_value__(
            name='autoScale', value=autoScale,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        forceOMPlot__internal__ = cast_value__(
            name='forceOMPlot', value=forceOMPlot,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            xVariable__internal__,
            yVariable__internal__,
        ]
        __kwrds = {
            'externalWindow': externalWindow__internal__,
            'fileName': fileName__internal__,
            'title': title__internal__,
            'grid': grid__internal__,
            'logX': logX__internal__,
            'logY': logY__internal__,
            'xLabel': xLabel__internal__,
            'yLabel': yLabel__internal__,
            'xRange': xRange__internal__,
            'yRange': yRange__internal__,
            'curveWidth': curveWidth__internal__,
            'curveStyle': curveStyle__internal__,
            'legendPosition': legendPosition__internal__,
            'footer': footer__internal__,
            'autoScale': autoScale__internal__,
            'forceOMPlot': forceOMPlot__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'plotParametric',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def readSimulationResult(
        self,
        filename,
        variables,
        size=None,
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
        # Argument check
        filename__internal__ = cast_value__(
            name='filename', value=filename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        variables__internal__ = cast_value__(
            name='variables', value=variables,
            optional=False,
            class_=VariableName,
            class_restrictions=(),
            sizes=(None,),
        )
        size__internal__ = cast_value__(
            name='size', value=size,
            optional=True,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            filename__internal__,
            variables__internal__,
        ]
        __kwrds = {
            'size': size__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'readSimulationResult',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def readSimulationResultSize(
        self,
        fileName,
    ):
        """
```modelica
function readSimulationResultSize
  input String fileName;
  output Integer sz;
end readSimulationResultSize;
```
        """
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'readSimulationResultSize',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def readSimulationResultVars(
        self,
        fileName,
        readParameters=None,
        openmodelicaStyle=None,
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
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        readParameters__internal__ = cast_value__(
            name='readParameters', value=readParameters,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        openmodelicaStyle__internal__ = cast_value__(
            name='openmodelicaStyle', value=openmodelicaStyle,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
        ]
        __kwrds = {
            'readParameters': readParameters__internal__,
            'openmodelicaStyle': openmodelicaStyle__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'readSimulationResultVars',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def filterSimulationResults(
        self,
        inFile,
        outFile,
        vars,
        numberOfIntervals=None,
        removeDescription=None,
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
        # Argument check
        inFile__internal__ = cast_value__(
            name='inFile', value=inFile,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        outFile__internal__ = cast_value__(
            name='outFile', value=outFile,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        vars__internal__ = cast_value__(
            name='vars', value=vars,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(None,),
        )
        numberOfIntervals__internal__ = cast_value__(
            name='numberOfIntervals', value=numberOfIntervals,
            optional=True,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )
        removeDescription__internal__ = cast_value__(
            name='removeDescription', value=removeDescription,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            inFile__internal__,
            outFile__internal__,
            vars__internal__,
        ]
        __kwrds = {
            'numberOfIntervals': numberOfIntervals__internal__,
            'removeDescription': removeDescription__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'filterSimulationResults',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def compareSimulationResults(
        self,
        filename,
        reffilename,
        logfilename,
        relTol=None,
        absTol=None,
        vars=None,
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
        # Argument check
        filename__internal__ = cast_value__(
            name='filename', value=filename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        reffilename__internal__ = cast_value__(
            name='reffilename', value=reffilename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        logfilename__internal__ = cast_value__(
            name='logfilename', value=logfilename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        relTol__internal__ = cast_value__(
            name='relTol', value=relTol,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        absTol__internal__ = cast_value__(
            name='absTol', value=absTol,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        vars__internal__ = cast_value__(
            name='vars', value=vars,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(None,),
        )

        # Pack positional arguments
        __args = [
            filename__internal__,
            reffilename__internal__,
            logfilename__internal__,
        ]
        __kwrds = {
            'relTol': relTol__internal__,
            'absTol': absTol__internal__,
            'vars': vars__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'compareSimulationResults',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def deltaSimulationResults(
        self,
        filename,
        reffilename,
        method,
        vars=None,
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
        # Argument check
        filename__internal__ = cast_value__(
            name='filename', value=filename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        reffilename__internal__ = cast_value__(
            name='reffilename', value=reffilename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        method__internal__ = cast_value__(
            name='method', value=method,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        vars__internal__ = cast_value__(
            name='vars', value=vars,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(None,),
        )

        # Pack positional arguments
        __args = [
            filename__internal__,
            reffilename__internal__,
            method__internal__,
        ]
        __kwrds = {
            'vars': vars__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'deltaSimulationResults',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def diffSimulationResults(
        self,
        actualFile,
        expectedFile,
        diffPrefix,
        relTol=None,
        relTolDiffMinMax=None,
        rangeDelta=None,
        vars=None,
        keepEqualResults=None,
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
        # Argument check
        actualFile__internal__ = cast_value__(
            name='actualFile', value=actualFile,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        expectedFile__internal__ = cast_value__(
            name='expectedFile', value=expectedFile,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        diffPrefix__internal__ = cast_value__(
            name='diffPrefix', value=diffPrefix,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        relTol__internal__ = cast_value__(
            name='relTol', value=relTol,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        relTolDiffMinMax__internal__ = cast_value__(
            name='relTolDiffMinMax', value=relTolDiffMinMax,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        rangeDelta__internal__ = cast_value__(
            name='rangeDelta', value=rangeDelta,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        vars__internal__ = cast_value__(
            name='vars', value=vars,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(None,),
        )
        keepEqualResults__internal__ = cast_value__(
            name='keepEqualResults', value=keepEqualResults,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            actualFile__internal__,
            expectedFile__internal__,
            diffPrefix__internal__,
        ]
        __kwrds = {
            'relTol': relTol__internal__,
            'relTolDiffMinMax': relTolDiffMinMax__internal__,
            'rangeDelta': rangeDelta__internal__,
            'vars': vars__internal__,
            'keepEqualResults': keepEqualResults__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'diffSimulationResults',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def diffSimulationResultsHtml(
        self,
        var,
        actualFile,
        expectedFile,
        relTol=None,
        relTolDiffMinMax=None,
        rangeDelta=None,
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
        # Argument check
        var__internal__ = cast_value__(
            name='var', value=var,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        actualFile__internal__ = cast_value__(
            name='actualFile', value=actualFile,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        expectedFile__internal__ = cast_value__(
            name='expectedFile', value=expectedFile,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        relTol__internal__ = cast_value__(
            name='relTol', value=relTol,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        relTolDiffMinMax__internal__ = cast_value__(
            name='relTolDiffMinMax', value=relTolDiffMinMax,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        rangeDelta__internal__ = cast_value__(
            name='rangeDelta', value=rangeDelta,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            var__internal__,
            actualFile__internal__,
            expectedFile__internal__,
        ]
        __kwrds = {
            'relTol': relTol__internal__,
            'relTolDiffMinMax': relTolDiffMinMax__internal__,
            'rangeDelta': rangeDelta__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'diffSimulationResultsHtml',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def checkTaskGraph(
        self,
        filename,
        reffilename,
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
        # Argument check
        filename__internal__ = cast_value__(
            name='filename', value=filename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        reffilename__internal__ = cast_value__(
            name='reffilename', value=reffilename,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            filename__internal__,
            reffilename__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'checkTaskGraph',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def checkCodeGraph(
        self,
        graphfile,
        codefile,
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
        # Argument check
        graphfile__internal__ = cast_value__(
            name='graphfile', value=graphfile,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        codefile__internal__ = cast_value__(
            name='codefile', value=codefile,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            graphfile__internal__,
            codefile__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'checkCodeGraph',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def val(
        self,
        var,
        timePoint=None,
        fileName=None,
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
        # Argument check
        var__internal__ = cast_value__(
            name='var', value=var,
            optional=False,
            class_=VariableName,
            class_restrictions=(),
            sizes=(),
        )
        timePoint__internal__ = cast_value__(
            name='timePoint', value=timePoint,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            var__internal__,
        ]
        __kwrds = {
            'timePoint': timePoint__internal__,
            'fileName': fileName__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'val',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def closeSimulationResultFile(
        self,
    ):
        """
```modelica
function closeSimulationResultFile
  output Boolean success;
end closeSimulationResultFile;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'closeSimulationResultFile',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getParameterNames(
        self,
        class_,
    ):
        """
```modelica
function getParameterNames
  input TypeName class_;
  output String[:] parameters;
end getParameterNames;
```
        """
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getParameterNames',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getParameterValue(
        self,
        class_,
        parameterName,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        parameterName__internal__ = cast_value__(
            name='parameterName', value=parameterName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            parameterName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getParameterValue',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getComponentModifierNames(
        self,
        class_,
        componentName,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        componentName__internal__ = cast_value__(
            name='componentName', value=componentName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            componentName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getComponentModifierNames',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getComponentModifierValue(
        self,
        class_,
        modifier,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        modifier__internal__ = cast_value__(
            name='modifier', value=modifier,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            modifier__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getComponentModifierValue',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getComponentModifierValues(
        self,
        class_,
        modifier,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        modifier__internal__ = cast_value__(
            name='modifier', value=modifier,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            modifier__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getComponentModifierValues',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getInstantiatedParametersAndValues(
        self,
        cls,
    ):
        """
```modelica
function getInstantiatedParametersAndValues
  input TypeName cls;
  output String[:] values;
end getInstantiatedParametersAndValues;
```
        """
        # Argument check
        cls__internal__ = cast_value__(
            name='cls', value=cls,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cls__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getInstantiatedParametersAndValues',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def removeComponentModifiers(
        self,
        class_,
        componentName,
        keepRedeclares=None,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        componentName__internal__ = cast_value__(
            name='componentName', value=componentName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        keepRedeclares__internal__ = cast_value__(
            name='keepRedeclares', value=keepRedeclares,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            componentName__internal__,
        ]
        __kwrds = {
            'keepRedeclares': keepRedeclares__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'removeComponentModifiers',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def removeExtendsModifiers(
        self,
        className,
        baseClassName,
        keepRedeclares=None,
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
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        baseClassName__internal__ = cast_value__(
            name='baseClassName', value=baseClassName,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        keepRedeclares__internal__ = cast_value__(
            name='keepRedeclares', value=keepRedeclares,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
            baseClassName__internal__,
        ]
        __kwrds = {
            'keepRedeclares': keepRedeclares__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'removeExtendsModifiers',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getConnectionCount(
        self,
        className,
    ):
        """
```modelica
function getConnectionCount
  input TypeName className;
  output Integer count;
end getConnectionCount;
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getConnectionCount',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getNthConnection(
        self,
        className,
        index,
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
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        index__internal__ = cast_value__(
            name='index', value=index,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
            index__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getNthConnection',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getAlgorithmCount(
        self,
        class_,
    ):
        """
```modelica
function getAlgorithmCount
  input TypeName class_;
  output Integer count;
end getAlgorithmCount;
```
        """
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getAlgorithmCount',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getNthAlgorithm(
        self,
        class_,
        index,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        index__internal__ = cast_value__(
            name='index', value=index,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            index__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getNthAlgorithm',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getInitialAlgorithmCount(
        self,
        class_,
    ):
        """
```modelica
function getInitialAlgorithmCount
  input TypeName class_;
  output Integer count;
end getInitialAlgorithmCount;
```
        """
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getInitialAlgorithmCount',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getNthInitialAlgorithm(
        self,
        class_,
        index,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        index__internal__ = cast_value__(
            name='index', value=index,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            index__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getNthInitialAlgorithm',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getAlgorithmItemsCount(
        self,
        class_,
    ):
        """
```modelica
function getAlgorithmItemsCount
  input TypeName class_;
  output Integer count;
end getAlgorithmItemsCount;
```
        """
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getAlgorithmItemsCount',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getNthAlgorithmItem(
        self,
        class_,
        index,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        index__internal__ = cast_value__(
            name='index', value=index,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            index__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getNthAlgorithmItem',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getInitialAlgorithmItemsCount(
        self,
        class_,
    ):
        """
```modelica
function getInitialAlgorithmItemsCount
  input TypeName class_;
  output Integer count;
end getInitialAlgorithmItemsCount;
```
        """
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getInitialAlgorithmItemsCount',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getNthInitialAlgorithmItem(
        self,
        class_,
        index,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        index__internal__ = cast_value__(
            name='index', value=index,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            index__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getNthInitialAlgorithmItem',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getEquationCount(
        self,
        class_,
    ):
        """
```modelica
function getEquationCount
  input TypeName class_;
  output Integer count;
end getEquationCount;
```
        """
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getEquationCount',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getNthEquation(
        self,
        class_,
        index,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        index__internal__ = cast_value__(
            name='index', value=index,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            index__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getNthEquation',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getInitialEquationCount(
        self,
        class_,
    ):
        """
```modelica
function getInitialEquationCount
  input TypeName class_;
  output Integer count;
end getInitialEquationCount;
```
        """
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getInitialEquationCount',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getNthInitialEquation(
        self,
        class_,
        index,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        index__internal__ = cast_value__(
            name='index', value=index,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            index__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getNthInitialEquation',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getEquationItemsCount(
        self,
        class_,
    ):
        """
```modelica
function getEquationItemsCount
  input TypeName class_;
  output Integer count;
end getEquationItemsCount;
```
        """
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getEquationItemsCount',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getNthEquationItem(
        self,
        class_,
        index,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        index__internal__ = cast_value__(
            name='index', value=index,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            index__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getNthEquationItem',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getInitialEquationItemsCount(
        self,
        class_,
    ):
        """
```modelica
function getInitialEquationItemsCount
  input TypeName class_;
  output Integer count;
end getInitialEquationItemsCount;
```
        """
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getInitialEquationItemsCount',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getNthInitialEquationItem(
        self,
        class_,
        index,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        index__internal__ = cast_value__(
            name='index', value=index,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            index__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getNthInitialEquationItem',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getAnnotationCount(
        self,
        class_,
    ):
        """
```modelica
function getAnnotationCount
  input TypeName class_;
  output Integer count;
end getAnnotationCount;
```
        """
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getAnnotationCount',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getNthAnnotationString(
        self,
        class_,
        index,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        index__internal__ = cast_value__(
            name='index', value=index,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            index__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getNthAnnotationString',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getImportCount(
        self,
        class_,
    ):
        """
```modelica
function getImportCount
  input TypeName class_;
  output Integer count;
end getImportCount;
```
        """
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getImportCount',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getNthImport(
        self,
        class_,
        index,
    ):
        """
```modelica
function getNthImport
  input TypeName class_;
  input Integer index;
  output String out[3] "{\"Path\",\"Id\",\"Kind\"}";
end getNthImport;
```
        """
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        index__internal__ = cast_value__(
            name='index', value=index,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
            index__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getNthImport',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def iconv(
        self,
        string,
        from_,
        to=None,
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
        # Argument check
        string__internal__ = cast_value__(
            name='string', value=string,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        from___internal__ = cast_value__(
            name='from_', value=from_,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        to__internal__ = cast_value__(
            name='to', value=to,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            string__internal__,
            from___internal__,
        ]
        __kwrds = {
            'to': to__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'iconv',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getDocumentationAnnotation(
        self,
        cl,
    ):
        """
```modelica
function getDocumentationAnnotation
  input TypeName cl;
  output String out[3] "{info,revision,infoHeader} TODO: Should be changed to have 2 outputs instead of an array of 2 Strings...";
end getDocumentationAnnotation;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getDocumentationAnnotation',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setDocumentationAnnotation(
        self,
        class_,
        info=None,
        revisions=None,
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
        # Argument check
        class___internal__ = cast_value__(
            name='class_', value=class_,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        info__internal__ = cast_value__(
            name='info', value=info,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        revisions__internal__ = cast_value__(
            name='revisions', value=revisions,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            class___internal__,
        ]
        __kwrds = {
            'info': info__internal__,
            'revisions': revisions__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setDocumentationAnnotation',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getTimeStamp(
        self,
        cl,
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
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getTimeStamp',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def stringTypeName(
        self,
        str,
    ):
        """
```modelica
function stringTypeName
  input String str;
  output TypeName cl;
end stringTypeName;
```
        """
        # Argument check
        str__internal__ = cast_value__(
            name='str', value=str,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            str__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'stringTypeName',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def stringVariableName(
        self,
        str,
    ):
        """
```modelica
function stringVariableName
  input String str;
  output VariableName cl;
end stringVariableName;
```
        """
        # Argument check
        str__internal__ = cast_value__(
            name='str', value=str,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            str__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'stringVariableName',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def typeNameString(
        self,
        cl,
    ):
        """
```modelica
function typeNameString
  input TypeName cl;
  output String out;
end typeNameString;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'typeNameString',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def typeNameStrings(
        self,
        cl,
    ):
        """
```modelica
function typeNameStrings
  input TypeName cl;
  output String out[:];
end typeNameStrings;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'typeNameStrings',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getClassComment(
        self,
        cl,
    ):
        """
```modelica
function getClassComment
  input TypeName cl;
  output String comment;
end getClassComment;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getClassComment',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def dirname(
        self,
        path,
    ):
        """
```modelica
function dirname
  input String path;
  output String dirname;
end dirname;
```
        """
        # Argument check
        path__internal__ = cast_value__(
            name='path', value=path,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            path__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'dirname',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def basename(
        self,
        path,
    ):
        """
```modelica
function basename
  input String path;
  output String basename;
end basename;
```
        """
        # Argument check
        path__internal__ = cast_value__(
            name='path', value=path,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            path__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'basename',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getClassRestriction(
        self,
        cl,
    ):
        """
```modelica
function getClassRestriction
  input TypeName cl;
  output String restriction;
end getClassRestriction;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getClassRestriction',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isType(
        self,
        cl,
    ):
        """
```modelica
function isType
  input TypeName cl;
  output Boolean b;
end isType;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isType',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isPackage(
        self,
        cl,
    ):
        """
```modelica
function isPackage
  input TypeName cl;
  output Boolean b;
end isPackage;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isPackage',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isClass(
        self,
        cl,
    ):
        """
```modelica
function isClass
  input TypeName cl;
  output Boolean b;
end isClass;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isClass',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isRecord(
        self,
        cl,
    ):
        """
```modelica
function isRecord
  input TypeName cl;
  output Boolean b;
end isRecord;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isRecord',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isBlock(
        self,
        cl,
    ):
        """
```modelica
function isBlock
  input TypeName cl;
  output Boolean b;
end isBlock;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isBlock',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isFunction(
        self,
        cl,
    ):
        """
```modelica
function isFunction
  input TypeName cl;
  output Boolean b;
end isFunction;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isFunction',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isPartial(
        self,
        cl,
    ):
        """
```modelica
function isPartial
  input TypeName cl;
  output Boolean b;
end isPartial;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isPartial',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isModel(
        self,
        cl,
    ):
        """
```modelica
function isModel
  input TypeName cl;
  output Boolean b;
end isModel;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isModel',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isConnector(
        self,
        cl,
    ):
        """
```modelica
function isConnector
  input TypeName cl;
  output Boolean b;
end isConnector;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isConnector',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isOptimization(
        self,
        cl,
    ):
        """
```modelica
function isOptimization
  input TypeName cl;
  output Boolean b;
end isOptimization;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isOptimization',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isEnumeration(
        self,
        cl,
    ):
        """
```modelica
function isEnumeration
  input TypeName cl;
  output Boolean b;
end isEnumeration;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isEnumeration',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isOperator(
        self,
        cl,
    ):
        """
```modelica
function isOperator
  input TypeName cl;
  output Boolean b;
end isOperator;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isOperator',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isOperatorRecord(
        self,
        cl,
    ):
        """
```modelica
function isOperatorRecord
  input TypeName cl;
  output Boolean b;
end isOperatorRecord;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isOperatorRecord',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isOperatorFunction(
        self,
        cl,
    ):
        """
```modelica
function isOperatorFunction
  input TypeName cl;
  output Boolean b;
end isOperatorFunction;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isOperatorFunction',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isProtectedClass(
        self,
        cl,
        c2,
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
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        c2__internal__ = cast_value__(
            name='c2', value=c2,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
            c2__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isProtectedClass',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getBuiltinType(
        self,
        cl,
    ):
        """
```modelica
function getBuiltinType
  input TypeName cl;
  output String name;
end getBuiltinType;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getBuiltinType',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def setInitXmlStartValue(
        self,
        fileName,
        variableName,
        startValue,
        outputFile,
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
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        variableName__internal__ = cast_value__(
            name='variableName', value=variableName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        startValue__internal__ = cast_value__(
            name='startValue', value=startValue,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        outputFile__internal__ = cast_value__(
            name='outputFile', value=outputFile,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
            variableName__internal__,
            startValue__internal__,
            outputFile__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'setInitXmlStartValue',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def ngspicetoModelica(
        self,
        netlistfileName,
    ):
        """
```modelica
function ngspicetoModelica
  input String netlistfileName;
  output Boolean success = false;
end ngspicetoModelica;
```
        """
        # Argument check
        netlistfileName__internal__ = cast_value__(
            name='netlistfileName', value=netlistfileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            netlistfileName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'ngspicetoModelica',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getInheritedClasses(
        self,
        name,
    ):
        """
```modelica
function getInheritedClasses
  input TypeName name;
  output TypeName inheritedClasses[:];
end getInheritedClasses;
```
        """
        # Argument check
        name__internal__ = cast_value__(
            name='name', value=name,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            name__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getInheritedClasses',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getComponentsTest(
        self,
        name,
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
        # Argument check
        name__internal__ = cast_value__(
            name='name', value=name,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            name__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getComponentsTest',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def isExperiment(
        self,
        name,
    ):
        """
```modelica
function isExperiment
  input TypeName name;
  output Boolean res;
end isExperiment;
```
        """
        # Argument check
        name__internal__ = cast_value__(
            name='name', value=name,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            name__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'isExperiment',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getSimulationOptions(
        self,
        name,
        defaultStartTime=None,
        defaultStopTime=None,
        defaultTolerance=None,
        defaultNumberOfIntervals=None,
        defaultInterval=None,
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
        # Argument check
        name__internal__ = cast_value__(
            name='name', value=name,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        defaultStartTime__internal__ = cast_value__(
            name='defaultStartTime', value=defaultStartTime,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        defaultStopTime__internal__ = cast_value__(
            name='defaultStopTime', value=defaultStopTime,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        defaultTolerance__internal__ = cast_value__(
            name='defaultTolerance', value=defaultTolerance,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )
        defaultNumberOfIntervals__internal__ = cast_value__(
            name='defaultNumberOfIntervals', value=defaultNumberOfIntervals,
            optional=True,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )
        defaultInterval__internal__ = cast_value__(
            name='defaultInterval', value=defaultInterval,
            optional=True,
            class_=numpy__.double,
            class_restrictions=(numpy__.float, numpy__.double),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            name__internal__,
        ]
        __kwrds = {
            'defaultStartTime': defaultStartTime__internal__,
            'defaultStopTime': defaultStopTime__internal__,
            'defaultTolerance': defaultTolerance__internal__,
            'defaultNumberOfIntervals': defaultNumberOfIntervals__internal__,
            'defaultInterval': defaultInterval__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getSimulationOptions',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getAnnotationNamedModifiers(
        self,
        name,
        vendorannotation,
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
        # Argument check
        name__internal__ = cast_value__(
            name='name', value=name,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        vendorannotation__internal__ = cast_value__(
            name='vendorannotation', value=vendorannotation,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            name__internal__,
            vendorannotation__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getAnnotationNamedModifiers',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getAnnotationModifierValue(
        self,
        name,
        vendorannotation,
        modifiername,
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
        # Argument check
        name__internal__ = cast_value__(
            name='name', value=name,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        vendorannotation__internal__ = cast_value__(
            name='vendorannotation', value=vendorannotation,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        modifiername__internal__ = cast_value__(
            name='modifiername', value=modifiername,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            name__internal__,
            vendorannotation__internal__,
            modifiername__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getAnnotationModifierValue',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def classAnnotationExists(
        self,
        className,
        annotationName,
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
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        annotationName__internal__ = cast_value__(
            name='annotationName', value=annotationName,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
            annotationName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'classAnnotationExists',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getBooleanClassAnnotation(
        self,
        className,
        annotationName,
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
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        annotationName__internal__ = cast_value__(
            name='annotationName', value=annotationName,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
            annotationName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getBooleanClassAnnotation',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def extendsFrom(
        self,
        className,
        baseClassName,
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
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        baseClassName__internal__ = cast_value__(
            name='baseClassName', value=baseClassName,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
            baseClassName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'extendsFrom',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def loadModelica3D(
        self,
        version=None,
    ):
        """
```modelica
function loadModelica3D
  input String version = "3.2.1";
  output Boolean status;
end loadModelica3D;
```
        """
        # Argument check
        version__internal__ = cast_value__(
            name='version', value=version,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
            'version': version__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'loadModelica3D',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def searchClassNames(
        self,
        searchText,
        findInText=None,
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
        # Argument check
        searchText__internal__ = cast_value__(
            name='searchText', value=searchText,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        findInText__internal__ = cast_value__(
            name='findInText', value=findInText,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            searchText__internal__,
        ]
        __kwrds = {
            'findInText': findInText__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'searchClassNames',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getAvailableLibraries(
        self,
    ):
        """
```modelica
function getAvailableLibraries
  output String[:] libraries;
end getAvailableLibraries;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getAvailableLibraries',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getUses(
        self,
        pack,
    ):
        """
```modelica
function getUses
  input TypeName pack;
  output String[:, :] uses;
end getUses;
```
        """
        # Argument check
        pack__internal__ = cast_value__(
            name='pack', value=pack,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            pack__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getUses',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getDerivedClassModifierNames(
        self,
        className,
    ):
        """
```modelica
function getDerivedClassModifierNames
  input TypeName className;
  output String[:] modifierNames;
end getDerivedClassModifierNames;
```
        """
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getDerivedClassModifierNames',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getDerivedClassModifierValue(
        self,
        className,
        modifierName,
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
        # Argument check
        className__internal__ = cast_value__(
            name='className', value=className,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        modifierName__internal__ = cast_value__(
            name='modifierName', value=modifierName,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            className__internal__,
            modifierName__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getDerivedClassModifierValue',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def generateEntryPoint(
        self,
        fileName,
        entryPoint,
        url=None,
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
        # Argument check
        fileName__internal__ = cast_value__(
            name='fileName', value=fileName,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        entryPoint__internal__ = cast_value__(
            name='entryPoint', value=entryPoint,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        url__internal__ = cast_value__(
            name='url', value=url,
            optional=True,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            fileName__internal__,
            entryPoint__internal__,
        ]
        __kwrds = {
            'url': url__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'generateEntryPoint',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def numProcessors(
        self,
    ):
        """
```modelica
function numProcessors
  output Integer result;
end numProcessors;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'numProcessors',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def runScriptParallel(
        self,
        scripts,
        numThreads=None,
        useThreads=None,
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
        # Argument check
        scripts__internal__ = cast_value__(
            name='scripts', value=scripts,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(None,),
        )
        numThreads__internal__ = cast_value__(
            name='numThreads', value=numThreads,
            optional=True,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )
        useThreads__internal__ = cast_value__(
            name='useThreads', value=useThreads,
            optional=True,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            scripts__internal__,
        ]
        __kwrds = {
            'numThreads': numThreads__internal__,
            'useThreads': useThreads__internal__,
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'runScriptParallel',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def exit(
        self,
        status,
    ):
        """
```modelica
function exit
  input Integer status;
end exit;
```
        """
        # Argument check
        status__internal__ = cast_value__(
            name='status', value=status,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            status__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'exit',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def threadWorkFailed(
        self,
    ):
        """
```modelica

```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'threadWorkFailed',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getMemorySize(
        self,
    ):
        """
```modelica
function getMemorySize
  output Real memory(unit = "MiB");
end getMemorySize;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getMemorySize',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def GC_gcollect_and_unmap(
        self,
    ):
        """
```modelica

```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'GC_gcollect_and_unmap',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def GC_expand_hp(
        self,
        size,
    ):
        """
```modelica
function GC_expand_hp
  input Integer size;
  output Boolean success;
end GC_expand_hp;
```
        """
        # Argument check
        size__internal__ = cast_value__(
            name='size', value=size,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            size__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'GC_expand_hp',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def GC_set_max_heap_size(
        self,
        size,
    ):
        """
```modelica
function GC_set_max_heap_size
  input Integer size;
  output Boolean success;
end GC_set_max_heap_size;
```
        """
        # Argument check
        size__internal__ = cast_value__(
            name='size', value=size,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            size__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'GC_set_max_heap_size',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def GC_get_prof_stats(
        self,
    ):
        """
```modelica
function GC_get_prof_stats
  output GC_PROFSTATS gcStats;
end GC_get_prof_stats;
```
        """
        # Argument check

        # Pack positional arguments
        __args = [
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'GC_get_prof_stats',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def checkInterfaceOfPackages(
        self,
        cl,
        dependencyMatrix,
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
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        dependencyMatrix__internal__ = cast_value__(
            name='dependencyMatrix', value=dependencyMatrix,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(None, None),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
            dependencyMatrix__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'checkInterfaceOfPackages',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def sortStrings(
        self,
        arr,
    ):
        """
```modelica
function sortStrings
  input String arr[:];
  output String sorted[:];
end sortStrings;
```
        """
        # Argument check
        arr__internal__ = cast_value__(
            name='arr', value=arr,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(None,),
        )

        # Pack positional arguments
        __args = [
            arr__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'sortStrings',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getClassInformation(
        self,
        cl,
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
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getClassInformation',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getTransitions(
        self,
        cl,
    ):
        """
```modelica
function getTransitions
  input TypeName cl;
  output String[:, :] transitions;
end getTransitions;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getTransitions',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def deleteTransition(
        self,
        cl,
        from_,
        to,
        condition,
        immediate,
        reset,
        synchronize,
        priority,
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
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        from___internal__ = cast_value__(
            name='from_', value=from_,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        to__internal__ = cast_value__(
            name='to', value=to,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        condition__internal__ = cast_value__(
            name='condition', value=condition,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )
        immediate__internal__ = cast_value__(
            name='immediate', value=immediate,
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        reset__internal__ = cast_value__(
            name='reset', value=reset,
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        synchronize__internal__ = cast_value__(
            name='synchronize', value=synchronize,
            optional=False,
            class_=numpy__.bool_,
            class_restrictions=(numpy__.bool, numpy__.bool_),
            sizes=(),
        )
        priority__internal__ = cast_value__(
            name='priority', value=priority,
            optional=False,
            class_=numpy__.intc,
            class_restrictions=(numpy__.int, numpy__.intc),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
            from___internal__,
            to__internal__,
            condition__internal__,
            immediate__internal__,
            reset__internal__,
            synchronize__internal__,
            priority__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'deleteTransition',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def getInitialStates(
        self,
        cl,
    ):
        """
```modelica
function getInitialStates
  input TypeName cl;
  output String[:, :] initialStates;
end getInitialStates;
```
        """
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'getInitialStates',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def deleteInitialState(
        self,
        cl,
        state,
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
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        state__internal__ = cast_value__(
            name='state', value=state,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
            state__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'deleteInitialState',
            args=__args,
            kwrds=__kwrds,
        )

        return __result

    def generateScriptingAPI(
        self,
        cl,
        name,
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
        # Argument check
        cl__internal__ = cast_value__(
            name='cl', value=cl,
            optional=False,
            class_=TypeName,
            class_restrictions=(),
            sizes=(),
        )
        name__internal__ = cast_value__(
            name='name', value=name,
            optional=False,
            class_=numpy__.str_,
            class_restrictions=(numpy__.str, numpy__.str_),
            sizes=(),
        )

        # Pack positional arguments
        __args = [
            cl__internal__,
            name__internal__,
        ]
        __kwrds = {
        }

        # Call function
        __result = OMCSession__call__(
            self,
            'generateScriptingAPI',
            args=__args,
            kwrds=__kwrds,
        )

        return __result


open_session = functools__.partial(OMCSession__open__, OMCSession)
