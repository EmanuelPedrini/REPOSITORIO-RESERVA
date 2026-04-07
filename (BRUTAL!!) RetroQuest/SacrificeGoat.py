# import pygame
# import sys
# import builtins
# import time
# from Kimera import kimera

# current_player = None
# player = None
# # ------------------ APP WINDOW ------------------
# class AppWindow:
#     def __init__(self, title, x, y, width, height, draw_func):
#         self.title = title
#         self.rect = pygame.Rect(x, y, width, height)
#         self.draw_func = draw_func
#         self.active = False

# # ------------------ CONFIG ------------------
# WIDTH, HEIGHT = 900, 600
# PRINT_DELAY = 0.002

# pygame.init()
# pygame.mixer.init()
# pygame.mixer.music.load("Music/music2.mp3")
# pygame.mixer.music.play(-1)

# screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
# pygame.display.set_caption("KIMERAHALLA")
# font = pygame.font.Font("Fonts/font2.ttf", 20)
# clock = pygame.time.Clock()

# lines = []
# current_input = ""
# scroll_offset = 0
# fullscreen = False
# typing = False
# image_surface = None

# # ------------------ STDOUT CUSTOM ------------------
# class Stdout:
#     def write(self, text):
#         global scroll_offset, typing
#         if text.strip() == "":
#             return
#         typing = True
#         scroll_offset = 0
#         lines_to_print = text.rstrip("\n").split("\n")
#         for part in lines_to_print:
#             line = ""
#             for char in part:
#                 line += char
#                 draw(lines_override=lines + [line], player=player)
#                 pygame.event.pump()
#                 time.sleep(PRINT_DELAY)
#             lines.append(part)
#             draw(player=player)
#             time.sleep(PRINT_DELAY / 2)
#         typing = False
#         draw(player=player)
#     def flush(self):
#         pass

# sys.stdout = Stdout()
# builtins.input = lambda prompt="": custom_input(prompt)

# # ------------------ FUNÇÕES ------------------
# def set_image(path):
#     global image_surface
#     image_surface = pygame.image.load(path).convert_alpha()
#     draw(player=player)

# def clear_image():
#     global image_surface
#     image_surface = None
#     draw(player=player)

# def draw(lines_override=None, player=None):
#     global current_player
#     player = current_player  # pega o player atual, se houver

#     screen.fill((0, 0, 0))
#     width, height = screen.get_size()
#     margin = 10
#     input_area = 40

#     # ---------- DIMENSÕES DA IMAGEM ----------
#     img_area_width = int(width * 0.4)
#     img_area_height = int(height * 0.4)
#     img_x = margin
#     img_y = margin

#     # ----- Caixa da imagem sempre definida -----
#     if image_surface:
#         img_w, img_h = image_surface.get_size()
#         scale = min(img_area_width / img_w, img_area_height / img_h, 1)
#         target_w = int(img_w * scale * 1.3)
#         target_h = int(img_h * scale * 1.2)
#         img_scaled = pygame.transform.scale(image_surface, (target_w, target_h))
#         box_rect = pygame.Rect(img_x - 3, img_y - 3, target_w + 6, target_h + 6)
#         pygame.draw.rect(screen, (0, 200, 0), box_rect, width=3, border_radius=5)
#         screen.blit(img_scaled, (img_x, img_y))
#     else:
#         box_rect = pygame.Rect(img_x, img_y, img_area_width, img_area_height)
#         pygame.draw.rect(screen, (0, 200, 0), box_rect, width=3, border_radius=5)

#     # ---------- ÁREA DE ATRIBUTOS ESCALÁVEL ----------
#     attr_x = margin
#     attr_y = box_rect.bottom + margin
#     attr_width = box_rect.width
#     attr_height = height - attr_y - input_area - margin
#     attr_rect = pygame.Rect(attr_x, attr_y, attr_width, attr_height)
#     pygame.draw.rect(screen, (0, 100, 0), attr_rect, border_radius=5)

#     if player:
#         # Fonte escalável: calcula tamanho baseado na altura da área
#         max_lines = 20  # número aproximado de linhas que caberão
#         dynamic_font_size = max(12, int(attr_height / max_lines))
#         attr_font = pygame.font.Font(None, dynamic_font_size)  # font_path é sua fonte principal

#         y_offset = 10
#         line_gap = dynamic_font_size + 4

