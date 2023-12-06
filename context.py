import json


class Context:

    def __init__(self, path) -> None:
        self._path = path

    def read_data(self) -> list:
        # Ktra path .json
        if '.json' not in self._path:
            raise Exception(f"The path '{self._path}' must be json file.")
        try:
            # Đọc file json
            with open(self._path, 'r', encoding="utf-8") as data:
                data = json.loads(data.read())

                return data

        # File not found exceptions
        except FileNotFoundError:
            raise FileNotFoundError(f"The file '{self._path}' does not exist.")
        # Other exceptions
        except Exception as e:
            raise Exception(e)
