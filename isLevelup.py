from PIL import Image

def isLevelup(FileName):
    Screenshot = Image.open(FileName)
    if Screenshot.size == (1920, 1080):
        pass
    elif Screenshot.size == (1080, 720):
        pass
    else:
        print(f'레벨업 분석을 지원하지 않는 이미지 크기 "{Screenshot.size}" 를 가진 파일 "{FileName}" 이 감지되었습니다.')
        return False

