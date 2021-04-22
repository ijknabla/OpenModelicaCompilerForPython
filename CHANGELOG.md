# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

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

[0.1.0]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.0.1...v0.1.0
[0.0.1]: https://github.com/ijknabla/OpenModelicaCompilerForPython/compare/v0.0.0...v0.0.1
[0.0.0]: https://github.com/ijknabla/OpenModelicaCompilerForPython/releases/tag/v0.0.0
