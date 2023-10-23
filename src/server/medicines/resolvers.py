from server.database.db_manager import base_manager
from server.medicines.models import MedicineOutput, MedicineInput

def get_medicine():
    res = base_manager.execute("SELECT id, title, dosage, type FROM medicine", many=True)
    print(res)
    medicines = []
    if not res:
        return None
    for medicine in res['data']:
        medicines.append(MedicineOutput(id=medicine[0], title=medicine[1], dosage=medicine[2], type=medicine[3]))
    return medicines


def get_current_medicine(medicine_id:int):
    res = base_manager.execute("SELECT id, title, dosage, type FROM medicine WHERE id = ?",
                             args=(medicine_id,), many=False)['data']
    if not res:
        return None
    return MedicineOutput(id=res[0], title=res[1], dosage=res[2], type=[3])


def add_medicine(new_medicine: MedicineInput):
    res = base_manager.execute("INSERT INTO medicine(title, dosage, type)"
                             "VALUES (?, ?, ?)"
                             "RETURNING id", args=(new_medicine.title, new_medicine.dosage, new_medicine.type))
    return res


def update_medicine(medicine_id: int, medicines: MedicineInput):
    res = base_manager.execute("UPDATE medicine SET title=?, dosage=?, type=? WHERE id=? RETURNING id ",
                             args=(medicines.title, medicines.dosage, medicines.type, medicine_id, ))
    return res['data'][0][0]


def delete_medicine(medicine_id: int):
    res = base_manager.execute("DELETE FROM medicine WHERE id=? RETURNING id ",
                             args=(medicine_id,))
    return res['data'][0][0]
