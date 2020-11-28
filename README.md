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
class Exception
class Warning

namespace omc4py.exception {
    class OMCException
    class OMCNotification
    class OMCWarning
    class OMCError

    OMCException <-- OMCNotification
    OMCException <-- OMCWarning
    OMCException <-- OMCError
}


Exception <-- omc4py.exception.OMCException

Exception <-- Warning
Warning <-- omc4py.exception.OMCNotification
Warning <-- omc4py.exception.OMCWarning
@enduml
-->
![class diagram of omc4py.exception](http://www.plantuml.com/plantuml/svg/SoWkIImgAStDuKhEIImkLd2jI4ujACdCpuFomnEByZBpqhcuyX9pKuiB4fDJ5V9paqqAAlLIOIeLghaKW02Ytj_N6Mu4gh1VVabcMcPo8gOCr0uqKugAyekuG68ePYhOwEgYcuPJ4S9WJ7c47RLSN5meKXW-r4FMZAuOPWcKncu0cei9AeO7kqDgNWemTW00)

Some Scripting API set error internal (not raise direct)

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
