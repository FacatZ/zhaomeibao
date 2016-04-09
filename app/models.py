#coding=utf-8
from .database import Base, db_session
from sqlalchemy import Column, String, Text, Integer, Float, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import backref, relationship
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask.ext.login import UserMixin, AnonymousUserMixin
from . import login_manager
from util import profile


class Permission:
    FOLLOW = 0x01
    READ_ARTICLES = 0x02
    WRITE_ARTICLES = 0x04
    MODERATE_ARTICLES = 0x08
    PUBLISH_PRODUCT = 0x10
    ADMINISTER = 0x80


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(Base, UserMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    
    username = Column(String(64), nullable=False, index=True)
    password_hash = Column(String(128))
    permissions = Column(Integer, default=15)

    #relationship
    productInformation = relationship('ProductInformation', backref='user', lazy='dynamic')
    articles = relationship('Article', backref='author', lazy='dynamic')

    #meta
    create_at = Column(DateTime, default=datetime.now)
    last_seen = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return '<User %s>' % (self.username)

    @property
    def password(self):
        #raise AttributeError('Password is not readable')
        return self.password_hash

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def can(self, permissions):
        return self.permissions & permissions == permissions

    def is_administrator(self):
        return self.can(Permission.ADMINISTER)

    def create_article(self, article):
        article.author = self
        try:
            db_session.commit()
            return True
        except Exception, e:
            db_session.rollback()
            return False

class AnonymousUser(AnonymousUserMixin):
    
    def can(self, permissions):
        return False
    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser


class ProductInformation(Base):

    __tablename__ = 'productInformation'

    id = Column(Integer, primary_key=True) #primary key
    
    typeid = Column(Integer, default=0) #1 for supply. 0 for demand
    
    #区分地区
    areaid = Column(Integer, default=0) 

    #分类关系
    ctgid = Column(Integer, ForeignKey('categories.id'))

    #用户关系
    uid   = Column(Integer, ForeignKey('users.id'))

    #工业指标关系
    indid = Column(Integer, ForeignKey('industryIndex.id'))

    #订单号
    ordnum = Column(String(64))
    
    #产地
    pdpid = Column(Integer, default=0) #省份id
    pdcid = Column(Integer, default=0) #城市id

    coal  = Column(String(64)) #煤种
    stock = Column(Integer) #库存
    count = Column(Integer) #需求量
    #价格部分
    price  = Column(Float) #价格
    prtype = Column(String(64)) #价格类型
    prpid  = Column(Integer) #省份
    prcid  = Column(Integer) #城市

    vldterm = Column(String(64)) #有效日期
    rldate  = Column(DateTime, default=datetime.now) #发布日期

    #交割地
    dpareaid = Column(Integer) #交割地id
    dppid  = Column(Integer) #省份
    dpcid  = Column(Integer) #城市
    dpaddr = Column(String(256)) #地址信息

    pdtype = Column(String(64), default=0) #产品类型 供货 0期货1现货
    paytype = Column(String(64), default=0) #需求 1现货2支票3电汇  

    remark = Column(String(256)) #备注
    onsale = Column(Boolean, default=False) #是否特价产品，默认为否

    @staticmethod
    def from_dict(dictionary):
        productInfo = ProductInformation()
        for key in dictionary:
            setattr(productInfo, key, dictionary[key])
        return productInfo

    def modify_from_dict(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def to_brief_json(self):
        indindex = self.industryIndex
        brief_json_dict = {
            u'category': self.category.name,
            u'coal': '...',
            u'qnetar': indindex.qnetar if indindex else None,
            u'star': indindex.star if indindex else None,
            u'stock': self.stock,
            u'dpareaid': profile.get_jiaogedi_name_by_id(self.dpareaid),
            u'price': self.price
        }
        return brief_json_dict

    def to_json(self):
        json_dict = {
            'areaid': self.areaid,
            'ctgid': self.ctgid,
            'ctgname': self.category.name,
            'uid': self.uid,
            'ordnum': self.ordnum,
            'pdpid': self.pdpid,
            'pdcid': self.pdcid,
            'coal': self.coal,
            'stock': self.stock,
            'price': self.price,
            'prtype': self.prtype,
            'prpid': self.prpid,
            'prcid': self.prcid,
            'vldterm': self.vldterm,
            'rldate': self.rldate,
            'dpareaid': self.dpareaid,
            'dppid': self.dppid,
            'dpcid': self.dpcid,
            'dpaddr': self.dpaddr,
            'pdtype': self.pdtype,
            'paytype': self.paytype,
            'remark': self.remark,
            'onsale': self.onsale
        }
        return json_dict

class Category(Base):
    '''
    产品信息类别表
    '''
    __tablename__ = 'categories'

    id = Column(Integer, primary_key=True)

    name = Column(String(64))

    productInformation = relationship('ProductInformation', backref='category', lazy='dynamic')


class IndustryIndex(Base):
    __tablename__ = 'industryIndex'

    id = Column(Integer, primary_key=True)

    productInformation = relationship('ProductInformation', backref='industryIndex', uselist=False)

    #水分
    mt  = Column(Float) #全水分
    mad = Column(Float) #内水

    #挥发粉
    var  = Column(Float) #收到基
    vad  = Column(Float) #空干基
    vdaf = Column(Float) #干燥无灰基

    #灰份
    aar = Column(Float) #收到基
    aad = Column(Float) #空干基

    #固定碳
    fcar = Column(Float) #收到基
    fcad = Column(Float) #空干基

    #全硫份
    star = Column(Float) #收到基
    stad = Column(Float) #空干基

    #低位发热量
    qnetar = Column(Integer) #收到基
    qnetad = Column(Integer) #空干基

    #粒度
    szuplm  = Column(Integer) #上限
    szlowlm = Column(Integer) #下限
    szppt   = Column(Integer) #占比

    @staticmethod
    def from_dict(dictionary):
        indindex = IndustryIndex()
        for key in dictionary:
            setattr(indindex, key, dictionary[key])
        return indindex

    def to_json(self):
        json_dict = {
            'mt':self.mt,
            'mad': self.mad,
            'var': self.var,
            'vad': self.vad,
            'vdaf': self.vdaf,
            'aar': self.aar,
            'aad': self.aad,
            'fcar': self.fcar,
            'fcad': self.fcad,
            'star': self.star,
            'stad': self.stad,
            'qnetar': self.qnetar,
            'qnetad': self.qnetad,
            'szuplm': self.szuplm,
            'szlowlm': self.szlowlm,
            'szppt': self.szppt
        }
        return json_dict

    def modify_from_dict(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])


class ArticleCategory(Base):
    '''
    文章类别表
    '''
    __tablename__ = 'articleCategories'

    id = Column(Integer, primary_key=True)

    name = Column(String(64))

    articles = relationship('Article', backref='category', lazy='dynamic')
    timestamp = Column(DateTime, default=datetime.now)


class Article(Base):

    __tablename__ = 'articles'

    id = Column(Integer, primary_key=True)

    ctgid = Column(Integer, ForeignKey('articleCategories.id'))
    uid = Column(Integer, ForeignKey('users.id'))
    title  = Column(String(128))
    body   = Column(Text)
    rldate = Column(DateTime, default=datetime.now)
    hits   = Column(Integer, default=0)

    #最近一次修改时间
    lastmodifed = Column(DateTime, default=datetime.now)
    
    def modify_from_dict(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def to_json(self):
        return {
            'id': self.id,
            'ctgid': self.ctgid,
            'ctgname':self.category.name,
            'title': self.title,
            'body': self.body
        }


class OrderNumberRecord(Base):
    __tablename__ = 'ordernumberrecords'

    id = Column(Integer, primary_key=True)
    last_date = Column(DateTime)
    count = Column(Integer)
    pdtype = Column(Integer)
