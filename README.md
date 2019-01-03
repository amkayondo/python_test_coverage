## Test Coverage for Python
[![Build Status](https://travis-ci.org/kayondo-edward/python_test_coverage.svg?branch=master)](https://travis-ci.org/kayondo-edward/python_test_coverage)

### steps to get you started
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
    
    after_success:
        coveralls
```    
5. Add the `.travis.yml` file to git, commit and push, to trigger a Travis CI build.
6. Check the build status page to see if your build `passes` or `fails`, according to the return status of the build command by visiting the `Travis CI` and selecting your repository.

