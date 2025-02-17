# -*- coding: utf-8 -*-

"""
paypalserversdk

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from paypalserversdk.api_helper import APIHelper
from paypalserversdk.models.link_description import LinkDescription
from paypalserversdk.models.money import Money
from paypalserversdk.models.network_transaction_reference import NetworkTransactionReference
from paypalserversdk.models.seller_protection import SellerProtection


class TransactionDetails(object):

    """Implementation of the 'Transaction Detail' model.

    The transaction details.

    Attributes:
        transaction_details (TransactionDetails): Details of the transaction.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transaction_details": 'transaction_details',
    }

    _optionals = [
        "transaction_details",
    ]

    def __init__(self,
                 transactions_details=APIHelper.SKIP,
                 ):
        """Constructor for the PaymentAuthorization class"""

        # Initialize members of the class
        if transactions_details is not APIHelper.SKIP:
            self.transactions_details = transactions_details

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        transactions_details = dictionary.get("transaction_details") if dictionary.get("transaction_details") else APIHelper.SKIP
    
        # Return an object of this model
        return cls(transactions_details,
                   )
