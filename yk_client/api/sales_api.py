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
from yk_client.model.create_reservation_request import CreateReservationRequest
from yk_client.model.create_reservation_response import CreateReservationResponse


class SalesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

        def __api_reservation_post(
            self,
            **kwargs
        ):
            """api_reservation_post  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_reservation_post(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                create_reservation_request (CreateReservationRequest): [optional]
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
                CreateReservationResponse
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
            return self.call_with_http_info(**kwargs)

        self.api_reservation_post = _Endpoint(
            settings={
                'response_type': (CreateReservationResponse,),
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/api/Reservation',
                'operation_id': 'api_reservation_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'create_reservation_request',
                ],
                'required': [],
                'nullable': [
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
                    'create_reservation_request':
                        (CreateReservationRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'create_reservation_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__api_reservation_post
        )

        def __api_sales_reservation_post(
            self,
            **kwargs
        ):
            """api_sales_reservation_post  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_sales_reservation_post(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                create_reservation_request (CreateReservationRequest): [optional]
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
                CreateReservationResponse
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
            return self.call_with_http_info(**kwargs)

        self.api_sales_reservation_post = _Endpoint(
            settings={
                'response_type': (CreateReservationResponse,),
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/api/sales/Reservation',
                'operation_id': 'api_sales_reservation_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'create_reservation_request',
                ],
                'required': [],
                'nullable': [
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
                    'create_reservation_request':
                        (CreateReservationRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'create_reservation_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json-patch+json',
                    'application/json',
                    'text/json',
                    'application/*+json'
                ]
            },
            api_client=api_client,
            callable=__api_sales_reservation_post
        )

        def __api_sales_reservation_upgrades_and_extras_post(
            self,
            **kwargs
        ):
            """api_sales_reservation_upgrades_and_extras_post  # noqa: E501

            This method makes a synchronous HTTP request by default. To make an
            asynchronous HTTP request, please pass async_req=True

            >>> thread = api.api_sales_reservation_upgrades_and_extras_post(async_req=True)
            >>> result = thread.get()


            Keyword Args:
                seller_reference (str, none_type): [optional]
                purchase_reference (str, none_type): [optional]
                development_id (str, none_type): [optional]
                plot_id (str, none_type): [optional]
                file_stream (file_type, none_type): [optional]
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
            return self.call_with_http_info(**kwargs)

        self.api_sales_reservation_upgrades_and_extras_post = _Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'Bearer'
                ],
                'endpoint_path': '/api/sales/Reservation/UpgradesAndExtras',
                'operation_id': 'api_sales_reservation_upgrades_and_extras_post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'seller_reference',
                    'purchase_reference',
                    'development_id',
                    'plot_id',
                    'file_stream',
                ],
                'required': [],
                'nullable': [
                    'seller_reference',
                    'purchase_reference',
                    'development_id',
                    'plot_id',
                    'file_stream',
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
                    'seller_reference':
                        (str, none_type,),
                    'purchase_reference':
                        (str, none_type,),
                    'development_id':
                        (str, none_type,),
                    'plot_id':
                        (str, none_type,),
                    'file_stream':
                        (file_type, none_type,),
                },
                'attribute_map': {
                    'seller_reference': 'SellerReference',
                    'purchase_reference': 'PurchaseReference',
                    'development_id': 'DevelopmentId',
                    'plot_id': 'PlotId',
                    'file_stream': 'FileStream',
                },
                'location_map': {
                    'seller_reference': 'form',
                    'purchase_reference': 'form',
                    'development_id': 'form',
                    'plot_id': 'form',
                    'file_stream': 'form',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'multipart/form-data'
                ]
            },
            api_client=api_client,
            callable=__api_sales_reservation_upgrades_and_extras_post
        )
