import requests


def test_enroll_dental_plan_via_api():
    session_id = "a967cffbcb533f978739cf9e88b816c7"             #Replace with your session ID

    url = "https://partner-dev-benefits.plansource.com/v1/self_service/cart/coverages"
    headers = {
        "Content-Type": "application/json",
        "Referer": "https://partner-dev-benefits.plansource.com/subscriber/benefits/current/plan/319900164?orgBenefitId=121137668",
        "x-csrf-token": "CseIAP8v3QpHulKwq5wVAFn9cHMe1sunXci/3ItqolrK4lmcq0r0lepVYg7r2NE6HwdMylw+NBwkpsrco50AVg=="     #Replace with your Token
    }

    cookies = {'_session_id': session_id}

    json_data = {
        "enrollment_context_type": "initial",
        "org_benefit_id": 121137668,
        "election": {
            "dependent_ids": [36739076],
            "org_plan_id": 319900164,
            "coverage_level_id": 459
        },
        "life_event_completed": False
    }

    response = requests.put(url, headers=headers, cookies=cookies, json=json_data)

    print(response.status_code)
    print(response.text)


    assert response.status_code == 200, "API enrollment failed"

    #To run this code, use:  pytest -s tests/test_enroll_dental_api.py
