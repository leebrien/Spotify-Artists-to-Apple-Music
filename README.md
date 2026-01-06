# Spotify-Artists-to-Apple-Music
Migrate your followed artists on Spotify with Apple Music

Currently, this **Python** automation tool utilizes **Selenium** to automate the **Chrome** browser interaction with Apple Music. I am currently using a hardcoded list of artists that it will read from. I will try to implement the API approach as soon as Spotify brings back the developer features.

---

## Usage

1.  **Open the script** (`migrator.py`).
2.  **Edit the Artist List (This is just a temporary workaround)**:
    Locate the `followed_artists` list at the top of the file and add the names of the artists you want to migrate:
    ```python
    # This is temporary until Spotify brings back developer access
    followed_artists = [
        "Kendrick Lamar",
        "Frank Ocean",
        "D'Angelo",
        # Add more artists here...
    ]
    ```
3.  **Run the script**:
    ```bash
    python migrator.py
    ```
4.  **Log In**:
    * A Chrome window will open.
    * **Manually log in** to your Apple Music account.
    * Once logged in, return to your terminal and press **ENTER**.
5.  The script will then visit each artist and favorite them for you.

---

## Roadmap
* [x] Apple Music Automation (Favorites)
* [ ] Fetch the "Followed Artists" list directly from Spotify (via API).

## Disclaimer
Please use responsibly and be aware of Apple's terms of service.
