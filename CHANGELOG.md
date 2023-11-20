# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]

### Added

- Support pickle serialize for `omc4py.TypeName`, `omc4py.VariableName`

### Changed

- Rename `async` session
    - `omc4py.v_1_21.aio.Session` => `omc4py.v_1_21.AsyncSession`
    - `omc4py.v_1_20.aio.Session` => `omc4py.v_1_20.AsyncSession`
    - ...
    - `omc4py.v_1_13.aio.Session` => `omc4py.v_1_13.AsyncSession`

### Removed

- `python==3.7` support
- `omc4py.latest` module

## [0.3.0a0] - 2023-07-30

### Added

- `omc4py.v_1_21` Support of _OpenModelica 1.21.x_
- Add Type-hints for session class
- Support asyncio (coroutine) in session class

## [0.2.1] - 2023-02-09

### Added

- `omc4py.v_1_20` Support of _OpenModelica 1.20.x_
- `omc4py.v_1_19` Support of _OpenModelica 1.19.x_

## [0.2.0] - 2023-02-02

### Fixed

- (development environment) Fix tests by GitHub Actions
- Fix status badges to latest

## [0.2.0a0] - 2023-02-01

### Changed

- Update modelica parser library to `modelicalang>=0.1`

## [0.1.1] - 2021-12-13
### Added
- `pyproject.toml` to unify package settings.
- `omc4py.v_1_18` support of _OpenModelica 1.18.x_

### Removed
- `setup.py`, `setup.cfg`, `requirements.txt` (unified to `pyproject.toml`)

## [0.1.0] - 2021-04-22
### Added
- `omc4py.v_1_17` Support of _OpenModelica 1.17.x_
- `omc4py.__version__` version string s.t. `"0.1.0"`
- CHANGELOG.md file for version management
- tests/ directory for testcases using pytest
### Removed
- `omc4py.v_1_14.OMCSession.oms_faultInjection` not available due to a bug in omc 1.14.1

## [0.0.1] - 2020-11-29
### Fixed
- setup.py fixed so that omc4py can be installed correctly

## 0.0.0 - 2020-11-29 [YANKED]
### Added
- COPYING file for OSMC-PL license
- omc4py/ directory (python package) for main package
- bootstrap/ directory (python package) for bootstrap of omc4py
- setup.py file to install omc4py
- MANIFEST.in file for setup.py
- README.md file for tutorial
- TODO.md file for action item management
### Security
- __This version cannot be installed with setup.py__ because the packages required to run are not listed correctly.

[Unreleased]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.3.0a0...HEAD
[0.3.0a0]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.2.1...v0.3.0a0
[0.2.1]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.2.0a0...v0.2.0
[0.2.0a0]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.1.1...v0.2.0a0
[0.1.1]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.0.1...v0.1.0
[0.0.1]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.0.0...v0.0.1
[0.0.0]: https://github.com/ijknabla/OpenModelicaCompilerForPython/releases/tag/v0.0.0
