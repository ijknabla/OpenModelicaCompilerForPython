
# Bootstrap for omc4py

## To generate interface files

```
python -m bootstrap interface-docker \
  -n 4 \
  -i ijknabla/openmodelica-python3 \
  omc1.13-py3.7-stretch \
  omc1.14-py3.7-buster \
  omc1.16-py3.7-buster \
  omc1.17-py3.7-buster \
  omc1.18-py3.7-bullseye \
  omc1.19-py3.7-bullseye \
  omc1.20-py3.7-bullseye \
  omc1.21-py3.7-bullseye \
  -o bootstrap/interface/ \
  --pip-cache-dir ~/.cache/pip
```
