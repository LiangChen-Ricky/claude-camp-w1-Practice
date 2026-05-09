# tip_calculator.py
# 小费计算器 —— 输入餐费和小费比例，输出明细
# Week 1 作业 | XiaoLiang

def get_amount():
    while True:
        raw = input("请输入餐费金额（例如：45.50 或 $45.50）：").strip()
        raw = raw.replace("$", "").replace("¥", "").replace(",", "").strip()
        try:
            amount = float(raw)
        except ValueError:
            print("❌ 请输入数字金额，例如：45.50\n")
            continue
        if amount <= 0:
            print("❌ 金额必须大于 0，请重新输入。\n")
            continue
        if amount > 100000:
            print("⚠️  金额超过 100,000，请确认是否正确？(y/n)：", end="")
            if input().strip().lower() != "y":
                continue
        return amount

def get_tip_rate():
    while True:
        raw = input("请输入小费比例（例如：15 表示 15%）：").strip().replace("%", "")
        try:
            rate = float(raw)
        except ValueError:
            print("❌ 请输入数字，例如：15\n")
            continue
        if rate < 0:
            print("❌ 小费比例不能为负数。\n")
            continue
        if rate > 100:
            print(f"⚠️  {rate}% 的小费比较高，常见比例是 10% / 15% / 20%。确认继续？(y/n)：", end="")
            if input().strip().lower() != "y":
                continue
        return rate / 100

def get_people():
    while True:
        raw = input("几个人平摊？（1人请直接按回车）：").strip()
        if raw == "":
            return 1
        try:
            n = int(raw)
        except ValueError:
            print("❌ 请输入整数，例如：3\n")
            continue
        if n < 1:
            print("❌ 至少1人。\n")
            continue
        return n

def main():
    print("=" * 40)
    print("       💰  小费计算器")
    print("=" * 40)
    amount = get_amount()
    rate = get_tip_rate()
    people = get_people()

    tip = amount * rate
    total = amount + tip
    per_person = total / people

    print()
    print(f"  餐费金额：  ${amount:.2f}")
    print(f"  小费({rate*100:.0f}%)：  ${tip:.2f}")
    print(f"  合计总额：  ${total:.2f}")
    if people > 1:
        print(f"  {people}人平摊：  每人 ${per_person:.2f}")
    print()

if __name__ == "__main__":
    main()
