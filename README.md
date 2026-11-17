# Запускаем постгресс в контейнере из рабочей папки
```
docker run -d \
  --name social-postgres \
  -e POSTGRES_USER=postgres \
  -e POSTGRES_PASSWORD=postgres \
  -e POSTGRES_DB=social_network \
  -p 5432:5432 \
  -v $(pwd)/migrations:/migrations \
  postgres:16
```

# Запускаем миграцию (либо руками через psql)
```
sudo docker exec social-postgres psql -U postgres -d social_network -f migrations/0001_init.sql
```

# Запуск проекта (Linux\Ubuntu)
## Создаём окружение
```
python3.12 -m venv .venv
```

## Активируем окружение
```
source .venv/bin/activate
```

## Устанавливаем зависимости

```
pip install -e .
```

## Запускаем приложение
```
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```