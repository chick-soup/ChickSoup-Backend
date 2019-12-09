from .models import Friend


class FriendService(object):
    @staticmethod
    def check_if_friend_or_not(host_id: int, guest_id: int) -> bool:
        return True if len(Friend.objects.filter(host_id=host_id, guest_id=guest_id).values()) else False

    @staticmethod
    def create_new_friend(host_id: int, guest_id: int) -> None:
        Friend(host_id=host_id, guest_id=guest_id).save()
