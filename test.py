from pyresparser import ResumeParser

data = ResumeParser('../Mohamed.pdf').get_extracted_data()
print(data['name'])