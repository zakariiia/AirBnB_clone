from datetime import datetime
import uuid
import models


class BaseModel:

    def __init__(self, *arg, **kwarg):
        """


        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

        if kwarg:
            for key, value in kwarg.items():
                if key == '__class__':
                    continue
                if key == 'updated_at' or key == 'created_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else :
                    setattr(self, key, value)
        models.storage.new(self)

    def save(self):
        
        """
        
        
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):

        """
        
        """
        instan_dict = self.__dict__.copy()
        instan_dict["__class__"] = self.__class__.__name__
        instan_dict["created_at"] = self.created_at.isoformat()
        instan_dict["updated_at"] = self.updated_at.isoformat()

        return instan_dict

    def __str__(self):
            
        """

        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
    