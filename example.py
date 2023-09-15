from line_plan_visualization import LinePlan
from line_plan_visualization import Lines
from line_plan_visualization import PhysicalRailWay
import random
import time

def main() -> None:
    # instance of class PhysicalRailway 
    example_pr = PhysicalRailWay("Beijing-Shanghai High-Speed Raiway",  # railway name
                                 {"BJN": "high",  # station name and level in order
                                  "LF": "low",
                                  "TJN": "high",
                                  "CZX": "medium",
                                  "DZD": "medium",
                                  "JNX": "high",
                                  "TA": "medium",
                                  "QFD": "medium",
                                  "TZD": "low",
                                  "ZZ": "low",
                                  "XZD": "high",
                                  "SZD": "low",
                                  "BBN": "medium",
                                  "DY": "low",
                                  "CZ": "low",
                                  "NJN": "high",
                                  "ZJN": "medium",
                                  "DYB": "low",
                                  "CZB": "medium",
                                  "WXD": "medium",
                                  "SZB": "medium",
                                  "KSN": "medium",
                                  "SHHQ": "high"})
    # 50 lines are randomly generated and lineIDs do not have to start at 0 or are ordered
    lines = {}
    for idx in range(25):
        lines[idx] = [random.randint(0, 1) for _ in range(len(example_pr))]  # len(PhysicalRaiway) returns the num of stations

    # instance of class Lines
    example_lines = Lines(lines)
    # instance of class LinePlan
    example_lp = LinePlan(example_pr, example_lines)
    # line plan can be drawn right now by function draw() without parameters as follows
    # example_lp.draw()
    # however, the default appearance parameters may not be appropriate for your line plan
    # then, you can pass in some custom parameters
    example_lp.draw(figsize=(23, 25),
                    lines_color='blue')
    # make sure that the function show() is called after the function save(file_path), otherwise your saved image will be blank
    example_lp.save(f"C:\\Users\\SteppePrince\\Desktop\\Temp\\pic\\{time.strftime('%H.%M.%S',time.localtime(time.time()))}.png")
    example_lp.show()

if __name__ == "__main__":
    main()

                                   