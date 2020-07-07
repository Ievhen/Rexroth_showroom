# Startup script

from IL_Program.box import Box
from IL_Program.section import Section

SECTION_NUM = 14

box1 = Box()

section = []
for i in range(SECTION_NUM):
    section.append(Section())

section[12].set_max_pallete_num(4)

print(section[12].get_max_pallete_num())