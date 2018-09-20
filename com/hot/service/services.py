from com.hot.config.db import DBHelper


class UserService:
    def vertify_user_by_phone_and_pw(self, phone, passwd):
        sql = """select user_id, phone, username, money, email, add_time
               from users where phone = %s and password = md5(%s)"""
        param = (phone, passwd)
        res = DBHelper.query_one(sql, param)
        return res

    def get_user_by_phone(self, phone):
        sql = "select user_id, phone, username, money, email, add_time from users where phone = %s"
        param = (phone,)
        return DBHelper.query_one(sql, param)

    def get_user_list(self):
        return DBHelper.query_all("select user_id, phone, username, money, email, add_time from users")


# if __name__ == '__main__':
#     user_service = UserService()
    # r = user_service.get_user_by_phone("18520523706")
    # r = user_service.getUserList()
    # r = user_service.vertify_user_by_phone_and_pw("18520523706", "123456")
    # print(r)
