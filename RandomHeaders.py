import random

user_agent_list = open("UserAgent.csv", "r").read().split("\n")
random.shuffle(user_agent_list)


def LoadHeader(lang=None):
    headers = {'User-Agent': random.choice(user_agent_list)}
    if lang is not None:
        # es-ES,es;q=0.9
        first_part = random.choice(lang)
        second_part = first_part.split("-")[-1].lower()
        headers["Accept-Language"] = "%s,%s;q=0.9" % (first_part, second_part)
        headers["Accept-Encoding"] = "gzip, deflate, br"
    return headers


if __name__ == "__main__":
    print(LoadHeader())
    print(LoadHeader(("es-ES", "en-US", "ca-ES")))
