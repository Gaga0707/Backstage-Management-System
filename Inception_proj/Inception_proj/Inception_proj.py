from flask import Flask, render_template, escape, request, redirect, url_for
import math
import pymysql

app = Flask(__name__,template_folder="templates")

numb = 10

#初始登录界面
@app.route('/')  
def LoginView():
    display = False
    return render_template('login.html',display = display)



#登陆后跳转主界面
@app.route("/login",methods=['GET','POST'])    
def login():
    #连接数据库
    select_user=[]
    db = pymysql.connect(
        host ="localhost",
        port = 3306,
        password = "cyw88758875",
        user = "root",
        database = "proj",
        charset = "utf8"
)
    #找到数据库 
    cur = db.cursor()   

    if request.method == "POST":
        user = request.form.get("logname")
        pwd = request.form.get("password")

        sq = "select * from users where logname = '%s' and password = %s;" %(str(user),int(pwd))
        cur.execute(sq)
        select_user = cur.fetchall()
        # selected_user = select_user[0]     #  很重要，select_user多了一个逗号
        db.commit()
        db.close()
        if select_user != ():
            return render_template('main.html',myname = user,select_user = select_user)  # 修改过
        else:
            display = True 
            return render_template('login.html',display = display)
    else:
        return redirect(url_for('LoginView'))
    


@app.route('/main/<string:myname>')
def main(myname):
    return render_template('main.html',myname=myname)#由于之前将myname这个参数传到main所以后续都要用到 后端也要用到


@app.route('/profile/<string:myname>',methods = ['GET','POST'])  #数据库连接在前面写了 如果要别的地方使用得重新写db=pymysql.connect...
def profile(myname):#只要用到myname就要在头部写出来<string:myname>
    #连接数据库
    db = pymysql.connect(
        host ="localhost",
        port = 3306,
        password = "cyw88758875",
        user = "root",
        database = "proj",
        charset = "utf8"
)

    cur=db.cursor()
    
    real_name=request.form.get('realname')#一定要和自己表中的名字一致
    mailbox=request.form.get('email')
    mobile_num=request.form.get('cellphone')    
    
    sql="select *from users where logname = '%s';" %(myname)#挑出名字为用户输入名字的这一行
    sql1="update users set realname = '%s',email = '%s',cellphone = '%s' where logname = '%s';" % (real_name,mailbox,mobile_num,myname)#当name和用户输入的名字（myname）一致时更新用户的真实姓名（real_name）
    try:
        cur.execute(sql)
        results=cur.fetchall()
        realname=results[0][2]#由于results是我们执行sql之后的结果：已经挑出来了我们用户输入名字的那一行所以第一个数字永远是[0]
        email=results[0][5]
        cellphone=results[0][6]
        db.commit()
        
        if request.method=='POST':
            cur.execute(sql1)
            db.commit()
            # return render_template('main.html',myname=myname,realname=realname,email=email,cellphone=cellphone)
            sq = "select * from users where logname = '%s';" %(str(myname))
            cur.execute(sq)
            select_user = cur.fetchall()
            # selected_user = select_user[0]     #  很重要，select_user多了一个逗号
            db.commit()
            db.close()

            return render_template ('main.html',myname=myname,select_user=select_user)
            # return render_template('main.html',myname=myname)
        else:
            return render_template('profile.html',myname=myname,realname=realname,email=email,cellphone=cellphone)
        
    except:
        db.rollback()
        cur.close()
        db.close()
        
    
    return render_template('profile.html')





@app.route("/editPwd/<string:myname>",methods = ['GET','POST'])
def editpwd(myname):#myname其实就是用户输入的用户名（数据库stu中表cls的user）
    if request.method == "POST":
        db=pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            password='cyw88758875',
            database='proj',
            charset='utf8'
    )
        
        cur = db.cursor() #想运用数据库调用数据库的内容就一定要有这句话

        oldpwd = request.form.get("oldpwd")
        # print(oldpwd)
        newpwd = request.form.get("newpwd")
        # print(newpwd)
        confirmpwd = request.form.get("confirmpwd")
        # print(confirmpwd)
        if newpwd == confirmpwd:
            error= False
        else:
            error = True 
            return render_template('editPwd.html',myname = myname,error = error)#如果新输入的密码和再次确定型输入的密码不一致就返回到html文件输出两次输入密码不一致
        #能进入到下面说明两次密码肯定是一致的
        sql ="select * from users where password = '%s'and logname = '%s';"%(oldpwd,myname)#从数据表里面挑选到用户名为用户输入以及密码是用户输入的密码的那一行用户
        sql2 = "update users set password = '%s' where logname = '%s';"%(newpwd,myname)#更新新的密码替换为旧的密码

        try:
            cur.execute(sql)
            results = cur.fetchall()
            db.commit()
            if results != ():#如果读取的这一行数据不为空 那么就把True赋值给display
                display = True
                cur.execute(sql2)
                db.commit()
                return redirect(url_for('LoginView'))
                # return render_template('main.html',myname = myname)
            else:
                display = False
                return render_template('editPwd.html',myname = myname ,display = display)

        except:
            db.rollback()

        cur.close()
        db.close()
    else:
        return render_template('editPwd.html',myname = myname)   

