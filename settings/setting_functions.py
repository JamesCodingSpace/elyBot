def get_channel_id(pattern):
    file_path = "settings/settings.txt"
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if pattern in line:
                    value = line.split(pattern)[-1].strip()
                    return value
        print(f"Das Muster '{pattern}' wurde in der Datei nicht gefunden.")
        return None
    except FileNotFoundError:
        print(f"Die Datei '{file_path}' wurde nicht gefunden.")
        return None
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return None
    
def get_duration(pattern):
    file_path = "settings/settings.txt"
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if pattern in line:
                    value = line.split(pattern)[-1].strip()
                    return value
        print(f"Das Muster '{pattern}' wurde in der Datei nicht gefunden.")
        return None
    except FileNotFoundError:
        print(f"Die Datei '{file_path}' wurde nicht gefunden.")
        return None
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return None    
    
def get_app_id(pattern):
    file_path = "settings/settings.txt"
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if pattern in line:
                    value = line.split(pattern)[-1].strip()
                    return value
        print(f"Das Muster '{pattern}' wurde in der Datei nicht gefunden.")
        return None
    except FileNotFoundError:
        print(f"Die Datei '{file_path}' wurde nicht gefunden.")
        return None
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return None

def get_spam_user_id(pattern):
    file_path = "settings/settings.txt"
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if pattern in line:
                    value = line.split(pattern)[-1].strip()
                    return value
        print(f"Das Muster '{pattern}' wurde in der Datei nicht gefunden.")
        return None
    except FileNotFoundError:
        print(f"Die Datei '{file_path}' wurde nicht gefunden.")
        return None
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return None    