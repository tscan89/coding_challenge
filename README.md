# Coding Challenge App

A skeleton flask app to use for a coding challenge.

## Install:

You can use a virtual environment (conda, venv, etc):
```
conda env create -f environment.yml
source activate user-profiles
```

Or just pip install from the requirements file
``` 
pip install -r requirements.txt
```

## Running the code

### Spin up the service

```
# start up local server
python -m run 
```

### Making Requests

```
curl -i "http://127.0.0.1:5000/health-check"
```

### Merge repositories within an organization from bitbucket and github (example)

```
curl -i "http://127.0.0.1:5000/merge/mailchimp
```


## Possible unit test scenarios

```
1. Mock non-200 response from bitbucket/github
2. Mock missing expected data field from bitbucket/github
```
