import uvicorn


if __name__ == "__main__":
    uvicorn.run("superbot.app:App", port=5000, log_level="info")
