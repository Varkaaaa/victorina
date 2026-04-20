CREATE_QUIZ = '''
CREATE table if NOT EXISTS quiz (
	id integer primary key, 
  	name text
)'''

CREATE_QUESTION = '''
CREATE table if NOT EXISTS question (
	id integer primary key, 
  	question text,
  	tema text,
  	right_txt text,
  	wrong text
)'''

CREATE_CONTENT = '''
CREATE table if NOT EXISTS quiz_content (
	id integer primary key, 
	quiz_id int,
	question_id int,
  	FOREIGN KEY (quiz_id) REFERENCES quiz(id),
  	FOREIGN KEY (question_id) REFERENCES question(id)
)'''

ADD_QUIZES = """INSERT INTO quiz (name) VALUES (?)"""
ADD_QUESTIONS = """INSERT INTO question (question, tema, right_txt, wrong) VALUES (?, ?, ?, ?)"""
ADD_CONTENT = """INSERT INTO quiz_content (quiz_id, question_id) VALUES (?, ?)"""
GET_FIRST = '''SELECT question_id
    FROM quiz_content
    WHERE quiz_id = ?
    ORDER BY question_id
    LIMIT 1'''

NEXT_QUESTION_ID = """
SELECT quiz_content.id, question.question, question.right_txt, question.wrong
    FROM question, quiz_content
    WHERE quiz_content.question_id = question.id
    AND quiz_content.id > ? AND quiz_content.quiz_id = ?
    ORDER BY quiz_content.id """

CHECK_RIGHT = '''
SELECT quiz_content.id, question.question, question.right_txt
    FROM question, quiz_content
    WHERE quiz_content.id = ? AND (question.right_txt LIKE ?)'''

QUIZES = [
    ('Какой ты смешарик?'), 
    ('Какой ты якубович?'), 
]

QUESTION =[
        ('Какой ты смешарик?','смысл жизни', 'упоротый', 'нормальный~шо есть смешарик~тупик'),
        ('любимое занятие?','хобби', 'гулятт', 'читать книги~смотреть шортсы~ходить в кино'),
        ('твоя любимая еда?','ам ам ам', 'макзавтрак', 'суп~кфс~суши'),
        ('твой любимый урок?','ыыы учиться ыыыы', 'сидеть на скамейке на физре', 'русский~литература~биология'),
        ('твоя любимая погода?','погода', 'негрятята падают на землю', 'негрятята с лазерами из глаз~солнечный негрятёнок~плаки плаки негрятенок'),
        ('спишь ли ты с плюшевым смешариком?','сон', 'конешна, я же маладец', 'нет я тупик~естественно~что за вопросы?'),
        
]

CONTENT = [
    (1,1),
    (1,2),
    (1,3),
    (1,4),
    (1,5),
    (1,6),
    (2,1),
    (2,2),
    (2,3),
    (2,4),
    (2,5),
    (2,6),
]

SELECT = 'SELECT * FROM '
DROP = 'DROP TABLE IF EXISTS '
INSERT = 'INSERT INTO '
PRAGMA = "PRAGMA foreign_keys=on"
