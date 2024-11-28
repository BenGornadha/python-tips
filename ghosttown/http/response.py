import datetime
import json
from typing import Union

from fastapi import Response, status

from jobresult.jobresult import JobResult


def http_response_success(json_response: dict) -> Response:
    json_response.update({'status': 'SUCCESS'})
    return create_http_response(json_response, is_success=True)


def http_response_failed(json_response: dict) -> Response:
    json_response.update({'status': 'FAILED'})
    return create_http_response(json_response, is_success=False)


def create_http_response(json_response: dict, is_success: bool) -> Response:
    json_message = _environment_json()
    json_message.update(json_response)
    return Response(content=json.dumps(json_message),
                    status_code=status.HTTP_200_OK if is_success else status.HTTP_500_INTERNAL_SERVER_ERROR,
                    media_type='application/json')


def _environment_json():
    return {"environment": "dev",
            "end_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }


def create_appropriate_http_response(job_result: Union[JobResult]) -> Response:
    if job_result.is_failed():
        return http_response_failed(job_result.to_dict())
    return http_response_success(job_result.to_dict())