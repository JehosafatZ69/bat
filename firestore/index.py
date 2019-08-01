#!/usr/bin/python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime, time, firebase

#Default credentials
cred = credentials.Certificate('serviceAccount.json')
firebase_admin.initialize_app(cred)

db = firestore.client()
#Data insert
doc_ref = db.collection(u'dev/data/filterscan').document().set({
    u'code':60002020202,
    u'createdAt': firestore.SERVER_TIMESTAMP,
    u'did':u"Raspbian",
    u'hasCode':True,
    u'alive':True,
})


#Extract data
dev_ref = db.collection(u'dev/data/filterscan')
docs = dev_ref.get()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))