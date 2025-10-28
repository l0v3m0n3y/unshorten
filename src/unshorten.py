import requests
class Client():
	def __init__(self):
		self.api="https://unshorten.me"
	def get_full_url(self,short_url:str):
		return requests.get(f"{self.api}/json/{short_url}").json()