from dataclasses import dataclass
from environs import Env

@dataclass
class DatabaseConfig:
    database: str           #Название БД
    db_host: str            #URL-адрес БД
    db_user: str            #Username пользователя БД
    db_password: str        #Пароль к БД

@dataclass
class TgBot:
    token: str              #токен для доступа к боту
    admin_ids: list[int]    #список админов бота

@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig

def load_config(path: str | None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                               admin_ids=list(map(int, env.list('ADMIN_IDS')))),
                  db=DatabaseConfig(database=env('DATABASE'),
                                    db_host=env('DB_HOST'),
                                    db_user=env('DB_USER'),
                                    db_password=env('DB_PASSWORD')))