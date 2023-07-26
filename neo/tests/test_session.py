from __future__ import annotations

from itertools import zip_longest

import pytest

import neo.session
import neo.session.aio
from neo import TypeName, VariableName
from neo.openmodelica import Component

from .session import Enum, one
from .session.aio import EmptySession, NestedSession, OneSession


@pytest.mark.parametrize(
    "name", ["OpenModelica.Scripting.getComponentsTest.Component"]
)
@pytest.mark.parametrize("use_typename", [False, True])
def test_get_components(
    session: neo.session.Session, name: TypeName | str, use_typename: bool
) -> None:
    s = session
    if use_typename:
        name = TypeName(name)
    _check_components(s.getComponents(name))


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "name", ["OpenModelica.Scripting.getComponentsTest.Component"]
)
@pytest.mark.parametrize("use_typename", [False, True])
async def test_async_get_components(
    async_session: neo.session.aio.Session,
    name: TypeName | str,
    use_typename: bool,
) -> None:
    s = async_session
    if use_typename:
        name = TypeName(name)
    _check_components(await s.getComponents(name))


def _check_components(components: list[Component]) -> None:
    assert isinstance(components, list)
    assert all(isinstance(component, Component) for component in components)
    for component, (class_name, name, dimensions) in zip_longest(
        components,
        [
            ("String", "className", []),
            ("String", "name", []),
            ("String", "comment", []),
            ("Boolean", "isProtected", []),
            ("Boolean", "isFinal", []),
            ("Boolean", "isFlow", []),
            ("Boolean", "isStream", []),
            ("Boolean", "isReplaceable", []),
            ("String", "variability", []),
            ("String", "innerOuter", []),
            ("String", "inputOutput", []),
            ("String", "dimensions", [":"]),
        ],
    ):
        assert component.className == TypeName(class_name)
        assert component.name == VariableName(name)
        assert isinstance(component.comment, str) and component.comment
        assert component.protected == "public"
        assert component.isFinal is False
        assert component.isFlow is False
        assert component.isStream is False
        assert component.isReplaceable is False
        assert component.variability == "unspecified"
        assert component.innerOuter == "none"
        assert component.inputOutput == "unspecified"
        assert component.dimensions == dimensions


@pytest.mark.asyncio
async def test_empty_session(empty_session: EmptySession) -> None:
    s = empty_session
    assert await s.empty() is None  # type: ignore


@pytest.mark.asyncio
async def test_one(one_session: OneSession) -> None:
    s = one_session
    result = await s.one()
    assert isinstance(result, one)
    assert result == (1.0, 1, True, "1", Enum.One)
    assert result == one(
        real=1.0, integer=1, boolean=True, string="1", enum=Enum.One
    )


@pytest.mark.asyncio
async def test_nested(nested_session: NestedSession) -> None:
    s = nested_session
    assert await s.level_1() == await s.Nested.level()
    assert await s.level_2() == await s.Nested.Nested.level()
    assert await s.level_3() == await s.Nested.Nested.Nested.level()
