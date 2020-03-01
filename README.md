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

Healthcheck:

```
curl -i "http://127.0.0.1:5000/health-check"
```

Merge repositories within an organization from bitbucket and github:

```
curl -i "http://127.0.0.1:5000/merge/{organization}"
```

Merge repositories within an organization from bitbucket and github (example):

Example request:
```
curl -i "http://127.0.0.1:5000/merge/mailchimp"
```

Example response:
```
{
    "Forked Repos": 4,
    "Original Repos": 26,
    "Total Watchers": 8030,
    "Repos": {
        "Topics": [
            "ChimpKit2",
            "email-blueprints",
            "MailChimp.tmbundle",
            "OAuth2-sample-apps",
            "play",
            "ChimpKit3",
            "statistrano",
            "mc_markdown",
            "IronBox-PHP",
            "Specs",
            "APIv3-examples",
            "content-style-guide",
            "country-region-selector",
            "mc-magento",
            "middleman-with-md-submodule-example",
            "mc-woocommerce",
            "mc-magento2",
            "auto-value-gson",
            "Mailchimp-SDK-iOS",
            "Mailchimp-SDK-Android",
            "mandrill-api-php",
            "mandrill-api-python",
            "mandrill-api-js",
            "mandrill-api-ruby",
            "mailchimp-api-node",
            "mailchimp-api-php",
            "mailchimp-api-python",
            "mailchimp-api-ruby",
            "mandrill-api-dart",
            "mandrill-api-node"
        ],
        "Count": 30
    },
    "Languages": {
        "Types": [
            "objective-c",
            "php",
            "ruby",
            "python",
            "javascript",
            "css",
            "java",
            "swift",
            "kotlin",
            "dart"
        ],
        "Count": 10
    }
}
```


## Possible unit test scenarios

```
1. Mock non-200 response from bitbucket/github
2. Mock missing expected data field from bitbucket/github
```
