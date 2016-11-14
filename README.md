# pysql
[![Build Status](https://travis-ci.org/mikefaraponov/pysql.svg?branch=master)](https://travis-ci.org/mikefaraponov/pysql) [![Coverage Status](https://coveralls.io/repos/github/mikefaraponov/pysql/badge.svg?branch=master)](https://coveralls.io/github/mikefaraponov/pysql?branch=master)
## Description
Demo for Database Security Course work which contains SQL injection vulnerabilities such as select and union injections

## Up and running
To install the project dependencies:
```sh
    pip install -r requirements.txt
```
To test project modules:
```sh
    nosetests
```
To run project:
```sh
    FLASK_APP=pysql/pysql.py flask run
```
Go to localhost:5000 and pentest it!

## Docker build
Build project by yourself:
```sh
    docker build . -t yourname/major:minor
```
Or pull from my repo:
```sh
    docker pull mikefaraponov/pysql
```

## Credits
* [@mikefaraponov](https://github.com/mikefaraponov)
