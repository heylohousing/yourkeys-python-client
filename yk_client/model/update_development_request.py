"""
    Yourkeys Public API

    This API exposes endpoints that can be used to interact with the Yourkeys system  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@yourkeys.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from yk_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)
from ..model_utils import OpenApiModel
from yk_client.exceptions import ApiAttributeError


def lazy_import():
    from yk_client.model.update_cml_request import UpdateCmlRequest
    globals()['UpdateCmlRequest'] = UpdateCmlRequest


class UpdateDevelopmentRequest(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'development_reference': (str, none_type,),  # noqa: E501
            'development_id': (str, none_type,),  # noqa: E501
            'development_name': (str, none_type,),  # noqa: E501
            'address': (str, none_type,),  # noqa: E501
            'address2': (str, none_type,),  # noqa: E501
            'town': (str, none_type,),  # noqa: E501
            'county': (str, none_type,),  # noqa: E501
            'postcode': (str, none_type,),  # noqa: E501
            'country': (str, none_type,),  # noqa: E501
            'completion_date': (datetime, none_type,),  # noqa: E501
            'phase_reference': (str, none_type,),  # noqa: E501
            'help_to_buy': (bool, none_type,),  # noqa: E501
            'help_to_buy_region': (str, none_type,),  # noqa: E501
            'spv_name': (str, none_type,),  # noqa: E501
            'spv_address1': (str, none_type,),  # noqa: E501
            'spv_address2': (str, none_type,),  # noqa: E501
            'spv_town': (str, none_type,),  # noqa: E501
            'spv_county': (str, none_type,),  # noqa: E501
            'spv_postcode': (str, none_type,),  # noqa: E501
            'spv_vat_number': (str, none_type,),  # noqa: E501
            'spv_country': (str, none_type,),  # noqa: E501
            'vendor_company_name': (str, none_type,),  # noqa: E501
            'terms_and_conditions': (str, none_type,),  # noqa: E501
            'land_tax_region': (str, none_type,),  # noqa: E501
            'shared_ownership_rental_percentage': (float, none_type,),  # noqa: E501
            'shared_ownership_equity_lower_percentage': (float, none_type,),  # noqa: E501
            'shared_ownership_equity_upper_percentage': (float, none_type,),  # noqa: E501
            'lease_management_fee_excluding_vat': (float, none_type,),  # noqa: E501
            'monthly_rent_increase': (str, none_type,),  # noqa: E501
            'uk_finance_disclosure_of_incentives_form_details': (UpdateCmlRequest,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'development_reference': 'developmentReference',  # noqa: E501
        'development_id': 'developmentId',  # noqa: E501
        'development_name': 'developmentName',  # noqa: E501
        'address': 'address',  # noqa: E501
        'address2': 'address2',  # noqa: E501
        'town': 'town',  # noqa: E501
        'county': 'county',  # noqa: E501
        'postcode': 'postcode',  # noqa: E501
        'country': 'country',  # noqa: E501
        'completion_date': 'completionDate',  # noqa: E501
        'phase_reference': 'phaseReference',  # noqa: E501
        'help_to_buy': 'helpToBuy',  # noqa: E501
        'help_to_buy_region': 'helpToBuyRegion',  # noqa: E501
        'spv_name': 'spvName',  # noqa: E501
        'spv_address1': 'spvAddress1',  # noqa: E501
        'spv_address2': 'spvAddress2',  # noqa: E501
        'spv_town': 'spvTown',  # noqa: E501
        'spv_county': 'spvCounty',  # noqa: E501
        'spv_postcode': 'spvPostcode',  # noqa: E501
        'spv_vat_number': 'spvVatNumber',  # noqa: E501
        'spv_country': 'spvCountry',  # noqa: E501
        'vendor_company_name': 'vendorCompanyName',  # noqa: E501
        'terms_and_conditions': 'termsAndConditions',  # noqa: E501
        'land_tax_region': 'landTaxRegion',  # noqa: E501
        'shared_ownership_rental_percentage': 'sharedOwnershipRentalPercentage',  # noqa: E501
        'shared_ownership_equity_lower_percentage': 'sharedOwnershipEquityLowerPercentage',  # noqa: E501
        'shared_ownership_equity_upper_percentage': 'sharedOwnershipEquityUpperPercentage',  # noqa: E501
        'lease_management_fee_excluding_vat': 'leaseManagementFeeExcludingVAT',  # noqa: E501
        'monthly_rent_increase': 'monthlyRentIncrease',  # noqa: E501
        'uk_finance_disclosure_of_incentives_form_details': 'ukFinanceDisclosureOfIncentivesFormDetails',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """UpdateDevelopmentRequest - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            development_reference (str, none_type): [optional]  # noqa: E501
            development_id (str, none_type): [optional]  # noqa: E501
            development_name (str, none_type): [optional]  # noqa: E501
            address (str, none_type): [optional]  # noqa: E501
            address2 (str, none_type): [optional]  # noqa: E501
            town (str, none_type): [optional]  # noqa: E501
            county (str, none_type): [optional]  # noqa: E501
            postcode (str, none_type): [optional]  # noqa: E501
            country (str, none_type): [optional]  # noqa: E501
            completion_date (datetime, none_type): [optional]  # noqa: E501
            phase_reference (str, none_type): [optional]  # noqa: E501
            help_to_buy (bool, none_type): [optional]  # noqa: E501
            help_to_buy_region (str, none_type): [optional]  # noqa: E501
            spv_name (str, none_type): [optional]  # noqa: E501
            spv_address1 (str, none_type): [optional]  # noqa: E501
            spv_address2 (str, none_type): [optional]  # noqa: E501
            spv_town (str, none_type): [optional]  # noqa: E501
            spv_county (str, none_type): [optional]  # noqa: E501
            spv_postcode (str, none_type): [optional]  # noqa: E501
            spv_vat_number (str, none_type): [optional]  # noqa: E501
            spv_country (str, none_type): [optional]  # noqa: E501
            vendor_company_name (str, none_type): [optional]  # noqa: E501
            terms_and_conditions (str, none_type): [optional]  # noqa: E501
            land_tax_region (str, none_type): [optional]  # noqa: E501
            shared_ownership_rental_percentage (float, none_type): [optional]  # noqa: E501
            shared_ownership_equity_lower_percentage (float, none_type): [optional]  # noqa: E501
            shared_ownership_equity_upper_percentage (float, none_type): [optional]  # noqa: E501
            lease_management_fee_excluding_vat (float, none_type): [optional]  # noqa: E501
            monthly_rent_increase (str, none_type): [optional]  # noqa: E501
            uk_finance_disclosure_of_incentives_form_details (UpdateCmlRequest): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """UpdateDevelopmentRequest - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            development_reference (str, none_type): [optional]  # noqa: E501
            development_id (str, none_type): [optional]  # noqa: E501
            development_name (str, none_type): [optional]  # noqa: E501
            address (str, none_type): [optional]  # noqa: E501
            address2 (str, none_type): [optional]  # noqa: E501
            town (str, none_type): [optional]  # noqa: E501
            county (str, none_type): [optional]  # noqa: E501
            postcode (str, none_type): [optional]  # noqa: E501
            country (str, none_type): [optional]  # noqa: E501
            completion_date (datetime, none_type): [optional]  # noqa: E501
            phase_reference (str, none_type): [optional]  # noqa: E501
            help_to_buy (bool, none_type): [optional]  # noqa: E501
            help_to_buy_region (str, none_type): [optional]  # noqa: E501
            spv_name (str, none_type): [optional]  # noqa: E501
            spv_address1 (str, none_type): [optional]  # noqa: E501
            spv_address2 (str, none_type): [optional]  # noqa: E501
            spv_town (str, none_type): [optional]  # noqa: E501
            spv_county (str, none_type): [optional]  # noqa: E501
            spv_postcode (str, none_type): [optional]  # noqa: E501
            spv_vat_number (str, none_type): [optional]  # noqa: E501
            spv_country (str, none_type): [optional]  # noqa: E501
            vendor_company_name (str, none_type): [optional]  # noqa: E501
            terms_and_conditions (str, none_type): [optional]  # noqa: E501
            land_tax_region (str, none_type): [optional]  # noqa: E501
            shared_ownership_rental_percentage (float, none_type): [optional]  # noqa: E501
            shared_ownership_equity_lower_percentage (float, none_type): [optional]  # noqa: E501
            shared_ownership_equity_upper_percentage (float, none_type): [optional]  # noqa: E501
            lease_management_fee_excluding_vat (float, none_type): [optional]  # noqa: E501
            monthly_rent_increase (str, none_type): [optional]  # noqa: E501
            uk_finance_disclosure_of_incentives_form_details (UpdateCmlRequest): [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
