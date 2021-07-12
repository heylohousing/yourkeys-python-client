# yk_client.LeadsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_leads_broker_add_post**](LeadsApi.md#api_leads_broker_add_post) | **POST** /api/Leads/Broker/Add | Endpoint for brokers to add leads. Validates the request then calls the leads API.
[**api_leads_broker_mortgage_application_submitted_post**](LeadsApi.md#api_leads_broker_mortgage_application_submitted_post) | **POST** /api/Leads/Broker/MortgageApplicationSubmitted | Endpoint for brokers to notify that the mortgage application has been submitted to the lender. &lt;br /&gt;  Mapped to progression milestone &#x3D;&gt; S3-1 Mortgage Application Submitted.
[**api_leads_broker_mortgage_offer_issued_post**](LeadsApi.md#api_leads_broker_mortgage_offer_issued_post) | **POST** /api/Leads/Broker/MortgageOfferIssued | Endpoint for brokers to notify that the mortgage offer has been issued. &lt;br /&gt;  Mapped to progression milestone &#x3D;&gt; S3-4 Mortgage Offer Issued.
[**api_leads_broker_reservation_reservation_id_get**](LeadsApi.md#api_leads_broker_reservation_reservation_id_get) | **GET** /api/Leads/Broker/Reservation/{reservationId} | 
[**api_leads_broker_reservations_get**](LeadsApi.md#api_leads_broker_reservations_get) | **GET** /api/Leads/Broker/Reservations | Endpoint for brokers to get reservations associated with leads.
[**api_leads_broker_update_put**](LeadsApi.md#api_leads_broker_update_put) | **PUT** /api/Leads/Broker/Update | Endpoint for brokers to update leads. Validates the request then calls the leads API.
[**api_leads_broker_valuation_instruction_post**](LeadsApi.md#api_leads_broker_valuation_instruction_post) | **POST** /api/Leads/Broker/ValuationInstruction | Endpoint for brokers to notify that the valuation has been booked. &lt;br /&gt;  Mapped to progression milestone &#x3D;&gt; S3-2 Valuation Booked.
[**api_leads_broker_valuation_received_post**](LeadsApi.md#api_leads_broker_valuation_received_post) | **POST** /api/Leads/Broker/ValuationReceived | Endpoint for brokers to notify that the valuation has been received (survey completed). &lt;br /&gt;  Mapped to progression milestone &#x3D;&gt; S3-3 Valuation Survey Completed.


# **api_leads_broker_add_post**
> api_leads_broker_add_post()

Endpoint for brokers to add leads. Validates the request then calls the leads API.

### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_client
from yk_client.api import leads_api
from yk_client.model.add_broker_leads_request import AddBrokerLeadsRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    add_broker_leads_request = AddBrokerLeadsRequest(
        leads=[
            AddBrokerLeadRequest(
                lead_reference="lead_reference_example",
                lead_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="status_example",
                case_reference="case_reference_example",
                applicants=[
                    Applicant(
                        contact_id="contact_id_example",
                        first_name="first_name_example",
                        last_name="last_name_example",
                        date_of_birth=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        phone="phone_example",
                        email="email_example",
                    ),
                ],
            ),
        ],
    ) # AddBrokerLeadsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Endpoint for brokers to add leads. Validates the request then calls the leads API.
        api_instance.api_leads_broker_add_post(add_broker_leads_request=add_broker_leads_request)
    except yk_client.ApiException as e:
        print("Exception when calling LeadsApi->api_leads_broker_add_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_broker_leads_request** | [**AddBrokerLeadsRequest**](AddBrokerLeadsRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**409** | Conflict |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_leads_broker_mortgage_application_submitted_post**
> api_leads_broker_mortgage_application_submitted_post()

Endpoint for brokers to notify that the mortgage application has been submitted to the lender. <br />  Mapped to progression milestone => S3-1 Mortgage Application Submitted.

### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_client
from yk_client.api import leads_api
from yk_client.model.application_submitted_to_lender_request import ApplicationSubmittedToLenderRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    application_submitted_to_lender_request = ApplicationSubmittedToLenderRequest(
        case=[
            ApplicationLenderSubmission(
                lender="lender_example",
                lender_sub_date="lender_sub_date_example",
                target_offer_date="target_offer_date_example",
                lead_reference="lead_reference_example",
                case_reference="case_reference_example",
                status="status_example",
            ),
        ],
    ) # ApplicationSubmittedToLenderRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Endpoint for brokers to notify that the mortgage application has been submitted to the lender. <br />  Mapped to progression milestone => S3-1 Mortgage Application Submitted.
        api_instance.api_leads_broker_mortgage_application_submitted_post(application_submitted_to_lender_request=application_submitted_to_lender_request)
    except yk_client.ApiException as e:
        print("Exception when calling LeadsApi->api_leads_broker_mortgage_application_submitted_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_submitted_to_lender_request** | [**ApplicationSubmittedToLenderRequest**](ApplicationSubmittedToLenderRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_leads_broker_mortgage_offer_issued_post**
> api_leads_broker_mortgage_offer_issued_post()

Endpoint for brokers to notify that the mortgage offer has been issued. <br />  Mapped to progression milestone => S3-4 Mortgage Offer Issued.

### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_client
from yk_client.api import leads_api
from yk_client.model.mortgage_offer_issued_request import MortgageOfferIssuedRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    mortgage_offer_issued_request = MortgageOfferIssuedRequest(
        case=[
            MortgageOfferIssued(
                offer_issued_date="offer_issued_date_example",
                offer_expiry_date="offer_expiry_date_example",
                lead_reference="lead_reference_example",
                case_reference="case_reference_example",
                status="status_example",
            ),
        ],
    ) # MortgageOfferIssuedRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Endpoint for brokers to notify that the mortgage offer has been issued. <br />  Mapped to progression milestone => S3-4 Mortgage Offer Issued.
        api_instance.api_leads_broker_mortgage_offer_issued_post(mortgage_offer_issued_request=mortgage_offer_issued_request)
    except yk_client.ApiException as e:
        print("Exception when calling LeadsApi->api_leads_broker_mortgage_offer_issued_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mortgage_offer_issued_request** | [**MortgageOfferIssuedRequest**](MortgageOfferIssuedRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_leads_broker_reservation_reservation_id_get**
> BrokerLeadReservationsResponse api_leads_broker_reservation_reservation_id_get(reservation_id)



### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_client
from yk_client.api import leads_api
from yk_client.model.broker_lead_reservations_response import BrokerLeadReservationsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    reservation_id = "reservationId_example" # str | 

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.api_leads_broker_reservation_reservation_id_get(reservation_id)
        pprint(api_response)
    except yk_client.ApiException as e:
        print("Exception when calling LeadsApi->api_leads_broker_reservation_reservation_id_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **reservation_id** | **str**|  |

### Return type

[**BrokerLeadReservationsResponse**](BrokerLeadReservationsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_leads_broker_reservations_get**
> BrokerLeadReservationsResponse api_leads_broker_reservations_get()

Endpoint for brokers to get reservations associated with leads.

### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_client
from yk_client.api import leads_api
from yk_client.model.broker_lead_reservations_response import BrokerLeadReservationsResponse
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Endpoint for brokers to get reservations associated with leads.
        api_response = api_instance.api_leads_broker_reservations_get()
        pprint(api_response)
    except yk_client.ApiException as e:
        print("Exception when calling LeadsApi->api_leads_broker_reservations_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**BrokerLeadReservationsResponse**](BrokerLeadReservationsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_leads_broker_update_put**
> api_leads_broker_update_put()

Endpoint for brokers to update leads. Validates the request then calls the leads API.

### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_client
from yk_client.api import leads_api
from yk_client.model.add_broker_leads_request import AddBrokerLeadsRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    add_broker_leads_request = AddBrokerLeadsRequest(
        leads=[
            AddBrokerLeadRequest(
                lead_reference="lead_reference_example",
                lead_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="status_example",
                case_reference="case_reference_example",
                applicants=[
                    Applicant(
                        contact_id="contact_id_example",
                        first_name="first_name_example",
                        last_name="last_name_example",
                        date_of_birth=dateutil_parser('1970-01-01T00:00:00.00Z'),
                        phone="phone_example",
                        email="email_example",
                    ),
                ],
            ),
        ],
    ) # AddBrokerLeadsRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Endpoint for brokers to update leads. Validates the request then calls the leads API.
        api_instance.api_leads_broker_update_put(add_broker_leads_request=add_broker_leads_request)
    except yk_client.ApiException as e:
        print("Exception when calling LeadsApi->api_leads_broker_update_put: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add_broker_leads_request** | [**AddBrokerLeadsRequest**](AddBrokerLeadsRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_leads_broker_valuation_instruction_post**
> api_leads_broker_valuation_instruction_post()

Endpoint for brokers to notify that the valuation has been booked. <br />  Mapped to progression milestone => S3-2 Valuation Booked.

### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_client
from yk_client.api import leads_api
from yk_client.model.valuation_instruction_request import ValuationInstructionRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    valuation_instruction_request = ValuationInstructionRequest(
        case=[
            ValuationInstruction(
                valuation_instruction_date="valuation_instruction_date_example",
                lead_reference="lead_reference_example",
                case_reference="case_reference_example",
                status="status_example",
            ),
        ],
    ) # ValuationInstructionRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Endpoint for brokers to notify that the valuation has been booked. <br />  Mapped to progression milestone => S3-2 Valuation Booked.
        api_instance.api_leads_broker_valuation_instruction_post(valuation_instruction_request=valuation_instruction_request)
    except yk_client.ApiException as e:
        print("Exception when calling LeadsApi->api_leads_broker_valuation_instruction_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **valuation_instruction_request** | [**ValuationInstructionRequest**](ValuationInstructionRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_leads_broker_valuation_received_post**
> api_leads_broker_valuation_received_post()

Endpoint for brokers to notify that the valuation has been received (survey completed). <br />  Mapped to progression milestone => S3-3 Valuation Survey Completed.

### Example

* Api Key Authentication (Bearer):
```python
import time
import yk_client
from yk_client.api import leads_api
from yk_client.model.valuation_received_request import ValuationReceivedRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = yk_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with yk_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    valuation_received_request = ValuationReceivedRequest(
        case=[
            ValuationReceived(
                valuation_received_date="valuation_received_date_example",
                lead_reference="lead_reference_example",
                case_reference="case_reference_example",
                status="status_example",
            ),
        ],
    ) # ValuationReceivedRequest |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Endpoint for brokers to notify that the valuation has been received (survey completed). <br />  Mapped to progression milestone => S3-3 Valuation Survey Completed.
        api_instance.api_leads_broker_valuation_received_post(valuation_received_request=valuation_received_request)
    except yk_client.ApiException as e:
        print("Exception when calling LeadsApi->api_leads_broker_valuation_received_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **valuation_received_request** | [**ValuationReceivedRequest**](ValuationReceivedRequest.md)|  | [optional]

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