# @app.route("/editPwd/<string:myname>",methods = ['GET','POST'])
# def editpwd(myname):#myname其实就是用户输入的用户名（数据库stu中表cls的user）
#     if request.method == "POST":
#         display = True
#         cerror=True
#         db=pymysql.connect(
#             host='localhost',
#             port=3306,
#             user='root',
#             password='hsy0724hsy',
#             database='proj',
#             charset='utf8'
#     )
        
#         cur = db.cursor() #想运用数据库调用数据库的内容就一定要有这句话

#         oldpwd = request.form.get("oldpwd")
#         # print(oldpwd)
#         newpwd = request.form.get("newpwd")
#         # print(newpwd)
#         confirmpwd = request.form.get("confirmpwd")
#         # print(confirmpwd)
#         if newpwd == confirmpwd:
#             cerror= True
#         else:
#             cerror = False 
#             # return render_template('editPwd.html',myname = myname,error = error)#如果新输入的密码和再次确定型输入的密码不一致就返回到html文件输出两次输入密码不一致
#         #能进入到下面说明两次密码肯定是一致的
#         sql ="select * from users where password = '%s'and logname = '%s';"%(oldpwd,myname)#从数据表里面挑选到用户名为用户输入以及密码是用户输入的密码的那一行用户
#         sql2 = "update users set password = '%s' where logname = '%s';"%(newpwd,myname)#更新新的密码替换为旧的密码

#         try:
#             cur.execute(sql)
#             results = cur.fetchall()
#             db.commit()
#             if results != ():#如果读取的这一行数据不为空 那么就把True赋值给display
#                 cur.execute(sql2)
#                 db.commit()
#                 # return render_template('editPwd.html',myname = myname ,display = display)
#                 return redirect(url_for('LoginView'))
#             else:
#                 display = False
#                 return render_template('editPwd.html',myname = myname ,display = display,cerror=cerror)
#         except:
#             db.rollback()

#             cur.close()
#             db.close()
#     else:
#         return render_template('editPwd.html',myname = myname) 














#  用户管理主界面
@app.route("/list_ur/<int:page>") 
def list_ur(page):
    #连接数据库
    db = pymysql.connect(
        host ="localhost",
        port = 3306,
        password = "cyw88758875",
        user = "root",
        database = "proj",
        charset = "utf8"
    )
    #找到数据库 
    cur = db.cursor()

    sq1 = "select * from users;"
    cur.execute(sq1)
    results = cur.fetchall()
    # print(dict(results))
    x1 = []
    x3 = ['logname','password','realname','user_type','gender','email','cellphone','workphone','user_state','del_state']
    users = []
    for i in range(len(results)):  #元组转列表
        x1.append(list(results[i]))
    # print(x1)
    for j in range(len(x1)):
        x={}
        x2 = []
        for h in range(len(x1[j])):
            x2.append(x1[j][h])
            x[x3[h]] = x2[h]
        users.append(x)     #----------------------------- 初始化“列表-字典“
    # print(users)
    db.commit()
    db.close()

    new_users = []                   # !!!!非常重要！！！！ 一面要显示的信息都在这里面！！！
    for i in range(len(users)):
        satrt = page * numb - numb   # 'numb'是一个全局变量，设置每一面显示的信息个数
        end = page * numb  
        if satrt <= i <end:
            new_users.append(users[i])


    nums = [ i+1 for i in range(math.ceil(len(users)/numb))]  #  是设置有多少页面的数字
    last = int(nums[-1])

    return render_template("user/list.html",**locals())


@app.route("/list_ware/<int:page>")
def list_ware(page):
    db = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="cyw88758875",
        database="proj",
        charset="utf8"
        )
#生成游标对象
    cur = db.cursor()
#数据库命令
    sql = "select * from ware;"
