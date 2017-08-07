# Implementing automatic testing and coverage checking for your GitHub repo

Apparently I'm the only person here who doesn't know how to do this, so this may be useless, but it helps me understand; so here is a small guide to getting your project tested automatically, with coveage reports.  
And because every node.js programmer seems to know hoz to do this, we'll focus on Python.

We will use Travis CI, Codacy and Coveralls, which are all free for open-source projects. (Thanks guys for doing this!). I'm assuming you'll know how to sign up using GitHub, and select your project(s) in those services by yourself. 

## Step 1: Writing some code.

Wether your routine starts with code or with tests, you should first get your codebase up and running. Having nothing to test will seriously impair your ability to add automatic testing to such (nonexistant) code.

## Step 2: Let's check for coverage

We'll first setup coverage on Coveralls, then on Codacy. I find it better to start with this rather than Travis as you'll come to build your scripts along while setting up coverage, and then you'll only have to plug them in Travis to automate the process.

### [Coveralls](https://coveralls.io/) [![Coverage Status](https://coveralls.io/repos/github/SolarLiner/implementing-testing/badge.svg?branch=master)](https://coveralls.io/github/SolarLiner/implementing-testing?branch=master)

Coveralls's interface with python is `python-coveralls` which is easily installeable with `pip`. After that, create a configuration file for it by creating a new file at the root called `.coveralls.yml` and edit it to add your repo\_token. Find your repo\_token by going to the settings on the Coveralls project.

Once everything is setup, just run  `coverage run $FILES && coverage xml && coveralls`

### [Codacy](https://www.codacy.com/) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/762b882cc76a4fddbd56587dfcbc275d)](https://www.codacy.com/app/solarliner/implementing-testing?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=SolarLiner/implementing-testing&amp;utm_campaign=Badge_Grade) [![Codacy Badge](https://api.codacy.com/project/badge/Coverage/762b882cc76a4fddbd56587dfcbc275d)](https://www.codacy.com/app/solarliner/implementing-testing?utm_source=github.com&utm_medium=referral&utm_content=SolarLiner/implementing-testing&utm_campaign=Badge_Coverage)

In order to send coverage to Codacy you'll need to install the python package `codacy-coverage` or similar for your language In Ubuntu 16.04+, you'll need to install and activate `virtualenv` for your repository as to avoid conflicts with the patched version of pip Canonical offers.

Then it's a matter of running your tests, `coverage run $FILES && coverage xml` and then `CODACY_PROJECT_TOKEN=$TOKEN python-codacy-coverage`. You can read more about setting up Codacy [here](https://support.codacy.com/hc/en-us/articles/207993835-Add-coverage-to-your-repo).  
Note that you don't need to run coverage twice, you can just chain codacy after coveralls.

Although we focused on code coverage with Codacy, the service offers much more analytics of your code.  
You don't need the two either, you can choose only one or the other: or a different service should one fit your needs better.

## Step 2: Get some automation going on

Now that we have everything ready, we'll strap Travis CI onto our repo. For the end user, Travis will be the most important part of the project as it will be able to test and build your project for you.  
Once you've activated Travis for your repo, check "build only if travis.yml is present" and maybe activate a daily or weekly build of your project, depending on how often it is updated.

### Configuring Travis CI

Since we have all our scripts ready, configuring Travis will be simple enough. Add a `.travis.yml` file at the root of your repo and add the following lines:
```yaml
dist: xenial
language: python
python:
    - "2.7" # List all supported versions of python here

install: pip install -r pip_req_test.txt
script: scripts/test.sh
after_success: scripts/coverage.sh
```

Change accordingly, but otherwise the configuration is there.  
Note that the different build steps are ran in order: `install > script > after_success | after_failure`. For a complete doc about the configuration, refer to the Travis doc: <https://docs.travis-ci.com/user/customizing-the-build>