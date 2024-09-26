# import pytest

# from movies.models import Genre

# pyteststmark = [pytest.mark.django_db]

# @pytest.mark.django_db
# def test_retrive_film_work():
#     genre_count = Genre.objects.count()
#     assert genre_count == 0
#     print(genre_count == 0)

"""
Pytest не неализован в связи с неизвестной мне ранее ошибкой БД.
psycopg.errors.InvalidSchemaName: schema "content" does not exist
ERROR api/v1/movies/tests/test_movies.py::test_retrive_film_work - django.db.utils.ProgrammingError: schema "content" does not exist

Решение пока не нашел. Если подскажите, буду крайне рад)
"""