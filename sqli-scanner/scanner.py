import requests
from bs4 import BeautifulSoup
import sys
from urllib.parse import urljoin

s = requests.Session()
s.headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0"

# Function to get all forms
def get_forms(url):
  soup = BeautifulSoup(s.get(url).content, "html.parser")
  return soup.find_all("form")

def form_details(form):
  detailsOfForm = {}
  action = form.attrs.get("action")
  method = form.attrs.get("method", "get")
  inputs = []
  
  for input_tag in form.find_all("input"):
    input_type = input_tag.attrs.get("type", "text")
    input_name = input_tag.attrs.get("name")
    input_value = input_tag.attrs.get("value", "")
    inputs.append({
      "type": input_type,
      "name": input_name,
      "value": input_value
    })
    
  detailsOfForm['action'] = action
  detailsOfForm['method'] = method
  detailsOfForm['inputs'] = inputs
  
  return detailsOfForm

def vulnerable(res):
  errs = {"quoted string not terminated properly",
          "unclosed quotation mark after char string",
          "you have an error in your SQL syntax"
          }

  for err in errs:
    if err in res.content.decode().lower():
      return True
  return False

def sqli_scan(url):
  forms = get_forms(url)
  print(f"[+] Detected {len(forms)} forms on {url}.")
  
  for form in forms:
    details = form_details(form)
  
    for i in "\"'":
      data = {}
      for input_tag in details['inputs']:
        if input_tag['type'] == "hidden" or input_tag['value']:
          data[input_tag['name']] = input_tag['value'] + i
        elif input_tag['type'] != 'submit':
          data[input_tag['name']] = f"test{i}"
      
      print(url)
      form_details(form)
      
      if details['method'] == 'post':
        res = s.post(url, data=data)
      elif details['method'] == 'get':
        res = s.get(url, params=data)
      
      if vulnerable(res):
        print("SQL injection detected in link: ", url)
      else:
        print("No SQL injection attack vulnerability detected")
        break

if __name__ == '__main__':
  urlToBeChecked = "http://127.0.0.1:3000/#/contact"
  sqli_scan(urlToBeChecked)