from ninja_extra import NinjaExtraAPI
from ninja_jwt.controller import NinjaJWTDefaultController

api = NinjaExtraAPI()
api.register_controllers(NinjaJWTDefaultController)

api.add_router('', 'app.accounts.api.router')
api.add_router('', 'app.crm.api.router')
