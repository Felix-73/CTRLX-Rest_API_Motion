import requests
from utils.helpers import handle_api_error
from utils.config import API_BASE_URL_TEMPLATE, AUTH_URL_TEMPLATE, USERNAME, PASSWORD, TIMEOUT

class ApiClient:

    # CONSTRUCTEUR DE LA CLASS
    def __init__(self, ip_address, axis_name, timeout=TIMEOUT):
        self.session = requests.Session()
        self.base_url = API_BASE_URL_TEMPLATE.format(ip_address=ip_address)
        self.auth_url = AUTH_URL_TEMPLATE.format(ip_address=ip_address)
        self.timeout = timeout
        self.axis_name = axis_name
        self.api_key = self.get_api_key()


    def get_api_key(self):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        data = {
            "password": PASSWORD,
            "name": USERNAME
        }
        try:
            response = self.session.post(self.auth_url, headers=headers, json=data, timeout=self.timeout, verify=False)
            handle_api_error(response)
            return response.json().get('access_token')
        except requests.RequestException as e:
            raise Exception(f"Failed to obtain API key: {e}")

    def move_absolute(self, axs_pos, vel, acc, dec):
        url = f"{self.base_url}/nodes/motion/axs/{self.axis_name}/cmd/pos-abs"
        headers = {'Authorization': f'Bearer {self.api_key}'}
        data = {
            "type": "object",
            "value": {
                "axsPos": axs_pos,
                "buffered": False,
                "lim": {
                    "vel": vel,
                    "acc": acc,
                    "dec": dec,
                    "jrkAcc": 0,
                    "jrkDec": 0
                }
            }
        }
        try:
            response = self.session.post(url, headers=headers, json=data, timeout=self.timeout, verify=False)
            handle_api_error(response)
            return response.text
        except requests.RequestException as e:
            return str(e)

    def power(self, state):
        url = f"{self.base_url}/nodes/motion/axs/{self.axis_name}/cmd/power"
        headers = {'Authorization': f'Bearer {self.api_key}'}
        data = {
            "type": "bool8",
            "value": state
        }
        try:
            response = self.session.post(url, headers=headers, json=data, timeout=self.timeout, verify=False)
            handle_api_error(response)
            return response.text
        except requests.RequestException as e:
            return str(e)