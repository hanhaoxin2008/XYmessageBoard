from flask import Blueprint,json,request,redirect
from ..model import model
api_bp = Blueprint('api', __name__,url_prefix='/api')

@api_bp.route('/add_message',methods=['POST'])
def add_message():
        #获取post
        name=request.form.get('name')
        content=request.form.get('content')
        major=request.form.get('major')
        area=request.form.get('area')
        school=request.form.get('school')
        #插入数据库
        m=model.Message(name=name,content=content,area=area,major=major,school=school)
        model.db.session.add(m)
        model.db.session.commit()
        #重定向回首页
        return  redirect('/')
#获取留言
@api_bp.route('/get_messages')
def get_messages():
    msg=model.Message.query.all()
    msg_list=[]
    #把字变成json
    for m in msg:
        msg_list.append(m.to_dict())
    return json.dumps({"messages":msg_list},ensure_ascii=False)
