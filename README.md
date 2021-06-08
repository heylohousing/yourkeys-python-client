# yk-client
This API exposes endpoints that can be used to interact with the Yourkeys system

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://www.yourkeys.com](https://www.yourkeys.com)

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import yk_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import yk_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import yk_client
from pprint import pprint
from yk_client.api import category_api
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
    api_instance = category_api.CategoryApi(api_client)
    referencenumber = "referencenumber_example" # str | 
categorycode = "categorycode_example" # str, none_type | 

    try:
        api_instance.api_progression_purchase_referencenumber_category_categorycode_put(referencenumber, categorycode)
    except yk_client.ApiException as e:
        print("Exception when calling CategoryApi->api_progression_purchase_referencenumber_category_categorycode_put: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*CategoryApi* | [**api_progression_purchase_referencenumber_category_categorycode_put**](docs/CategoryApi.md#api_progression_purchase_referencenumber_category_categorycode_put) | **PUT** /api/progression/purchase/{referencenumber}/category/{categorycode} | 
*DocumentsApi* | [**api_reservation_referencenumber_documents_category_company_id_get**](docs/DocumentsApi.md#api_reservation_referencenumber_documents_category_company_id_get) | **GET** /api/reservation/{referencenumber}/documents/{category}/{companyId} | 
*DocumentsApi* | [**api_reservation_referencenumber_documents_category_get**](docs/DocumentsApi.md#api_reservation_referencenumber_documents_category_get) | **GET** /api/reservation/{referencenumber}/documents/{category} | 
*DocumentsApi* | [**api_reservation_referencenumber_documents_file_file_id_get**](docs/DocumentsApi.md#api_reservation_referencenumber_documents_file_file_id_get) | **GET** /api/reservation/{referencenumber}/documents/file/{fileId} | 
*DocumentsApi* | [**api_reservation_referencenumber_documents_instructionpack_file_id_get**](docs/DocumentsApi.md#api_reservation_referencenumber_documents_instructionpack_file_id_get) | **GET** /api/reservation/{referencenumber}/documents/instructionpack/{fileId} | 
*DocumentsApi* | [**api_reservation_referencenumber_documents_instructionpack_get**](docs/DocumentsApi.md#api_reservation_referencenumber_documents_instructionpack_get) | **GET** /api/reservation/{referencenumber}/documents/instructionpack | 
*EventApi* | [**api_progression_purchase_referencenumber_event_eventcode_put**](docs/EventApi.md#api_progression_purchase_referencenumber_event_eventcode_put) | **PUT** /api/progression/purchase/{referencenumber}/event/{eventcode} | 
*HealthCheckApi* | [**api_health_check_get**](docs/HealthCheckApi.md#api_health_check_get) | **GET** /api/HealthCheck | 
*InventoryApi* | [**api_inventory_blocks_delete**](docs/InventoryApi.md#api_inventory_blocks_delete) | **DELETE** /api/Inventory/blocks | 
*InventoryApi* | [**api_inventory_blocks_post**](docs/InventoryApi.md#api_inventory_blocks_post) | **POST** /api/Inventory/blocks | 
*InventoryApi* | [**api_inventory_blocks_put**](docs/InventoryApi.md#api_inventory_blocks_put) | **PUT** /api/Inventory/blocks | 
*InventoryApi* | [**api_inventory_development_livestatusupdate_put**](docs/InventoryApi.md#api_inventory_development_livestatusupdate_put) | **PUT** /api/Inventory/development/livestatusupdate | 
*InventoryApi* | [**api_inventory_developments_post**](docs/InventoryApi.md#api_inventory_developments_post) | **POST** /api/Inventory/developments | 
*InventoryApi* | [**api_inventory_developments_put**](docs/InventoryApi.md#api_inventory_developments_put) | **PUT** /api/Inventory/developments | 
*InventoryApi* | [**api_inventory_housebuilder_seller_reference_development_development_id_block_block_id_plots_get**](docs/InventoryApi.md#api_inventory_housebuilder_seller_reference_development_development_id_block_block_id_plots_get) | **GET** /api/Inventory/housebuilder/{sellerReference}/development/{developmentId}/block/{blockId}/plots | 
*InventoryApi* | [**api_inventory_housebuilder_seller_reference_development_development_id_blocks_get**](docs/InventoryApi.md#api_inventory_housebuilder_seller_reference_development_development_id_blocks_get) | **GET** /api/Inventory/housebuilder/{sellerReference}/development/{developmentId}/blocks | 
*InventoryApi* | [**api_inventory_housebuilder_seller_reference_developments_get**](docs/InventoryApi.md#api_inventory_housebuilder_seller_reference_developments_get) | **GET** /api/Inventory/housebuilder/{sellerReference}/developments | 
*InventoryApi* | [**api_inventory_plots_delete**](docs/InventoryApi.md#api_inventory_plots_delete) | **DELETE** /api/Inventory/plots | 
*InventoryApi* | [**api_inventory_plots_post**](docs/InventoryApi.md#api_inventory_plots_post) | **POST** /api/Inventory/plots | 
*InventoryApi* | [**api_inventory_plots_put**](docs/InventoryApi.md#api_inventory_plots_put) | **PUT** /api/Inventory/plots | 
*LeadsApi* | [**api_leads_broker_add_post**](docs/LeadsApi.md#api_leads_broker_add_post) | **POST** /api/Leads/Broker/Add | Endpoint for brokers to add leads. Validates the request then calls the leads API.
*LeadsApi* | [**api_leads_broker_mortgage_application_submitted_post**](docs/LeadsApi.md#api_leads_broker_mortgage_application_submitted_post) | **POST** /api/Leads/Broker/MortgageApplicationSubmitted | Endpoint for brokers to notify that the mortgage application has been submitted to the lender. &lt;br /&gt;  Mapped to progression milestone &#x3D;&gt; S3-1 Mortgage Application Submitted.
*LeadsApi* | [**api_leads_broker_mortgage_offer_issued_post**](docs/LeadsApi.md#api_leads_broker_mortgage_offer_issued_post) | **POST** /api/Leads/Broker/MortgageOfferIssued | Endpoint for brokers to notify that the mortgage offer has been issued. &lt;br /&gt;  Mapped to progression milestone &#x3D;&gt; S3-4 Mortgage Offer Issued.
*LeadsApi* | [**api_leads_broker_reservation_reservation_id_get**](docs/LeadsApi.md#api_leads_broker_reservation_reservation_id_get) | **GET** /api/Leads/Broker/Reservation/{reservationId} | 
*LeadsApi* | [**api_leads_broker_reservations_get**](docs/LeadsApi.md#api_leads_broker_reservations_get) | **GET** /api/Leads/Broker/Reservations | Endpoint for brokers to get reservations associated with leads.
*LeadsApi* | [**api_leads_broker_valuation_instruction_post**](docs/LeadsApi.md#api_leads_broker_valuation_instruction_post) | **POST** /api/Leads/Broker/ValuationInstruction | Endpoint for brokers to notify that the valuation has been booked. &lt;br /&gt;  Mapped to progression milestone &#x3D;&gt; S3-2 Valuation Booked.
*LeadsApi* | [**api_leads_broker_valuation_received_post**](docs/LeadsApi.md#api_leads_broker_valuation_received_post) | **POST** /api/Leads/Broker/ValuationReceived | Endpoint for brokers to notify that the valuation has been received (survey completed). &lt;br /&gt;  Mapped to progression milestone &#x3D;&gt; S3-3 Valuation Survey Completed.
*LogoApi* | [**logo_development_main_account_development_id_get**](docs/LogoApi.md#logo_development_main_account_development_id_get) | **GET** /Logo/development-main-account/{developmentId} | 
*LogoApi* | [**logo_seller_developer_id_get**](docs/LogoApi.md#logo_seller_developer_id_get) | **GET** /Logo/seller/{developerId} | 
*OnfidoApi* | [**api_onfido_webhook_post**](docs/OnfidoApi.md#api_onfido_webhook_post) | **POST** /api/Onfido/Webhook | 
*PassthroughApi* | [**api_passthrough_generate_passthrough_url_post**](docs/PassthroughApi.md#api_passthrough_generate_passthrough_url_post) | **POST** /api/Passthrough/GeneratePassthroughUrl | 
*ProgressionApi* | [**api_progression_purchase_referencenumber_code_put**](docs/ProgressionApi.md#api_progression_purchase_referencenumber_code_put) | **PUT** /api/progression/purchase/{referencenumber}/{code} | 
*RegressionApi* | [**api_regression_purchase_referencenumber_code_delete**](docs/RegressionApi.md#api_regression_purchase_referencenumber_code_delete) | **DELETE** /api/regression/purchase/{referencenumber}/{code} | 
*RegressionApi* | [**api_regression_purchase_referencenumber_last_delete**](docs/RegressionApi.md#api_regression_purchase_referencenumber_last_delete) | **DELETE** /api/regression/purchase/{referencenumber}/last | 
*SalesApi* | [**api_reservation_post**](docs/SalesApi.md#api_reservation_post) | **POST** /api/Reservation | 
*SalesApi* | [**api_sales_reservation_post**](docs/SalesApi.md#api_sales_reservation_post) | **POST** /api/sales/Reservation | 
*SalesApi* | [**api_sales_reservation_upgrades_and_extras_post**](docs/SalesApi.md#api_sales_reservation_upgrades_and_extras_post) | **POST** /api/sales/Reservation/UpgradesAndExtras | 
*SellerApi* | [**api_seller_reference_number_developments_development_id_plots_get**](docs/SellerApi.md#api_seller_reference_number_developments_development_id_plots_get) | **GET** /api/Seller/{referenceNumber}/developments/{developmentId}/plots | Returns all plots with an AVABL status for a the supplied development that the supplied seller has access to.
*SellerApi* | [**api_seller_reference_number_developments_get**](docs/SellerApi.md#api_seller_reference_number_developments_get) | **GET** /api/Seller/{referenceNumber}/developments | 


## Documentation For Models

 - [AddBrokerLeadRequest](docs/AddBrokerLeadRequest.md)
 - [AddBrokerLeadsRequest](docs/AddBrokerLeadsRequest.md)
 - [Applicant](docs/Applicant.md)
 - [ApplicationLenderSubmission](docs/ApplicationLenderSubmission.md)
 - [ApplicationSubmittedToLenderRequest](docs/ApplicationSubmittedToLenderRequest.md)
 - [BlockResponse](docs/BlockResponse.md)
 - [BlocksResponse](docs/BlocksResponse.md)
 - [BrokerLeadReservationId](docs/BrokerLeadReservationId.md)
 - [BrokerLeadReservationsResponse](docs/BrokerLeadReservationsResponse.md)
 - [Client](docs/Client.md)
 - [ClientAddress](docs/ClientAddress.md)
 - [ClientParty](docs/ClientParty.md)
 - [CmlConstructionRequest](docs/CmlConstructionRequest.md)
 - [CmlFreeholderRequest](docs/CmlFreeholderRequest.md)
 - [CmlSellerDetailsRequest](docs/CmlSellerDetailsRequest.md)
 - [CmlSeparateLeaseGroundRentDetailsRequest](docs/CmlSeparateLeaseGroundRentDetailsRequest.md)
 - [CmlTenureRequest](docs/CmlTenureRequest.md)
 - [CmlWarrantyProfessionalConsultantAccreditationRequest](docs/CmlWarrantyProfessionalConsultantAccreditationRequest.md)
 - [CorporateDetails](docs/CorporateDetails.md)
 - [CreateBlockRequest](docs/CreateBlockRequest.md)
 - [CreateBlockResponse](docs/CreateBlockResponse.md)
 - [CreateBlocksRequest](docs/CreateBlocksRequest.md)
 - [CreateBlocksResponse](docs/CreateBlocksResponse.md)
 - [CreateCmlRequest](docs/CreateCmlRequest.md)
 - [CreateDevelopmentRequest](docs/CreateDevelopmentRequest.md)
 - [CreateDevelopmentResponse](docs/CreateDevelopmentResponse.md)
 - [CreateDevelopmentsRequest](docs/CreateDevelopmentsRequest.md)
 - [CreateDevelopmentsResponse](docs/CreateDevelopmentsResponse.md)
 - [CreatePlotRequest](docs/CreatePlotRequest.md)
 - [CreatePlotResponse](docs/CreatePlotResponse.md)
 - [CreatePlotsRequest](docs/CreatePlotsRequest.md)
 - [CreatePlotsResponse](docs/CreatePlotsResponse.md)
 - [CreateReservationRequest](docs/CreateReservationRequest.md)
 - [CreateReservationResponse](docs/CreateReservationResponse.md)
 - [DeleteBlockRequest](docs/DeleteBlockRequest.md)
 - [DeleteBlockResponse](docs/DeleteBlockResponse.md)
 - [DeleteBlocksRequest](docs/DeleteBlocksRequest.md)
 - [DeleteBlocksResponse](docs/DeleteBlocksResponse.md)
 - [DeletePlotRequest](docs/DeletePlotRequest.md)
 - [DeletePlotResponse](docs/DeletePlotResponse.md)
 - [DeletePlotsRequest](docs/DeletePlotsRequest.md)
 - [DeletePlotsResponse](docs/DeletePlotsResponse.md)
 - [DevelopmentPlot](docs/DevelopmentPlot.md)
 - [DocumentStoreCategory](docs/DocumentStoreCategory.md)
 - [GetPlotResponse](docs/GetPlotResponse.md)
 - [GetPlotsResponse](docs/GetPlotsResponse.md)
 - [InventoryDevelopmentResponse](docs/InventoryDevelopmentResponse.md)
 - [InventoryDevelopmentsResponse](docs/InventoryDevelopmentsResponse.md)
 - [MortgageOfferIssued](docs/MortgageOfferIssued.md)
 - [MortgageOfferIssuedRequest](docs/MortgageOfferIssuedRequest.md)
 - [PassthroughUrlRequest](docs/PassthroughUrlRequest.md)
 - [PassthroughUrlResponse](docs/PassthroughUrlResponse.md)
 - [PlotsResponse](docs/PlotsResponse.md)
 - [ProblemDetails](docs/ProblemDetails.md)
 - [PurchasePath](docs/PurchasePath.md)
 - [SellerDevelopmentResponse](docs/SellerDevelopmentResponse.md)
 - [SellerDevelopmentsResponse](docs/SellerDevelopmentsResponse.md)
 - [SetDevelopmentLiveFlagRequest](docs/SetDevelopmentLiveFlagRequest.md)
 - [UpdateBlockRequest](docs/UpdateBlockRequest.md)
 - [UpdateBlockResponse](docs/UpdateBlockResponse.md)
 - [UpdateBlocksRequest](docs/UpdateBlocksRequest.md)
 - [UpdateBlocksResponse](docs/UpdateBlocksResponse.md)
 - [UpdateCmlRequest](docs/UpdateCmlRequest.md)
 - [UpdateDevelopmentRequest](docs/UpdateDevelopmentRequest.md)
 - [UpdateDevelopmentResponse](docs/UpdateDevelopmentResponse.md)
 - [UpdateDevelopmentsRequest](docs/UpdateDevelopmentsRequest.md)
 - [UpdateDevelopmentsResponse](docs/UpdateDevelopmentsResponse.md)
 - [UpdatePlotRequest](docs/UpdatePlotRequest.md)
 - [UpdatePlotResponse](docs/UpdatePlotResponse.md)
 - [UpdatePlotsRequest](docs/UpdatePlotsRequest.md)
 - [UpdatePlotsResponse](docs/UpdatePlotsResponse.md)
 - [ValuationInstruction](docs/ValuationInstruction.md)
 - [ValuationInstructionRequest](docs/ValuationInstructionRequest.md)
 - [ValuationReceived](docs/ValuationReceived.md)
 - [ValuationReceivedRequest](docs/ValuationReceivedRequest.md)


## Documentation For Authorization


## Bearer

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

support@yourkeys.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in yk_client.apis and yk_client.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from yk_client.api.default_api import DefaultApi`
- `from yk_client.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import yk_client
from yk_client.apis import *
from yk_client.models import *
```

