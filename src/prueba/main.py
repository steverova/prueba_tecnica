from logic import get_coordinates, get_neighborhood, increase_address

__author__ = "steverova"
__copyright__ = "steverova"
__license__ = "MIT"

def main():

    init_address = "1300 SE Stark Street, Portland, OR 97214"

    #step #1 get coordinates with the address
    coord = get_coordinates(init_address)
    
    #step #2 get get neighborhood with coordinates 
    neighborhood = get_neighborhood(coord)
    #step #3 print neighborhood
    print('Address: '+ init_address)
    print('Neighborhood: '+ neighborhood)
    print("============================")
    #step 4 - recursive function to increase address
    increase_address(init_address, neighborhood)
    
if __name__ == "__main__":
    main()
