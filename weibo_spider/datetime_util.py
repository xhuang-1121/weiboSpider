from datetime import datetime


def str_to_time(text):
    """将字符串转换成时间类型"""
    return (
        datetime.strptime(text, '%Y-%m-%d %H:%M')
        if ':' in text
        else datetime.strptime(text, '%Y-%m-%d')
    )
