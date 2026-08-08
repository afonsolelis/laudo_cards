import asyncio
import os
import sys
from unittest.mock import AsyncMock, MagicMock, patch

import pytest
from fastapi import HTTPException

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import main  # noqa: E402


def _fake_graders(existente, cadastradas):
    """Simula a collection `graders` sem precisar de um MongoDB real."""
    fake = MagicMock()
    fake.find_one = AsyncMock(return_value=existente)
    cursor = MagicMock()
    cursor.to_list = AsyncMock(return_value=[{"name": n} for n in cadastradas])
    fake.find = MagicMock(return_value=cursor)
    return fake


def test_graduadora_cadastrada_e_aceita():
    fake = _fake_graders({"name": "Manafix"}, ["Manafix"])
    with patch.object(main, "graders_collection", fake):
        # nao deve levantar
        asyncio.run(main.validate_grading_company("Manafix"))


def test_graduadora_nao_cadastrada_retorna_400():
    fake = _fake_graders(None, ["Manafix", "PSA"])
    with patch.object(main, "graders_collection", fake):
        with pytest.raises(HTTPException) as exc:
            asyncio.run(main.validate_grading_company("MGS"))

    assert exc.value.status_code == 400  # nosec
    # a mensagem deve listar as opcoes validas para o usuario se corrigir
    assert "MGS" in exc.value.detail  # nosec
    assert "Manafix" in exc.value.detail  # nosec
    assert "PSA" in exc.value.detail  # nosec
