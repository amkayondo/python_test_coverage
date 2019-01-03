## Test Coverage for Python
[![Build Status](https://travis-ci.org/kayondo-edward/python_test_coverage.svg?branch=master)](https://travis-ci.org/kayondo-edward/python_test_coverage)

### steps to get you started

## Step One (Setting up travis)
1. Signup to [travis](travis-ci.com) with Github
2. Accept the Authorization of Travis CI. You’ll be redirected to GitHub.
3. Click the green Activate button, and select the repositories you want to use with Travis CI.
4. Add a .travis.yml file to your repository to tell Travis CI what to do.

```
    # Identify language and version
    language: python
    python:
        - "3.6"
    # command to install dependencies
    install:
        - pip install -r requirements.txt
        - pip install coveralls
    # command to run tests
    script:
        - python numbers.py cov
    # step two
    after_success:
        coveralls
```    
5. Add the `.travis.yml` file to git, commit and push, to trigger a Travis CI build.
6. Check the build status page to see if your build `passes` or `fails`, according to the return status of the build command by visiting the `Travis CI` and selecting your repository.

## Step Two (setting up coveralls)
1. Signup to [coveralls](https://coveralls.io) with Github
2. Accept the Authorization of Travis CI. You’ll be redirected to GitHub.
3. Add a `Git Repo` on `coveralls`
4. add `.coveralls.yml` file to the project. Follow the next steps to add add the travis key [Next Step](https://coveralls.io/github/kayondo-edward/python_test_coverage)
5. Commit and push, to trigger coveralls