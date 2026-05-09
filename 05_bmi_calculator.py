# bmi_calculator.py
# BMI 计算器 —— 输入身高体重，输出 BMI 及健康建议
# Week 1 作业 | XiaoLiang

import re

def extract_number(raw):
    """从字符串中提取第一个数字（支持小数）"""
    match = re.search(r"-?\d+\.?\d*", raw)
    if match:
        return float(match.group())
    return None

def get_height():
    while True:
        raw = input("请输入身高（单位：cm，例如：175）：").strip()
        value = extract_number(raw)
        if value is None:
            print("❌ 请输入数字，例如：175\n")
            continue
        # 自动识别：用户可能输入的是米（如 1.75）
        if 1.0 <= value <= 3.0:
            converted = round(value * 100)
            confirm = input(f"⚠️  检测到 {value}，看起来是米？自动换算为 {converted} cm，正确吗？(y/n)：").strip().lower()
            if confirm == "y":
                value = converted
            else:
                print("请重新输入（以厘米为单位）：\n")
                continue
        if value < 50 or value > 250:
            print(f"❌ {value}cm 不在合理范围（50～250cm），请重新输入。\n")
            continue
        return value

def get_weight():
    while True:
        raw = input("请输入体重（单位：kg，例如：68）：").strip()
        value = extract_number(raw)
        if value is None:
            print("❌ 请输入数字，例如：68\n")
            continue
        if value < 20 or value > 300:
            print(f"❌ {value}kg 不在合理范围（20～300kg），请重新输入。\n")
            continue
        return value

def bmi_category(bmi):
    if bmi < 18.5:
        return "偏轻", "建议适当增加营养摄入，均衡饮食。"
    elif bmi < 24.0:
        return "正常", "恭喜！你的体重处于健康范围，请保持。"
    elif bmi < 28.0:
        return "偏重", "建议适量运动，注意饮食结构。"
    else:
        return "肥胖", "建议咨询医生或营养师，制定健康管理计划。"

def main():
    print("=" * 40)
    print("       ⚖️   BMI 计算器")
    print("=" * 40)
    height_cm = get_height()
    weight_kg = get_weight()

    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    category, advice = bmi_category(bmi)

    print()
    print(f"  身高：{height_cm} cm   体重：{weight_kg} kg")
    print(f"  📊 BMI：{bmi:.1f}（{category}）")
    print(f"  💡 建议：{advice}")
    print()
    print("  ⚠️  BMI 仅供参考，不替代专业医疗诊断。")
    print()

if __name__ == "__main__":
    main()

