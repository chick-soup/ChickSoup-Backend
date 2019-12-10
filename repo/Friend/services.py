from .models import Friend


class FriendService(object):
    @staticmethod
    def check_if_friend_or_not(host_id: int, guest_id: int) -> bool:
        return True if len(Friend.objects.filter(host_id=host_id, guest_id=guest_id).values()) else False

    @staticmethod
    def create_new_friend(host_id: int, guest_id: int) -> None:
        Friend(host_id=host_id, guest_id=guest_id).save()

    @staticmethod
    def check_both_friend(id1: int, id2: int) -> bool:
        if FriendService.check_if_friend_or_not(id1, id2) and FriendService.check_if_friend_or_not(id2, id1):
            return True
        return False

    @staticmethod
    def delete_friend(host_id: int, guest_id: int) -> None:
        Friend.objects.get(host_id=host_id, guest_id=guest_id).delete()
        Friend.objects.get(host_id=guest_id, guest_id=host_id).delete()

    @staticmethod
    def check_put_bad_request(data: dict) -> bool:
        count = 0
        for key in ['mute', 'hidden', 'bookmark']:
            if key in data:
                count += 1
        if count is 1:
            return False
        return True