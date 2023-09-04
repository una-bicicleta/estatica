#!/usr/bin/python3

from aws_cdk import (
    aws_apigateway as apigateway
)

import hashlib

resource = api.root.add_resource("example")
resource.add_method(
    "GET",
    authorization_type=apigateway.AuthorizationType.NONE  # Sensitive
)

AWS_SECRET_KEY = "AKIAWOKAWOKAWOK"

username = "ADMIN"
password = "PASSWORD"

hashed_password = hashlib.md5(password)


def ok():
    a = True
    if a:
        print("OK")
    else:
        print("Still OK")


def plus(c, d):
    return c + d