# -*- coding: utf-8 -*-
"""GET-запросы: проверяем чтение данных через API."""

import pytest


def test_get_single_post(session, base_url):
    """Один пост: статус 200 и нужные поля в JSON."""
    r = session.get(f"{base_url}/posts/1")
    assert r.status_code == 200
    data = r.json()
    assert data["id"] == 1
    assert "title" in data
    assert "body" in data
    assert data["userId"] == 1


def test_get_all_posts(session, base_url):
    """Список постов: всего должно быть 100."""
    r = session.get(f"{base_url}/posts")
    assert r.status_code == 200
    assert len(r.json()) == 100


def test_get_nonexistent_post(session, base_url):
    """Негативный тест: несуществующий пост -> 404."""
    r = session.get(f"{base_url}/posts/99999")
    assert r.status_code == 404


@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_get_posts_by_id(session, base_url, post_id):
    """Параметризованный тест: разные id возвращают свой пост."""
    r = session.get(f"{base_url}/posts/{post_id}")
    assert r.status_code == 200
    assert r.json()["id"] == post_id


def test_post_has_comments(session, base_url):
    """У поста есть комментарии, и каждый привязан именно к нему."""
    r = session.get(f"{base_url}/posts/1/comments")
    assert r.status_code == 200
    comments = r.json()
    assert len(comments) > 0
    for c in comments:
        assert c["postId"] == 1
