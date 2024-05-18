import re

signaturen = "BC 7410 P498 BC 7410 P869 BC 7410 S322 BC 7410 S349 bc 7410 S415"
regex = re.compile('[a-z]')
print(regex.findall(signaturen))
