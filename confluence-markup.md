h1. Order Payment Orders APIs Allows the creation, viewing and management of payment orders

*Version:* v1.0.0

----

{toc:printable=true|style=square|minLevel=2|maxLevel=3|type=list|outline=false|include=.*}

h2. Endpoints

    h3. createPaymentOrder
    {status:colour=Yellow|title=post|subtle=false}
    {code}
    post /order/paymentOrders
    {code}
    *Summary:* 
    *Description:* 


    h4. Parameters

        h5. Body Parameter
        ||Name||Description||Required||Default||Pattern||
        |payload |body Payload |(/) | |  |


        h5. Header Parameters
        ||Name||Description||Required||Default||Pattern||
        
        h5. Query Parameters
        ||Name||Description||Required||Default||Pattern||
        |validateOnly |The identifier to indicate if it is set to only validate or not. |(x) | |  |





    h4. Responses
        *Status Code:* 200
        *Message:*     PaymentOrderResponse
        {code:title=Response Type}
PaymentOrderResponse
        {code}
        See [#models]



        {code:title=Response Schema |collapse=true}
{
  "description" : "PaymentOrderResponse",
  "schema" : {
    "$ref" : "#/definitions/PaymentOrderResponse"
  }
}
        {code}
        *Status Code:* 0
        *Message:*     ScreenErrorResponse
        {code:title=Response Type}
ScreenErrorResponse
        {code}
        See [#models]



        {code:title=Response Schema |collapse=true}
{
  "description" : "ScreenErrorResponse",
  "schema" : {
    "$ref" : "#/definitions/ScreenErrorResponse"
  }
}
        {code}
    ----

    h3. deletePaymentOrder
    {status:colour=Yellow|title=delete|subtle=false}
    {code}
    delete /order/paymentOrders/{paymentOrderId}
    {code}
    *Summary:* 
    *Description:* 


    h4. Parameters
        h5. Path Parameters
        ||Name||Description||Required||Default||Pattern||
        |paymentOrderId |The unique reference number of payment |(/) | |  |



        h5. Header Parameters
        ||Name||Description||Required||Default||Pattern||
        
        h5. Query Parameters
        ||Name||Description||Required||Default||Pattern||
        |validateOnly |The identifier to indicate if it is set to only validate or not. |(x) | |  |





    h4. Responses
        *Status Code:* 200
        *Message:*     PaymentOrderResponse
        {code:title=Response Type}
PaymentOrderResponse
        {code}
        See [#models]



        {code:title=Response Schema |collapse=true}
{
  "description" : "PaymentOrderResponse",
  "schema" : {
    "$ref" : "#/definitions/PaymentOrderResponse"
  }
}
        {code}
        *Status Code:* 0
        *Message:*     ScreenErrorResponse
        {code:title=Response Type}
ScreenErrorResponse
        {code}
        See [#models]



        {code:title=Response Schema |collapse=true}
{
  "description" : "ScreenErrorResponse",
  "schema" : {
    "$ref" : "#/definitions/ScreenErrorResponse"
  }
}
        {code}
    ----

    h3. getPaymentOrder
    {status:colour=Yellow|title=get|subtle=false}
    {code}
    get /order/paymentOrders/{paymentOrderId}
    {code}
    *Summary:* 
    *Description:* 


    h4. Parameters
        h5. Path Parameters
        ||Name||Description||Required||Default||Pattern||
        |paymentOrderId |The unique reference number of payment |(/) | |  |



        h5. Header Parameters
        ||Name||Description||Required||Default||Pattern||
        
        h5. Query Parameters
        ||Name||Description||Required||Default||Pattern||
        |currentPaymentState | |(x) | |  |

|paymentStatus |Indicates the Status Code of the payment. Every payment in the hub is tracked using a status code which depicts the current stage at which payment is in the workflow |(x) | |  |

|paymentOrderProductId |Indicates the payment order product for which payment is initiated |(x) | |  |

|debitAccountId |Indicates the debit account number of the payment |(x) | |  |

|orderingCustomerId |Indicates the customer id for the ordering customer |(x) | |  |

|pageSize |The total number of records per page |(x) | |  |

|pageStart |The record from which the response should be displayed |(x) | |  |

|pageToken |Unique id expected to get as part of response from t24 on every enquiry request. |(x) | |  |





    h4. Responses
        *Status Code:* 200
        *Message:*     PaymentOrderResponse
        {code:title=Response Type}
PaymentOrderResponse1
        {code}
        See [#models]



        {code:title=Response Schema |collapse=true}
{
  "description" : "PaymentOrderResponse",
  "schema" : {
    "$ref" : "#/definitions/PaymentOrderResponse1"
  }
}
        {code}
        *Status Code:* 0
        *Message:*     QueryErrorResponse
        {code:title=Response Type}
QueryErrorResponse
        {code}
        See [#models]



        {code:title=Response Schema |collapse=true}
{
  "description" : "QueryErrorResponse",
  "schema" : {
    "$ref" : "#/definitions/QueryErrorResponse"
  }
}
        {code}
    ----

    h3. getPaymentOrderCountryRules
    {status:colour=Yellow|title=get|subtle=false}
    {code}
    get /order/paymentOrders/countryRules
    {code}
    *Summary:* 
    *Description:* 


    h4. Parameters


        h5. Header Parameters
        ||Name||Description||Required||Default||Pattern||
        
        h5. Query Parameters
        ||Name||Description||Required||Default||Pattern||
        |countryId |ISO country code of the financial institution.  |(x) | |  |

|pageSize |The total number of records per page |(x) | |  |

|pageStart |The record from which the response should be displayed |(x) | |  |

|pageToken |Unique id expected to get as part of response from t24 on every enquiry request. |(x) | |  |





    h4. Responses
        *Status Code:* 200
        *Message:*     PaymentOrderCountryRulesResponse
        {code:title=Response Type}
PaymentOrderCountryRulesResponse
        {code}
        See [#models]



        {code:title=Response Schema |collapse=true}
{
  "description" : "PaymentOrderCountryRulesResponse",
  "schema" : {
    "$ref" : "#/definitions/PaymentOrderCountryRulesResponse"
  }
}
        {code}
        *Status Code:* 0
        *Message:*     QueryErrorResponse
        {code:title=Response Type}
QueryErrorResponse
        {code}
        See [#models]



        {code:title=Response Schema |collapse=true}
{
  "description" : "QueryErrorResponse",
  "schema" : {
    "$ref" : "#/definitions/QueryErrorResponse"
  }
}
        {code}
    ----

    h3. getPaymentOrderProducts
    {status:colour=Yellow|title=get|subtle=false}
    {code}
    get /order/paymentOrders/products
    {code}
    *Summary:* 
    *Description:* 


    h4. Parameters


        h5. Header Parameters
        ||Name||Description||Required||Default||Pattern||
        
        h5. Query Parameters
        ||Name||Description||Required||Default||Pattern||
        |paymentProductGroupId | |(x) | |  |

|paymentOrderProductId |Indicates the payment order product for which payment is initiated |(x) | |  |

|pageSize |The total number of records per page |(x) | |  |

|pageStart |The record from which the response should be displayed |(x) | |  |

|pageToken |Unique id expected to get as part of response from t24 on every enquiry request. |(x) | |  |





    h4. Responses
        *Status Code:* 200
        *Message:*     PaymentOrderProductsResponse
        {code:title=Response Type}
PaymentOrderProductsResponse
        {code}
        See [#models]



        {code:title=Response Schema |collapse=true}
{
  "description" : "PaymentOrderProductsResponse",
  "schema" : {
    "$ref" : "#/definitions/PaymentOrderProductsResponse"
  }
}
        {code}
        *Status Code:* 0
        *Message:*     QueryErrorResponse
        {code:title=Response Type}
QueryErrorResponse
        {code}
        See [#models]



        {code:title=Response Schema |collapse=true}
{
  "description" : "QueryErrorResponse",
  "schema" : {
    "$ref" : "#/definitions/QueryErrorResponse"
  }
}
        {code}
    ----

    h3. getPaymentOrderPurposes
    {status:colour=Yellow|title=get|subtle=false}
    {code}
    get /order/paymentOrders/purposes
    {code}
    *Summary:* 
    *Description:* 


    h4. Parameters


        h5. Header Parameters
        ||Name||Description||Required||Default||Pattern||
        
        h5. Query Parameters
        ||Name||Description||Required||Default||Pattern||
        |paymentOrderPurposeCodeId |Indicates the Id of payment purpose code i.e. purpose of the instruction based on a set of pre-defined categories. |(x) | |  |

|pageSize |The total number of records per page |(x) | |  |

|pageStart |The record from which the response should be displayed |(x) | |  |

|pageToken |Unique id expected to get as part of response from t24 on every enquiry request. |(x) | |  |





    h4. Responses
        *Status Code:* 200
        *Message:*     PaymentOrderPurposesResponse
        {code:title=Response Type}
PaymentOrderPurposesResponse
        {code}
        See [#models]



        {code:title=Response Schema |collapse=true}
{
  "description" : "PaymentOrderPurposesResponse",
  "schema" : {
    "$ref" : "#/definitions/PaymentOrderPurposesResponse"
  }
}
        {code}
        *Status Code:* 0
        *Message:*     QueryErrorResponse
        {code:title=Response Type}
QueryErrorResponse
        {code}
        See [#models]



        {code:title=Response Schema |collapse=true}
{
  "description" : "QueryErrorResponse",
  "schema" : {
    "$ref" : "#/definitions/QueryErrorResponse"
  }
}
        {code}
    ----

    h3. getPaymentOrders
    {status:colour=Yellow|title=get|subtle=false}
    {code}
    get /order/paymentOrders
    {code}
    *Summary:* 
    *Description:* 


    h4. Parameters


        h5. Header Parameters
        ||Name||Description||Required||Default||Pattern||
        
        h5. Query Parameters
        ||Name||Description||Required||Default||Pattern||
        |paymentOrderId |The unique reference number of payment |(x) | |  |

|currentPaymentState | |(x) | |  |

|paymentStatus |Indicates the Status Code of the payment. Every payment in the hub is tracked using a status code which depicts the current stage at which payment is in the workflow |(x) | |  |

|paymentOrderProductIdNE | |(x) | |  |

|paymentOrderProductId |Indicates the payment order product for which payment is initiated |(x) | |  |

|debitAccountId |Indicates the debit account number of the payment |(x) | |  |

|orderingCustomerId |Indicates the customer id for the ordering customer |(x) | |  |

|pageSize |The total number of records per page |(x) | |  |

|pageStart |The record from which the response should be displayed |(x) | |  |

|pageToken |Unique id expected to get as part of response from t24 on every enquiry request. |(x) | |  |





    h4. Responses
        *Status Code:* 200
        *Message:*     PaymentOrdersResponse
        {code:title=Response Type}
PaymentOrderResponse1
        {code}
        See [#models]



        {code:title=Response Schema |collapse=true}
{
  "description" : "PaymentOrdersResponse",
  "schema" : {
    "$ref" : "#/definitions/PaymentOrderResponse1"
  }
}
        {code}
        *Status Code:* 0
        *Message:*     QueryErrorResponse
        {code:title=Response Type}
QueryErrorResponse
        {code}
        See [#models]



        {code:title=Response Schema |collapse=true}
{
  "description" : "QueryErrorResponse",
  "schema" : {
    "$ref" : "#/definitions/QueryErrorResponse"
  }
}
        {code}
    ----

    h3. updatePaymentOrder
    {status:colour=Yellow|title=put|subtle=false}
    {code}
    put /order/paymentOrders/{paymentOrderId}
    {code}
    *Summary:* 
    *Description:* 


    h4. Parameters
        h5. Path Parameters
        ||Name||Description||Required||Default||Pattern||
        |paymentOrderId |The unique reference number of payment |(/) | |  |


        h5. Body Parameter
        ||Name||Description||Required||Default||Pattern||
        |payload |body Payload |(/) | |  |


        h5. Header Parameters
        ||Name||Description||Required||Default||Pattern||
        
        h5. Query Parameters
        ||Name||Description||Required||Default||Pattern||
        |validateOnly |The identifier to indicate if it is set to only validate or not. |(x) | |  |





    h4. Responses
        *Status Code:* 200
        *Message:*     PaymentOrderResponse
        {code:title=Response Type}
PaymentOrderResponse
        {code}
        See [#models]



        {code:title=Response Schema |collapse=true}
{
  "description" : "PaymentOrderResponse",
  "schema" : {
    "$ref" : "#/definitions/PaymentOrderResponse"
  }
}
        {code}
        *Status Code:* 0
        *Message:*     ScreenErrorResponse
        {code:title=Response Type}
ScreenErrorResponse
        {code}
        See [#models]



        {code:title=Response Schema |collapse=true}
{
  "description" : "ScreenErrorResponse",
  "schema" : {
    "$ref" : "#/definitions/ScreenErrorResponse"
  }
}
        {code}
    ----

h2. Models

        h3. ErrorHeader
        ||Field Name||Required||Type||Description||
         |id | |String |The Identifier of the record created |
 |status | |String |The status of the record |
 |transactionStatus | |String |The status of the transaction |
 |audit | |ScreenHeader_audit | |
        h3. OverrideBody
        ||Field Name||Required||Type||Description||
         |overrideDetails | |array[overrideBody_overrideDetails] | |
        h3. OverrideBody_overrideDetails
        ||Field Name||Required||Type||Description||
         |id | |String |The identifier of the override |
 |description | |String |The actual override message |
        h3. PayloadHeader
        ||Field Name||Required||Type||Description||
         |override | |PayloadHeader_override | |
 |audit | |PayloadHeader_audit | |
        h3. PayloadHeader_audit
        ||Field Name||Required||Type||Description||
         |versionNumber | |String |The CURR.NO. of the record |
        h3. PayloadHeader_override
        ||Field Name||Required||Type||Description||
         |overrideDetails | |array[PayloadHeader_override_overrideDetails] | |
        h3. PayloadHeader_override_overrideDetails
        ||Field Name||Required||Type||Description||
         |id | |String |The identifier of the override |
 |description | |String |The actual override message |
 |responseCode | |String |The user input to accept/reject the override. |
        h3. PaymentOrder
        ||Field Name||Required||Type||Description||
         |header | |PayloadHeader | |
 |body | |PaymentOrderBody | |
        h3. PaymentOrderBody
        ||Field Name||Required||Type||Description||
         |narratives | |array[PaymentOrderBody_narratives] |The additional text printed on descriptive statements in addition to the standard narrative and/or reference |
 |additionalInformations | |array[PaymentOrderBody_additionalInformations] |Additional Information provided to add context |
 |remittanceInformations | |array[PaymentOrderBody_remittanceInformations] |Indicates the remittance information that is supplied to enable the matching/reconciliation of an entry with the items that the payment is intended to settle, such as commercial invoices in an accounts&#39; receivable system, in an unstructured form. |
 |signatories | |array[PaymentOrderBody_signatories] |The authorised signatories for the payments can be specified here. More applicable in case of corporate payments where multiple signatories are required to sign a payment instruction |
 |invoiceReferences | |array[PaymentOrderBody_invoiceReferences] |It provides the reference of the invoice  |
 |charges | |array[PaymentOrderBody_charges] |The charges or fees for this transaction |
 |overrides | |array[PaymentOrderBody_overrides] |The override message is captured  that was generated at the time of commitment of the transaction to the database. |
 |paymentOrderProductId | |String |Indicates the payment order product for which payment is initiated |
 |debitAccountId | |String |Indicates the debit account number of the payment |
 |debitAccountIBAN | |String |Indicates the debit account IBAN of the payment |
 |debitCurrency | |String |Indicates the currency of debit account |
 |debitValueDate | |date |The date on which the Invocation amount will be debited for settlement |
 |creditAccountId | |String |This is the account which will be credited for the instruction |
 |creditAccountIBAN | |String |Indicates the IBAN of the credit account |
 |orderingCustomerId | |String |Indicates the customer id for the ordering customer |
 |orderingCustomerName | |String |Indicates the name of Ordering Customer |
 |paymentCurrencyId | |String |The currency of payment. |
 |amount | |BigDecimal |This is the payment amount |
 |executionDate | |date |The date when payment will be processed |
 |treasuryRate | |String |The Treasury rate for the conversion between payment currency and the ordering currency |
 |forexSpread | |String |The spread that is applied to the published internal exchange rates to derive the final exchange rate or the customer rate for the transaction for currency conversion between ordering currency and payment currency |
 |forexCustomerRate | |String |The exchange rate that is actually applied for currency conversion between ordering currency and payment currency in case of transactions involving FX conversion.  |
 |orderingPortfolio | |String |Indicates the portfolio id for the debit side if the account belongs to a specific portfolio |
 |creditPortfolio | |String |Indicates the portfolio id for the credit side if the account belongs to a specific portfolio |
 |orderingReference | |String |The reference related to the ordering details |
 |chargeBearer | |String |Indicates who will bear all charges for the payment. Allowed options are Recipient To Pay All Charges, Pay My Bank&#39;s Charges or Pay My Bank Charges Only |
 |beneficiaryId | |String |Indicates the Id of beneficiary when beneficiary details are stored |
 |beneficiaryAccountId | |String |Indicates the account number of the beneficiary |
 |beneficiaryBIC | |String |BIC (Bank Identifier Code) of the beneficiary customer  |
 |beneficiaryName | |String |Name of beneficiary |
 |accountWithBankBIC | |String |This is the BIC code of the institution where beneficiary holds an account |
 |beneficiaryBankClearingCode | |String |Clearing code or sort code of the beneficiary bank |
 |accountWithBankClearingCode | |String |This is the national clearing code or sort code of the institution where beneficiary holds an account |
 |clearingChannel | |String |Indicates the clearing channel for the payment in the ISO format of the Clearing System Identifiers |
 |structuredCreditorReference | |String |This is the unique reference, as assigned by the creditor, to unambiguously refer to the payment |
 |beneficiaryCountryCode | |String | |
 |beneficiaryIBAN | |String |The IBAN of the beneficiary&#39;s account |
 |accountWithBankIBAN | |String |This is the IBAN of the institution where beneficiary holds an account |
 |requiredCreditValueDate | |date |The credit value date i.e. tentative date on which the payment system will process the payment |
 |purpose | |String |Indicates the purpose code of the payment |
 |structuredCommunicationCode | |String |Creditor reference in a coded form i.e - RADM (RemittanceAdviceMessage) - RPIN (RelatedPaymentInstruction) - FXDR (ForeignExchangeDealReference) - DISP (DispatchAdvice) - PUOR (PurchaseOrder) - SCOR (StructuredCommunicationReference) |
 |structuredIssuer | |String |Entity that assigns the identification |
 |endToEndReference | |String |This indicates the end to end reference for the payment. This field can be provided by one who instructs the payment and flows through the lifecycle of payment.  |
 |instructionIdReference | |String |\&quot;Indicates the unique identification as assigned by an instructing party for an instructed party to  unambiguously identify the instruction.\&quot; |
 |termsAndConditions | |String |Specifies the terms and conditions in the text format for the payment instruction, if any. |
 |indicativeRate | |String |The indicative rate at the time of submitting a payment initiation request. Actual rate with which the payment will be processed will be calculated/ fetched during payment processing.  |
 |chargeAccountId | |String |Indicates the account to which the charges has to be levied. Used when charges are to be taken from a separate account |
 |chargeAccountCurrencyId | |String |When a charge account is specified, this field indicates the currency of the charge account |
 |creditValueDate | |date |The value date applied to the credit side of a payment |
 |PSDCompliant | |String |Defines whether the transaction is PSD (Payment Services Directive) compliant or not. |
 |totalDebitAmount | |BigDecimal |The total debit amount including the charges associated for the payment |
 |localInstrumentCode | |String | |
 |recordStatus | |String |General status of the record. Possible values: - null - authorised - IHLD - input, on hold - INAU - input, not authorised - INA2 - input, authorised, pending second authorisation - INAO - input, not authorised with blocking overrides - RNAU - reversed, not authorised - RNAO - reversed, not authorised with blocking overrides |
        h3. PaymentOrderBody_additionalInformations
        ||Field Name||Required||Type||Description||
         |additionalInformation | |String |Additional Information provided to add context |
        h3. PaymentOrderBody_charges
        ||Field Name||Required||Type||Description||
         |chargeType | |String |Holds the type of the charges to be collected |
 |chargeName | |String |The description of the charge to be taken for payment |
 |chargeCurrency | |String |Indicates the charge currency in which charge amount will be taken for the instruction |
 |chargeAmount | |BigDecimal |Indicates the charge amount in the charge currency which is to be applied for instruction for e.g. charge to be taken for payment stop instruction |
 |chargeAccountCurrencyAmount | |BigDecimal | |
        h3. PaymentOrderBody_invoiceReferences
        ||Field Name||Required||Type||Description||
         |invoiceReference | |String |It provides the reference of the invoice  |
        h3. PaymentOrderBody_narratives
        ||Field Name||Required||Type||Description||
         |narrative | |String |The additional text printed on descriptive statements in addition to the standard narrative and/or reference |
        h3. PaymentOrderBody_overrides
        ||Field Name||Required||Type||Description||
         |override | |String |The override message is captured  that was generated at the time of commitment of the transaction to the database. |
        h3. PaymentOrderBody_remittanceInformations
        ||Field Name||Required||Type||Description||
         |remittanceInformation | |String |Indicates the remittance information that is supplied to enable the matching/reconciliation of an entry with the items that the payment is intended to settle, such as commercial invoices in an accounts&#39; receivable system, in an unstructured form. |
        h3. PaymentOrderBody_signatories
        ||Field Name||Required||Type||Description||
         |signatory | |String |The authorised signatories for the payments can be specified here. More applicable in case of corporate payments where multiple signatories are required to sign a payment instruction |
        h3. PaymentOrderCountryRulesResponse
        ||Field Name||Required||Type||Description||
         |header | |QueryHeader | |
 |body | |PaymentOrderCountryRulesResponseBody | |
        h3. PaymentOrderCountryRulesResponseBody
        ||Field Name||Required||Type||Description||
                h3. PaymentOrderCountryRulesResponseBody_inner
        ||Field Name||Required||Type||Description||
         |clearingChannelIds | |array[PaymentOrderProductsResponseBody_inner_clearingChannelIds] | |
 |paymentCurrencyIds | |array[PaymentOrderProductsResponseBody_inner_paymentCurrencyIds] |The currency of payment. |
 |countryId | |String |ISO country code of the financial institution.  |
 |displayName | |String |Name used for display or enrichment purposes |
 |IBANSupport | |String | |
 |BICSupport | |String | |
 |sortCodeSupport | |String | |
        h3. PaymentOrderProductsResponse
        ||Field Name||Required||Type||Description||
         |header | |QueryHeader | |
 |body | |PaymentOrderProductsResponseBody | |
        h3. PaymentOrderProductsResponseBody
        ||Field Name||Required||Type||Description||
                h3. PaymentOrderProductsResponseBody_inner
        ||Field Name||Required||Type||Description||
         |paymentProductGroupIds | |array[PaymentOrderProductsResponseBody_inner_paymentProductGroupIds] | |
 |paymentCurrencyIds | |array[PaymentOrderProductsResponseBody_inner_paymentCurrencyIds] |The currency of payment. |
 |orderingCurrencyIds | |array[PaymentOrderProductsResponseBody_inner_orderingCurrencyIds] | |
 |countryIds | |array[PaymentOrderProductsResponseBody_inner_countryIds] |ISO country code of the financial institution.  |
 |clearingChannelIds | |array[PaymentOrderProductsResponseBody_inner_clearingChannelIds] | |
 |additionalInformations | |array[PaymentOrderProductsResponseBody_inner_additionalInformations] |Additional Information provided to add context |
 |paymentOrderProductId | |String |Indicates the payment order product for which payment is initiated |
 |displayName | |String |Name used for display or enrichment purposes |
 |rank | |String |Indicates the rank of the payment order product within the group.  |
 |payThroughBeneficiary | |String |Defines whether payment initiation can be done by providing beneficiary details. This is applicable when beneficiary is not within the same bank |
 |futureDate | |date |Indicates if a future dated instruction can be inputted for the specific payment order product |
 |requiredCreditValue | |String |Indicates if required credit value date can be inputted for the specific payment order product while initiating a payment |
 |IBANSupport | |String | |
 |BICSupport | |String | |
 |sortCodeSupport | |String | |
 |narrative | |String |The additional text printed on descriptive statements in addition to the standard narrative and/or reference |
 |weblink | |String |The web link for additional information |
 |forexSupport | |String | |
 |defaultChargeOption | |String |Indicates the charge option which will be defaulted at the time of payment initiation for specific payment order product i.e. Recipient To Pay All Charges, Pay My Bank&#39;s Charges or Pay My Bank Charges Only. |
 |checkTransparency | |String | |
 |awaitExternalSubmit | |String | |
        h3. PaymentOrderProductsResponseBody_inner_additionalInformations
        ||Field Name||Required||Type||Description||
         |additionalInformation | |String |Additional Information provided to add context |
        h3. PaymentOrderProductsResponseBody_inner_clearingChannelIds
        ||Field Name||Required||Type||Description||
         |clearingChannelId | |String | |
        h3. PaymentOrderProductsResponseBody_inner_countryIds
        ||Field Name||Required||Type||Description||
         |countryId | |String |ISO country code of the financial institution.  |
        h3. PaymentOrderProductsResponseBody_inner_orderingCurrencyIds
        ||Field Name||Required||Type||Description||
         |orderingCurrencyId | |String | |
        h3. PaymentOrderProductsResponseBody_inner_paymentCurrencyIds
        ||Field Name||Required||Type||Description||
         |paymentCurrencyId | |String |The currency of payment. |
        h3. PaymentOrderProductsResponseBody_inner_paymentProductGroupIds
        ||Field Name||Required||Type||Description||
         |paymentProductGroupId | |String | |
        h3. PaymentOrderPurposesResponse
        ||Field Name||Required||Type||Description||
         |header | |QueryHeader | |
 |body | |PaymentOrderPurposesResponseBody | |
        h3. PaymentOrderPurposesResponseBody
        ||Field Name||Required||Type||Description||
                h3. PaymentOrderPurposesResponseBody_inner
        ||Field Name||Required||Type||Description||
         |paymentOrderPurposeCodeId | |String |Indicates the Id of payment purpose code i.e. purpose of the instruction based on a set of pre-defined categories. |
 |displayName | |String |Name used for display or enrichment purposes |
 |classification | |String |This indicates a high-level classification of payment purpose code. i.e. purpose of the instruction based on a set of pre-defined categories. |
 |definition | |String |This indicates a full description of payment purpose code. i.e. purpose of the instruction based on a set of pre-defined categories. |
        h3. PaymentOrderResponse
        ||Field Name||Required||Type||Description||
         |header | |ScreenHeader | |
 |body | |PaymentOrderResponseBody | |
        h3. PaymentOrderResponse1
        ||Field Name||Required||Type||Description||
         |header | |QueryHeader | |
 |body | |PaymentOrderResponse1Body | |
        h3. PaymentOrderResponse1Body
        ||Field Name||Required||Type||Description||
                h3. PaymentOrderResponse1Body_inner
        ||Field Name||Required||Type||Description||
         |debits | |array[PaymentOrderResponse1Body_inner_debits] |Debit value of the transaction  |
 |credits | |array[PaymentOrderResponse1Body_inner_credits] |Credit value of the transaction |
 |narratives | |array[PaymentOrderResponse1Body_inner_narratives] |The additional text printed on descriptive statements in addition to the standard narrative and/or reference |
 |additionalInformations | |array[PaymentOrderResponse1Body_inner_additionalInformations] |Additional Information provided to add context |
 |remittanceInformations | |array[PaymentOrderResponse1Body_inner_remittanceInformations] |Indicates the remittance information that is supplied to enable the matching/reconciliation of an entry with the items that the payment is intended to settle, such as commercial invoices in an accounts&#39; receivable system, in an unstructured form. |
 |beneficiaries | |array[PaymentOrderResponse1Body_inner_beneficiaries] |Identifies the Beneficiary name and address of the Standing Order |
 |invoiceReferences | |array[PaymentOrderResponse1Body_inner_invoiceReferences] |It provides the reference of the invoice  |
 |charges | |array[PaymentOrderResponse1Body_inner_charges] |The charges or fees for this transaction |
 |paymentOrderId | |String |The unique reference number of payment |
 |paymentOrderProductId | |String |Indicates the payment order product for which payment is initiated |
 |orderingCustomerId | |String |Indicates the customer id for the ordering customer |
 |orderingCustomerName | |String |Indicates the name of Ordering Customer |
 |paymentCurrencyId | |String |The currency of payment. |
 |amount | |BigDecimal |This is the payment amount |
 |executionDate | |date |The date when payment will be processed |
 |treasuryRate | |String |The Treasury rate for the conversion between payment currency and the ordering currency |
 |forexSpread | |String |The spread that is applied to the published internal exchange rates to derive the final exchange rate or the customer rate for the transaction for currency conversion between ordering currency and payment currency |
 |forexCustomerRate | |String |The exchange rate that is actually applied for currency conversion between ordering currency and payment currency in case of transactions involving FX conversion.  |
 |orderingPortfolio | |String |Indicates the portfolio id for the debit side if the account belongs to a specific portfolio |
 |creditPortfolio | |String |Indicates the portfolio id for the credit side if the account belongs to a specific portfolio |
 |orderingReference | |String |The reference related to the ordering details |
 |chargeBearer | |String |Indicates who will bear all charges for the payment. Allowed options are Recipient To Pay All Charges, Pay My Bank&#39;s Charges or Pay My Bank Charges Only |
 |accountWithBankBIC | |String |This is the BIC code of the institution where beneficiary holds an account |
 |beneficiaryBankClearingCode | |String |Clearing code or sort code of the beneficiary bank |
 |accountWithBankClearingCode | |String |This is the national clearing code or sort code of the institution where beneficiary holds an account |
 |clearingChannel | |String |Indicates the clearing channel for the payment in the ISO format of the Clearing System Identifiers |
 |structuredCreditorReference | |String |This is the unique reference, as assigned by the creditor, to unambiguously refer to the payment |
 |signatory | |String |The authorised signatories for the payments can be specified here. More applicable in case of corporate payments where multiple signatories are required to sign a payment instruction |
 |purpose | |String |Indicates the purpose code of the payment |
 |structuredCommunicationCode | |String |Creditor reference in a coded form i.e - RADM (RemittanceAdviceMessage) - RPIN (RelatedPaymentInstruction) - FXDR (ForeignExchangeDealReference) - DISP (DispatchAdvice) - PUOR (PurchaseOrder) - SCOR (StructuredCommunicationReference) |
 |structuredIssuer | |String |Entity that assigns the identification |
 |endToEndReference | |String |This indicates the end to end reference for the payment. This field can be provided by one who instructs the payment and flows through the lifecycle of payment.  |
 |instructionIdReference | |String |\&quot;Indicates the unique identification as assigned by an instructing party for an instructed party to  unambiguously identify the instruction.\&quot; |
 |termsAndConditions | |String |Specifies the terms and conditions in the text format for the payment instruction, if any. |
 |paymentStatus | |String |Indicates the Status Code of the payment. Every payment in the hub is tracked using a status code which depicts the current stage at which payment is in the workflow |
 |currentStatus | |String |This indicates the current status of payment order |
 |internalStatus | |String |This indicates a full description of payment purpose code. i.e. purpose of the instruction based on a set of pre-defined categories. |
 |systemId | |String |The system application identifier from which the entry was generated |
 |indicativeRate | |String |The indicative rate at the time of submitting a payment initiation request. Actual rate with which the payment will be processed will be calculated/ fetched during payment processing.  |
 |PSDCompliant | |String |Defines whether the transaction is PSD (Payment Services Directive) compliant or not. |
 |versionNumber | |String | |
        h3. PaymentOrderResponse1Body_inner_additionalInformations
        ||Field Name||Required||Type||Description||
         |additionalInformation | |String |Additional Information provided to add context |
        h3. PaymentOrderResponse1Body_inner_beneficiaries
        ||Field Name||Required||Type||Description||
         |beneficiaryId | |String |Indicates the Id of beneficiary when beneficiary details are stored |
 |beneficiaryAccountId | |String |Indicates the account number of the beneficiary |
 |beneficiaryBIC | |String |BIC (Bank Identifier Code) of the beneficiary customer  |
 |beneficiaryName | |String |Name of beneficiary |
 |beneficiaryCountryCode | |String | |
 |beneficiaryIBAN | |String |The IBAN of the beneficiary&#39;s account |
 |accountWithBankIBAN | |String |This is the IBAN of the institution where beneficiary holds an account |
        h3. PaymentOrderResponse1Body_inner_charges
        ||Field Name||Required||Type||Description||
         |chargeAccountId | |String |Indicates the account to which the charges has to be levied. Used when charges are to be taken from a separate account |
 |chargeAccountCurrencyId | |String |When a charge account is specified, this field indicates the currency of the charge account |
 |chargeType | |String |Holds the type of the charges to be collected |
 |chargeName | |String |The description of the charge to be taken for payment |
 |chargeCurrencyId | |String |Specifies the currency of the charge amount. Allowed only when a charge amount is specified  |
 |chargeAmount | |String |Indicates the charge amount in the charge currency which is to be applied for instruction for e.g. charge to be taken for payment stop instruction |
 |chargeAccountCurrencyAmount | |BigDecimal | |
        h3. PaymentOrderResponse1Body_inner_credits
        ||Field Name||Required||Type||Description||
         |creditAccountId | |String |This is the account which will be credited for the instruction |
 |creditAccountIBAN | |String |Indicates the IBAN of the credit account |
 |requiredCreditValueDate | |date |The credit value date i.e. tentative date on which the payment system will process the payment |
 |creditValueDate | |date |The value date applied to the credit side of a payment |
        h3. PaymentOrderResponse1Body_inner_debits
        ||Field Name||Required||Type||Description||
         |debitAccountId | |String |Indicates the debit account number of the payment |
 |debitAccountIBAN | |String |Indicates the debit account IBAN of the payment |
 |debitCurrency | |String |Indicates the currency of debit account |
 |debitValueDate | |date |The date on which the Invocation amount will be debited for settlement |
 |totalDebitAmount | |BigDecimal |The total debit amount including the charges associated for the payment |
        h3. PaymentOrderResponse1Body_inner_invoiceReferences
        ||Field Name||Required||Type||Description||
         |invoiceReference | |String |It provides the reference of the invoice  |
        h3. PaymentOrderResponse1Body_inner_narratives
        ||Field Name||Required||Type||Description||
         |narrative | |String |The additional text printed on descriptive statements in addition to the standard narrative and/or reference |
        h3. PaymentOrderResponse1Body_inner_remittanceInformations
        ||Field Name||Required||Type||Description||
         |remittanceInformation | |String |Indicates the remittance information that is supplied to enable the matching/reconciliation of an entry with the items that the payment is intended to settle, such as commercial invoices in an accounts&#39; receivable system, in an unstructured form. |
        h3. PaymentOrderResponseBody
        ||Field Name||Required||Type||Description||
         |narratives | |array[PaymentOrderBody_narratives] |The additional text printed on descriptive statements in addition to the standard narrative and/or reference |
 |additionalInformations | |array[PaymentOrderBody_additionalInformations] |Additional Information provided to add context |
 |remittanceInformations | |array[PaymentOrderBody_remittanceInformations] |Indicates the remittance information that is supplied to enable the matching/reconciliation of an entry with the items that the payment is intended to settle, such as commercial invoices in an accounts&#39; receivable system, in an unstructured form. |
 |signatories | |array[PaymentOrderBody_signatories] |The authorised signatories for the payments can be specified here. More applicable in case of corporate payments where multiple signatories are required to sign a payment instruction |
 |invoiceReferences | |array[PaymentOrderBody_invoiceReferences] |It provides the reference of the invoice  |
 |charges | |array[PaymentOrderBody_charges] |The charges or fees for this transaction |
 |overrides | |array[PaymentOrderBody_overrides] |The override message is captured  that was generated at the time of commitment of the transaction to the database. |
 |paymentOrderProductId | |String |Indicates the payment order product for which payment is initiated |
 |debitAccountId | |String |Indicates the debit account number of the payment |
 |debitAccountIBAN | |String |Indicates the debit account IBAN of the payment |
 |debitCurrency | |String |Indicates the currency of debit account |
 |debitValueDate | |date |The date on which the Invocation amount will be debited for settlement |
 |creditAccountId | |String |This is the account which will be credited for the instruction |
 |creditAccountIBAN | |String |Indicates the IBAN of the credit account |
 |orderingCustomerId | |String |Indicates the customer id for the ordering customer |
 |orderingCustomerName | |String |Indicates the name of Ordering Customer |
 |paymentCurrencyId | |String |The currency of payment. |
 |amount | |BigDecimal |This is the payment amount |
 |executionDate | |date |The date when payment will be processed |
 |treasuryRate | |String |The Treasury rate for the conversion between payment currency and the ordering currency |
 |forexSpread | |String |The spread that is applied to the published internal exchange rates to derive the final exchange rate or the customer rate for the transaction for currency conversion between ordering currency and payment currency |
 |forexCustomerRate | |String |The exchange rate that is actually applied for currency conversion between ordering currency and payment currency in case of transactions involving FX conversion.  |
 |orderingPortfolio | |String |Indicates the portfolio id for the debit side if the account belongs to a specific portfolio |
 |creditPortfolio | |String |Indicates the portfolio id for the credit side if the account belongs to a specific portfolio |
 |orderingReference | |String |The reference related to the ordering details |
 |chargeBearer | |String |Indicates who will bear all charges for the payment. Allowed options are Recipient To Pay All Charges, Pay My Bank&#39;s Charges or Pay My Bank Charges Only |
 |beneficiaryId | |String |Indicates the Id of beneficiary when beneficiary details are stored |
 |beneficiaryAccountId | |String |Indicates the account number of the beneficiary |
 |beneficiaryBIC | |String |BIC (Bank Identifier Code) of the beneficiary customer  |
 |beneficiaryName | |String |Name of beneficiary |
 |accountWithBankBIC | |String |This is the BIC code of the institution where beneficiary holds an account |
 |beneficiaryBankClearingCode | |String |Clearing code or sort code of the beneficiary bank |
 |accountWithBankClearingCode | |String |This is the national clearing code or sort code of the institution where beneficiary holds an account |
 |clearingChannel | |String |Indicates the clearing channel for the payment in the ISO format of the Clearing System Identifiers |
 |structuredCreditorReference | |String |This is the unique reference, as assigned by the creditor, to unambiguously refer to the payment |
 |beneficiaryCountryCode | |String | |
 |beneficiaryIBAN | |String |The IBAN of the beneficiary&#39;s account |
 |accountWithBankIBAN | |String |This is the IBAN of the institution where beneficiary holds an account |
 |requiredCreditValueDate | |date |The credit value date i.e. tentative date on which the payment system will process the payment |
 |purpose | |String |Indicates the purpose code of the payment |
 |structuredCommunicationCode | |String |Creditor reference in a coded form i.e - RADM (RemittanceAdviceMessage) - RPIN (RelatedPaymentInstruction) - FXDR (ForeignExchangeDealReference) - DISP (DispatchAdvice) - PUOR (PurchaseOrder) - SCOR (StructuredCommunicationReference) |
 |structuredIssuer | |String |Entity that assigns the identification |
 |endToEndReference | |String |This indicates the end to end reference for the payment. This field can be provided by one who instructs the payment and flows through the lifecycle of payment.  |
 |instructionIdReference | |String |\&quot;Indicates the unique identification as assigned by an instructing party for an instructed party to  unambiguously identify the instruction.\&quot; |
 |termsAndConditions | |String |Specifies the terms and conditions in the text format for the payment instruction, if any. |
 |indicativeRate | |String |The indicative rate at the time of submitting a payment initiation request. Actual rate with which the payment will be processed will be calculated/ fetched during payment processing.  |
 |chargeAccountId | |String |Indicates the account to which the charges has to be levied. Used when charges are to be taken from a separate account |
 |chargeAccountCurrencyId | |String |When a charge account is specified, this field indicates the currency of the charge account |
 |creditValueDate | |date |The value date applied to the credit side of a payment |
 |PSDCompliant | |String |Defines whether the transaction is PSD (Payment Services Directive) compliant or not. |
 |totalDebitAmount | |BigDecimal |The total debit amount including the charges associated for the payment |
 |localInstrumentCode | |String | |
 |recordStatus | |String |General status of the record. Possible values: - null - authorised - IHLD - input, on hold - INAU - input, not authorised - INA2 - input, authorised, pending second authorisation - INAO - input, not authorised with blocking overrides - RNAU - reversed, not authorised - RNAO - reversed, not authorised with blocking overrides |
        h3. QueryErrorResponse
        ||Field Name||Required||Type||Description||
         |header | |ErrorHeader | |
 |error | |QueryErrorResponseBody | |
        h3. QueryErrorResponseBody
        ||Field Name||Required||Type||Description||
         |code | |String |The identifier of the error message |
 |message | |String |The actual t24 error message |
 |type | |String |The identifier of error type |
        h3. QueryHeader
        ||Field Name||Required||Type||Description||
         |audit | |ScreenHeader_audit | |
 |page_size | |Integer |The total number of records per page |
 |page_start | |Integer |The record from which the response should be displayed |
 |total_size | |Integer |The total number of records present |
 |page_token | |String |Unique id expected to get as part of response from t24 on every enquiry request |
        h3. ScreenErrorResponse
        ||Field Name||Required||Type||Description||
         |header | |ErrorHeader | |
 |error | |ScreenErrorResponseBody | |
 |override | |overrideBody | |
        h3. ScreenErrorResponseBody
        ||Field Name||Required||Type||Description||
         |errorDetails | |array[ScreenErrorResponseBody_errorDetails] | |
 |type | |String |The identifier of error type |
        h3. ScreenErrorResponseBody_errorDetails
        ||Field Name||Required||Type||Description||
         |fieldName | |String |The name of the field |
 |code | |String |The identifier of the error message |
 |message | |String |The actual t24 error message |
        h3. ScreenHeader
        ||Field Name||Required||Type||Description||
         |id | |String |The Identifier of the record created |
 |status | |String |The status of the record |
 |transactionStatus | |String |The status of the transaction |
 |audit | |ScreenHeader_audit | |
        h3. ScreenHeader_audit
        ||Field Name||Required||Type||Description||
         |T24_time | |Integer |Time taken to response by T24 |
 |versionNumber | |String |The CURR.NO. of the record |
 |parse_time | |Integer |Time taken to parse the response by IRIS |
