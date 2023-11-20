from bunny import db
from typing import Dict, List, Union



permitdb = db.pmprotection

async def is_approved() -> list:
    pm = await permitdb.find_one({'permit': 'protection'})
    if not pm:
        return []
    return pm['users']


async def approve(user_ud: int):
    pm = await is_approved()
    pm.append(user_ud)
    await permitdb.update_one(
        {'permit': 'protection'},
        {
            '$set': {
                'users': pm
            }
        },
        upsert=True
    )


async def disapprove(user_ud: int):
    pm = await is_approved()
    pm.remove(user_ud)
    await permitdb.update_one(
        {'permit': 'protection'},
        {
            '$set': {
                'users': pm
            }
        },
        upsert=True
    )
