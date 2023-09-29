resource "aws_api_gateway_method" "noncompliantapi" {
  authorization = "NONE" # Sensitive
  http_method   = "GET"
}

resource "aws_instance" "example" {
  associate_public_ip_address = true # Sensitive
}

resource "aws_dms_replication_instance" "example" {
  publicly_accessible = true # Sensitive
}