#执行命令
    cur.execute(sql)
    db.commit()
    results = cur.fetchall()

    new_users = []
    # print(len(results))
    for i in range(len(results)):    #  'users'注意修改
        start = page * numb-numb     #这里的 '1'是可以修改的，设置“每一面”显示的“信息个数”
        end = page * numb          # e.g.  改成‘3’，则每一面会显示 3 个数据
        if start <= i <end:
            new_users.append(results[i])   #  'users'注意修改

    nums = [ i+1 for i in range(math.ceil(len(results)/numb))]  #  设置“页面方块”的个数（1，2，3，4，5，6·······）  #  'users'注意修改
    last = int(nums[-1])

    return render_template('warehouse/list.html', warehouse=new_users,nums = nums,page = page,last = last)



@app.route('/category/<int:page>')
def category(page):
    db=pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='cyw88758875',
        database='proj',
        charset='utf8'
)
    cur = db.cursor() #想运用数据库调用数据库的内容就一定要有这句话
    sq ='select *from category;'#进入表
    cur.execute(sq)#执行sq
    results = cur.fetchall()
    # print(results)
    
    new_users = []
    for i in range(len(results)):
        satrt = page * numb - numb   # '5'是一个全局变量，设置每一面显示的信息个数
        end = page * numb  
        if satrt <= i <end:
            new_users.append(results[i])

    nums = [ i+1 for i in range(math.ceil(len(results)/numb))]  #  '2' 是设置有多少页面的数字
    last = int(nums[-1])
    return render_template('category/list.html',**locals())












@app.route("/rem/<name>/<page>") #  返回值 'name' 和 'page'（name用于索引用户；page用于返回删除用户所在的界面）  在list.html中定义
def rem_ur(name,page):           #  返回值 'name' 和 'page'（name用于索引用户；page用于返回删除用户所在的界面）  在list.html中定义
    #  连接数据库
    db = pymysql.connect(
        host ="localhost",
        port = 3306,
        password = "cyw88758875",
        user = "root",
        database = "proj",
        charset = "utf8"
        )
    #找到数据库 
    cur=db.cursor()
    
    try:
        sq3="delete from users where logname='%s';"  %(name)   #  删除 logname = name 的用户
        cur.execute(sq3)
        db.commit()

        sq4 = "select * from users;"    #  遍历删除后数据库的数据量
        cur.execute(sq4)
        results4 = cur.fetchall()

        #  获得删除后的页面数
        page3=math.ceil(len(results4)/numb)  
        if page3<=int(page):
            return redirect(url_for('list_ur',page=page3))  
        else:
            return redirect(url_for('list_ur',page=page-1))  
    except:
        db.rollback()
    db.close()
    return redirect(url_for('list_ur',page=page))  
    




@app.route("/delet/<name>/<page>")
def delet(name,page):
    db = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="cyw88758875",
        database="proj",
        charset="utf8"
        )
#生成游标对象
    cur = db.cursor()
    try:
        sq3="delete from ware where name='%s';"  %(name)   #  删除 logname = name 的用户
        cur.execute(sq3)
        db.commit()
        sq4 = "select * from ware ;"    #  遍历删除后数据库的数据量
        cur.execute(sq4)
        results4 = cur.fetchall()

        #  获得删除后的页面数
        page3=math.ceil(len(results4)/numb)  
        if page3<=int(page):
            return redirect(url_for('list_ware',page=page3))  # 函数改
        else:
            return redirect(url_for('list_ware',page=page-1))  # 函数改
    except:
        db.rollback()
    db.close()
    return redirect(url_for('list_ware',page=page))  # 函数改




@app.route('/category_del/<category_id>/<page>')
def category_del(category_id,page):
    db=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    password='cyw88758875',
    database='proj',
    charset='utf8'
)
    cur = db.cursor() #想运用数据库调用数据库的内容就一定要有这句话
    try:
        sq3="delete from category where id= %s ;"%(int(category_id))
        cur.execute(sq3)
        db.commit()

        sq4 = "select * from category;"
        cur.execute(sq4)

        results4 = cur.fetchall()
        page3=math.ceil(len(results4)/numb)
        if page3<=int(page):
            return redirect(url_for('category',page=page3))
        else:
            return redirect(url_for('category',page=page-1))
    except:
        db.rollback()
    db.close()
    return redirect(url_for('category',page=page))


    










