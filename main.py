print('Приложение для учёта прогресса в играх')
print('Функции: \n add_item(game) \n show_all \n delete_item')
import json
import sqlite3
connection = sqlite3.connect('my_games.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Games (
id INTEGER PRIMARY KEY,
name TEXT NOT NULL,
progress REAL,
playtime REAL
)
''')
e = input('Выберите действие: ')
JSON_NAME = 'games_backup.json'
def save_to_json():
    conn = sqlite3.connect('my_games.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, progress, playtime FROM Games')
    games = cursor.fetchall()
    conn.close()

    games_list = [
        {
            "id": game[0],
            "name": game[1],
            "progress": game[2],
            "playtime": game[3]
        }
        for game in games
    ]

    try:
        with open(JSON_NAME, 'w', encoding='utf-8') as f:
            json.dump(games_list, f, indent=4, ensure_ascii=False)
        print(f"Данные сохранены в {JSON_NAME}")
    except Exception as e:
        print(f"Ошибка сохранения в JSON: {e}")
def add_item(i):
    game=input('Name of the game: ')
    progress=float(input('Progress: '))
    playtime=float(input('Session(in h.): '))

    connection = sqlite3.connect('my_games.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Games(name, progress, playtime) VALUES (?,?,?)', (game,progress,playtime))
    connection.commit()
    connection.close()
    save_to_json()
    return print(f'name {game}, progress {progress}% session {playtime}h успешно добавлены в БД')
def show_all(i):
    connection = sqlite3.connect('my_games.db')
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM Games')
    games = cursor.fetchall()
    # for game in games:
    print(games)
def delete_item(i):
    a = input('Введите название игры для удаления: ')
    connection = sqlite3.connect('my_games.db')
    cursor = connection.cursor()
    cursor.execute(f'DELETE FROM Games WHERE name=?', (a,))
    connection.commit()
    connection.close()
    save_to_json()
    return print('Игра успешно удалена из БД')

if e == 'add_item':
    print(add_item(1))
if e == 'show_all':
    print('id|Игра|Прогресс|Игровое Время')
    print(show_all(1))
if e == 'delete_item':
    print(delete_item(1))