if not exist "venv" (
	python -m venv venv
)
"venv/Scripts/pip.exe" install pygame
"venv/Scripts/pip.exe" install pywin32