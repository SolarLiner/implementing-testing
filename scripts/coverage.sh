

CODACY_PROJECT_TOKEN=$(cat coverage_codacy.token)
coverage run src/**/*
coverage xml
python-codacy-coverage
