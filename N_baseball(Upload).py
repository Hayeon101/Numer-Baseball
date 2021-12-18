"""
*게임 방벙*
1. 시작 버튼을 누른다.
2. 숫자는 정해졌으니, 숫자 4개를 임의로 입력한다. (중복은 안 됨)
3. 스트라이크 개수와 볼 개수는 사라지기 때문에 어디 적어 놓아야 한다.
4. 이후 다음 버튼을 눌러 계속 진행한다.
5. 숫자를 모두 맞히면 CLEAR!! 라는 문구가 나오며, 5초 후 자동으로 꺼진다.

*유의사항*
1. 마구 누르면 pygame 특성상(?) 오류가 걸릴 수 있으므로 차분하게 진행해야 한다.
2. 설정 버튼은 장식이다.
3. 게임을 또 하고 싶다면 다시 켜야 한다.
"""

import pygame
import random
#----------------------------------------------------------------------------------
pygame.init() # 초기화

screen_width = 720 # 가로
screen_height = 480 # 세로
screen = pygame.display.set_mode((screen_width, screen_height)) # 화면 설정

pygame.display.set_caption("숫자 야구") # 게임 타이틀

# FPS
clock = pygame.time.Clock()
#----------------------------------------------------------------------------------
# 사용자 게임 초기화
programIcon = pygame.image.load('경로\\아이콘.png') # 파이게임 윈도우 아이콘 지정
pygame.display.set_icon(programIcon)

background = pygame.image.load("경로\\배경.png")     # 필요 사진들 불러오기
gscreen = pygame.image.load("경로\\게임화면.png")
next = pygame.image.load("경로\\다음.png")
cover = pygame.image.load("경로\\가리개.png")

font = pygame.font.SysFont("arial", 80)  # 폰트 설정
Sfont = pygame.font.SysFont("arial", 30)
Cfont = pygame.font.SysFont("arial", 140)

# 변수 설정
c = 1
s_cnt = 0
b_cnt = 0

def overlap(deflist): # 숫자 4개 리스트 중 중복된 숫자가 있는지 검사
    overlapC = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if deflist[i] == deflist[j] and i != j:
                overlapC += 1
    print(overlapC != 0)
    return overlapC != 0
def typing(c, n): # 입력한 숫자를 화면에 표시
    text = font.render(str(num), True, (0, 170, 170))
    if c < 5 and n == 0:
        if c == 1:
            background.blit(text, (90,140))
        if c == 2:
            background.blit(text, (182,140))
        if c == 3:
            background.blit(text, (274,140))
        if c == 4:
            background.blit(text, (366,140))
        answer.append(num)
        return 1
    else:
        return 0

running = True # 게임 진행 중
while running:
    dt = clock.tick(30) # 프레임 수
    # 2. 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if 27 <= pos[0] <= 234 and 369 <= pos[1] <= 449: # '시작' 버튼
                print("시작")
                N = I = II = III = IV = V = VI = VII = VIII = IX = 0
                s_cnt = 0
                b_cnt = 0
                rn = [0, 0, 0, 0]
                while overlap(rn): # 중복된 숫자를 제거하며 랜덤한 숫자 생성
                    print("이전", rn)
                    rn[0] = random.randint(0,9)
                    rn[1] = random.randint(0,9)
                    rn[2] = random.randint(0,9)
                    rn[3] = random.randint(0,9)
                print(rn)
                answer = []
                c = 1
                background.blit(gscreen, (50, 37))
        if event.type == pygame.MOUSEBUTTONDOWN and c >= 1: # '0' 버튼
            if 508 <= pos[0] <= 703 and 240 <= pos[1] <= 298:
                num = 0
                c += typing(c, N)
                N = 1
                print(answer)
            elif 508 <= pos[0] <= 565 and 171 <= pos[1] <= 227: # '1' 버튼
                num = 1
                c += typing(c, I)
                I = 1
                print(answer)
            elif 577 <= pos[0] <= 634 and 171 <= pos[1] <= 227: # '2' 버튼
                num = 2
                c += typing(c, II)
                II = 1
                print(answer)
            elif 646 <= pos[0] <= 703 and 171 <= pos[1] <= 227: # '3' 버튼
                num = 3
                c += typing(c, III)
                III = 1
                print(answer)
            elif 508 <= pos[0] <= 565 and 102 <= pos[1] <= 157: # '4' 버튼
                num = 4
                c += typing(c, IV)
                IV = 1
                print(answer)
            elif 577 <= pos[0] <= 634 and 102 <= pos[1] <= 157: # '5' 버튼
                num = 5
                c += typing(c, V)
                V = 1
                print(answer)
            elif 646 <= pos[0] <= 703 and 102 <= pos[1] <= 157: # '6' 버튼
                num = 6
                c += typing(c, VI)
                VI = 1
                print(answer)
            elif 508 <= pos[0] <= 565 and 35 <= pos[1] <= 88: # '7' 버튼
                num = 7
                c += typing(c, VII)
                VII = 1
                print(answer)
            elif 577 <= pos[0] <= 634 and 35 <= pos[1] <= 88: # '8' 버튼
                num = 8
                c += typing(c, VIII)
                VIII = 1
                print(answer)
            elif 646 <= pos[0] <= 703 and 35 <= pos[1] <= 88: # '9' 버튼
                num = 9
                c += typing(c, IX)
                IX = 1
                print(answer)
        if c == 5: # 정답과 비교
            for i in range(0,4):
                for j in range(0,4):
                    if rn[i] == answer[j]:
                        if i == j:
                            s_cnt += 1
                        elif i != j:
                            b_cnt += 1
                        break
            ball = Sfont.render(str(b_cnt), True, (0, 145, 0))
            strike = Sfont.render(str(s_cnt), True, (204, 150, 0))
            background.blit(ball, (98, 244))
            background.blit(strike, (98, 289))
            background.blit(next, (505, 305))
            c += 1
            print(f"Strike: {s_cnt}\nBall: {b_cnt}")
        if s_cnt == 4: # 정답을 맞추었을 때
            print("CLEAR!!")
            clear = Cfont.render("CLEAR!!", True, (000, 000, 000))
            background.blit(cover, (505, 305))
            background.blit(clear, (145,150))
            running = False
        if c == 6 and event.type == pygame.MOUSEBUTTONDOWN: # 정답을 맞추지 못했을 때
                if 505 <= pos[0] <= 705 and 305 <= pos[1] <= 375:
                    N = I = II = III = IV = V = VI = VII = VIII = IX = 0
                    answer.clear()
                    s_cnt = 0
                    b_cnt = 0
                    c = 1
                    background.blit(cover, (505, 305))
                    background.blit(gscreen, (50, 37))


    # 화면 채우기
    screen.blit(background, (0, 0))



    pygame.display.update() # 화면 업데이트 반복


# pygame 종료
pygame.time.wait(5000)
pygame.quit()