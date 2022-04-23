from PIL import Image

def isLevelup(FileName):
    Screenshot = Image.open(FileName)
    if Screenshot.size == (1920, 1080):
        count = 0
        for x in range(940, 970 + 1):
            for y in range(171, 172 + 1):
                r, g, b, a = Screenshot.getpixel((x, y))
                if r >= 170 and r <= 200 and g >= 145 and g <= 170 and b >= 50 and b <= 100:
                    count += 1
        if count >= 40:
            return True
        else:
            return False
    elif Screenshot.size == (1366, 768):
        count = 0
        for x in range(663, 680 + 1):
            for y in range(171, 172 + 1):
                r, g, b, a = Screenshot.getpixel((x, y))
                if r >= 220 and r <= 255 and g >= 155 and g <= 190 and b <= 20:
                    count += 1
        if count >= 34:
            return True
        else:
            return False
                
    else:
        print(f'레벨업 분석을 지원하지 않는 이미지 크기 "{Screenshot.size}" 를 가진 파일 "{FileName}" 이 감지되었습니다.')
        return True


