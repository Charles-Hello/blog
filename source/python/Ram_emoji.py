import emoji
import random

def get_random_emoji():
    # 获取所有可用的Emoji表情符号的Unicode编码
    all_emoji_unicode = emoji.unicode_codes.get_aliases_unicode_dict().values()

    # 随机选择一个Emoji表情符号的Unicode编码，并将其转换为字符串类型
    random_unicode = random.choice(list(all_emoji_unicode))
    random_unicode_str = str(random_unicode)

    # 将Unicode编码转换为对应的Emoji表情符号
    random_emoji = emoji.emojize(random_unicode_str)

    return random_emoji

# 调用函数获取随机的Emoji表情符号
random_emoji = get_random_emoji()
