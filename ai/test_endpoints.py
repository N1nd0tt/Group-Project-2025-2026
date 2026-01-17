import requests
import json

BASE_URL = "http://localhost:8000"


def test_world_generation():
    print("\n--- Testing World Generation ---")
    payload = {
        "theme": "Dark Fantasy",
        "tone": "Grim",
        "temperature": 0.8
    }
    try:
        response = requests.post(f"{BASE_URL}/gen/world", json=payload)
        response.raise_for_status()
        print("Success!")
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"Error: {e}")
        if 'response' in locals():
            print(response.text)


def test_character_generation():
    print("\n--- Testing Character Generation ---")
    payload = {
        "race": "Elf",
        "character_class": "Rogue",
        "level": 3,
        "temperature": 0.7
    }
    try:
        response = requests.post(f"{BASE_URL}/gen/character", json=payload)
        response.raise_for_status()
        print("Success!")
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"Error: {e}")
        if 'response' in locals():
            print(response.text)


def test_chat():
    print("\n--- Testing DM Chat ---")
    payload = {
        "input_text": "I define look around the tavern.",
        "history": [],
        "temperature": 0.5
    }
    try:
        response = requests.post(f"{BASE_URL}/dm/chat", json=payload)
        response.raise_for_status()
        print("Success!")
        print(json.dumps(response.json(), indent=2))
    except Exception as e:
        print(f"Error: {e}")
        if 'response' in locals():
            print(response.text)


if __name__ == "__main__":
    test_world_generation()
    test_character_generation()
    test_chat()
