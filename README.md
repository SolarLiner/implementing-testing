# Implementing automatic testing and coverage checking for your GitHub repo

Apparently I'm the only person here who doesn't know how to do this, so this may be useless, but it helps me understand; so here is a small guide to getting your project tested automatically, with coveage reports.  
And because every node.js programmer seems to know hoz to do this, we'll focus on Python.

We will use Travis CI, Codacy and Coveralls, which are all free for open-source projects. (Thanks guys for doing this!)

## Step 1: Writing some code.

Wether your routine starts with code or with tests, you should first get your codebase up and running. Having nothing to test will seriously impair your ability to add automatic testing to such (nonexistant) code.

## Step 2: Let's check for coverage

We'll first setup coverage on Coveralls, then on Codacy. I find it better to start with this rather than Travis as you'll come to build your scripts along while setting up coverage, and then you'll only have to plug them in Travis to automate the process.

### Coveralls

