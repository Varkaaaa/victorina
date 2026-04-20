from zapros import * 
import sqlite3
from contextlib import contextmanager


class DB():
    def __init__(self, name = 'baza.db'):
        self.name = name
    
    @contextmanager
    def _get_connection(self):
        """Контекстный менеджер для управления соединением."""
        conn = sqlite3.connect(self.name)
        # тип а-ля словарь
        #conn.row_factory = sqlite3.Row
        # попытайся дождаться ответа функции в конце закрой соединения
        try:
            yield conn
        finally:
            conn.close()

    def execute(self, query=CREATE_QUIZ):
        query = query.replace('--','')
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
            conn.commit()
            return data   
        
    def execute_data(self, query=CREATE_QUIZ, data = None):
        query = query.replace('--','')
        if type(data) == str:
            data = [data]
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, data)
            data = cursor.fetchall()
            conn.commit()
            return data

def set_base():
    db = DB()
    db.execute(DROP+'question')
    db.execute(DROP+'question')
    db.execute(DROP+'quiz_content')
    db.execute(PRAGMA)    
    db.execute()
    db.execute(CREATE_QUESTION)
    db.execute(CREATE_CONTENT)
    for quiz in QUIZES:
        db.execute_data(ADD_QUIZES, quiz)   
        
    for quiz in QUESTIONS:
        db.execute_data(ADD_QUESTIONS, quiz)    
        
    for quiz in CONTENT:
        db.execute_data(ADD_CONTENT, quiz)
    return db

        
if __name__ == "__main__":
    db = set_base()

