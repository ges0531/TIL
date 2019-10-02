-- SQLite
-- SELECT DISTINCT age FROM users;

-- SELECT * FROM users WHERE age=30;
-- SELECT * FROM users WHERE age >= 30;

-- SELECT first_name FROM users WHERE age >= 30;

-- users 에서 age 30이상, 성이 '김' 인 사람의 성과 나이만 가져온다면?
-- SELECT age, last_name FROM users
-- WHERE age >= 30 AND last_name='김'
-- LIMIT 10; -- 10개만

-- COUNT
-- SELECT COUNT(*) FROM users;

-- AVG, SUM, MIN, MAX (숫자 컬럼만 가능)
-- 30살 이상인 사람들의 평균나이
-- SELECT AVG(age) FROM users
-- WHERE age >= 30;

-- users 에서 잔액이 가장 높은 사람의 first_name과 잔액
-- SELECT first_name, MAX(balance) FROM users;

-- users 에서 30살 이상인 사람의 계좌 평균 잔액은?
-- SELECT first_name, AVG(balance) FROM users WHERE age >= 30;

-- wild cards
-- SELECT * FROM users WHERE age LIKE '3_';

-- users에서 지역번호가 02 인 사람은?
-- SELECT * FROM users WHERE phone LIKE '02-%';

-- users에서 이름이 '준'으로 끝나는 사람만?
-- SELECT * FROM users WHERE first_name LIKE '%준';

-- users 에서 중간 번호가 5114인 사람만?
-- SELECT * FROM users WHERE phone LIKE '%5114%';

-- ORDER
-- SELECT * FROM users ORDER BY age DESC LIMIT 10;

-- SELECT age, balance FROM users
-- ORDER BY age, balance LIMIT 10;

-- users 에서 계좌잔액순으로 내림차순 정렬하여 해당하는 사람의 성과 이름을 10개만 뽑아보면?
SELECT first_name, last_name, balance FROM users
ORDER BY balance DESC LIMIT 10;