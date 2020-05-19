"""
Korean number list
- cardinal number: 기수. 순서를 정의(일 이 삼...)
- ordinal number: 서수. 셈이 가능(하나 둘 셋...)
"""


class chgList:
    def __init__(self):
        # unit
        self.cardUnit = {
            "kg": ["키로", "키로그램", "킬로", "킬로그램", "킬로그람"],
            'g': ["그램", "그람"],
            'L': ["리터"],
            "mL": ["밀리리터", "미리리터", "미리", "밀리"],
            "cm": ["센치미터", "센티미터"],
            "mm": ["밀리미터"],
            "m": ["미터"],
            "원": ["원"],
            "달러": ["달러"],
        }
        self.ordUnit = {
            "개입": ["개입"],
            "개": ["개"],
            "명": ["명"],
            "묶음": ["묶음"],
            "단": ["단"],
            "모": ["모"],
            "세트": ["세트"],
            "병": ["병"],
            "장": ["장"],
            "박스": ["박스"],
            "봉지": ["봉지"],
            "팩": ["팩"],
            "줄": ["줄"],
            "망": ["망"],
            "포": ["포"],
            "말": ["말"],
            "캔": ["캔"],
            "판": ["판"],
            "자루": ["자루"],
            "가마니": ["가마니"],
            "통": ["통"],
        }

        # numList
        self.cardNum = [
            ("일", 1),
            ("이", 2),
            ("삼", 3),
            ("사", 4),
            ("오", 5),
            ("육", 6),
            ("칠", 7),
            ("팔", 8),
            ("구", 9),
            ("십", 10),                      # idx: 9
            ("백", 100),                     # idx: 10
            ("천", 1000),                    # idx: 11
            ("만", 10000),                   # idx: 12
            ("억", 100000000),               # idx: 13
            ("조", 1000000000000),           # idx: 14
            ("경", 10000000000000000),       # idx: 15
            ("해", 100000000000000000000),   # idx: 16
        ]
        self.ordNum = [                     # keep this part
            ("한", 1),
            ("두", 2),
            ("둘", 2),
            ("세", 3),
            ("셋", 3),
            ("네", 4),
            ("넷", 4),
            ("다섯", 5),
            ("여섯", 6),
            ("일곱", 7),
            ("여덟", 8),
            ("여덜", 8),
            ("아홉", 9),
        ]