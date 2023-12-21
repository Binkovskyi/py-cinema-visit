from __future__ import annotations

from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


class CinemaHall:

    def __init__(self, number: int) -> None:
        self.number = number

    # ----------------------------------beginning and end of the movie
    def movie_session(
            self, movie_name: str,
            customers: list | list[Customer],
            cleaning_staff: Cleaner
    ) -> None:

        print(f'\"{movie_name}\" started in hall number {self.number}.')
        for el in customers:
            if isinstance(el, Customer):
                el.watch_movie(movie_name)
            else:
                customer = Customer(el["name"], el["food"])
                customer.watch_movie(movie_name)
        print(f'\"{movie_name}\" ended.')
        cleaning_staff.clean_hall(self.number)