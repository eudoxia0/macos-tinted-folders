all: GenericFolderIcon.iconset

GenericFolderIcon.icns:
	cp /System/Library/CoreServices/CoreTypes.bundle/Contents/Resources/GenericFolderIcon.icns GenericFolderIcon.icns

GenericFolderIcon.iconset: GenericFolderIcon.icns
	iconutil -c iconset GenericFolderIcon.icns

.PHONY: clean
clean:
	rm -f GenericFolderIcon.icns
	rm -rf GenericFolderIcon.iconset
