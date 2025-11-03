
import sys
import requests



def main():
    # user input cli number of bitcoins "n" 
    # if argument cannot be converted to float => sys.exit + error message.
    try:
        n = float(sys.argv[1])
        
        amount = get_price(n)

        
        print(f"${amount:,.4f}")                        # output the current price of "n" bitcoins in USD to 4-dp, using "," as a thousands separator

        

    except ValueError:
        sys.exit("Command-line argument is not a number")
    except IndexError:
        sys.exit("Missing command-line arument")
        



def get_price(n):
    try:
    
        #query the API for the price index as index
        "rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey " # replace YourApiKey

        my_api = "ea6e1222f89d05d83c0954b3a88c469ebb2dd8312466c9a8ecb107b4c01acac0"
        url = "https://rest.coincap.io/v3/"
        response = requests.get(f"{url}price/bysymbol/BTC?apiKey={my_api}")
        value = float(response.json()["data"][0])

        price = n*value
        return price

    # catch exceptions 
    except requests.RequestException:
        sys.exit("Request Exception Errpr")
    


main()