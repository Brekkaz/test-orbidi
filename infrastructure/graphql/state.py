from strawberry.fastapi import BaseContext
from domain.usecases.category_usecase import Category
from domain.usecases.location_usecase import Location
from strawberry.dataloader import DataLoader


class AppState(BaseContext):

    def __init__(
        self,
        category: Category,
        location: Location,
        categories_loader: DataLoader,
        location_loader: DataLoader,
    ):
        super().__init__()
        self.category = category
        self.location = location
        self.categories_loader = categories_loader
        self.location_loader = location_loader
