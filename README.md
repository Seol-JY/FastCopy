# Fast Copy


![시연](https://i.imgur.com/jCP7HOL.gif)



## 소개
Easy Copy는 사용자가 지정한 항목들을 빠르고 정확하게 복사하는 프로그램입니다.  
Python언어로 제공되며, 최대 8개의 항목을 지정할 수 있습니다.


## 사용방법
  
-  소스코드를 사용 목적에 따라 수정합니다.
  
```python

class main:
    def __init__(self):
        self.select1 = ['CD001002', '웹 프로그래밍']
        self.select2 = ['복사할항목1', '설명1']
        self.select3 = ['복사할항목2', '설명2']
        self.select4 = ['복사할항목3', '설명3']
        self.select5 = ['복사할항목4', '설명4']
        self.select6 = ['복사할항목5', '설명5']
        self.select7 = ['복사할항목6', '설명6']
        self.select8 = ['복사할항목7', '설명7']

```
  
-  select리스트의 첫번째가 복사할 내용, 두번째가 설명입니다.
  
-  Copy!! 버튼을 누르면 내용이 복사되며, 해당항목이 강조됩니다.
  
-  파이썬 개발환경이 구축되지 않은 다른 컴퓨터에서 사용 시  
   pyinstaller모듈을 사용해 실행파일로 Export하여 사용하는것을 권장합니다.