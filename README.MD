# File transfer

> The project is a file transfer project. you could share your files in localhost or on a server with all around the 
> world.

In this project, we create django project that has app (also a model) named `File`. 
This app is responsible for getting file from the host and deploy on django site.  


## Installation

- Clone the repository.
- Create virtual environment using `python -m virtualenv --python=python3 env`.
- Activate env (in linux use `. env/bin/activate`).
- Install requirements.txt using `pip install -r requirements.txt`.

## Usage example

- Get your IP address (in linux use `hostname -I`).
- Create admin user using `./manage.py createsuperuser`.
  - set username, email (optional) and password.
- Run django on your IP address, and a free port (e.g. `./manage.py runserver 192.168.1.4:8000`).
- Go to admin `/admin`.
- Enter your username and password.
- Go to `/admin/File/file/` and add a file (set a name and upload file).
- Connect your other device to same network (in case of local network).
- Go to the home page and download your file.

## TODO

- [ ] Add styling
- [ ] Add create / login method in home page.
- [ ] Create private / public files type.
- [ ] Create password-protected files.