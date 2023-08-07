import pytest

from crawler_benefit.contract.steps.etl_contract import EtlContract
from crawler_benefit.exceptions.steps.etl_exception import EtlException
from crawler_benefit.queue_driver.rabbitmq.consumer.get_benefit_by_cpf_consumer import (
    GetBenefitByCpfConsumer,
)
from crawler_benefit.steps.pipeline_benefit import PipelineBenefit


def test_etl_integration_consumer_success(mocker):
    benefit = "234243241"
    time_function_duration = 22
    cpf = "13975866055"
    data = {"benefit_number": benefit, "time_function_duration": time_function_duration, "cpf": cpf}
    mocker_extract = mocker.patch.object(
        PipelineBenefit, "_extract", return_value=EtlContract(data, "Extract", data["time_function_duration"])
    )
    mocker_transform = mocker.patch.object(
        PipelineBenefit, "_transform", return_value=EtlContract(data, "Transform", data["time_function_duration"])
    )
    mocker_load = mocker.patch.object(
        PipelineBenefit, "_load", return_value=EtlContract(data, "Load", data["time_function_duration"])
    )

    message = {"cpf": "87923601062", "password": "aKgnTKFCDl", "login": "login"}
    GetBenefitByCpfConsumer().consume(message)
    mocker_transform.assert_called()
    mocker_extract.assert_called()
    mocker_load.assert_called()


def test_etl_integration_consumer_failed_with_extract_was_error(mocker):
    benefit = "234243241"
    time_function_duration = 22
    cpf = "13975866055"
    data = {"benefit_number": benefit, "time_function_duration": time_function_duration, "cpf": cpf}
    mocker_extract = mocker.patch.object(
        PipelineBenefit, "_extract", side_effect=EtlException("Extract", {}, "error when running extract stage")
    )
    mocker_transform = mocker.patch.object(
        PipelineBenefit, "_transform", return_value=EtlContract(data, "Transform", data["time_function_duration"])
    )
    mocker_load = mocker.patch.object(
        PipelineBenefit, "_load", return_value=EtlContract(data, "Load", data["time_function_duration"])
    )

    message = {"cpf": "87923601062", "password": "aKgnTKFCDl", "login": "login"}
    with pytest.raises(EtlException):
        GetBenefitByCpfConsumer().consume(message)
    mocker_transform.assert_not_called()
    mocker_extract.assert_called()
    mocker_load.assert_not_called()


def test_etl_integration_consumer_failed_with_transform_was_error(mocker):
    benefit = "234243241"
    time_function_duration = 22
    cpf = "13975866055"
    data = {"benefit_number": benefit, "time_function_duration": time_function_duration, "cpf": cpf}
    mocker_extract = mocker.patch.object(
        PipelineBenefit, "_extract", return_value=EtlContract(data, "Transform", data["time_function_duration"])
    )
    mocker_transform = mocker.patch.object(
        PipelineBenefit, "_transform", side_effect=EtlException("Transform", {}, "error when running transform stage")
    )
    mocker_load = mocker.patch.object(
        PipelineBenefit, "_load", return_value=EtlContract(data, "Load", data["time_function_duration"])
    )

    message = {"cpf": "87923601062", "password": "aKgnTKFCDl", "login": "login"}
    with pytest.raises(EtlException):
        GetBenefitByCpfConsumer().consume(message)
    mocker_transform.assert_called()
    mocker_extract.assert_called()
    mocker_load.assert_not_called()


def test_etl_integration_consumer_failed_with_load_was_error(mocker):
    benefit = "234243241"
    time_function_duration = 22
    cpf = "13975866055"
    data = {"benefit_number": benefit, "time_function_duration": time_function_duration, "cpf": cpf}
    mocker_extract = mocker.patch.object(
        PipelineBenefit, "_extract", return_value=EtlContract(data, "Extract", data["time_function_duration"])
    )
    mocker_transform = mocker.patch.object(
        PipelineBenefit, "_transform", return_value=EtlContract(data, "Transform", data["time_function_duration"])
    )
    mocker_load = mocker.patch.object(
        PipelineBenefit, "_load", side_effect=EtlException("Load", {}, "error when running load stage")
    )

    message = {"cpf": "87923601062", "password": "aKgnTKFCDl", "login": "login"}
    with pytest.raises(EtlException):
        GetBenefitByCpfConsumer().consume(message)
    mocker_transform.assert_called()
    mocker_extract.assert_called()
    mocker_load.assert_called()
