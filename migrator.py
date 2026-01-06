from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import urllib.parse 

# This is just mock data representing followed artists from Spotify
followed_artists = [
    "Sampha",
    "Daniel Caesar",
    "Sza",
    "FKA Twigs",
    "Tyler, The Creator",
    "Doechii"
]

# Launch the Chrome browser
print("Launching Chrome...")
driver = webdriver.Chrome() 
driver.maximize_window()
driver.get("https://music.apple.com")

# Enter login credentials manually before proceeding
print("------------------------------------------------")
print("PLEASE LOG IN to Apple Music in the Chrome window.")
input("Once you are logged in, press ENTER here to start migration...")
print("------------------------------------------------")

# This loops through each followed artist and favorites them on Apple Music
for artist in followed_artists:
    print(f"\nProcessing: {artist}")
    
    # Search the artist
    safe_name = urllib.parse.quote(artist)
    search_url = f"https://music.apple.com/us/search?term={safe_name}"
    driver.get(search_url)
    
    try:
        # Wait for search results to load
        time.sleep(2) # Let search results load

        # Click on the Artist Tab
        artist_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href*='/artist/']"))
        )
        artist_link.click()
        
        # Inside the artist page, click the 'More' button (three dots)
        time.sleep(3) # Let profile load
        more_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[data-testid='more-button']"))
        )
        more_button.click()
        
        # Click the 'Favorite' option
        time.sleep(1) # Let menu open
        favorite_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "[title='Favorite']"))
        )
        favorite_button.click()
        print(f"--> SUCCESS! {artist} has been favorited.")
        
        time.sleep(2) # Brief pause before next one
        
    except Exception as e:
        print(f"--> Could not favorite {artist}.")
        print("    (They might already be favorited, or the page loaded too slowly)")

print("\n------------------------------------------------")
print("Migration Complete!")
print("------------------------------------------------")
driver.quit()