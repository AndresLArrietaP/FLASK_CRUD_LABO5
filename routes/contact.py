from flask import Blueprint,request,jsonify
from models.contact import Contact
from utils.db import db

contact=Blueprint('contact',__name__)

@contact.route('/',methods=['GET'])
def getContactos():
    if request.method=='GET':
        data={}
        contactos=Contact.query.all()
        db.session.close()
        data['contactos']=contactos
        return jsonify(data)