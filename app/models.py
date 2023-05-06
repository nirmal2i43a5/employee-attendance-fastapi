
from sqlalchemy import Column, Integer, String, DateTime, Date, func, ForeignKey, Boolean
from sqlalchemy.orm import relationship,declarative_base

Base = declarative_base()

class Department(Base):
    __tablename__ = "departments"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    employee = relationship("Employee", backref="department")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())



class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean(), default=True)
    is_superuser = Column(Boolean(), default=False)
    # employee = relationship("Employee", back_populates="user")
    employee = relationship("Employee", backref="user")
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    address = Column(String)
    contact = Column(String)
    # image
    # thumbnail
    attendance = relationship("Attendance", backref="employee")
    user_id = Column(Integer, ForeignKey('users.id'))
    department_id = Column(Integer, ForeignKey('departments.id'))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    

class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey('employees.id'))
    status = Column(Boolean(), default=True)
    remarks = Column(String(),index = True)
    attendance_date = Column(Date, default=func.now())
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())




