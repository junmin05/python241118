import pygame
import random

# 색상 정의
COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "GRAY": (128, 128, 128)
}

# 테트리미노 모양 정의
SHAPES = [
    [[1, 1, 1, 1]],  # I
    [[1, 1], [1, 1]],  # O
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1, 0], [0, 1, 1]],  # S
    [[0, 1, 1], [1, 1, 0]]   # Z
]

class Tetris:
    def __init__(self):
        pygame.init()
        
        # 게임 설정
        self.width = 300
        self.height = 600
        self.block_size = 30
        self.grid_width = self.width // self.block_size
        self.grid_height = self.height // self.block_size
        
        # 게임 창 생성
        self.screen = pygame.display.set_mode((self.width + 200, self.height))
        pygame.display.set_caption("테트리스")
        
        # 게임 상태
        self.board = [[0] * self.grid_width for _ in range(self.grid_height)]
        self.score = 0
        self.level = 1
        
        # 현재 블록 초기화
        self.current_piece = self.new_piece()
        self.game_over = False
        
        # 게임 속도 설정
        self.clock = pygame.time.Clock()
        self.fall_time = 0
        self.fall_speed = 1000  # 밀리초 단위
        
    def new_piece(self):
        # 새로운 테트리미노 생성
        shape = random.choice(SHAPES)
        return {
            'shape': shape,
            'x': self.grid_width // 2 - len(shape[0]) // 2,
            'y': 0
        }
        
    def draw(self):
        self.screen.fill(COLORS["BLACK"])
        
        # 보드 그리기
        for y in range(self.grid_height):
            for x in range(self.grid_width):
                if self.board[y][x]:
                    pygame.draw.rect(self.screen, COLORS["WHITE"],
                                   [x * self.block_size, y * self.block_size,
                                    self.block_size - 1, self.block_size - 1])
        
        # 현재 조각 그리기
        if self.current_piece:
            for y, row in enumerate(self.current_piece['shape']):
                for x, cell in enumerate(row):
                    if cell:
                        pygame.draw.rect(self.screen, COLORS["WHITE"],
                                       [(self.current_piece['x'] + x) * self.block_size,
                                        (self.current_piece['y'] + y) * self.block_size,
                                        self.block_size - 1, self.block_size - 1])
        
        # 점수와 레벨 표시
        font = pygame.font.Font(None, 36)
        score_text = font.render(f'점수: {self.score}', True, COLORS["WHITE"])
        level_text = font.render(f'레벨: {self.level}', True, COLORS["WHITE"])
        self.screen.blit(score_text, (self.width + 10, 20))
        self.screen.blit(level_text, (self.width + 10, 60))
        
        pygame.display.flip()
        
    def run(self):
        while not self.game_over:
            self.clock.tick(60)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True
                    
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move(-1)
                    elif event.key == pygame.K_RIGHT:
                        self.move(1)
                    elif event.key == pygame.K_DOWN:
                        self.drop()
                    elif event.key == pygame.K_UP:
                        self.rotate()
            
            # 자동 낙하
            self.fall_time += self.clock.get_rawtime()
            if self.fall_time >= self.fall_speed:
                self.fall_time = 0
                self.drop()
            
            self.draw()
            
        pygame.quit()
        
    def move(self, dx):
        self.current_piece['x'] += dx
        if not self.valid_move():
            self.current_piece['x'] -= dx
            
    def drop(self):
        self.current_piece['y'] += 1
        if not self.valid_move():
            self.current_piece['y'] -= 1
            self.freeze()
            self.clear_lines()
            self.current_piece = self.new_piece()
            if not self.valid_move():
                self.game_over = True
                
    def rotate(self):
        # 현재 조각을 시계 방향으로 90도 회전
        shape = self.current_piece['shape']
        self.current_piece['shape'] = list(zip(*shape[::-1]))
        if not self.valid_move():
            self.current_piece['shape'] = shape
            
    def valid_move(self):
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_piece['x'] + x
                    new_y = self.current_piece['y'] + y
                    
                    if (new_x < 0 or new_x >= self.grid_width or
                        new_y >= self.grid_height or
                        (new_y >= 0 and self.board[new_y][new_x])):
                        return False
        return True
        
    def freeze(self):
        for y, row in enumerate(self.current_piece['shape']):
            for x, cell in enumerate(row):
                if cell:
                    self.board[self.current_piece['y'] + y][self.current_piece['x'] + x] = 1
                    
    def clear_lines(self):
        lines_cleared = 0
        for y in range(self.grid_height - 1, -1, -1):
            if all(self.board[y]):
                del self.board[y]
                self.board.insert(0, [0] * self.grid_width)
                lines_cleared += 1
                
        if lines_cleared:
            self.score += lines_cleared * 100
            self.level = self.score // 1000 + 1
            self.fall_speed = max(100, 1000 - (self.level - 1) * 100)

if __name__ == "__main__":
    game = Tetris()
    game.run()