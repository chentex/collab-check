# Collab check

Generated from: [Python Container Action Template](https://github.com/jacobtomlinson/python-container-action)

## Usage

This will check against a repository secret for authorized users, so first we need to set this secret up

- Go to your repository Settings > Secrets
- Click `New repository secret`
- Set the name to `AUTHORIZED`
- In the value section put the `login` handles for the users you want to authorize as a coma sepparated values. E.g.: `octocat,chentex,anotheruser`
- Save

With this in place create a workflow yaml with the following content

### Example workflow

```yaml
name: Collab check
on: [pull_request]
jobs:
  build:
    runs-on: "ubuntu-latest"
    steps:
    - uses: actions/checkout@master
    - name: Run action
      id: collab-check
      env:
        PR_NUMBER: ${{ github.event.number }}
        AUTHORIZED: ${{ secrets.AUTHORIZED }}
      uses: chentex/collab-check@master
```

This action will gather the PR environment and check if the user that created the PR is in the Authorized users secret we created before.

If the user is in the list of the Authorized users it will exit with 0. If not it will exit with 1.