#         # Lista de atributos do player
#         attrs_to_render = [
#             f"{player.nickname} STATS",
#             f"Level: [ {player.level} ]  XP: [ {player.xp} / {player.xptonext} ]",
#             f"HP   : [ {player.acthp} / {player.total_max_hp} ] + ( {player.shieldstat} ) SHIELD",
#             f"Mana : [ {player.actmana} / {player.max_mana} ]",
#             f"STR  : {player.total_strg} ( {player.base_strg} )",
#             f"DEX  : {player.total_dex} ( {player.base_dex} )",
#             f"VIT  : {player.total_vit} ( {player.base_vit} )",
#             f"INT  : {player.total_intel} ( {player.base_intel} )",
#             f"CHA  : {player.total_cha} ( {player.base_cha} )",
#             f"LUCK : {player.total_luck} ( {player.base_luck} )",
#             f"Dodge     : {player.dodge}",
#             f"Vampirism : {player.vampirism}",
#             f"Thorns    : {player.thorns}",
#             f"Armor     : {player.armor}",
    
#         ]

#         for attr_line in attrs_to_render:
#             text_surface = attr_font.render(attr_line, True, (255, 255, 255))
#             screen.blit(text_surface, (attr_rect.x + 10, attr_rect.y + y_offset))
#             y_offset += line_gap
#     else:
#         # Se não há player, mostra mensagem
#         empty_text = font.render("Player not selected", True, (200, 200, 200))
#         screen.blit(empty_text, (attr_rect.x + 10, attr_rect.y + 10))

#     # ---------- ÁREA DE TEXTO ----------
#     text_x = box_rect.right + margin
#     text_y = margin
#     text_width = width - text_x - margin
#     text_height = height - text_y - input_area - margin
#     pygame.draw.rect(screen, (0, 50, 0), (text_x, text_y, text_width, text_height))

#     # ---------- LINHAS DO TERMINAL ----------
#     line_height = 22
#     use_lines = lines_override if lines_override else lines
#     rendered_lines = []
#     for line in use_lines:
#         words = line.split(' ')
#         current_line = ""
#         for word in words:
#             test_line = current_line + (' ' if current_line else '') + word
#             if font.size(test_line)[0] > text_width - 10:
#                 if current_line:
#                     rendered_lines.append(current_line)
#                 current_line = word
#             else:
#                 current_line = test_line
#         if current_line:
#             rendered_lines.append(current_line)

#     max_lines_terminal = text_height // line_height
#     start = max(0, len(rendered_lines) - max_lines_terminal - scroll_offset)
#     end = start + max_lines_terminal
#     y = text_y
#     for line in rendered_lines[start:end]:
#         text_surface = font.render(line, True, (0, 255, 110))
#         screen.blit(text_surface, (text_x + 5, y))
#         y += line_height

#     # ---------- LINHA DE INPUT ----------
#     pygame.draw.line(screen, (60, 60, 60), (0, height - input_area), (width, height - input_area))
#     input_text = font.render("> " + current_input, True, (255, 255, 255))
#     screen.blit(input_text, (10, height - 30))

#     pygame.display.flip()

# def custom_input(prompt=""):
#     global current_input, scroll_offset, screen, fullscreen, typing
#     if prompt:
#         lines.append(prompt)
#     current_input = ""
#     backspace_timer = 0
#     while True:
#         dt = clock.tick(60) / 1000
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             elif event.type == pygame.VIDEORESIZE and not fullscreen:
#                 screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)
#             elif event.type == pygame.MOUSEWHEEL:
#                 scroll_offset += event.y
#                 scroll_offset = max(0, min(scroll_offset, len(lines)))
#             elif event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_F11:
#                     fullscreen = not fullscreen
#                     if fullscreen:
#                         screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#                     else:
#                         screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
#                 if not typing:
#                     if event.key == pygame.K_RETURN:
#                         value = current_input
#                         lines.append("> " + current_input)
#                         current_input = ""
#                         scroll_offset = 0
#                         draw(player=player)
#                         return value
#                     elif event.key == pygame.K_BACKSPACE:
#                         current_input = current_input[:-1]
#                         backspace_timer = 0.3
#                     else:
#                         current_input += event.unicode
#         keys = pygame.key.get_pressed()
#         if keys[pygame.K_BACKSPACE] and not typing:
#             backspace_timer -= dt
#             if backspace_timer <= 0:
#                 current_input = current_input[:-1]
#                 backspace_timer = 0.09
#         draw(player=player)


# # ------------------ TESTE ------------------
# # Troque o caminho abaixo por uma imagem válida no seu PC
# set_image("Images/imagemteste.jpg")  # <<<<<<<<<<<<<<<< substitua pela sua imagem
# draw(player=player)