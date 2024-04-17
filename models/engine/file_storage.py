import json
from models.base_model import BaseModel

class FileStorage:
    """Represent an abstracted storage engine."""
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary of instantiated objects in __objects."""
        if cls is not None:
            cls_dict = {}
            for k, v in self.__objects.items():
                if isinstance(v, cls):
                    cls_dict[k] = v
            return cls_dict
        return self.__objects

    def new(self, obj):
        """Set obj in __objects with key <obj_class_name>.id."""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                for o in json.load(f).values():
                    name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(name)(**o))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete a given object from __objects, if it exists."""
        if obj is not None:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects.pop(key, None)

    def close(self):
        """Call the reload method."""
        self.reload()
