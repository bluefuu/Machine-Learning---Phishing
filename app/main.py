import Features
import MLModel

url = "https://www.optus.com.au/"
url14 = "https://www.linkfire.com/"
url1 = "https://globalinfohost.com/landingpage/dd263864-38a2-466a-be2f-4e5ec6c5e042/mthzm4r_hzib_ekunll2tnc0tdjldeg0lh9s9kemwws"
url2 = "http://206.189.85.218/download-film-sea-fever-2020-sub-indo/"
url3 = "http://stolizaparketa.ru/wp-content/themes/twentyfifteen/css/read/chinavali/index.php?email=jsmith@imaphost.com"

fl = Features.Feature(url14)
farray = fl.getList()

mlmodel = MLModel.MLModel()

result = mlmodel.test(farray)

not_phishing = result.get('is_phishing=0')
is_phishing = result.get('is_phishing=1')

print("Phishing %: " + str(is_phishing))
print("Not Phishing %: " + str(not_phishing))