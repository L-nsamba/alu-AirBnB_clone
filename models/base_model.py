#!/usr/bin/python3
"""Module defining the BaseModel class."""
import uuid
from datetime import datetime
import models


class BaseModel:
    """Base class for all AirBnB clone models."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel instance.

        Args:
            kwargs (dict): Key/value pairs of attributes (optional).
        """
        if kwargs:
            # Load instance from dictionary (deserialization)
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
            # Ensure id exists
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
        else:
            # New instance creation
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return string representation of the instance."""
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update updated_at timestamp and save to storage."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation of the instance for serialization."""
        dict_copy = self.__dict__.copy()
        dict_copy["__class__"] = type(self).__name__
        # Convert datetime objects to ISO format strings
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        return dict_copy
