# BackTest
 
For launch this project, type in terminal: 
```Python
cd pro
```
Then
```Python
python manage.py runserver
```

Task :
We need to make a django app that will implement a tree-like menu, observing the following conditions:
* The menu is implemented via a template tag
* Everything above the highlighted item is expanded. The first nesting level below the highlighted item is also expanded.
* Stored in the database.
* Can be edited in the standard Django admin
* The active menu item is determined on the basis of the URL of the current page.
* There can be several menus on one page. They are determined by name.
* When you click on the menu, you jump to the specified URL. The URL can be specified either explicitly or through named url.
* For drawing each menu, it takes exactly 1 query to the database.
* Need a django-app, which allows you to contribute to the database menu (one or more) through the admin interface, and draw the menu by name on any page you want.
 {% draw_menu 'main_menu' %}
* Should only use Django and the standard Python library when doing the task from the libraries.
