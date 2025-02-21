from chat.models import Message
from channels.db import database_sync_to_async


@database_sync_to_async
def save_message(user, text, room_name):
    """create a message record
    """
    try:
        new_message = Message.objects.create(user=user, text=text, room_name=room_name)
        new_message.save()
        return True
    except Exception as e:
        return False
