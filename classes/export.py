class Export:
    def __init__(self, vehicle_id: int, link: str, title: str, photos: str, price: int, info: str, location: str, site_name: str, year: int, is_automat: bool):
        self.vehicle_id = vehicle_id
        self.link = link
        self.title = title
        self.photos = photos
        self.price = price
        self.info = info
        self.location = location
        self.site_name = site_name
        self.year = year
        self.is_automat = is_automat
