
# OpenModelicaCompilerForPython [![License: OSMC-PL](https://img.shields.io/badge/license-OSMC--PL-lightgrey.svg)](./COPYING) [![lint.yml](https://github.com/ijknabla/OpenModelicaCompilerForPython/actions/workflows/lint.yml/badge.svg)](https://github.com/ijknabla/OpenModelicaCompilerForPython/actions/workflows/lint.yml) [![Pytest](https://github.com/ijknabla/OpenModelicaCompilerForPython/actions/workflows/test.yml/badge.svg)](https://github.com/ijknabla/OpenModelicaCompilerForPython/actions/workflows/test.yml)

OpenModelica compiler (omc) interface for Python

## Change log

[See CHANGELOG.md](./CHANGELOG.md)

## Installation

```bash
$ python3 -m pip install OpenModelicaCompiler
```

`omc4py` is acutual package name.

```python
import omc4py
```

### Prerequisites

Follow the link

| Platform | Link |
| :------- | :--- |
| Windows  | [https://openmodelica.org/download/download-windows/](https://openmodelica.org/download/download-windows/) |
| Linux    | [https://openmodelica.org/download/download-linux/](https://openmodelica.org/download/download-linux/) |
| Mac      | [https://openmodelica.org/download/download-mac/](https://openmodelica.org/download/download-mac/) |

And ensure `omc` command installed.

```
$ omc --version
OpenModelica 1.22.1
```

For Windows, it will work if omc.exe exists in the default installation.

```
"C:\Program Files\OpenModelica1.22.1-64bit\bin\omc.exe" --version
OpenModelica v1.22.1 (64-bit)
```

## Usage

### Open session

`omc4py.open_session()` returns session object which interfaces to omc.

```python
from omc4py import open_session

with open_session() as session:
    print(session.getVersion())
```

If `omc4py.open_session` cannot find omc, a valid omc command or executable path can be specified.

```python
from omc4py import open_session

with open_session(
    "C:/Program Files/OpenModelica1.22.1-64bit/bin/omc.exe"
) as session:
    print(session.getVersion())
```

### Call OpenModelica Scripting API via session

The OpenModelica Scripting API is available from the methods of session object.

See [UserGuide for OpenModelica Scripting API](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/latest/scripting_api.html)

OpenModelica classes and Python classes are converted to each other.
For example, the following OpenModelica function can be used from the following Python methods.

```modelica
// Modelica declaration

// Returns the version of the Modelica compiler.
function getVersion
  input TypeName cl = $Code(OpenModelica);
  output String version;
end getVersion;
```

```python
# Python interface
from typing import Union
from omc4py import TypeName

class Session:
    def getVersion(self, cl: Union[TypeName, str, None] = None) -> str:
        """
        Returns the version of the Modelica compiler.
        """
        ...
```

#### Class conversion between OpenModelica and Python

| OpenModelica | input (argument) | output (return) | description |
| :- | :- | :- | :- |
| `Real` | `float` | `float` |
| `Integer` | `int` | `int` |
| `Boolean x;` | `bool` | `bool` |
| `String x;` | `str` | `str` |
| `TypeName` | `omc4py.TypeName \| str` | `omc4py.TypeName` |
| `VariableName` | `omc4py.VariableName \| str` | `omc4py.VariableName` |
| `VariableNames` | `Sequence[omc4py.VariableName \| str]` | `list[omc4py.VariableName \| str]` |
| `type T = enumeration(a, b, c);` | `T \| Literal["a", "b", "c"]` | `T` |
| `record T ...` | `T` | `T` | `T` is dataclass |
| `T[:]` | `Sequence[T]` | `list[T]` |
| `T[:,:]` | `Sequence[Sequence[T]]` | `list[list[T]]` |
| `T x = ${default};` | `x: T \| None = None` | N/A |
| `function f` returns Multiple outputs | N/A | `class F(NamedTuple): ...` returned | NamedTuple name is the capitalized name of the function |


#### Exception handling

<!--
@startuml
namespace omc4py.exception {
    OMCException <-- OMCNotification
    OMCException <-- OMCWarning
    OMCException <-- OMCError
    OMCException <-- OMCRuntimeError
}

Exception <-- omc4py.exception.OMCException

Exception <-ri- Warning
Warning <-- omc4py.exception.OMCNotification
Warning <-- omc4py.exception.OMCWarning

Exception <-ri- RuntimeError
RuntimeError <-- omc4py.exception.OMCRuntimeError
@enduml
-->
![class diagram of omc4py.exception](http://www.plantuml.com/plantuml/svg/SoWkIImgAStDuSfBp4qjBaXCJbN8pqqsAQZKIwr8JYqeoSpFKwZcKW02VrzdLxYGZQukIC0lloGpBJCv4II6Kr5uOb5UPbuwJddNegBy8fooGQLv9PcvgH15jLnSA0emtAg7R0Igug9CNGMOKw0qTYFG_4LGCLGUqpOKfoDpS1g5eiCXDIy563C0)

- `OMCNotification`, `OMCWarning`, `OMCError` are raised from _omc_
- `OMCRuntimeError` is raised from `omc4py` python implementation (not from _omc_)

We are not sure about whole OpenModelica's exception handling policy.
Through `omc4py` project, We found that there are 4 situation for expection caused by function calls.

omc behavior

1. Function returns "\n" instead of valid value (no exception info)
1. Function returns formatted error messages (contains sourceInfo, level, kind, message) instead of valid value
1. Function returns unformatted error message (typically, startswith "* Error") instead of valid value
1. Function returns valid value and set exception messages internally

`omc4py` behavior

1) function returns `None` instead of valid result (no exception will be sent)
1) function send `OMCNotification` or `OMCWarning`, or raise `OMCError`
1) function raise `OMCRuntimeError` with the message returned by the omc
1) function returns valid value. You can check exceptions explicitly by `session.__check__()`

