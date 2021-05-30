# flake8: noqa

"""
    Yourkeys Public API

    This API exposes endpoints that can be used to interact with the Yourkeys system  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@yourkeys.com
    Generated by: https://openapi-generator.tech
"""


__version__ = "1.0.0"

# import ApiClient
from yk_client.api_client import ApiClient

# import Configuration
from yk_client.configuration import Configuration

# import exceptions
from yk_client.exceptions import OpenApiException
from yk_client.exceptions import ApiAttributeError
from yk_client.exceptions import ApiTypeError
from yk_client.exceptions import ApiValueError
from yk_client.exceptions import ApiKeyError
from yk_client.exceptions import ApiException