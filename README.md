# Implementing automatic testing and coverage checking for your GitHub repo

Apparently I'm the only person here who doesn't know how to do this, so this may be useless, but it helps me understand; so here is a small guide to getting your project tested automatically, with coveage reports.  
And because every node.js programmer seems to know hoz to do this, we'll focus on Python.

We will use Travis CI, Codacy and Coveralls, which are all free for open-source projects. (Thanks guys for doing this!)

## Step 1: Writing some code.

Wether your routine starts with code or with tests, you should first get your codebase up and running. Having nothing to test will seriously impair your ability to add automatic testing to such (nonexistant) code.

## Step 2: Let's check for coverage

We'll first setup coverage on Coveralls, then on Codacy. I find it better to start with this rather than Travis as you'll come to build your scripts along while setting up coverage, and then you'll only have to plug them in Travis to automate the process.

### Coveralls

Coveralls's interface with python is `python-coveralls` which is easily installeable with `pip`. After that, create a configuration file for it by creating a new file at the root called `.coveralls.yml` and edit it to add your repo\_token. Find your repo\_token by going to the settings on the Coveralls project.

### Codacy

In order to send coverage to Codacy you'll need to install the python package `codacy-coverage` or similar for your language In Ubuntu 16.04+, you'll need to install and activate `virtualenv` for your repository as to avoid conflicts with the patched version of pip Canonical offers.

Then it's a matter of running your tests, `coverage run $FILES && coverage xml` and then `CODACY_PROJECT_TOKEN=$TOKEN python-codacy-coverage`. You can read more about setting up Codacy [here](https://support.codacy.com/hc/en-us/articles/207993835-Add-coverage-to-your-repo).