from sqlalchemy import Column, String, DateTime, Text, Boolean
from sqlalchemy.sql import func
import uuid

from ..database import Base

def generate_uuid():
    return str(uuid.uuid4())

class RoomDB(Base):
    """数据库中的Room表模型
    
    注意: 此模型已针对MySQL 8.0进行了优化
    """
    __tablename__ = "rooms"
    
    # 指定MySQL表的字符集和排序规则
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_general_ci'
    }

    # 在MySQL中，使用VARCHAR替代PostgreSQL的TEXT类型较好
    id = Column(String(36), primary_key=True, default=generate_uuid)
    room_id = Column(String(12), unique=True, index=True, nullable=False)
    name = Column(String(30), nullable=False)
    status = Column(String(10), nullable=False, default="offline")
    # MySQL 8.0支持默认CURRENT_TIMESTAMP和ON UPDATE CURRENT_TIMESTAMP
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    description = Column(String(1000), nullable=True)  # MySQL中使用VARCHAR(1000)替代TEXT
    is_public = Column(Boolean, default=True)

    def __repr__(self):
        return f"<Room(room_id='{self.room_id}', name='{self.name}', status='{self.status}')>" 