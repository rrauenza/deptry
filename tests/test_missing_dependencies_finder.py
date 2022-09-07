from deptry.dependency import Dependency
from deptry.missing_dependencies_finder import MissingDependenciesFinder
from deptry.module import Module


def test_simple():
    dependencies = []
    modules = [Module("foobar", dependencies)]
    deps = MissingDependenciesFinder(imported_modules=modules, dependencies=dependencies).find()
    assert len(deps) == 1
    assert deps[0] == "foobar"


def test_simple_with_ignore():
    dependencies = []
    modules = [Module("foobar", dependencies)]
    deps = MissingDependenciesFinder(
        imported_modules=modules, dependencies=dependencies, ignore_missing=["foobar"]
    ).find()
    assert len(deps) == 0