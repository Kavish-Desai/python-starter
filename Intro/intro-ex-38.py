# 
# File: intro-ex-38.py
# Auth: Martin Burolla
# Date: 8/31/2021
# Desc: 
#

def main():
  roomsList = [
    { 
      'room' : 
      { 
        'name' : 'kitchen',
        'color' : 'blue',
        'dimensions' : 
        { 
          'width' : 10, 'length' : 20, 'height' : 8 
        }
      }
    },
    { 
      'room' : 
      { 
        'name' : 'living room',
        'color' : 'blue',
        'dimensions' : 
        { 
          'width' : 10, 'length' : 20, 'height' : 10 
        }
      }
    },
    { 
      'room' : 
      { 
        'name' : 'family room',
        'color' : 'tan',
        'dimensions' : 
        { 
          'width' : 10, 'length' : 20, 'height' : 8 
        }
      }
    },
    { 
      'room' : 
      { 
        'name' : 'bathroom',
        'color' : 'blue',
        'dimensions' : 
        { 
          'width' : 5, 'length' : 8, 'height' : 10 
        }
      }
    },
  ]

  PRICE_PER_SQUARE_FEET = .15

  filterRoomList = list(filter(lambda x: x['room']['color'] == 'blue' and x['room']['dimensions']['height'] == 10, roomsList))
  costList = list(map(lambda x: x['room']['dimensions']['length'] * x['room']['dimensions']['width'], filterRoomList))
  
  # lc = [r['room']['dimensions']['length'] * r['room']['dimensions']['width'] for r in roomsList if r['room']['color'] == 'blue' and r['room']['dimensions']['height'] == 10]
  # cost = sum(lc) * PRICE_PER_SQUARE_FEET
  # print(cost)

  cost = sum(costList) * PRICE_PER_SQUARE_FEET
  print(cost)

if __name__ == "__main__":  
  main()
