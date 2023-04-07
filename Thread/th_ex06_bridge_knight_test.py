from th_ex04_Bridge import Bridge
from th_ex05_Knights import Knight

print("Start Simulation - -")
bridge = Bridge()

Knight(bridge, "일연조", "일천").start()
Knight(bridge, "이연조", "이천").start()
Knight(bridge, "삼연조", "삼천").start()
Knight(bridge, "사연조", "사천").start()
Knight(bridge, "오연조", "오천").start()