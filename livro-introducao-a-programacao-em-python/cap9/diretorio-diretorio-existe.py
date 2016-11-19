# -*- coding: utf-8 -*-
import os
if os.path.exists("lorem") and os.path.isdir("lorem"):
	print("O diretório existe")
else:
	print("No ecssiste")