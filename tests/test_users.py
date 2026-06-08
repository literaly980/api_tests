# -*- coding: utf-8 -*-
"""Валидация данных пользователей в ответе API."""


def test_users_count(session, base_url):
    """Пользователей должно быть ровно 10."""
    r = session.get(f"{base_url}/users")
    assert r.status_code == 200
    assert len(r.json()) == 10


def test_user_email_is_valid(session, base_url):
    """У каждого пользователя корректный email (есть @ и точка)."""
    users = session.get(f"{base_url}/users").json()
    for u in users:
        assert "@" in u["email"]
        assert "." in u["email"]


def test_user_has_required_fields(session, base_url):
    """В карточке пользователя есть все обязательные поля."""
    data = session.get(f"{base_url}/users/1").json()
    for field in ["id", "name", "username", "email", "address"]:
        assert field in data
