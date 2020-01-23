from django.contrib.auth import get_user_model

def get_user(id=None,email=None):
    User = get_user_model()
    if id is None and email is None:
        raise Exception("Either id or email is required to retrieve user")
    user = None
    try:
        if id:
            user = User.objects.get(id=id)
        if email:
            user = User.objects.get(email=email)
    except User.DoesNotExist:
        pass
    return user
