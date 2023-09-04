#!/usr/bin/python3

from aws_cdk import (
    aws_apigateway as apigateway
)

resource = api.root.add_resource("example")
resource.add_method(
    "GET",
    authorization_type=apigateway.AuthorizationType.NONE  # Sensitive
)

AWS_SECRET_KEY = "AKIAWOKAWOKAWOK"