#  添加用户
@app.route("/add_ur",methods = ['GET','POST'])
def add_nur():
    #连接数据库
    db = pymysql.connect(
        host ="localhost",
        port = 3306,
        password = "cyw88758875",
        user = "root",
        database = "proj",
        charset = "utf8"
    )
    #找到数据库 
    cur = db.cursor()  

    try:
        if request.method == "POST":  #  获取用户输入值
            user_logname = request.form.get("logname")
            user_password = request.form.get("password")
            user_realname = request.form.get("realname")
            user_user_type = request.form.get("user_type")
            user_gender = request.form.get("gender")
            user_email = request.form.get("email")
            user_cellphone = request.form.get("cellphone")
            user_workphone = request.form.get("workphone")
            user_user_state = request.form.get("user_state")
            user_del_state = request.form.get("del_state")
            #判断添加用户的名称是否有重复
            sqx = "select * from users;"
            cur.execute(sqx)
            db.commit()
            results = cur.fetchall()
            for i in range(len(results)):
                x = True
                if user_logname == results[i][0]:
                    print(results[i][0])
                    x = False
                    return render_template('user/add.html',x = x) 
            #  在数据库添加用户信息    
            sq2 = "insert into users values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" %(user_logname,
                                                                                                 user_password,
                                                                                                 user_realname,
                                                                                                 user_user_type,
                                                                                                 user_gender,
                                                                                                 user_email,
                                                                                                 user_cellphone,
                                                                                                 user_workphone,
                                                                                                 user_user_state,
                                                                                                 user_del_state) 
            cur.execute(sq2)
            db.commit()
            return redirect(url_for('list_ur',page = 1))     
        else:
            return render_template('user/add.html')
    except:
        db.rollback()
    db.close()
    return redirect(url_for('list_ur', page = 1))


@app.route("/add_ware",methods = ['GET','POST'])
def add_ware():
    db = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="cyw88758875",
        database="proj",
        charset="utf8"
        )
#生成游标对象
    cur = db.cursor()
# #数据库命令
#     sql = "select * from ware;"
# #执行命令
#     cur.execute(sql)
    try:
        if request.method == "POST":     
            add_name = request.form.get("name")
            add_master = request.form.get("master")
            add_address= request.form.get("address")
            add_commit= request.form.get("commit")
            sqx = "select * from ware;"
            cur.execute(sqx)
            db.commit()
            results = cur.fetchall()
            for i in range(len(results)):
                x = True
                if add_name == results[i][0]:
                    print(results[i][0])
                    x = False
                    return render_template('warehouse/add.html',x = x)
            sq1 = "insert into ware values('%s','%s','%s','%s');"%(add_name,add_master,add_address,add_commit)

            cur.execute(sq1)
            db.commit()
            db.close()
            return redirect(url_for('list_ware',page = 1))
        else:
            return render_template('warehouse/add.html')
    except:
        db.rollback()
    db.close()
    return redirect(url_for('list_ware', page = 1))






@app.route("/category_add",methods = ['GET','POST'])     #鼠标点击信号是GET型，用户输入是POST型
def category_add():
    db=pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='cyw88758875',
        database='proj',
        charset='utf8'
)

#找到数据库 
    cur = db.cursor()  

    try:
        if request.method == "POST":     
            category_warehouse_name = request.form.get("ck_name")
            category_user_name = request.form.get("kh_name")
            category_region_floor = request.form.get("region")
            category_group_type = request.form.get("gg")
            category_column = request.form.get("ck_column")
            category_row = request.form.get("ck_row")                                  #   等号前的变量名可以不改（只存在py函数内）
            cate_gory_storeys = request.form.get("layer")                    #   等号后括号内变量名需要改（！要与自己创建的数据库变量名一致！）
            category_box_num = request.form.get("box_num")
            category_records_series = request.form.get("records_series")
            category_records_date = request.form.get("records_date")
            category_box2_num = request.form.get("box2_num")
            category_goods_allocation = request.form.get("goods_num")
    
            sq1 = "insert into category(ck_name,kh_name,region,gg,ck_column,ck_row,layer,box_num,records_series,records_date,box2_num,goods_num) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" %(category_warehouse_name,category_user_name,category_region_floor,category_group_type,category_column,category_row,cate_gory_storeys,category_box_num,category_records_series,category_records_date,category_box2_num,category_goods_allocation)
            cur.execute(sq1)
            
            db.commit()
            db.close()

            return redirect(url_for('category',page=1))
        else:
            return render_template('category/add.html')
    except:
        db.rollback()
        return redirect(url_for('category',page=1))












