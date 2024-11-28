from __future__ import annotations

from typing import Dict, Any, Optional, Final

JsonType = Dict[str, Any]



class JobResult:

    def __init__(self, is_success: bool) -> None:
        self.success = is_success
        self.error_message: str = ""
        self.success_message: str = ""
        self.value: Any = None

    def is_success(self) -> bool:
        return self.success

    def is_failed(self) -> bool:
        return not self.success

    def to_dict(self) -> Dict[str, Any]:
        if not self.success:
            return {"error_message": self.error_message, "Is success": self.is_success()}
        else:
            dict_to_return: Dict[str, Any] = {"Is success": self.is_success()}
            dict_to_return.update({"success_message": self.success_message})
            return dict_to_return

    def get_value_or_none(self) -> Optional[Any]:
        if self.is_failed():
            return None
        return self.value

    def get_error_message_or_none(self) -> Optional[str]:
        if self.is_success():
            return None
        return self.error_message

    def get_error_message_augmented(self) -> str:
        if self.is_success():
            return ""
        return f"{type(self).__name__}: {self.error_message}"

    def __eq__(self, other) -> bool:
        if not isinstance(other, JobResult):
            return False
        else:
            return self.success == other.success and self.value == other.value \
                   and self.success_message == other.success_message and self.error_message == other.error_message

    def __str__(self) -> str:
        return str(self.to_dict())

    def __repr__(self) -> str:
        return f'success={self.success} error_message={self.error_message} success_message={self.success_message} ' \
               f'value={self.value}'

    @staticmethod
    def create_job_failed(message: str) -> JobResult:
        job_result = JobResult(is_success=False)
        job_result.error_message = message
        return job_result

    @staticmethod
    def create_job_success(message="", value=None) -> JobResult:
        job_result = JobResult(is_success=True)
        job_result.success_message = message
        job_result.value = value
        return job_result


class HttpJobResult(JobResult):
    def __init__(self, response_status_code: int, response_body: Optional[JsonType] = None):
        super().__init__(is_success=False)
        self._response_status_code = response_status_code
        self._response_body = response_body
        self.success = self._extract_status_code()
        self._extract_message()

    def _extract_status_code(self) -> bool:
        return self._response_status_code in [200, 201, 202]

    def _extract_message(self) -> None:
        if self.is_failed():
            self.error_message = "ERROR REMOTE API"
        else:
            self.success_message = "SUCCESS REMOTE API"

    def to_dict(self) -> JsonType:
        result = super().to_dict()
        result.update({"status_code": self.get_status_code(), "body": self.get_body()})
        return result

    def get_body(self) -> Optional[JsonType]:
        return self._response_body

    def get_status_code(self) -> int:
        return self._response_status_code

    def __repr__(self):
        return super().__repr__() + f" response_status_code={self.get_status_code()} response_body={self.get_body()}"

    def __eq__(self, other):
        return super().__eq__ \
               and self.get_status_code() == other.get_status_code() \
               and self.get_body() == other.get_body()


class AllJobsResults:
    PREFIX_MESSAGES: Final = "Sumup AllJobsResults :"

    def __init__(self) -> None:
        self.all_jr: Dict[str, JobResult] = {}

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AllJobsResults):
            return False
        return (self.all_jr == other.all_jr)

    def add(self, job_name: str, job_result: JobResult) -> None:
        self.all_jr[job_name] = job_result

    def at_least_one_failed(self) -> bool:
        self._raise_error_if_empty()
        for jr in self.all_jr.values():
            if jr.is_failed():
                return True
        return False

    def all_success(self) -> bool:
        return not self.at_least_one_failed()

    def get_jr(self, job_name: str) -> JobResult:
        if job_name not in self.all_jr:
            raise MissingJobResultInAllJobsResultsError
        return self.all_jr[job_name]

    def _raise_error_if_empty(self) -> None:
        if not self.all_jr:
            raise EmptyAllJobsResultsError

    def get_augmented_errors_msgs(self) -> str:
        result = []
        for job_name, a_jr in self.all_jr.items():
            if a_jr.is_failed():
                result.append(f"job_name={job_name} -- job_type={a_jr.get_error_message_augmented()}\n")
        return "".join(result)

    def get_jr_value_or_none(self, job_name: str) -> Any:
        return self.get_jr(job_name=job_name).get_value_or_none()

    def _jr_message_formating(self, job_name: str, job_result: JobResult) -> str:
        if job_result.is_success():
            return f" [{job_name}]=SUCCESS"
        return f" [{job_name}]=<{job_result.error_message}>"

    def sum_up_to_jr(self) -> JobResult:
        jobs_names = ""

        for job_name, job_result in self.all_jr.items():
            jobs_names += self._jr_message_formating(job_name=job_name, job_result=job_result)

        message = "Sumup AllJobsResults :" + jobs_names
        if self.all_success():
            return JobResult.create_job_success(message=message)

        return JobResult.create_job_failed(message=message)


class EmptyAllJobsResultsError(Exception):
    pass


class MissingJobResultInAllJobsResultsError(Exception):
    pass
