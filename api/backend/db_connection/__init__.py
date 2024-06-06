from flaskext.mysql import MySQL
from pymysql import cursors

db = MySQL(cursorclass=cursors.DictCursor)
