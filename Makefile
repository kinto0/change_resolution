build_all:
	pyinstaller change_resolution.py 
clean:
	rm -rf build/*
	rm -rf dist/*
