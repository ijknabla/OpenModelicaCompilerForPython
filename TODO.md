# Parsing `getClassNames` takes to long time

```python3
from omc4py.session.v_1_13_0 import open_session

session = open_session()
session.loadModel("Modelica")

# enable logger to check getClassNames responce
import logging
omc4py_logger = logging.getLogger("omc4py")
omc4py_logger.setLevel(logging.DEBUG)
omc4py_logger.addHandler(logging.StreamHandler())

# omc answers quickly, but python parser is too slow
session.getClassNames("Modelica", recursice=True)

```
