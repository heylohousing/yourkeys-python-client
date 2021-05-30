# openapi_client.LeadsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_leads_broker_add_post**](LeadsApi.md#api_leads_broker_add_post) | **POST** /api/Leads/Broker/Add | Endpoint for SPF to add leads. Validates the request then calls the leads API.


# **api_leads_broker_add_post**
> api_leads_broker_add_post()

Endpoint for SPF to add leads. Validates the request then calls the leads API.

### Example

* Api Key Authentication (Bearer):
```python
import time
import openapi_client
from openapi_client.api import leads_api
from openapi_client.model.add_broker_leads_request import AddBrokerLeadsRequest
from pprint import pprint
# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
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
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = leads_api.LeadsApi(api_client)
    add_broker_leads_request = AddBrokerLeadsRequest(
        leads=[
            AddBrokerLeadRequest(
                lead_reference="lead_reference_example",
                lead_date=dateutil_parser('1970-01-01T00:00:00.00Z'),
                status="status_example",
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
        # Endpoint for SPF to add leads. Validates the request then calls the leads API.
        api_instance.api_leads_broker_add_post(add_broker_leads_request=add_broker_leads_request)
    except openapi_client.ApiException as e:
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

