import random

def generate_fake_location():
    keywords = ['宝城', '仙林', '蜀山', '琼华', '龙泉', '白云', '流云', '清风', '绝峰', '鹿角']
    suffixes = ['镇', '市', '街', '巷', '门', '山', '岭', '洞', '林', '庄']
    return random.choice(keywords) + random.choice(suffixes)

# 示例输出
for _ in range(10):
    print(generate_fake_location())