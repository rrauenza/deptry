# Configuration with pyproject.toml

## Configuration

_deptry_ can be configured by adding a `[tool.deptry]` section to _pyproject.toml_. The possible arguments are:

- `ignore_directories`: `List`
- `ignore_notebooks`: `bool`
- `ignore_obsolete`: `List`
- `ignore_missing`: `List`
- `ignore_transitive`: `List`
- `skip_obsolete`: `bool`
- `skip_missing`: `bool`
- `skip_transitive`: `bool`

An example of such a section is given below.

```
[tool.deptry]
ignore_directories = [
  '.venv','tests','docs'
]
ignore_obsolete = [
  'alpha',
  'beta'
]
ignore_transitive = [
  'gamma'
]
skip_missing = true
```

## Lookup hierarchy

Command-line options have defaults that you can see with `deptry --help`. A _pyproject.toml_ can override those defaults. Finally, options provided by the user on the command line override both.