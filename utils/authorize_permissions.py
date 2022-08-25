import xml.etree.ElementTree as ET

from utils.connect import connection_obj

tree = ET.parse('./config/queries.xml')

root = tree.getroot()

def authorize_permissions(user_id, role):
    search_role_id_query = root[8].text.format(user_id)

    cnx = connection_obj.getInstance()

    cursor = cnx.cursor()
    cursor.execute(search_role_id_query)

    search_list = list(cursor)

    role_id = search_list[0][0]

    search_role_name_query = root[9].text.format(role_id)
    cursor.execute(search_role_name_query)

    search_list = list(cursor)
    role_name = search_list[0][0]

    if role_name == role:
        return True
    return False