@app.route("/edit_ur/<name>/<page>/<user>",methods = ['POST','GET'])  #  返回值 name 和 page 和 user 
def edit_ur(name,page,user):                                       #  (前两者与‘删除’功能一致；)
                                                                   #  (user 是指被索引用户的所有信息值（表中一整行数据）)
    user = eval(user)  #  user 返回类型为str，要把它转换为原来的变量类型

    #连接数据库
    db = pymysql.connect(
        host ="localhost",
        port = 3306,
        password = "cyw88758875",
        user = "root",
        database = "proj",
        charset = "utf8"
)
    #找到数据库 
    cur = db.cursor()

    try:
        if request.method == "POST":                             # 参考 add函数 + SQL的update语法(update 表名 set 变量1 = ‘’，变量2 = ‘’，···· where 变量x = '')
            user_logname = request.form.get("logname")
            user_realname = request.form.get("realname")
            user_type = request.form.get("user_type")
            user_gender = request.form.get("gender")
            user_email = request.form.get("email")
            user_cellphone = request.form.get("cellphone")
            user_workphone = request.form.get("workphone")
            user_state = request.form.get("user_state")
            user_del_state = request.form.get("del_state")
            sq5 = "update users set logname='%s',realname='%s',user_type='%s',gender='%s',email='%s',cellphone='%s',workphone='%s',user_state='%s',del_state='%s' where logname = '%s';" %(user_logname,
                                                                                                                                                                                           user_realname,
                                                                                                                                                                                           user_type,
                                                                                                                                                                                           user_gender,
                                                                                                                                                                                           user_email,
                                                                                                                                                                                           user_cellphone,
                                                                                                                                                                                           user_workphone,
                                                                                                                                                                                           user_state,
                                                                                                                                                                                           user_del_state,
                                                                                                                                                                                           name)                                                                                   

            cur.execute(sq5)
            db.commit()
            return redirect(url_for('list_ur',page = page))    # 函数改  # 调用有输入值的函数，在后面补充输入值
        else:
            return render_template('user/edit.html',**locals()) # 路径
        
    except:
        db.rollback()
    db.close()
    return redirect(url_for('list_ur', page = page))     # 函数改  # 调用有输入值的函数，在后面补充输入值



@app.route("/edit_ware/<name>/<page>/<ware>",methods = ['GET','POST'])
def edit_ware(name,page,ware):
    ware = eval(ware)
    db = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="cyw88758875",
        database="proj",
        charset="utf8"
        )
#生成游标对象
    cur = db.cursor()
    try:
        if request.method == "POST":     
            edit_name = request.form.get("name")
            edit_master = request.form.get("master")
            edit_address= request.form.get("address")
            edit_commit= request.form.get("commit")
            # sq1 = "insert into ware values('%s','%s','%s','%s');"%(add_name,add_master,add_address,add_commit)
            sq2 = "update ware set name = '%s',master = '%s',address = '%s',commit = '%s' where name = '%s';"%(edit_name,edit_master,edit_address,edit_commit,name)
            cur.execute(sq2)
            db.commit()
            return redirect((url_for('list_ware',page = page)))
        else:
            return render_template('warehouse/edit.html',**locals())
    except:
        db.rollback
    db.close()
    return redirect((url_for('list_ware',page = page)))




@app.route('/category_edit/<category_id>/<page>/<i>',methods = ['GET','POST'])
def category_edit(category_id,page,i):
    i=eval(i)
    
    db=pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='cyw88758875',
        database='proj',
        charset='utf8'
)

#找到数据库 
    cur = db.cursor()   
       
    try:
        if request.method == "POST":     
            category_warehouse_name = request.form.get("ck_name")
            category_user_name = request.form.get("kh_name")
            category_region_floor = request.form.get("region")
            category_group_type = request.form.get("gg")
            category_column = request.form.get("ck_column")
            category_row = request.form.get("ck_row")                                  #   等号前的变量名可以不改（只存在py函数内）
            cate_gory_storeys = request.form.get("layer")                    #   等号后括号内变量名需要改（！要与自己创建的数据库变量名一致！）
            category_box_num = request.form.get("box_num")
            category_records_series = request.form.get("records_series")
            category_records_date = request.form.get("records_date")
            category_box2_num = request.form.get("box2_num")
            category_goods_allocation = request.form.get("goods_num")
            #第一种语法
            sq1 = "update category set ck_name = '%s',kh_name = '%s',region = '%s',gg = '%s',ck_column = '%s',ck_row = '%s',layer = '%s',box_num = '%s',records_series = '%s',records_date = '%s',box2_num = '%s',goods_num = '%s' where id = %s;" %(category_warehouse_name,category_user_name,category_region_floor,category_group_type,category_column,category_row,cate_gory_storeys,category_box_num,category_records_series,category_records_date,category_box2_num,category_goods_allocation,category_id)

            cur.execute(sq1)
            
            db.commit()
            db.close()
            # return render_template('category/list.html')
            return redirect(url_for('category', page=page))
        else:
            return render_template('category/edit.html',**locals())
    except:
        db.rollback()
    return redirect(url_for('category',page=page))




if __name__ == '__main__':
    app.run(debug = True)