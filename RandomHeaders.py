import random

user_agent_list = open("UserAgent.csv", "r").read().split("\n")
random.shuffle(user_agent_list)


def LoadHeader():
    return {'User-Agent': random.choice(user_agent_list)}


if __name__ == "__main__":
    print(LoadHeader())
