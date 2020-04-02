# SSAFY_Daliy_Project

## 200317|Day07| Collection 사용

### Collection

-   데이터를 저장하는 기본적인 자료구조들을 한 곳에 모아 관리하고 편하게 사용하기 위해서 제공하는 것을 의미

- python에는 collections라는 모듈이 있음

- ```python
  from collections import deque
  from collections import OrderedDict
  from collections import defaultdict
  from collections import Counter
  from collections import namedtuple
  ```

### 산출물

- python 코드

  - ```python
    import datetime
    
    
    def getDays(year, month):
        if month == 2:
            return (29 if ((year % 4) == 0) and ((year % 100) != 0) or ((year % 400 ) == 0) else 28)
        return date_dict[month]
        
    
    dt = datetime.datetime.today()
    date_dict = {1: 31, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    print(getDays(dt.year, dt.month))
    ```

