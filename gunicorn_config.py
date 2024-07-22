import asyncio

def on_starting(server):
    print("Running initialization script...")
    asyncio.run(run_initialization())

async def run_initialization():
    # This is where you call your initialization script's main function
    from initialize import main
    await main()

bind = '0.0.0.0:8000'
workers = 4  # Adjust the number of workers as needed
