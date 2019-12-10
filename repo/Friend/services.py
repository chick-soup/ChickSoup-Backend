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
    def check_friend_status(host_id: int, guest_id: int, key: str) -> bool:
        if key is 'mute':
            return Friend.objects.get(host_id=host_id, guest_id=guest_id).mute
        if key is 'hidden':
            return Friend.objects.get(host_id=host_id, guest_id=guest_id).hidden
        if key is 'bookmark':
            return Friend.objects.get(host_id=host_id, guest_id=guest_id).bookmark

    @staticmethod
    def delete_friend(host_id: int, guest_id: int) -> None:
        Friend.objects.get(host_id=host_id, guest_id=guest_id).delete()
        Friend.objects.get(host_id=guest_id, guest_id=host_id).delete()

    @staticmethod
    def set_friend_status(host_id: int, guest_id: int, key: str, status: bool) -> None:
        friend = Friend.objects.get(host_id=host_id, guest_id=guest_id)
        if key is 'mute':
            friend.mute = status
        if key is 'hidden':
            friend.hidden = status
        if key is 'bookmark':
            friend.bookmark = status
        friend.save()


class UserPutAPIService(object):
    @staticmethod
    def check_put_bad_request(data: dict) -> bool:
        count = 0
        for key in ['mute', 'hidden', 'bookmark']:
            if key in data and (data[key] is '0' or data[key] is '1'):
                count += 1
        if count is 1:
            return False
        return True

    @staticmethod
    def get_key_from_data(data: dict) -> str:
        if 'mute' in data:
            return 'mute'
        if 'hidden' in data:
            return 'hidden'
        if 'bookmark' in data:
            return 'bookmark'
