## Disk Usage

This script approximates the linux du command with the 
--apparent-size flag set. It has options also for various 
block sizes and human readable output.

### Usage
```
python3 du.py [--help] [-b | -k | -m | -g] [-h] [path]

estimate file space usage

positional arguments:
  path    the parent path to be analyzed

optional arguments:
  --help  show this help message and exit
  -b      set the block size as 1 byte
  -k      set the block size as 1 kilobyte
  -m      set the block size as 1 megabyte
  -g      set the block size as 1 gigabyte
  -h      format the response to be human readable

```

#### Usage Example

```python3 du.py -m -h ./data```

### Testing
Run `python3 test_du.py` to execute the five builtin tests