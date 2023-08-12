import json
from firebase_admin import firestore

from database import use_database
import sqs
from schema.main import ImageProgress, Img2ImgResponse


DB = use_database()


def create_progress(status: str):
    @firestore.transactional
    def update_in_transaction(transaction, doc_ref):
        doc_id = doc_ref.id
        transaction.update(doc_ref, {"_id": doc_id})

    try:
        transaction = DB.transaction()
        
        image_progress = ImageProgress(
            _id="",
            status=status,
            imageUrl="",
            worker=None
        )
        _, doc_ref = DB.collection("imageProgress").add(image_progress.dict())
        update_in_transaction(transaction, doc_ref)

        return True, Img2ImgResponse(id=doc_ref.id)
    except Exception as e:
        print(e)
        return False, None


def send_message(dto):
    sqs.send_message(json.dumps(dto.dict()))
