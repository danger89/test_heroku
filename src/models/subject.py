from __future__ import annotations

from typing import final

from peewee import TextField, IntegerField

from src.models.bases import Indexed, BaseModelEnum

__all__ = ['Subject']


@final
class Subject(Indexed, BaseModelEnum):
    """
    CREATE TABLE subject (
        name Smallint
            PRIMARY KEY,
        name Text NOT NULL
            UNIQUE
            CHECK (name != ''),
        number_of_tasks Int NOT NULL
            CHECK (number_of_tasks != 0)
    );
    """
    MATHEMATICS: Subject
    RUSSIAN_LANGUAGE: Subject

    @classmethod
    def _init_static(cls):
        pass
        # cls.RUSSIAN_LANGUAGE = cls.get(name=1)
        # cls.MATHEMATICS = cls.get(name=2)

    name: str = TextField()
    number_of_tasks: int = IntegerField()

    @classmethod
    def get_by_id(cls, id) -> Subject:
        return super().get_by_id(id)

    @classmethod
    def get_by_name(cls, name: str) -> Subject:
        return super().get(name=name)

    def delete_instance(self, recursive=False, delete_nullable=False):
        raise NotImplementedError
