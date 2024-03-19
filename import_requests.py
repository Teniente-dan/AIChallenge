import requests
import time

# List of product names to search for
product_names = ['car', 'car', 'chair']  # Replace these with actual product names

def fetch_product_recall_info(product_name):
    """Fetch recall information for a given product."""
    # Format the URL with the current product name
    url = f'https://www.saferproducts.gov/RestWebServices/Recall?ProductName={product_name}&format=json'
    
    try:
        # Make the HTTP GET request
        # print url
        print(url)
        response = requests.get(url)
        
        # Check if the response status code is 200 (OK)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            print(f"Data for {product_name}: {data}")  # You can replace this with saving or processing logic
        else:
            print(f"Failed to fetch data for {product_name}. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while fetching data for {product_name}: {e}")

def main():
    for product_name in product_names:
        fetch_product_recall_info(product_name)
        time.sleep(1)  # Pause for a second between requests to avoid overwhelming the server

if __name__ == "__main__":
    main()
