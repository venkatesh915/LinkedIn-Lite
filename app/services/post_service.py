from app.repositories.post_repository import (
    create_post,
    get_post_by_id,
    get_all_posts,
    update_post,
    delete_post
)


def add_post(db, post):
    return create_post(db, post)


def get_post(db, post_id):
    post = get_post_by_id(db, post_id)

    if not post:
        raise Exception("Post not found")

    return post


def list_posts(db):
    return get_all_posts(db)


def edit_post(db, post_id, post_data):
    post = get_post_by_id(db, post_id)

    if not post:
        raise Exception("Post not found")

    return update_post(db, post_id, post_data)


def remove_post(db, post_id):
    post = get_post_by_id(db, post_id)

    if not post:
        raise Exception("Post not found")

    return delete_post(db, post_id)