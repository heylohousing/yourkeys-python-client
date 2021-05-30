"""
    Yourkeys Public API

    This API exposes endpoints that can be used to interact with the Yourkeys system  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@yourkeys.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from yk_client.api_client import ApiClient, Endpoint as _Endpoint
from yk_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)


class CategoryApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __api_progression_purchase_referencenumber_category_categorycode_put(
            self,
            referencenumber,
            categorycode,
            **kwargs
        ):
            """api_progression_purchase_referencenumber_category_categorycode_put  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_progression_purchase_referencenumber_category_categorycode_put(referencenumber, categorycode, async_req=True)
            >>> result = thread.get()

            Args:
                referencenumber (str):
                categorycode (str, none_type):

            Keyword Args:
                _return_http_data_only (bool): response data without head status
                    code and headers. Default is True.
                _preload_content (bool): if False, the urllib3.HTTPResponse object
                    will be returned without reading/decoding response data.
                    Default is True.
                _request_timeout (float/tuple): timeout setting for this request. If one
                    number provided, it will be total request timeout. It can also
                    be a pair (tuple) of (connection, read) timeouts.
                    Default is None.
                _check_input_type (bool): specifies if type checking
                    should be done one the data sent to the server.
                    Default is True.
                _check_return_type (bool): specifies if type checking
                    should be done one the data received from the server.
                    Default is True.
                _host_index (int/None): specifies the index of the server
                    that we want to use.
                    Default is read from the configuration.
                async_req (bool): execute request asynchronously

            Returns:
                None
                    If the method is called asynchronously, returns the request
                    thread.
            """
            kwargs['async_req'] = kwargs.get(
                'async_req', False
            )
            kwargs['_return_http_data_only'] = kwargs.get(
                '_return_http_data_only', True
            )
            kwargs['_preload_content'] = kwargs.get(
                '_preload_content', True
            )
            kwargs['_request_timeout'] = kwargs.get(
                '_request_timeout', None
            )
            kwargs['_check_input_type'] = kwargs.get(
                '_check_input_type', True
            )
            kwargs['_check_return_type'] = kwargs.get(
                '_check_return_type', True
            )
            kwargs['_host_index'] = kwargs.get('_host_index')
            kwargs['referencenumber'] = \
                referencenumber
            kwargs['categorycode'] = \
                categorycode
            return self.call_with_http_info(**kwargs)

        self.api_progression_purchase_referencenumber_category_categorycode_put = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/api/progression/purchase/{referencenumber}/category/{categorycode}',
                'operation_id': 'api_progression_purchase_referencenumber_category_categorycode_put',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'referencenumber',
                    'categorycode',
                ],
                'required': [
                    'referencenumber',
                    'categorycode',
                ],
                'nullable': [
                    'categorycode',
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'referencenumber':
                        (str,),
                    'categorycode':
                        (str, none_type,),
                },
                'attribute_map': {
                    'referencenumber': 'referencenumber',
                    'categorycode': 'categorycode',
                },
                'location_map': {
                    'referencenumber': 'path',
                    'categorycode': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [],
                'content_type': [],
            },
            api_client=api_client,
            callable=__api_progression_purchase_referencenumber_category_categorycode_put
        )
