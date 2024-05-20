## Getting Started

- pypi
  ```python
  >>> from korNum.chgFormat import kor2num
  >>> text1 = "맛있는 포카칩이 구천팔백칠십육억오천사백삼십이만천백십일원!"
  >>> print(kor2num(text1))
  맛있는 포카칩이 987654321111원!
  >>> text2 = "맛있는 포카칩이 구천팔백칠십육억오천사백삼십이만천백십일원에서 오백십만육십구원, 만사천칠백원을 거쳐 이제는 천오백원으로!"
  >>> print(kor2num(text2))
  맛있는 포카칩이 987654321111원에서 5100069원, 14700원을 거쳐 이제는 1500원으로!
  ```
- source code:
  `python run.py`
