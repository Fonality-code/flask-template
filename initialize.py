from config.mongodb import init_db
from dotenv import load_dotenv
import asyncio

async def main():
    print("Loading environment variables...")
    load_dotenv()
    print("Starting database initialization...")
    await init_db()
    print("Database initialized")

if __name__ == '__main__':
    asyncio.run(main())

