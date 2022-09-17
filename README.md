
# Vicarius Automation

Vicarius Automation Project is a Python project for Vicarius UI automation
<p align="center">
    <img src="https://mms.businesswire.com/media/20220209005459/en/1354130/5/vicarius_logo_full_black.jpg"/>
</p>

## Setup

1) Clone this repository
2) Install the required packages using pip
3) Run the tests via pytest framework

Cloning project
```batch
git clone https://github.com/SaharItzhak/Vicarius.git
``` 

Intalling required packages
```batch
pip install -r requirements.txt
``` 

Example pytest command
```batch
pytest tests\scan -n 4 -v -s --headless_mode True --html=reports/report.html -m sign_up -k invalid_email
```
Prerequisites
```batch
Chrome
Python >= 3
```


## Flags

```text
-v: (optional) pytest flag - Controls the verbosity of pytest output
-s: (optional) pytest flag - Show Output, do not capture
-n: (optional) pytest flag - Send tests to multiple CPUs
-m: (optional) pytest flag - Run only tests with matching marker
-k: (optional) pytest flag - Only run tests that match expression (and fixtures)
--html=report.html: (optional) pytest-html flag - Whether to generate an html report
--headless_mode: (optional) automation flag: Whether to hide browser while running the automation
```

## Description

```text
In this project, there are 3 main testing batches:
1) Product page
2) Sign in page
3) Sign up page
This project will run sanity tests on all 3 components.
To run only by expression use the -k flag, example "pytest -k invalid_email".
To run only by markers use the -m flag, example - "pytest -m sign_up".
```
