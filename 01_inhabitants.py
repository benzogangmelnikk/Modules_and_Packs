# -*- coding: utf-8 -*-

import room_1
import room_2

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

folks_1 = ", ".join(room_1.folks)
folks_2 = ", ".join(room_2.folks)
print('В комнате room_1 живут: ' + folks_1)
print('В комнате room_2 живут: ' + folks_2)


