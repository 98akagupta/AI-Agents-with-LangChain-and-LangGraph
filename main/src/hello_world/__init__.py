from dotenv import load_dotenv
import os

load_dotenv()


def main() -> None:
    print("Hello from hello-world!")
    print(f"Environment variable OPENAI_API_KEY: {os.getenv('OPENAI_API_KEY')}")


if __name__ == "__main__":
    main()
