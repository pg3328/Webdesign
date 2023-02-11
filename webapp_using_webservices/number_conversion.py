import requests
import xml.etree.ElementTree as ET

url = "https://number-conversion-service.p.rapidapi.com/webservicesserver/NumberConversion.wso"

payload = """<?xml version='1.0' encoding='utf-8'?>
<soap:Envelope xmlns:soap='http://schemas.xmlsoap.org/soap/envelope/'>
  <soap:Body>
    <NumberToWords xmlns='http://www.dataaccess.com/webservicesserver/'>
      <ubiNum>4815</ubiNum>
    </NumberToWords>
  </soap:Body>
</soap:Envelope>"""
headers = {
	"content-type": "application/xml",
	"X-RapidAPI-Key": "ec55b003camshd61dfb0aac9f0b2p1b50a3jsn47d6d4860adf",
	"X-RapidAPI-Host": "number-conversion-service.p.rapidapi.com"
}

response = requests.request("POST", url, data=payload, headers=headers)
response.text
root = ET.fromstring(response.text)
converted_number = root.text
print(converted_number)

