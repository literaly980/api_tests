# -*- coding: utf-8 -*-
"""Создание / изменение / удаление ресурса: POST, PUT, DELETE."""


def test_create_post(session, base_url):
    """POST создаёт ресурс -> 201, в ответе наши данные и новый id."""
    payload = {"title": "Тест", "body": "Текст теста", "userId": 1}
    r = session.post(f"{base_url}/posts", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert "id" in data


def test_update_post(session, base_url):
    """PUT обновляет ресурс -> 200 и возвращает новые данные."""
    payload = {"id": 1, "title": "Обновлено", "body": "Новый текст", "userId": 1}
    r = session.put(f"{base_url}/posts/1", json=payload)
    assert r.status_code == 200
    assert r.json()["title"] == "Обновлено"


def test_delete_post(session, base_url):
    """DELETE удаляет ресурс -> 200."""
    r = session.delete(f"{base_url}/posts/1")
    assert r.status_code == 200
