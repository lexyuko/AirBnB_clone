#!/usr/bin/python3

"""a class called base_model that defines ll common methods and attributes for other classes """

import models
from uuid import uuid4
from datetime import datetime
class BaseModel:

    """This is class called basemodel for HBnB project"""
    def __int__(self, *args, **kwargs):
        """initialize a new basemodel

        Args:
            *args (any): Unused.
            **Kwargs (dict): key/value pairs of attributes
        """
        dformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, dformat)
                else:
                    self.__dict__[k] = v

        else:
            models.storage.new(self)

    def save(self):
        """Update Update_at with current datetime"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the basemodel instance.
        includes the key/value pair __class__ representing
        the class name of the object.
        """
        gdict = self.__dict__.copy()
        gdict["created_at"] = self.created_at.isoformat()
        gdict["updated_at"] = self.updated_at.isoformat()
        gdict["__class__"] = self.__class__.__name__
        return gdict

    def __str__(self):
        """return the print of the basemodel instance"""
        clname = self.__class__.__name__
        return "[{}] ({}) {} ".format(clname, self.id, self.__dict__)