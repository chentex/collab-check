# Collab check

Generated from: (Python Container Action Template)[https://github.com/jacobtomlinson/python-container-action]

## Usage

This action will gather the PR environment and check if the user that created the PR is in the Authorized users.

If this check succeeds will return a 0 code, after this action you could run other actions.

If it fails it will exit with error code 1.

### Example workflow

```yaml
name: Collab check
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
    - name: Run action
      uses: chentex/collab-check@master
```

## Examples

> NOTE: People ❤️ cut and paste examples. Be generous with them!
