# Today Keyword

## 200115

### HTTP접근 제어 CORS(Cross-Origin Resource Sharing)

- 도메인(서브 도메인 포함)
- 포트
- 프로토콜



크롤링

크롬 드라이버

셀레니움



## 200116

### Redux

- 3가지 원칙
  - 진실은 하나의 소스로부터
    - 모든 상태는 하나의 스토어 안에 하나의 객체 트리 구조로 저장됩니다.
  - 상태는 읽기 전용이다
    - 상태를 변화시키는 유일한 방법은 무슨 일이 벌어지는 지를 묘사하는 액션 객체를 전달하는 방법뿐입니다.
  - 변화는 순수 함수로 작성되어야한다
    - 액션에 의해 상태 트리가 어떻게 변화하는 지를 지정하기 위해 프로그래머는 순수 리듀서를 작성해야합니다.
    - 동일한 input을 넣었을 때 동일한 output이 나와야 한다 => 순수 함수





## 200117

### Indexed DB

- 50MB 정도의 용량이 허용되어 있음
- 대용량 데이터 사용 시에 성능 이슈가 있음



### Storage



### Cookie

- 저장 가능한 공간의 크기가 매우 작고 텍스트 형태로 저장
- 만료시간 설정이 가능하다
- 요청에 실어서 서버로 전송하는 일이 잦음
- 인정 정보 등을 보관할 때 사용함
- 4kb의 크기를 갖는다



http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&wr_id=1896&sca=99&sfl=wr_hit&stx=2634 - 사냥꾼





## 200120

리부트가 필요한 경우: sudo shutdown  -r now



## 200122

jomation.com - front end 포트폴리오



## 200123

- 동기
  - 
- 비동기
  - Javascript
    - callback
    - promise
    - Async/await



## 200128

https://lab.ssafy.com/SanghyunLee/algotips



## 200129

- 보급로 재귀

  - 종료조건 => 목적지에 도달하는것

  - 재귀로 해야하는것 => 4방향 탐색

  - 가지치기

  - 메모이제이션

    - 특정지점에 도달했을 때 최소값을 저장해둔다

    - 새로운 배열을 만든다

    - ```python
      if sum < memoization[y][x] {
          memoization[y][x] = sum;
      }
      else {
          return;
      }
      ```

    - 

  - 휴리스틱(인간의 직관)

    - 출발지가 항상 왼쪽 위
    - 도착지가 항상 아래쪽 밑
    - 아래 => 오른쪽 => 위 => 왼쪽
