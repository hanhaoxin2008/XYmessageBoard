from ..db import db
class Message(db.Model):
    __tablename__ = 'messages'
    #主键
    id = db.Column(db.Integer, primary_key=True)
    #名称
    name = db.Column(db.String(20))
    #地区
    area = db.Column(db.String(20))
    #学校
    school = db.Column(db.String(20))
    #专业
    major = db.Column(db.String(20))
    #留言内容
    content = db.Column(db.String(200))
    #留言时间
    create_time = db.Column(db.DateTime, default=db.func.now())
    def __init__(self,name, area, school, major, content):
        self.name = name
        self.area = area
        self.school = school
        self.major = major
        self.content = content
    def to_dict(self):
        return {
            'id': self.id,
            "name":self.name,
            'area': self.area,
            'school': self.school,
            'major': self.major,
            'content': self.content,
            'create_time': self.create_time.strftime('%Y-%m-%d %H:%M:%S')
        }