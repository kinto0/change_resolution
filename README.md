# change_resolution: a resolution changing utility for windows

(mostly copied from [gamestream_launchpad](https://github.com/cgarst/gamestream_launchpad)

## Usage
positional arguments:
  width
  height

options:
  -h, --help            show this help message and exit
  -r REFRESH_RATE, --refresh-rate REFRESH_RATE (optional)

example:
`./change_resolution.exe 2560 1440 -r 50`

## Development (windows only?)
```
pip install -r requirements.txt
python change_resolution.py <width> <height> [-r <refresh rate>]
```

To build an executable:
```
pyinstaller --onefile change_resolution.py
```
