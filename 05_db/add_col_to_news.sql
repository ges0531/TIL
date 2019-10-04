ALTER TABLE news
ADD COLUMN created_at DATETIME 
NOT NULL DEFAULT 1;
-- 기존에 있는 애들한테는 1을 넣어준다.