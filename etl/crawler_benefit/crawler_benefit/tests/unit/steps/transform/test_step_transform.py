from crawler_benefit.contract.steps.etl_contract import EtlContract
from crawler_benefit.steps.transform.transform import Transform


def test_step_transform_with_remove_special_character():
    benefit_number_expect = "1234242"
    data = {"benefit_number": "123.424-2", "cpf": "13975866055"}
    etl_contract = EtlContract(data=data, stage="Extract", time=20)
    result = Transform(etl_contract=etl_contract).transform()
    assert result.data["benefit_number"] == benefit_number_expect


def test_step_transform_without_remove_special_character():
    benefit_number_expect = "1234242"
    data = {"benefit_number": benefit_number_expect, "cpf": "13975866055"}
    etl_contract = EtlContract(data=data, stage="Extract", time=20)
    result = Transform(etl_contract=etl_contract).transform()
    assert result.data["benefit_number"] == benefit_number_expect
