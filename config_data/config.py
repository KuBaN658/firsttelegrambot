from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    database: str
    db_host: str
    db_user: str
    db_password: str


@dataclass
class TgBot:
    token: str
    admin_ids: list[int]


@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig


env: Env = Env()
# Добавляем в переменные окружения данные, прочитанные из файла .env
env.read_env()
# Создаем экземпляр класса Config и наполняем его данными из переменных окружения
config = Config(tg_bot=TgBot(token=env('BOT_TOKEN'),
                             admin_ids=list(map(int, env.list('ADMIN_IDS')))),
                db=DatabaseConfig(database=env('DATABASE'),
                                  db_host=env('DB_HOST'),
                                  db_user=env('DB_USER'),
                                  db_password=env('DB_PASSWORD')))

