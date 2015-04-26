project=backend

all: clean syncdb superuser run

clean:
	-rm -rf *~*
	-find . -name '*.pyc' -exec rm {} \;
	-rm -f $(project)/database/*.db

fresh_syncdb:
	-rm -f $(project)/database/*.db
	python $(project)/manage.py syncdb --noinput

syncdb:
	python $(project)/manage.py syncdb --noinput

shell:
	python $(project)/manage.py shell

superuser:
	python $(project)/manage.py createsuperuser

run:
	python $(project)/manage.py runserver localhost:8080
