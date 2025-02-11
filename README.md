Fish style process substitution ([psub](https://fishshell.com/docs/current/cmds/psub.html)) for xonsh.

## Installation

To install use pip:

```bash
xpip install xontrib-psub
# or: xpip install -U git+https://github.com/mingmingrr/xontrib-psub
```

## Usage

```bash
xontrib load psub
```

## Examples

```bash
vim $(git show rc.xsh | psub -s .xsh)
```

## Credits

This package was created with [xontrib cookiecutter template](https://github.com/xonsh/xontrib-cookiecutter).

