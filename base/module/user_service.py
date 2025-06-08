from base.models import User

def create_user_service(data):
    return User.objects.create(
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        email=data.get('email'),
        password=data.get('password'),
        is_active=data.get('is_active') == 'on'
    )

def update_user_service(user_id, data=None):
    user = User.objects.get(id=user_id)
    if data:
        user.first_name = data.get('first_name')
        user.last_name = data.get('last_name')
        user.email = data.get('email')
        user.password = data.get('password')
        user.is_active = data.get('is_active') == 'on'
        user.save()
    return user

def list_users_service():
    return User.objects.all()

def delete_user_service(user_id):
    User.objects.filter(id=user_id).delete()
