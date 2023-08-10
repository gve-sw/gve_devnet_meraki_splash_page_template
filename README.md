# gve_devnet_meraki_splash_page_template
code that provides a template to implement a click through splash page for Meraki Dashboard


## Contacts
* Jorge Banegas
* Rey Diaz

## Solution Components
* Meraki
* MR
* Flask

## Prerequisites
- [Docker](https://www.docker.com/get-started) installed on your machine.
- Python

## Installation/Configuration
1. Clone this repository with `git clone [repository name]`
2. Edit grant base url (nxx) in config.py file (go to your meraki dashboard and look up your unique url prefix)
```python
base_grant_url = 'https://nxxx.network-auth.com/splash/grant'
```
![/IMAGES/0image.png](/IMAGES/url_prefix.png)

3. Set up a Python virtual environment. Make sure Python 3 is installed in your environment, and if not, you may download Python [here](https://www.python.org/downloads/). Once Python 3 is installed in your environment, you can activate the virtual environment with the instructions found [here](https://docs.python.org/3/tutorial/venv.html).

4. Install the requirements with `pip3 install -r requirements.txt`

## Usage
To run the program, use the command:
```
$ python3 app.py
```

Open a web browser and go to http://localhost:5000 to access the custom Meraki splash page.

## Custom Meraki Splash Page
1. Log in to your Meraki Dashboard.
2. Navigate to the appropriate network and go to "Wireless > Splash page."
3. Select SSID to configure splash page
3. Select the "Click-through" option for Splash Page Type.
4. Enter the URL of your custom splash page in the "Custom splash URL" field.
5. Save your settings.

## Docker Setup and Running (optional)
1. Open a terminal window and navigate to the root directory of the cloned repository.
2. Build the Docker image using the provided Dockerfile:
    
    `docker build -t custom-splash-page .`

    This command builds the Docker image using the specified tag (custom-splash-page). The . at the end indicates that the Dockerfile is located in the current directory.
3. Once the image is built, you can run the container:
    
    `docker run -d -p 5000:5000 custom-splash-page`

    This command runs the container in detached mode (-d) and maps port 5000 from the host to port 5000 in the container. Adjust the port mapping as needed.
4. Feel free to change the host ip address/port for the container

    `CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]`

# Screenshots
![/IMAGES/0image.png](/IMAGES/splash_page.png)


![/IMAGES/0image.png](/IMAGES/0image.png)

### LICENSE

Provided under Cisco Sample Code License, for details see [LICENSE](LICENSE.md)

### CODE_OF_CONDUCT

Our code of conduct is available [here](CODE_OF_CONDUCT.md)

### CONTRIBUTING

See our contributing guidelines [here](CONTRIBUTING.md)

#### DISCLAIMER:
<b>Please note:</b> This script is meant for demo purposes only. All tools/ scripts in this repo are released for use "AS IS" without any warranties of any kind, including, but not limited to their installation, use, or performance. Any use of these scripts and tools is at your own risk. There is no guarantee that they have been through thorough testing in a comparable environment and we are not responsible for any damage or data loss incurred with their use.
You are responsible for reviewing and testing any scripts you run thoroughly before use in any non-testing environment.