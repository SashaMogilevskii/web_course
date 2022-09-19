from fastapi import APIRouter

from app import contracts

router = APIRouter()


@router.get("/")
def read_root():
    return {'message':'This is first page!!!!!'}


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": f'Number is {item_id}'}


@router.get("/users/")
async def read_user(user_id: str, q: str | None =None):
    if q:
        return {
            'item_id': user_id,
            'q': q
        }
    return {"item_id": f'User is {user_id}'}

@router.post("/items/")
async def create_item(item: contracts.Item):  
    item_dict = item.dict()

    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
