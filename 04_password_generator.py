# password_generator.py
# 简单密码生成器 —— 用户输入长度，生成随机密码
# Week 1 作业 | XiaoLiang

import random
import string

MIN_LEN = 8
MAX_LEN = 64

def get_length():
    while True:
        raw = input(f"请输入密码长度（{MIN_LEN}～{MAX_LEN} 位）：").strip()
        try:
            length = int(float(raw))
        except ValueError:
            print("❌ 请输入整数，例如：16\n")
            continue
        if float(raw) != int(float(raw)):
            print(f"⚠️  小数已自动取整为 {length} 位。")
        if length < MIN_LEN:
            print(f"❌ 长度 {length} 太短，不安全！最少 {MIN_LEN} 位。\n")
            continue
        if length > MAX_LEN:
            print(f"❌ 长度 {length} 超出上限 {MAX_LEN} 位，请重新输入。\n")
            continue
        return length

def generate_password(length):
    chars = string.ascii_letters + string.digits + string.punctuation
    # 确保至少包含各类字符一个
    pwd = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation),
    ]
    pwd += [random.choice(chars) for _ in range(length - 4)]
    random.shuffle(pwd)
    return "".join(pwd)

def check_strength(pwd):
    has_upper = any(c.isupper() for c in pwd)
    has_lower = any(c.islower() for c in pwd)
    has_digit = any(c.isdigit() for c in pwd)
    has_symbol = any(c in string.punctuation for c in pwd)
    score = sum([has_upper, has_lower, has_digit, has_symbol])
    if score == 4 and len(pwd) >= 12:
        return "🟢 强（大小写 + 数字 + 符号）"
    elif score >= 3:
        return "🟡 中等"
    else:
        return "🔴 弱，建议增加长度或字符种类"

def main():
    print("=" * 40)
    print("       🔑  密码生成器")
    print("=" * 40)
    length = get_length()
    while True:
        pwd = generate_password(length)
        print(f"\n✅  密码：{pwd}")
        print(f"   强度：{check_strength(pwd)}")
        print("⚠️  请勿通过聊天或邮件分享此密码。\n")
        again = input("重新生成一个？(y/n)：").strip().lower()
        if again != "y":
            print("👋 密码已生成，请妥善保管！")
            break

if __name__ == "__main__":
    main()
