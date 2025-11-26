import uvicorn

# ANSI Colors
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"

def print_banner(host, port):
    base_url = f"http://{host}:{port}"

    print("\n" + CYAN + "=" * 65 + RESET)
    print(BOLD + MAGENTA + " 🚀 FASTAPI SERVER STATUS ".center(65) + RESET)
    print(CYAN + "=" * 65 + RESET)

    print(f"{GREEN}[INFO]{RESET} Starting FastAPI server...")
    print(f"{YELLOW}[INFO]{RESET} Base URL     : {CYAN}{base_url}{RESET}")
    print(f"{YELLOW}[INFO]{RESET} Host         : {CYAN}{host}{RESET}")
    print(f"{YELLOW}[INFO]{RESET} Port         : {CYAN}{port}{RESET}")
    print(f"{YELLOW}[INFO]{RESET} API Docs     : {CYAN}{base_url}/docs{RESET}")
    print(f"{YELLOW}[INFO]{RESET} ReDoc Docs   : {CYAN}{base_url}/redoc{RESET}")
    print(f"{YELLOW}[INFO]{RESET} Health Check : {CYAN}{base_url}/health-check{RESET}")

    print(CYAN + "=" * 65 + RESET + "\n")


if __name__ == "__main__":
    host = "localhost"
    port = 8000

    # Print nice banner
    print_banner(host, port)

    # Start Uvicorn server
    uvicorn.run(
        "app.main:app",
        host=host,
        port=port,
        reload=True
    )
