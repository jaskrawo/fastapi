import pytest
from app import models


# TODO
@pytest.fixture
def vote_on_post(test_posts, session, test_user):
    new_vote = models.Vote(post_id=test_posts[3].id, user_id=test_user['id'])
    session.add(new_vote)
    session.commit()



def test_vote_on_post(authorized_client, test_posts):
    data = {
        "post_id": test_posts[3].id,
        "dir": 1
    }
    res = authorized_client.post("/vote/", json=data)
    assert res.status_code == 201

def test_vote_twice_on_post(authorized_client, test_posts, vote_on_post):
    data = {
        "post_id": test_posts[3].id,
        "dir": 1
    }
    res = authorized_client.post("/vote/", json=data)
    assert res.status_code == 409

def test_delete_vote_on_post(authorized_client, test_posts, vote_on_post):
    data = {
        "post_id": test_posts[3].id,
        "dir": 0
    }
    res = authorized_client.post("/vote/", json=data)
    assert res.status_code == 201


def test_vote_non_existent_post(authorized_client, test_posts):
    data = {
        "post_id": 30000000,
        "dir": 1
    }
    res = authorized_client.post("/vote/", json=data)
    assert res.status_code == 404

def test_delete_vote_non_existent_vote(authorized_client, test_posts):
    data = {
        "post_id": test_posts[3].id,
        "dir": 0
    }
    res = authorized_client.post("/vote/", json=data)
    assert res.status_code == 404

def test_vote_unauthorized_user(client, test_posts):
    data = {
        "post_id": test_posts[3].id,
        "dir": 1
    }
    res = client.post("/vote/", json=data)
    assert res.status_code == 401