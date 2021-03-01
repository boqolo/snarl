from Types import *
from Util import log, intifyTuple

"""
What a json room looks like: 
{ "type"   : "room",
  "origin" : (point),
  "bounds" : (boundary-data),
  "layout" : (tile-layout)
}
"""


def convertJsonRoom(origin: list, boundaryData: list,
                    tileLayout: list):
    boardEnum = BoardEnum.ROOM
    log(str(boundaryData))
    dimensions = intifyTuple(tuple(boundaryData))
    upperLeftCorner = intifyTuple(tuple(origin))
    tiles = []
    doorLocations = []
    for i in range(len(tileLayout)):
        for j in range(len(tileLayout[i])):
            if tileLayout[i][j] == 0:
                temp = Tile(TileEnum.WALL, (i, j), False)
                tiles.append(temp)
            elif tileLayout[i][j] == 2:
                temp = Tile(TileEnum.DOOR, (i, j), False)
                tiles.append(temp)
                doorLocations.append((i, j))
            else:
                temp = Tile(TileEnum.DEFAULT, (i, j), False)
                tiles.append(temp)

    return Board(tiles, upperLeftCorner, dimensions, boardEnum,
                 doorLocations)


"""
What a json hallway looks like:
{ 
  "from": (point),
  "to": (point),
  "waypoints": (point-list)
}
"""


def convertJsonHallway(fromPoint: list, toPoint: list, waypoints: list):
    allWaypoints = waypoints + [toPoint]
    fromTemp = fromPoint
    tiles = []

    while len(allWaypoints) > 0:
        toTemp = allWaypoints[0]
        fromX, fromY = intifyTuple(tuple(fromTemp))
        toX, toY = intifyTuple(tuple(toTemp))
        if fromX == toX:
            toBigger = toY > fromY
            for i in range(0, abs(toY - fromY)):
                newTilePos = (fromX, fromY + i) if toBigger else (
                    fromX, fromY - i)
                newTile = Tile(TileEnum.DEFAULT, newTilePos)
                tiles.append(newTile)
        elif fromY == toY:
            toBigger = toX > fromX
            for i in range(0, abs(toX - fromX)):
                newTilePos = (fromX + i, fromY) if toBigger else (
                    fromX - i, fromY)
                newTile = Tile(TileEnum.DEFAULT, newTilePos)
                tiles.append(newTile)
        else:
            print(" YOU GAVE US A BAD LIST OF WAYPOINTS SIR")
        fromTemp = toTemp
        fromX, fromY = fromTemp
        del allWaypoints[0]

    tiles.append(Tile(TileEnum.DEFAULT, tuple(toPoint)))
    # NOTE: origin = -1,-1 for a hallway
    board = Board(tiles, intifyTuple(tuple(fromPoint)), (-1, -1),
                  BoardEnum.HALLWAY,
                  [intifyTuple(tuple(fromPoint)), intifyTuple(tuple(toPoint))])
    # for tile in board.tiles:
    #     log(str(tile.location))
    return board


"""
What a json level looks like:
{ 
  "rooms": (room-list),
  "hallways": (hall-list),
  "objects": [ { "type": "key", "position": (point) }, 
               { "type": "exit", "position": (point) } ]
}
"""


def convertJsonLevel(rooms: list, hallways: list, objects: list):
    boundsList = lambda boundaryData: [boundaryData["rows"],
                                       boundaryData["columns"]]
    roomBoards = [
        convertJsonRoom(room["origin"], boundsList(room["bounds"]),
                        room["layout"]) for room
        in rooms]
    hallwayBoards = [
        convertJsonHallway(hallway["from"], hallway["to"], hallway["waypoints"])
        for hallway in hallways]
    keyObj = list(filter(lambda obj: obj["type"] == "key", objects)).pop()
    exitObj = list(filter(lambda obj: obj["type"] == "exit", objects)).pop()
    keyLoc = intifyTuple(tuple(keyObj["position"]))
    exitLoc = intifyTuple(tuple(exitObj["position"]))
    return Level(keyLoc, exitLoc, roomBoards + hallwayBoards, False)
