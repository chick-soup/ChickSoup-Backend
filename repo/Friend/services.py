from .models import Friend

from Profile.services import ProfileService
from User.services import UserService


class FriendService(object):
    @staticmethod
    def check_request_friend(host_id: int, guest_id: int) -> bool:
        return True if len(Friend.objects.filter(host_id=host_id, guest_id=guest_id).values()) else False

    @staticmethod
    def create_new_friend(host_id: int, guest_id: int) -> None:
        Friend(host_id=host_id, guest_id=guest_id).save()

    @staticmethod
    def check_both_friend(id1: int, id2: int) -> bool:
        if FriendService.check_request_friend(id1, id2) and FriendService.check_request_friend(id2, id1):
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
    def check_relationship(id1: int, id2: int) -> int:
        """
        두 회원의 primary key를 받아 서로의 친구 관계를 반환해준다.
        :param id1: 첫 번째 사용자 id
        :param id2: 두 번째 사용자 id
        :return: integer
        3 -> 두 사용자는 서로 친구임
        2 -> 두 번째 사용자가 첫 번째 사용자에게 친구 요청을 보냄
        1 -> 첫 번째 사용자가 두 번째 사용자에게 친구 요청을 보냄
        0 -> 두 사용자 간에 친구 요청이 없음
        """

        if FriendService.check_both_friend(id1=id1, id2=id2):
            relate = 3
        elif FriendService.check_request_friend(host_id=id2, guest_id=id1):
            relate = 2
        elif FriendService.check_request_friend(host_id=id1, guest_id=id2):
            relate = 1
        else:
            relate = 0

        return relate

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

    @staticmethod
    def get_friend_list(pk: int) -> list:
        return_list = []

        for friend in Friend.objects.filter(host_id=pk):
            if not UserService.check_pk_exists(friend.guest_id):
                continue
            if not FriendService.check_both_friend(id1=pk, id2=friend.guest_id):
                continue
            profile = ProfileService.get_profile_with_pk(friend.guest_id)
            return_list.append([friend.guest_id, profile.nickname, "" if profile.status_message is None else profile.status_message, friend.mute, friend.hidden, friend.bookmark])

        return return_list

    @staticmethod
    def get_request_list(host_id: int) -> list:
        return_list = []

        for friend in Friend.objects.filter(host_id=host_id):
            if not UserService.check_pk_exists(friend.guest_id):
                continue
            if FriendService.check_both_friend(id1=friend.host_id, id2=friend.guest_id):
                continue
            profile = ProfileService.get_profile_with_pk(friend.guest_id)
            return_list.append([friend.guest_id, profile.nickname, "" if profile.status_message is None else profile.status_message, friend.mute, friend.hidden, friend.bookmark])

        return return_list

    @staticmethod
    def get_response_list(host_id: int) -> list:
        return_list = []

        for friend in Friend.objects.filter(guest_id=host_id):
            if not UserService.check_pk_exists(friend.host_id):
                continue
            if FriendService.check_both_friend(id1=friend.host_id, id2=friend.guest_id):
                continue
            profile = ProfileService.get_profile_with_pk(friend.host_id)
            return_list.append([friend.host_id, profile.nickname, "" if profile.status_message is None else profile.status_message, friend.mute, friend.hidden, friend.bookmark])

        return return_list

    @staticmethod
    def sort_list(friend_list: list) -> list:
        friend_list.sort(key=lambda x: x[1])
        return friend_list

    @staticmethod
    def sort_list_with_bookmark(friend_list: list) -> list:
        return_list = []
        friend_list = FriendService.sort_list(friend_list)

        for friend in friend_list:
            if friend[5] is True:
                return_list.append(friend)

        for friend in friend_list:
            if friend[5] is False:
                return_list.append(friend)

        return return_list

    @staticmethod
    def convert_list_to_dict(friend_list: list) -> dict:
        return_dict = {}
        count = 1
        for friend in friend_list:
            return_dict[count] = {
                'id': friend[0],
                'nickname': friend[1],
                'status_message': friend[2],
                'mute': friend[3],
                'hidden': friend[4],
                'bookmark': friend[5]
            }
            count += 1
        return return_dict

    @staticmethod
    def filter_if_mute_false(friend_list: list) -> list:
        return_list = []
        for friend in friend_list:
            if friend[3] is False:
                continue
            return_list.append(friend)
        return return_list

    @staticmethod
    def filter_if_hidden_false(friend_list: list) -> list:
        return_list = []
        for friend in friend_list:
            if friend[4] is False:
                continue
            return_list.append(friend)
        return return_list


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
