from config.mongodb import init_db
import asyncio

async def main():
    print("Starting database initialization...")
    await init_db()
    print("Database initialized")

if __name__ == '__main__':
    asyncio.run(main())