project=backend
front=frontend

all: clean install syncdb superuser run

clean:
	-rm -rf *~*
	-find . -name '*.pyc' -exec rm {} \;
	-rm -f $(project)/database/*.db
	-rm -rf $(front)/dist

cleanall: clean
	-rm -rf $(front)/bower_components
	-rm -rf $(front)/node_modules

fresh_syncdb:
	-rm -f $(project)/database/*.db
	python $(project)/manage.py syncdb --noinput

syncdb:
	python $(project)/manage.py syncdb --noinput

install:
	bash -c "cd frontend; npm install; grunt install"

shell:
	python $(project)/manage.py shell

superuser:
	python $(project)/manage.py createsuperuser

front:
	grunt --base $(front) --gruntfile $(front)/Gruntfile.js

back:
	python $(project)/manage.py runserver localhost:8080