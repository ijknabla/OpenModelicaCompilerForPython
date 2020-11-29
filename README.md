# OpenModelicaCompilerForPython
OpenModelica compiler (omc) interface for Python>=3.6

## Quick tour

### Setup

Check OpenModelica install on your system.  
[https://openmodelica.org/](https://openmodelica.org/)

```bash
$ omc --version
```

Install _OpenModelicaCompiler_ with pip.
```
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

It is also possible to launch multiple versions of omc at the same time by explicitly specifying omc.

```python3
from contextlib import ExitStack
import omc4py

with ExitStack() as stack:
    session_13 = stack.enter_context(
        omc4py.open_session("C:/OpenModelica1.13.0-64bit/bin/omc.exe")
    )
    session_14 = stack.enter_context(
        omc4py.open_session("C:/Program Files/OpenModelica1.14.0-64bit/bin/omc.exe")
    )

    print("v1.13.0:", session_13.getVersion())
    print("v1.14.0:", session_14.getVersion())
```

As shown above, __It is recommended to call `omc4py.open_session` via with-statement__ for secure resource handling.

But, sometimes you want to use session object interactively, (like _OMShell_) `omc4py` manages omc processes created in current python interpreter, and ensure to close at exit interpreter.

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

All methods of session as same as modelica-functions in _OpenModelica.Scripting.*_ in terms of argument types and return value types. If you want to know accurate signature, read `help(session)` or Scripting API section of OpenModelica UserGuide.

- [UserGuide for OpenModelica Scripting API (v1.14)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/1.14/scripting_api.html)
- [UserGuide for OpenModelica Scripting API (v1.15)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/1.15/scripting_api.html)
- [UserGuide for OpenModelica Scripting API (v1.16)](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/1.16/scripting_api.html)

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

#### Error

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

- Function returns "\n" instead of valid value (no exception info)
- Function returns formatted error message (contains sourceInfo, level, kind) instead of valid value
- Function returns unformatted error message (typically, startswith "* Error") instead of valid value
- Function returns valid value and set exception messages internally

In `omc4py`...  
1st case, function returns `None` instead of valid result (no exception will be sent).  
2nd and 3rd case, function send `OMCNotification`, `OMCWarning` or `OMCError`.  
4th case, function do not send any exception. You can check exceptions explicitly by `session.__check__()`

Noramally, 4th case seems to be _notification_ or _warning_. If you want to be sure to check for exceptions, call `session.__check__()` before exit doubtful context.

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

#### Typical API

##### `loadModel`

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

##### `getClassNames`

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

##### `getComponents`

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
