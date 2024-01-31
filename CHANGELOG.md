# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.3.1] - 2024-01-24

### Added

- `omc4py.v_1_23` Support of _OpenModelica 1.23.x_

### Changed
- Accept `PathLike` for argument
    - `*dir`
    - `*dirName`
    - `*directory`
    - `*file`
    - `*file[0-9]`
    - `*fileName`
    - `*fileNames`
    - `*path`

## [0.3.0] - 2024-01-23

### Fixed

- `OpenModelica.Scripting.CheckSettingsResult`
    - Rename `SENDDATALIBS` => `RTLIBS`
- Fixed a mistake where `OMCRuntimeError` inherited `OMCError`.

### Changed

- More effective OpenModelica literal parser

## [0.3.0a4] - 2023-11-22

### Added

- Windows support
    - Auto search latest omc.exe form `C:\Program Files\OpenModelica*\bin\omc.exe`
    - Add tornado dependency support async zmq call

## [0.3.0a3] - 2023-11-21

### Fixed

- float, record input argument

## [0.3.0a2] - 2023-11-21

### Fixed

- Fixed an expression for a function that has only one argument with no default value. s.t. `buildModel`

## [0.3.0a1] - 2023-11-21

### Added

- Support pickle serialize for `omc4py.TypeName`, `omc4py.VariableName`
- `omc4py.v_1_22` Support of _OpenModelica 1.22.x_

### Changed

- Rename `async` session
    - `omc4py.v_1_21.aio.Session` => `omc4py.v_1_21.AsyncSession`
    - `omc4py.v_1_20.aio.Session` => `omc4py.v_1_20.AsyncSession`
    - ...
    - `omc4py.v_1_13.aio.Session` => `omc4py.v_1_13.AsyncSession`

### Removed

- `python==3.7` support
- `omc4py.latest` module
- Support of _OpenModelica<1.13.0_

## [0.3.0a0] - 2023-07-30

### Added

- `omc4py.v_1_21` Support of _OpenModelica 1.21.x_
- Add Type-hints for session class
- Support asyncio (coroutine) in session class

## [0.2.2] - 2023-11-01

### Fixed

- Dependencies for `modelicalang`
    - `0.1.0a0`
    - `0.1.0a1`

## [0.2.1] - 2023-02-09 [YANKED]

### Added

- `omc4py.v_1_20` Support of _OpenModelica 1.20.x_
- `omc4py.v_1_19` Support of _OpenModelica 1.19.x_

## [0.2.0] - 2023-02-02 [YANKED]

### Fixed

- (development environment) Fix tests by GitHub Actions
- Fix status badges to latest

## [0.2.0a0] - 2023-02-01 [YANKED]

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

[Unreleased]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.3.1...HEAD
[0.3.0]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.3.0a4...v0.3.0
[0.3.0a4]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.3.0a3...v0.3.0a4
[0.3.0a3]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.3.0a2...v0.3.0a3
[0.3.0a2]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.3.0a1...v0.3.0a2
[0.3.0a1]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.3.0a0...v0.3.0a1
[0.3.0a0]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.2.2...v0.3.0a0
[0.2.2]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.2.0a0...v0.2.0
[0.2.0a0]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.1.1...v0.2.0a0
[0.1.1]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.0.1...v0.1.0
[0.0.1]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.0.0...v0.0.1
[0.0.0]: https://github.com/ijknabla/OpenModelicaCompilerForPython/releases/tag/v0.0.0
