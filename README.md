# PostIt Website
## Description
This website provides a service for users to post and view photos. Users can create an accout,
then upload and view photos. Users that are not logged in can only view photos. Users that are
logged in can view photos in full resolution, otherwise, only low resolution photos are shown.

## Features
- Users can create an account
- Users can upload photos.
- Users can view photos.
- Users can view photos in full resolution if logged in.
- Photos are stored in a database and can be viewed by all users.
- Each photo has its own category, and a description.
- All photos are displayed on the home page, based on categories.

## Technologies
- Python (Flask)
- HTML (with Jinja2 templating)
- CSS
- SQLite (for database management)
- Docker (for containerization)

## Installation
1. Clone the repository
2. Install Docker
3. Run the following command in the root directory of the repository:
    ```bash
    docker build -t iap1-tema .
    ```
4. Run the following command to start the container:
    ```bash
    docker run -p 5000:5000 -it iap1-tema
    ```
5. Open a browser and go to
    ```bash
    localhost:5000
    ```