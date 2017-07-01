def marshal_current_user(user):
    return dict(
        username=user.username,
        email=user.email
    )
