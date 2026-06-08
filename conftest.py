# -*- coding: utf-8 -*-
"""Общие фикстуры для всех тестов (pytest подхватывает их автоматически)."""

import pytest
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

BASE_URL = "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def session():
    """HTTP-сессия на все тесты.

    - trust_env=False => запросы идут НАПРЯМУЮ, мимо системного прокси (Hiddify/VPN).
    - Retry => повтор при временных сбоях сети (429/5xx), чтобы тесты не были флаки.
    """
    s = requests.Session()
    s.trust_env = False
    s.headers.update({"Accept": "application/json"})

    retry = Retry(
        total=3,
        backoff_factor=0.5,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET", "POST", "PUT", "DELETE"],
    )
    adapter = HTTPAdapter(max_retries=retry)
    s.mount("https://", adapter)
    s.mount("http://", adapter)

    yield s
    s.close()


@pytest.fixture
def base_url():
    return BASE_URL
