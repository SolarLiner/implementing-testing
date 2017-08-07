#! /bin/sh

coverage run src/*
coverage xml
env CODACY_PROJECT_TOKEN=$(cat ./scripts/coverage_codacy.token) python-codacy-coverage
