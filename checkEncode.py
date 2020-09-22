from chardet.universaldetector import UniversalDetector
# Возвращает кодировку текстового файла
def check_encoding(file):
	detector = UniversalDetector()
	with open(file, 'rb') as fh:
	    for line in fh:
	        detector.feed(line)
	        if detector.done:
	            break
	    detector.close()
	return detector.result['encoding']


print(check_encoding('vb.mtxr'))
