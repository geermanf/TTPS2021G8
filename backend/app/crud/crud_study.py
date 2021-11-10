from typing import List, Optional
from sqlalchemy.sql import func
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from app.models import Study, SampleBatch, StudyHistory
from app.schemas import StudyCreate, StudyUpdate
from datetime import datetime


class CRUDStudy(CRUDBase[Study, StudyCreate, StudyUpdate]):
    def create_with_owner(
        self, db: Session, *, obj_in: StudyCreate, employee_id: int
    ) -> Study:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data, employee_id=employee_id)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_multi_by_owner(
        self, db: Session, *, employee_id: int, skip: int = 0, limit: int = 100
    ) -> List[Study]:
        return (
            db.query(self.model)
            .filter(Study.employee_id == employee_id)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def update_state(self, db: Session, db_obj: Study, new_state: str,
                     employee_id: int, updated_date: Optional[datetime] = None) -> Study:
        # TODO: validar orden de los estados
        history = StudyHistory(
            study_id=db_obj.id, state=db_obj.current_state,
            state_entered_date=db_obj.current_state_entered_date,
            employee_id=employee_id)
        db.add(history)
        db_obj.current_state = new_state
        if updated_date is None:
            date_time = func.now()
        else:
            date_time = updated_date
        db_obj.updated_date = date_time
        db_obj.current_state_entered_date = date_time
        SampleBatch.new_if_qualifies(new_state=new_state, db=db)
        db.commit()
        db.refresh(db_obj)
        return db_obj


study = CRUDStudy(Study)
