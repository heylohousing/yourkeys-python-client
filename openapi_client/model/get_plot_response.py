"""
    Yourkeys Public API

    This API exposes endpoints that can be used to interact with the Yourkeys system  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: support@yourkeys.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
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
from openapi_client.exceptions import ApiAttributeError



class GetPlotResponse(ModelNormal):
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
        return {
            'id': (str,),  # noqa: E501
            'development_id': (str, none_type,),  # noqa: E501
            'block_id': (str, none_type,),  # noqa: E501
            'plot_no': (str, none_type,),  # noqa: E501
            'uprn': (str, none_type,),  # noqa: E501
            'developer_code': (str, none_type,),  # noqa: E501
            'plot_price': (float, none_type,),  # noqa: E501
            'meter': (str, none_type,),  # noqa: E501
            'ft': (str, none_type,),  # noqa: E501
            'tenure': (str, none_type,),  # noqa: E501
            'is_live': (bool,),  # noqa: E501
            'status_code': (str, none_type,),  # noqa: E501
            'completion_date': (datetime, none_type,),  # noqa: E501
            'offer_price': (float, none_type,),  # noqa: E501
            'oss_meter': (str, none_type,),  # noqa: E501
            'oss_ft': (str, none_type,),  # noqa: E501
            'pre_sold': (bool,),  # noqa: E501
            'address': (str, none_type,),  # noqa: E501
            'town': (str, none_type,),  # noqa: E501
            'county': (str, none_type,),  # noqa: E501
            'postcode': (str, none_type,),  # noqa: E501
            'country': (str, none_type,),  # noqa: E501
            'lease_length_year': (int, none_type,),  # noqa: E501
            'ground_rent_review_frequency_in_years': (int, none_type,),  # noqa: E501
            'ground_rent_methodology': (str, none_type,),  # noqa: E501
            'service_charge_initial_amount': (float, none_type,),  # noqa: E501
            'service_charge_payment_frequency': (str, none_type,),  # noqa: E501
            'dwelling_type': (str, none_type,),  # noqa: E501
            'bedrooms': (int, none_type,),  # noqa: E501
            'bathrooms': (int, none_type,),  # noqa: E501
            'reservation_fee': (float, none_type,),  # noqa: E501
            'area_metre': (str, none_type,),  # noqa: E501
            'area_ft': (str, none_type,),  # noqa: E501
            'lease_commencement_date': (datetime, none_type,),  # noqa: E501
            'estate_charge_initial_amount': (float, none_type,),  # noqa: E501
            'estate_charge_payment_frequency': (str, none_type,),  # noqa: E501
            'ground_rent_initial_amount': (float, none_type,),  # noqa: E501
            'ground_rent_percentage': (float, none_type,),  # noqa: E501
            'ground_rent_calculation_method': (str, none_type,),  # noqa: E501
            'floor': (int, none_type,),  # noqa: E501
            'energy_sap_rating': (int, none_type,),  # noqa: E501
            'shared_ownership': (bool, none_type,),  # noqa: E501
            'spv_override': (bool,),  # noqa: E501
            'spv_name': (str, none_type,),  # noqa: E501
            'spv_address1': (str, none_type,),  # noqa: E501
            'spv_address2': (str, none_type,),  # noqa: E501
            'spv_town': (str, none_type,),  # noqa: E501
            'spv_county': (str, none_type,),  # noqa: E501
            'spv_postcode': (str, none_type,),  # noqa: E501
            'spv_country_id': (int, none_type,),  # noqa: E501
            'spv_vat_number': (str, none_type,),  # noqa: E501
            'equity_share': (float, none_type,),  # noqa: E501
            'share_value': (float, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'development_id': 'developmentId',  # noqa: E501
        'block_id': 'blockId',  # noqa: E501
        'plot_no': 'plotNo',  # noqa: E501
        'uprn': 'uprn',  # noqa: E501
        'developer_code': 'developerCode',  # noqa: E501
        'plot_price': 'plotPrice',  # noqa: E501
        'meter': 'meter',  # noqa: E501
        'ft': 'ft',  # noqa: E501
        'tenure': 'tenure',  # noqa: E501
        'is_live': 'isLive',  # noqa: E501
        'status_code': 'statusCode',  # noqa: E501
        'completion_date': 'completionDate',  # noqa: E501
        'offer_price': 'offerPrice',  # noqa: E501
        'oss_meter': 'ossMeter',  # noqa: E501
        'oss_ft': 'ossFt',  # noqa: E501
        'pre_sold': 'preSold',  # noqa: E501
        'address': 'address',  # noqa: E501
        'town': 'town',  # noqa: E501
        'county': 'county',  # noqa: E501
        'postcode': 'postcode',  # noqa: E501
        'country': 'country',  # noqa: E501
        'lease_length_year': 'leaseLengthYear',  # noqa: E501
        'ground_rent_review_frequency_in_years': 'groundRentReviewFrequencyInYears',  # noqa: E501
        'ground_rent_methodology': 'groundRentMethodology',  # noqa: E501
        'service_charge_initial_amount': 'serviceChargeInitialAmount',  # noqa: E501
        'service_charge_payment_frequency': 'serviceChargePaymentFrequency',  # noqa: E501
        'dwelling_type': 'dwellingType',  # noqa: E501
        'bedrooms': 'bedrooms',  # noqa: E501
        'bathrooms': 'bathrooms',  # noqa: E501
        'reservation_fee': 'reservationFee',  # noqa: E501
        'area_metre': 'areaMetre',  # noqa: E501
        'area_ft': 'areaFt',  # noqa: E501
        'lease_commencement_date': 'leaseCommencementDate',  # noqa: E501
        'estate_charge_initial_amount': 'estateChargeInitialAmount',  # noqa: E501
        'estate_charge_payment_frequency': 'estateChargePaymentFrequency',  # noqa: E501
        'ground_rent_initial_amount': 'groundRentInitialAmount',  # noqa: E501
        'ground_rent_percentage': 'groundRentPercentage',  # noqa: E501
        'ground_rent_calculation_method': 'groundRentCalculationMethod',  # noqa: E501
        'floor': 'floor',  # noqa: E501
        'energy_sap_rating': 'energySapRating',  # noqa: E501
        'shared_ownership': 'sharedOwnership',  # noqa: E501
        'spv_override': 'spvOverride',  # noqa: E501
        'spv_name': 'spvName',  # noqa: E501
        'spv_address1': 'spvAddress1',  # noqa: E501
        'spv_address2': 'spvAddress2',  # noqa: E501
        'spv_town': 'spvTown',  # noqa: E501
        'spv_county': 'spvCounty',  # noqa: E501
        'spv_postcode': 'spvPostcode',  # noqa: E501
        'spv_country_id': 'spvCountryId',  # noqa: E501
        'spv_vat_number': 'spvVatNumber',  # noqa: E501
        'equity_share': 'equityShare',  # noqa: E501
        'share_value': 'shareValue',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """GetPlotResponse - a model defined in OpenAPI

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
            id (str): [optional]  # noqa: E501
            development_id (str, none_type): [optional]  # noqa: E501
            block_id (str, none_type): [optional]  # noqa: E501
            plot_no (str, none_type): [optional]  # noqa: E501
            uprn (str, none_type): [optional]  # noqa: E501
            developer_code (str, none_type): [optional]  # noqa: E501
            plot_price (float, none_type): [optional]  # noqa: E501
            meter (str, none_type): [optional]  # noqa: E501
            ft (str, none_type): [optional]  # noqa: E501
            tenure (str, none_type): [optional]  # noqa: E501
            is_live (bool): [optional]  # noqa: E501
            status_code (str, none_type): [optional]  # noqa: E501
            completion_date (datetime, none_type): [optional]  # noqa: E501
            offer_price (float, none_type): [optional]  # noqa: E501
            oss_meter (str, none_type): [optional]  # noqa: E501
            oss_ft (str, none_type): [optional]  # noqa: E501
            pre_sold (bool): [optional]  # noqa: E501
            address (str, none_type): [optional]  # noqa: E501
            town (str, none_type): [optional]  # noqa: E501
            county (str, none_type): [optional]  # noqa: E501
            postcode (str, none_type): [optional]  # noqa: E501
            country (str, none_type): [optional]  # noqa: E501
            lease_length_year (int, none_type): [optional]  # noqa: E501
            ground_rent_review_frequency_in_years (int, none_type): [optional]  # noqa: E501
            ground_rent_methodology (str, none_type): [optional]  # noqa: E501
            service_charge_initial_amount (float, none_type): [optional]  # noqa: E501
            service_charge_payment_frequency (str, none_type): [optional]  # noqa: E501
            dwelling_type (str, none_type): [optional]  # noqa: E501
            bedrooms (int, none_type): [optional]  # noqa: E501
            bathrooms (int, none_type): [optional]  # noqa: E501
            reservation_fee (float, none_type): [optional]  # noqa: E501
            area_metre (str, none_type): [optional]  # noqa: E501
            area_ft (str, none_type): [optional]  # noqa: E501
            lease_commencement_date (datetime, none_type): [optional]  # noqa: E501
            estate_charge_initial_amount (float, none_type): [optional]  # noqa: E501
            estate_charge_payment_frequency (str, none_type): [optional]  # noqa: E501
            ground_rent_initial_amount (float, none_type): [optional]  # noqa: E501
            ground_rent_percentage (float, none_type): [optional]  # noqa: E501
            ground_rent_calculation_method (str, none_type): [optional]  # noqa: E501
            floor (int, none_type): [optional]  # noqa: E501
            energy_sap_rating (int, none_type): [optional]  # noqa: E501
            shared_ownership (bool, none_type): [optional]  # noqa: E501
            spv_override (bool): [optional]  # noqa: E501
            spv_name (str, none_type): [optional]  # noqa: E501
            spv_address1 (str, none_type): [optional]  # noqa: E501
            spv_address2 (str, none_type): [optional]  # noqa: E501
            spv_town (str, none_type): [optional]  # noqa: E501
            spv_county (str, none_type): [optional]  # noqa: E501
            spv_postcode (str, none_type): [optional]  # noqa: E501
            spv_country_id (int, none_type): [optional]  # noqa: E501
            spv_vat_number (str, none_type): [optional]  # noqa: E501
            equity_share (float, none_type): [optional]  # noqa: E501
            share_value (float, none_type): [optional]  # noqa: E501
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
        """GetPlotResponse - a model defined in OpenAPI

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
            id (str): [optional]  # noqa: E501
            development_id (str, none_type): [optional]  # noqa: E501
            block_id (str, none_type): [optional]  # noqa: E501
            plot_no (str, none_type): [optional]  # noqa: E501
            uprn (str, none_type): [optional]  # noqa: E501
            developer_code (str, none_type): [optional]  # noqa: E501
            plot_price (float, none_type): [optional]  # noqa: E501
            meter (str, none_type): [optional]  # noqa: E501
            ft (str, none_type): [optional]  # noqa: E501
            tenure (str, none_type): [optional]  # noqa: E501
            is_live (bool): [optional]  # noqa: E501
            status_code (str, none_type): [optional]  # noqa: E501
            completion_date (datetime, none_type): [optional]  # noqa: E501
            offer_price (float, none_type): [optional]  # noqa: E501
            oss_meter (str, none_type): [optional]  # noqa: E501
            oss_ft (str, none_type): [optional]  # noqa: E501
            pre_sold (bool): [optional]  # noqa: E501
            address (str, none_type): [optional]  # noqa: E501
            town (str, none_type): [optional]  # noqa: E501
            county (str, none_type): [optional]  # noqa: E501
            postcode (str, none_type): [optional]  # noqa: E501
            country (str, none_type): [optional]  # noqa: E501
            lease_length_year (int, none_type): [optional]  # noqa: E501
            ground_rent_review_frequency_in_years (int, none_type): [optional]  # noqa: E501
            ground_rent_methodology (str, none_type): [optional]  # noqa: E501
            service_charge_initial_amount (float, none_type): [optional]  # noqa: E501
            service_charge_payment_frequency (str, none_type): [optional]  # noqa: E501
            dwelling_type (str, none_type): [optional]  # noqa: E501
            bedrooms (int, none_type): [optional]  # noqa: E501
            bathrooms (int, none_type): [optional]  # noqa: E501
            reservation_fee (float, none_type): [optional]  # noqa: E501
            area_metre (str, none_type): [optional]  # noqa: E501
            area_ft (str, none_type): [optional]  # noqa: E501
            lease_commencement_date (datetime, none_type): [optional]  # noqa: E501
            estate_charge_initial_amount (float, none_type): [optional]  # noqa: E501
            estate_charge_payment_frequency (str, none_type): [optional]  # noqa: E501
            ground_rent_initial_amount (float, none_type): [optional]  # noqa: E501
            ground_rent_percentage (float, none_type): [optional]  # noqa: E501
            ground_rent_calculation_method (str, none_type): [optional]  # noqa: E501
            floor (int, none_type): [optional]  # noqa: E501
            energy_sap_rating (int, none_type): [optional]  # noqa: E501
            shared_ownership (bool, none_type): [optional]  # noqa: E501
            spv_override (bool): [optional]  # noqa: E501
            spv_name (str, none_type): [optional]  # noqa: E501
            spv_address1 (str, none_type): [optional]  # noqa: E501
            spv_address2 (str, none_type): [optional]  # noqa: E501
            spv_town (str, none_type): [optional]  # noqa: E501
            spv_county (str, none_type): [optional]  # noqa: E501
            spv_postcode (str, none_type): [optional]  # noqa: E501
            spv_country_id (int, none_type): [optional]  # noqa: E501
            spv_vat_number (str, none_type): [optional]  # noqa: E501
            equity_share (float, none_type): [optional]  # noqa: E501
            share_value (float, none_type): [optional]  # noqa: E501
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