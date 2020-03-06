<div class="badges">
    <a href="https://pypi.python.org/pypi/drf-social-auth">
        <img src="https://img.shields.io/pypi/v/drf-social-auth.svg">
    </a>
</div>

---

# drf-social-auth

Social Authentication For Django Rest Framework

---

## Overview

Social Authentication For Django Rest Framework

## Requirements

* Python (2.7, 3.3, 3.4)
* Django (1.6, 1.7)

## Installation

Install using `pip`...

```bash
$ pip install drf_social
```
## Usage  
-------  
  
1. Add to Installed Apps
`INSTALLED_APPS = [  
  'social_django',  
  'drf_social'  
] `  
2. Configure provider at django admin

## Customization
-------------

Custom JWT Token Response
1. Inherit from SocialLoginView with custom serializer


## Documentation

To build the documentation, you'll need to install `mkdocs`.

```bash
$ pip install mkdocs
```

To preview the documentation:

```bash
$ mkdocs serve
Running at: http://127.0.0.1:8000/
```

To build the documentation:

```bash
$ mkdocs build
```
