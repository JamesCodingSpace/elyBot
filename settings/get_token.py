def get_token():
    file_path = "../../botToken/botToken.txt"
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"Die Datei wurde nicht gefunden.")
        return None
