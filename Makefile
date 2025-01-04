.PHONY: all
all:
	python3 generate.py

.PHONY: clean
clean:
	rm -f GenericFolderIcon.icns
	rm -rf GenericFolderIcon.iconset
	rm -rf output
