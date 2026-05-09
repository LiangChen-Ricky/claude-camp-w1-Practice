# greeting.py
# 个性化问候语 —— 输入姓名和年龄，输出格式化问候
# Week 1 作业 | XiaoLiang

CREATOR_ID = "xiaoliang"

def get_name():
    while True:
        name = input("请输入你的姓名：").strip()
        if not name:
            print("❌ 姓名不能为空，请至少输入1个字符。\n")
            continue
        if len(name) > 50:
            print("❌ 姓名太长，请输入50字以内。\n")
            continue
        return name

def get_age():
    while True:
        raw = input("请输入你的年龄：").strip()
        try:
            age = int(float(raw))
        except ValueError:
            print("❌ 年龄需要输入数字，例如：25\n")
            continue
        if age < 1 or age > 120:
            print(f"⚠️  {age} 不是合理年龄，请输入 1 到 120 之间的数字。\n")
            continue
        return age

def get_greeting(age):
    if age < 13:
        return "你好小朋友，希望你每天开心！"
    elif age < 18:
        return "青春是最宝贵的财富，好好加油！"
    elif age < 60:
        return "希望你工作顺利，生活充实！"
    else:
        return "岁月沉淀，智慧与日俱增，您好！"

def main():
    print("=" * 40)
    print("       👋  个性化问候语")
    print("=" * 40)
    name = get_name()
    age = get_age()

    print()
    if name.strip().lower() == CREATOR_ID:
        print("🎉 欢迎回来，XiaoLiang！")
        print("   你是本程序的创建者，向你致敬！")
        print(f"   你今年 {age} 岁，继续加油学习 Python！")
    else:
        greeting = get_greeting(age)
        print(f"你好，{name}！")
        print(f"你今年 {age} 岁。{greeting}")
    print()

if __name__ == "__main__":
    main()
