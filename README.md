
# OpenModelicaCompilerForPython [![License: OSMC-PL](https://img.shields.io/badge/license-OSMC--PL-lightgrey.svg)](./COPYING) [![Flake8](https://github.com/ijknabla/OpenModelicaCompilerForPython/workflows/Flake8/badge.svg)](https://github.com/ijknabla/OpenModelicaCompilerForPython/actions?query=workflow%3AFlake8)

OpenModelica compiler (omc) interface for Python>=3.6

## Tested omc versions

[![Pytest (omc1.13.0)](https://github.com/ijknabla/OpenModelicaCompilerForPython/workflows/Pytest%20(omc1.13.0)/badge.svg)](https://github.com/ijknabla/OpenModelicaCompilerForPython/actions?query=workflow%3A%22Pytest+%28omc1.13.0%29%22)
[![Pytest (omc1.13.2)](https://github.com/ijknabla/OpenModelicaCompilerForPython/workflows/Pytest%20(omc1.13.2)/badge.svg)](https://github.com/ijknabla/OpenModelicaCompilerForPython/actions?query=workflow%3A%22Pytest+%28omc1.13.2%29%22)

[![Pytest (omc1.14.1)](https://github.com/ijknabla/OpenModelicaCompilerForPython/workflows/Pytest%20(omc1.14.1)/badge.svg)](https://github.com/ijknabla/OpenModelicaCompilerForPython/actions?query=workflow%3A%22Pytest+%28omc1.14.1%29%22)
[![Pytest (omc1.14.2)](https://github.com/ijknabla/OpenModelicaCompilerForPython/workflows/Pytest%20(omc1.14.2)/badge.svg)](https://github.com/ijknabla/OpenModelicaCompilerForPython/actions?query=workflow%3A%22Pytest+%28omc1.14.2%29%22)

[![Pytest (omc1.16.0)](https://github.com/ijknabla/OpenModelicaCompilerForPython/workflows/Pytest%20(omc1.16.0)/badge.svg)](https://github.com/ijknabla/OpenModelicaCompilerForPython/actions?query=workflow%3A%22Pytest+%28omc1.16.0%29%22)
[![Pytest (omc1.16.1)](https://github.com/ijknabla/OpenModelicaCompilerForPython/workflows/Pytest%20(omc1.16.1)/badge.svg)](https://github.com/ijknabla/OpenModelicaCompilerForPython/actions?query=workflow%3A%22Pytest+%28omc1.16.1%29%22)
[![Pytest (omc1.16.5)](https://github.com/ijknabla/OpenModelicaCompilerForPython/workflows/Pytest%20(omc1.16.5)/badge.svg)](https://github.com/ijknabla/OpenModelicaCompilerForPython/actions?query=workflow%3A%22Pytest+%28omc1.16.5%29%22)

[![Pytest (omc1.17.0)](https://github.com/ijknabla/OpenModelicaCompilerForPython/workflows/Pytest%20(omc1.17.0)/badge.svg)](https://github.com/ijknabla/OpenModelicaCompilerForPython/actions?query=workflow%3A%22Pytest+%28omc1.17.0%29%22)

## Change log

[See CHANGELOG.md](./CHANGELOG.md)

## Quick tour

### Setup

Make sure that OpenModelica is installed on your system.

```bash
$ omc --version
```

OpenModelica official page [https://openmodelica.org/](https://openmodelica.org/)

Install OpenModelicaCompiler with pip.

```bash
$ python3 -m pip install OpenModelicaCompiler
```

`omc4py` is acutual package name. `omc4py.open_session()` will return session object which interfaces to omc.

```python3
#!/usr/bin/env python3
import omc4py

with omc4py.open_session() as session:
    print(session.getVersion())
```

### More usage about `open_session(...)`

If `omc4py.open_session` cannot find omc, such as if you have not added OpenModelica to your _PATH_ environment variable, you can specify a valid omc command name or omc executable path by `str`.

```python3
import omc4py

with omc4py.open_session(
    "C:/OpenModelica1.13.0-64bit/bin/omc.exe"
) as session:
    print(session.getVersion())
```

It is also possible to open multiple sessions with different versions of omc at the same time by explicitly specifying omc.

```python3
import omc4py

with \
    omc4py.open_session(
        "C:/OpenModelica1.13.0-64bit/bin/omc.exe"
    ) as session_13, \
    omc4py.open_session(
        "C:/Program Files/OpenModelica1.14.0-64bit/bin/omc.exe"
    ) as session_14:

    print("v1.13.0:", session_13.getVersion())
    print("v1.14.0:", session_14.getVersion())
```

As shown above, __it is recommended to ensure that session is closed by calling `omc4py.open_session()` via with-statement__.

However, sometimes you want to use session interactively, like OMShell. `omc4py` closes all unclosed sessions when exiting the python interpreter.

```python3
>>> from omc4py import *
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

```python3
>>> from omc4py import *
>>> session = open_session()
>>> session.__close__()
>>>
>>> exit()
```

### About session API

All session methods are _OpenModelica.Scripting.*_ functions. The names and types of arguments and return values are the same as the original modelica function, and session internally converts between the python class and the modelica class.

If you want to know more about each session method, you can display it with the `help ()` function.

- [UserGuide for OpenModelica Scripting API (v1.14)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/1.14/scripting_api.html)
- [UserGuide for OpenModelica Scripting API (v1.15)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/1.15/scripting_api.html)
- [UserGuide for OpenModelica Scripting API (v1.16)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/1.16/scripting_api.html)
- [UserGuide for OpenModelica Scripting API (v1.17)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/1.17/scripting_api.html)

- [UserGuide for OpenModelica Scripting API (latest)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/latest/scripting_api.html)


[Documentation in OpenModelica build server](https://build.openmodelica.org/Documentation/OpenModelica.Scripting.html) shows exhaustive information about _OpenModelica.Scripting_. You will find sub-packages not explained user guide.

- _OpenModelica.Scripting.Internal.*_
- _OpenModelica.Scripting.Experimental.*_

They are available from absolute reference

```python3
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

```python3
import omc4py

with omc4py.open_session() as session:
    assert(session.loadModel("Modelica"))  # load MSL
```

```python3
import omc4py

with omc4py.open_session() as session:
    assert(session.loadModel("Modelica", ["3.2.3"]))  # load MSL 3.2.3
```

#### `getClassNames`

Returns array of class names in the given class

```python3
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
    assert(session.loadModel("Modelica", ["3.2.3"]))
    for component in session.getComponents("Modelica.Constants"):
        print(
            f"{component.className.last_identifier!s:<20}"
            f"{component.name!s:<15}"
            f"{component.comment!r}"
        )
```

- - -

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

```python3
from omc4py import open_session

def doubtful_task(session):
    # session.doubtful_API1(...)
    # session.doubtful_API2(...)
    # session.doubtful_API3(...)
    session.__check__()

with open_session() as session:
    doubtful_task(session)
```
