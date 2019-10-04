CREATE TABLE articles (
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
-- 이어서 작성하면 바로 에러 (; 빠졌을 때)

INSERT INTO articles VALUES ('1번 제목', '1번 내용');
