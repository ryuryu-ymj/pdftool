PDF command-line tool using PyMuPDF.

# Usage
```
Usage: pdftool [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  compress  Compress PDF file size.
  resize    Resize PDF pages.
```

# Installation
### pip
```shell
pip install git+https://github.com/ryuryu-ymj/pdftool.git
```

### uv
```shell
uv tool install git+https://github.com/ryuryu-ymj/pdftool.git
```


# Shell completion
### fish
```shell
_PDFTOOL_COMPLETE=fish_source pdftool > ~/.config/fish/completions/pdftool.fish
```
