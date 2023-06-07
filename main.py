import network_tokens_hooker
import donate_detector


def main():
    nicknames = input('Write nicknames to check... ').split()
    tokens = network_tokens_hooker.get_session_data()
    donate_getter = donate_detector.HolyworldRequester(*tokens)
    for nickname in nicknames:
        print(donate_getter.get_user_info(nickname))


if __name__ == '__main__':
    main()
