import json
import uuid
from jsonschema import ValidationError, validate
import pytest
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_
from commonUtils import generate_Order_id, printRequestPayload, printResponsePayload
from expectedResults import EXPECTED_RESULTS


'''
TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''


@pytest.mark.parametrize("status", [("available"), ("sold"), ("pending")])
def test_patch_order_by_id(status, generate_Order_id):
    expReslt_OrdNotFound = EXPECTED_RESULTS["order_not_found"]
    expReslt_StatCd = EXPECTED_RESULTS["status_codes"]
    endPoint = EXPECTED_RESULTS["endpoint"]
    orderId = generate_Order_id
    orderId = generate_Order_id
    test_endpoint = f"{endPoint['patch_store_by_orderId']}{orderId}"
    data = {"status": status}

    printRequestPayload(data, test_endpoint)

    response = updateOrder(test_endpoint, data)
    responsePayload = printResponsePayload(response)

    assert response.status_code == expReslt_StatCd['not_found']
    assert responsePayload['message'] == expReslt_OrdNotFound['message']

    # Validate the response schema against the defined schema in schemas.py
    # validate(instance=response.json(), schema=schemas.pet)
    for orderObj in response.json():
        try:
            validate(orderObj, schemas.orderNotFound)
            print(f"Object {str(orderObj)} is valid.")
        except ValidationError as e:
            print(f"Validation error for object {str(orderObj)}: {e}")


def updateOrder(test_endpoint, data):
    response = api_helpers.patch_api_data(test_endpoint, data)
    return response
