""""
Strictly for fetching data from Canvas endpoint
"""

import requests

class CanvasClient:
    def __init__(self, base_url, api_token):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_token}"
            })

    def get_assignments(self, course_id):
    
        url = f"{self.base_url}/api/v1/courses/{course_id}/assignments"

        response = self.session.get(url)

        response.raise_for_status()

        return response.json()
