from __future__ import annotations

from typing import List

from pydantic import BaseModel


class BenefitModelRequest(BaseModel):
    login: str
    password: str
    cpf: str
