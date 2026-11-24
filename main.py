from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

class Character(BaseModel):
    id: int
    name: str
    ability: str
    description: str

class CharacterUpdate(BaseModel):
    name: str | None = None
    ability: str | None = None
    description: str | None = None

app = FastAPI()

characters = [
    {
        "id": 1,
        "name": "Thief",
        "ability": "Steal",
        "description": "Steals a random card from another player in the same clearing."
    },
    {
        "id": 2,
        "name": "Tinker",
        "ability": "Day Labor",
        "description": "Recovers a matching or bird card from the discard pile."
    },
    {
        "id": 3,
        "name": "Ranger",
        "ability": "Hideout",
        "description": "Repairs three items and ends Daylight immediately."
    },
    {
        "id": 4,
        "name": "Vagrant",
        "ability": "Instigate",
        "description": "Provokes battles between players and benefits from removed pieces."
    },
    {
        "id": 5,
        "name": "Arbiter",
        "ability": "Protector",
        "description": "Supports defenders in battle in exchange for a victory point."
    },
    {
        "id": 6,
        "name": "Scoundrel",
        "ability": "Scorched Earth",
        "description": "Destroys enemy pieces in a clearing and permanently blocks access."
    },
    {
        "id": 7,
        "name": "Adventurer",
        "ability": "Improvise",
        "description": "Substitutes and damages an item to complete a quest."
    },
    {
        "id": 8,
        "name": "Harrier",
        "ability": "Glide",
        "description": "Travels directly to any clearing by exhausting a torch."
    },
    {
        "id": 9,
        "name": "Ronin",
        "ability": "Swift Strike",
        "description": "Exhausts a sword to inflict an additional battle hit."
    },
    {
        "id": 10,
        "name": "Cheat",
        "ability": "Con",
        "description": "Completes a quest using any two items and recycles the quest."
    },
    {
        "id": 11,
        "name": "Gladiator",
        "ability": "Duel",
        "description": "Sacrifices item durability to eliminate a warrior and draw a card without becoming hostile."
    },
    {
        "id": 12,
        "name": "Jailor",
        "ability": "Coerce",
        "description": "Substitutes a matching card for item exhaustion at a victory point cost."
    }
]

@app.get("/characters")
def get_characters(name: str | None = None):
    if name is None:
        return characters

    return [
        character
        for character in characters
        if name.lower() in character["name"].lower()
    ]

@app.get("/characters/{character_id}")
def get_character(character_id: int):
    for character in characters:
        if character["id"] == character_id:
            return character

    raise HTTPException(
    status_code=404,
    detail="Character not found"
)

@app.post("/characters", status_code=201)
def add_character(character: Character):
    for existing in characters:
        if existing["id"] == character.id:
            raise HTTPException(
                status_code=409,
                detail="ID already exists"
            )

    characters.append(character.model_dump())
    return character

@app.delete("/characters/{character_id}")
def delete_character(character_id: int):
    for character in characters:
        if character["id"] == character_id:
            characters.remove(character)
            return {"message": "Character deleted"}

    raise HTTPException(
    status_code=404,
    detail="Character not found"
)

@app.put("/characters/{character_id}")
def replace_character(character_id: int, updated: Character):
    for index, character in enumerate(characters):
        if character["id"] == character_id:
            characters[index] = updated.model_dump()
            characters[index]["id"] = character_id
            return characters[index]

    raise HTTPException(
    status_code=404,
    detail="Character not found"
)

@app.patch("/characters/{character_id}")
def update_character(character_id: int, updated: CharacterUpdate):
    for character in characters:
        if character["id"] == character_id:
            changes = updated.model_dump(exclude_none=True)
            character.update(changes)
            return character

    raise HTTPException(
    status_code=404,
    detail="Character not found"
)