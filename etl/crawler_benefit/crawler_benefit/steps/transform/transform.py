import re

from crawler_benefit.contract.steps.etl_contract import EtlContract


class Transform:
    def __init__(self, etl_contract: EtlContract):
        self.etl_data = etl_contract

    def transform(self) -> EtlContract:
        benefit_number_with_special_character = self.etl_data.data["benefit_number"]
        if benefit_number_with_special_character is not None:
            benefit_number = re.sub(r"[^a-zA-Z0-9]", "", benefit_number_with_special_character)
            self.etl_data.data["benefit_number"] = benefit_number
            self.etl_data.data["benefit_number_with_special_character"] = benefit_number_with_special_character
        return EtlContract(self.etl_data.data, "Transform", "0")
