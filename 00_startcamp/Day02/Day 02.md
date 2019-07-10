# 190709 startcamp - day2

## What is git?

### 정의

- scm(source code manager) / vcs(version control system)

- ''~''는 집을 의미 (Ex, student)

- 버전관리를 해주는 감시카메라

  EX)

  최종발표.pptx

  최종발표_final.pptx

  최종최종발표.pptx

  

  ...

  

  최종발표v1-1차완료본.pptx

  최종발표v2-챕터2삭제.pptx

  최종발표v3-챕터2수정.pptx



### git 명령어

- `git` 

  - `git init` : 관리 시작(master)

  - `git status` : 상태를 물어보는 명령어

  - `git log` : 사진(commit)들 로그를 보여줌

  - `git add <filename> `: 파일 등록(변화하는 모든것을 추적)(여기보세요)

  - `git commit -m '<message>'`  : 버전을 만든다(찰칵)

    - 빨간색일때는 commit이 안됨

      add -> commit

  - `git push` : 보내기(백업)

  - `git add -A(= git add .)` : 파일 한번에 add하겠다.

- `cd`(change directory) 

  - cd .. : 위로가기
  - cd 폴더명 : 더블클릭
  - cd tap 두번 : 보기 제시 -> tap 자동완성

- `mkdir`(make directory) : 폴더 만들기
- `touch` : 파일 생성
  - `touch .gitignore` : .gitignore안에 있는 내용 무시
    - .명령어 : 명령어를 숨김(단,gitignore는 제외)
- `-V` : 버전확인 (EX, python -V)
- `ls` : list의 줄임말, 폴더안에 뭐가 있나요
- `remote add origin` : 방향 가르키기

### Webbrowser에서 내용 가져오기

- `요청, 주소, 응답, 문서(HTML, XML, Json 등)`
- 문서 -> F12 -> 수정 가능

### 인터넷 창 열기

```python
import webbrowser # webbrowser 함수 덩어리를 서랍에서 가져온다.

urls = ['www.github.com',
'www.google.com',
'www.yotube.com'
'www.slack.com'
'www.naver.com'] # urls의 리스트를 만든다.

for url in urls:
    webbrowser.open(url) # webbrowser를 연다.
```



### 코스피 찾기

```python
import requests # 가져오기 함수 덩어리를 서랍에서 꺼낸다. 
import bs4 # 파이썬이 쉽게 읽을 수 있도록 도와준다.

url = 'https://finance.naver.com/sise/' # 코스피 페이지를 url에 저장한다.
response = requests.get(url).text # 코스피 페이지를 text형태로 가져와서 response에 저장한다.
text = bs4.BeautifulSoup(response, 'html.parser') # response를 파이썬이 읽기 쉽게 만들어 주고 text에 저장한다.
kospi = text.select_one('#KOSPI_now') # 페이지의 전체 문서 중 #KOSPI_now 하나의 내용만 가져온다.

print(kospi.text) # kospi.text를 출력한다.
```

* 설치하기(사오기) : pip install 함수명



### 멜론 인기차트(1~50)

```python
import requests # 가져오기 함수 덩어리를 서랍에서 꺼낸다.
import bs4 # 파이썬이 쉽게 읽을 수 있도록 도와준다.
import csv # 읽기/쓰기 함수 덩어리를 서랍에서 꺼낸다.

url = 'https://www.melon.com/chart/index.htm' # 멜론 페이지를 url에 저장한다.

headers = {'User-Agent':':)'}
response = requests.get(url, headers=headers).text #어떤 애들은 필요한 몇몇 정보가 더 있다.
text = bs4.BeautifulSoup(response, 'html.parser') # response를 파이썬이 읽기 쉽게 만들어 주고 text에 저장한다.
rows = text.select('.1st50')  # 페이지의 전체 문서 중 #KOSPI_now 여러개의 내용을 가져온다.

writer = csv.writer(open('melon50.csv', 'w', encoding='utf-8'))
writer.writerow(['순위','제목','가수'])

for row in rows:
    rank = row.select_one('td:nth-child(2) > div > span.rank').text
    title = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = row.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    writer.writerow([rank, title, artist])  

```





