@echo OFF
REM Creates a dump of posts into a _dumps/YYYY_mm_dd_HH:MM.json fixture

CALL python manage.py dumpdata blog.BlogPost -o _dumps/%DATE:-=_%_%TIME:~0,2%-%TIME:~3,2%.json