Normally, 4th case seems to be _notification_ or _warning_. If you want to be sure to check for exceptions, call `session.__check__()` before exit doubtful context.

```python
from omc4py import open_session

def doubtful_task(session):
    # session.doubtful_API1(...)
    # session.doubtful_API2(...)
    # session.doubtful_API3(...)
    session.__check__()

with open_session() as session:
    doubtful_task(session)
```


#### Asyncio feature

The session class has a counterpart asynchronous session class.
If `asyncio=True` is specified in open_session, an asynchronous session object can be opened.

```python
from omc4py import open_session

with open_session(asyncio=True) as session:
    await session.getVersion()
```

session object and asynchronous session object can be cross-referenced by the synchronous and asynchrnous attributes.

![diagram](https://www.plantuml.com/plantuml/svg/SoWkIImgAStDuKhEIImkLWXEBIxEpCzJgEPIK2Ykp4lEAChFooyjje9908KJKSGTGJoOP2t458WWfKPnmGpGqjM5wu6gGKYWw4BLeuHakXAAEhWoNLqj1QL4tEeSKlDIW8430000)

```python
from omc4py import open_session

with open_session() as session:
    # This session is synchronous
    # Synchronous calling
    session.getVersion()

    # Get asynchronous session by attribute
    async_session = session.asynchronous

    # Asynchronous calling
    await async_session.getVersion()
```

```python
from omc4py import open_session

with open_session(asyncio=True) as async_session:
    # This session is asynchronous
    # Asynchronous calling
    await async_session.getVersion()

    # Get synchronous session by attribute
    session = async_session.synchronous

    # Synchronous calling
    session.getVersion()
```

## Tips

### Multiple session

It is also possible to open multiple sessions with different versions of omc at the same time by explicitly specifying omc.

```python
from omc4py import open_session

with \
    open_session(
        "C:/Program Files/OpenModelica1.22.1-64bit/bin/omc.exe"
    ) as session_1_22, \
    open_session(
        "C:/Program Files/OpenModelica1.21.0-64bit/bin/omc.exe"
    ) as session_1_21:

    print("v1.22.1:", session_1_22.getVersion())
    print("v1.21.0:", session_1_21.getVersion())
```

### omc4py as interactive shell

As shown above, __it is recommended to ensure that session is closed by calling `omc4py.open_session()` via with-statement__.

However, sometimes you want to use session interactively, like OMShell. `omc4py` closes all unclosed sessions when exiting the python interpreter.

```python
>>> from omc4py import open_session
>>> session = open_session()
>>> session.loadString("""
... package A
...     package B
...             package C
...             end C;
...     end B;
... end A;
... """)
True
>>> list(session.getClassNames("A", recursive=True))
[TypeName('A'), TypeName('A.B'), TypeName('A.B.C')]
>>>
>>>
>>> exit()  # session will be closed internally
```

Besides, session object has `__close__` method to explicitly close session.

```python
>>> from omc4py import open_session
>>> session = open_session()
>>> session.__close__()
>>>
>>> exit()
```

### About session API

- [UserGuide for OpenModelica Scripting API (latest)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/latest/scripting_api.html)
- [UserGuide for OpenModelica Scripting API (v1.21)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/1.21/scripting_api.html)
- [UserGuide for OpenModelica Scripting API (v1.20)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/1.20/scripting_api.html)
- [UserGuide for OpenModelica Scripting API (v1.19)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/1.19/scripting_api.html)
- [UserGuide for OpenModelica Scripting API (v1.18)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/1.18/scripting_api.html)
- [UserGuide for OpenModelica Scripting API (v1.17)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/1.17/scripting_api.html)
- [UserGuide for OpenModelica Scripting API (v1.16)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/1.16/scripting_api.html)
- [UserGuide for OpenModelica Scripting API (v1.15)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/1.15/scripting_api.html)
- [UserGuide for OpenModelica Scripting API (v1.14)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/1.14/scripting_api.html)

[Documentation in OpenModelica build server](https://build.openmodelica.org/Documentation/OpenModelica.Scripting.html) shows exhaustive information about _OpenModelica.Scripting_. You will find sub-packages not explained user guide.

- _OpenModelica.Scripting.Internal.*_
- _OpenModelica.Scripting.Experimental.*_

They are available from absolute reference

```python
# Example for "timerTick" and "timerTock"
# in "OpenModelica.Scripting.Internal.Time"
from omc4py import open_session
from time import sleep

timer_index: int = 1

with open_session() as session:
    session.OpenModelica.Scripting.Internal.Time.timerTick(timer_index)

    sleep(0.1)

    # show elapsed time from last timerTick
    print(session.OpenModelica.Scripting.Internal.Time.timerTock(timer_index))
```

- - -

Let me introduce typical API functions!

#### `loadModel`

Load library and returns True if success. You can specify versions by second argument

```python
import omc4py

with omc4py.open_session() as session:
    assert(session.loadModel("Modelica"))  # load MSL
```

```python
import omc4py

with omc4py.open_session() as session:
    assert(session.loadModel("Modelica", ["4.0.0"]))  # load MSL 4.0.0
```

#### `getClassNames`

Returns array of class names in the given class

```python
import omc4py

with omc4py.open_session() as session:
    assert(session.loadModel("Modelica"))
    for className in session.getClassNames("Modelica"):
        print(className)
```

By default, `getClassNames()` only returns "sub" classes. If you want to know all classes belongs to the class set `recursive=True`.

```python3
import omc4py

with omc4py.open_session() as session:
    assert(session.loadModel("Modelica"))
    for className in session.getClassNames("Modelica", recursive=True):
        print(className)  # many class names will be printed
```

#### `getComponents`

Returns array of component (variable, parameter, constant, ...etc) profiles

```python3
import omc4py

with omc4py.open_session() as session:
    assert(session.loadModel("Modelica", ["4.0.0"]))
    for component in session.getComponents("Modelica.Constants"):
        print(
            f"{component.className.last_identifier!s:<20}"
            f"{component.name!s:<15}"
            f"{component.comment!r}"
        )
```
