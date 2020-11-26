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

```
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

All methods of session are function in `OpenModelica.Scripting.*`. If you want to know accurate signature, read `help(session)` or [UserGuide for OpenModelica Scripting API](https://www.openmodelica.org/doc/OpenModelicaUsersGuide/latest/scripting_api.html)

```python3
# Show current omc version
from omc4py import open_session

with open_session() as session:
    print(session.getVersion())
```

Features in:

- `OpenModelica.Scripting.Internal`
- `OpenModelica.Scripting.Experimental`

available from absolute reference

```python3
# Call "stat" in "OpenModelica.Scripting.Internal"
from omc4py import open_session

with open_session() as session:
    print(session.OpenModelica.Scripting.Internal.stat(__file__))
```

- - -

All types of arguments for function call checked by session.
```python3
# "sortString" only take one sequence of string as argument
from omc4py import open_session

with open_session() as session:
    session.sortStrings(
        ["a", "b", "0", "1e5"]
    )  # OK

    # session.sortStrings(
    #     ["a", "b", 0, "1e5"]
    # )  # NG

    # session.sortStrings(
    #     ["a", "b", "0", 1e5]
    # )  # NG
```
