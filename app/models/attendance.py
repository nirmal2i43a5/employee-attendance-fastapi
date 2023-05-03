
from sqlalchemy import Column, Integer, String, DateTime, Date, func, ForeignKey, Boolean
from sqlalchemy.orm import relationship

from app.db import Base



class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    status = Column(Boolean(), default=True)
    remarks = Column(String(),index = True)
    attendance_date = Column(Date, default=func.now())
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

