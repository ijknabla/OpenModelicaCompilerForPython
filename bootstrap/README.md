
# Bootstrap for omc4py

## To generate interface files

```
python -m bootstrap interface-docker \
  -n 4 \
  -i ijknabla/openmodelica \
  v1.14.2-python3.8 \
  v1.16.2-python3.8 \
  v1.17.0-python3.8 \
  v1.18.0-python3.8 \
  v1.19.2-python3.8 \
  v1.20.0-python3.8 \
  v1.21.0-python3.8 \
  v1.22.0-python3.8 \
  -o bootstrap/interface/ \
  --pip-cache-dir ~/.cache/pip
```

## To generate code from interface files
```
python -m bootstrap code bootstrap/interface/*.yaml -o omc4py/
```
