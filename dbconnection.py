import MySQLdb as mdb

def DBConnection():
    try:
        db = mdb.connect('localhost', 'root', '', 'jlneon')
        print('Succeeded To Connect Database')


    except mdb.Error as e:
        print('Failed To Connect Database')

