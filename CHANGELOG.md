# Changelog

## v1.0.0

- Fix order of operations of HMAC function in `hashed_id()`. Previously, the
  function computed `HMAC(app_id, device_id)`. It now matches the Go [machineid](https://github.com/keygen-sh/machineid)
  package, computing `HMAC(device_id, app_id)`. This is a breaking change for
  all previously generated hashed IDs, so update accordingly.
