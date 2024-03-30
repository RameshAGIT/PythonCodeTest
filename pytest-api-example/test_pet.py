from jsonschema.exceptions import ValidationError
from jsonschema import validate
import pytest
from commonUtils import printResponsePayload
import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_
from expectedResults import EXPECTED_RESULTS

'''
TODO: Finish this test by...
1) Troubleshooting and fixing the test failure
The purpose of this test is to validate the response matches the expected schema defined in schemas.py
'''

expReslt_StatCd = EXPECTED_RESULTS["status_codes"]
endPoint = EXPECTED_RESULTS["endpoint"]


# @pytest.mark.skip('Skipping...')
def test_pet_schema():
    test_endpoint = endPoint['get_pet_by_id']
    response = api_helpers.get_api_data(test_endpoint)
    printResponsePayload(response)
    assert response.status_code == expReslt_StatCd['success']
    # Validate the response schema against the defined schema in schemas.py
    print(schemas.pet)
    validate(instance=response.json(), schema=schemas.pet)


'''
TODO: Finish this test by...
1) Extending the parameterization to include all available statuses
2) Validate the appropriate response code
3) Validate the 'status' property in the response is equal to the expected status
4) Validate the schema for each object in the response
'''


@pytest.mark.skip('Skipping...')
@pytest.mark.parametrize("status", [("available"), ("sold"), ("pending")])
def test_find_by_status_200(status):
    test_endpoint = endPoint['get_pet_by_status']
    params = {
        "status": status
    }
    response = api_helpers.get_api_data(test_endpoint, params)
    responsePayLoad = printResponsePayload(response)

    assert response.status_code == expReslt_StatCd['success']

    for pet in responsePayLoad:
        assert pet['status'] == status

    for petObj in responsePayLoad:
        try:
            validate(petObj, schemas.pet)
            print(f"Object {str(petObj)} is valid.")
        except ValidationError as e:
            print(f"Validation error for object {str(petObj)} : {e}")


'''
TODO: Finish this test by...
1) Testing and validating the appropriate 404 response for /pets/{pet_id}
2) Parameterizing the test for any edge cases
'''


@pytest.mark.skip('Skipping...')
def test_get_by_id_404():
    test_endpoint = endPoint['get_pet_by_id_404']
    response = api_helpers.get_api_data(test_endpoint)
    printResponsePayload(response)
    assert response.status_code == expReslt_StatCd['not_found']
