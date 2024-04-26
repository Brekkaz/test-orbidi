from strawberry.fastapi import BaseContext
from domain.usecases.category_usecase import Category
from domain.usecases.location_usecase import Location

class AppState(BaseContext):

    def __init__(self, category: Category, location: Location):
        super().__init__()
        self.category = category
        self.location = location

        
