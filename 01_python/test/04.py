# 파일명을 변경하지 마시오.
# 아래에 Word 클래스를 작성하시오.


class Word:

    def __init__(self):
        wordbook = {}
        self.wordbook = wordbook
        self.my_dict = {}

    def add(self, key, value):
        self.key = key
        self.value = value
        self.wordbook[self.key] = self.value
        return self.wordbook

    def delete(self, key):
        if self.key in self.wordbook:  # 안에 있으면 뺀다
            self.wordbook.pop(self.key)
            return True
        else:
            return False

    def print(self):
        return print(self.wordbook)









# 실행 결과를 확인하기 위한 코드입니다. 수정하지 마시오.
if __name__ == '__main__':
    my_book = Word()
    my_book.add('grape', '포도')
    my_book.add('peach', '복숭아')
    my_book.add('watermelon', '수박')
    my_book.add('mango', '망고')
    my_book.print()
    print(my_book.delete('watermelon'))
    print(my_book.delete('mango'))
    print(my_book.delete('carrot'))
    my_book.print()
