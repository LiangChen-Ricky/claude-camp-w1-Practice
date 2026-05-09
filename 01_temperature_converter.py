# temperature_converter.py
# 温度转换器 —— 摄氏度与华氏度互转
# Week 1 作业 | XiaoLiang

def get_temp():
    while True:
        raw = input("请输入温度数值（例如：25 或 -10）：").strip()
        raw = raw.replace("°C","").replace("°F","").replace("°","").strip()
        try:
            temp = float(raw)
        except ValueError:
            print("❌ 请输入数字，例如：25 或 -10.5\n")
            continue
        if temp < -273.15:
            print(f"❌ {temp}°C 低于绝对零度（-273.15°C），物理上不存在，请重新输入。\n")
            continue
        if temp > 10000:
            print(f"⚠️  {temp} 超出合理范围，请重新输入。\n")
            continue
        return temp

def get_direction():
    while True:
        d = input("转换方向：输入 C（摄氏→华氏）或 F（华氏→摄氏）：").strip().upper()
        if d in ("C", "F"):
            return d
        print("❌ 只接受 C 或 F，请重新输入。\n")

def main():
    print("=" * 40)
    print("       🌡️  温度转换器")
    print("=" * 40)
    while True:
        temp = get_temp()
        direction = get_direction()
        if direction == "C":
            result = temp * 9 / 5 + 32
            print(f"\n✅  {temp}°C  =  {result:.2f}°F\n")
        else:
            result = (temp - 32) * 5 / 9
            print(f"\n✅  {temp}°F  =  {result:.2f}°C\n")
        again = input("再转换一次？(y/n)：").strip().lower()
        if again != "y":
            print("👋 再见！")
            break

if __name__ == "__main__":
    main()
