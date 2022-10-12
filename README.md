# py-machineid

Get the unique machine ID of any host (without admin privileges).

Sponsored by:

[![Keygen logo](https://user-images.githubusercontent.com/6979737/175406169-bd8bf064-7343-4bd1-94b7-a773ecec07b8.png)](https://keygen.sh)

_A software licensing and distribution API built for developers._

## Install

Install using [`pip`](https://docs.python.org/3/installing/index.html):

```bash
python3 -m pip install py-machineid
```

## Usage

To obtain the raw GUID of the device, use `id() -> str`:

```python
import machineid

print(machineid.id())
```

To obtain an anonymized (hashed) version of the GUID, see below. The
`hashed_id(str) -> str` function takes an optional application ID,
which will ensure a unique ID per-app for the same device.

```python
import machineid

print(machine.hashed_id('myappid'))
print(machine.hashed_id())
```

## Thanks

Special thanks to Denis Brodbeck for his Go package, [`machineid`](https://github.com/denisbrodbeck/machineid).
