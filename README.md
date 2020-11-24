# OpenModelicaCompilerForPython
OpenModelica compiler (omc) interface for Python>=3.6

## What's this?

When omc4py.open_session() is called in with-statement, it returns session instance bound to omc executable.
```python3
from omc4py import open_session

with open_session() as session:
    ...
```

If `open_session()` cannot find the executable of omc,  
One solution is to add destination of omc executable to the environ `PATH`.  
Another solution is to specify omc executable path by argument of `open_session(${path_to_omc})`.

```
# open/close different version sessions
from omc4py import open_session

with open_session(
    "C:/Program Files/OpenModelica1.14.0-64bit/bin/omc.exe"
) as session:
    ...


with open_session(
    "C:/Program Files/OpenModelica1.14.1-64bit/bin/omc.exe"
) as session:
    ...
```

- - -

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
