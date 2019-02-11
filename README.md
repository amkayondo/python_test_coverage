## Test Coverage for Python
[![Build Status](https://travis-ci.org/kayondo-edward/python_test_coverage.svg?branch=master)](https://travis-ci.org/kayondo-edward/python_test_coverage)

### steps to get you started
## Here is how it Work
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
    # Run pytest
        - pytest
    # step two
    after_success:
        coveralls
```    
5. Add the `.travis.yml` file to git, commit and push, to trigger a Travis CI build.
6. Check the build status page to see if your build `passes` or `fails`, according to the return status of the build command by visiting the `Travis CI` and selecting your repository.

## Step Two (setting up coveralls)
`coveralls.io` is one of the cloud-based services that can collect and display test coverage reports. It is free for Open Source projects hosted on `GitHub` or `BitBucket`.

1. Make sure Travis-CI is already enabled for your project and the tests pass.

2. Register on the `Coveralls`. web site using your `GitHub` account. Look for the "`Add repos`" button, select the GitHub repo that you'd like to enable.

3. You already have a `.travis.yml` file in the root of your repository, now you only need to add a few more entries.

```
 # Identify language and version
    language: python
    python:
        - "3.6"
    # command to install dependencies
    install:
        - pip install -r requirements.txt
        - pip install pytest
        - pip install pytest-cov
        - pip install coveralls
    # command to run tests
    script:
        - pytest --cov=test_coverage/
    # step two
    after_success:
        coveralls
```
The important part is to install `pytest`, `pytest-cov `that allows us to generate the coverage report locally. (Meaning on the `Travis-CI` server.) We also need to install `coveralls` that can submit the the report to the `Coveralls.io`.

In the script part we need to run `pytest` with the `--cov` flag. You don't need to give a parameter to that `flag`, but then you might get reports on code that is not relevant to your application. It is better to pass the directory name of your module to it like `--cov=test_coverage/` so the coverage report will be restricted to code in that directory.

You also need to tell Travis-CI to run the `coveralls` command after the test ran successfully.

That's it. Your coverage reports should start flowing to `Coveralls.io`
