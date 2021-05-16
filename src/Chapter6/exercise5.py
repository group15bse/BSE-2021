string = 'X-DSPAM-Confidence:0.8475'
begin=string.find(":")
extract=string[begin+1:]
extract=float(extract)
print(type(extract))