PACKAGE_NAME = color-brightness.sublime-package

build:
	rm -f $(PACKAGE_NAME)
	zip $(PACKAGE_NAME) * -x Makefile
