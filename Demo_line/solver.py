# Startup script
from Demo_line.box import Box
from Demo_line.section import Section

SECTION_NUM = 14

box1 = Box()

section = []
for i in range(SECTION_NUM):
    section.append(Section())

section[12].set_max_pallete_num(4)

print(section[12].get_max_pallete_num())
