import json
# [] : 리스트, 시퀀스형 테이터를 관리, 크기를 지정하지 않아도 자동 크기 조절, Mutable(읽기, 쓰기), 데이터 타입이 아무거나 와도 됨
# {} : 딕셔너리, 키와 값의 쌍으로 구성되어있음
# () : 튜플, 시퀀스형 데이터 Immutable(읽기만 가능), Packing / Unpacking

# person = 10, "M", "경기도 수원시", "곰돌이", True
# print(person)
# age, gender, addr, name, adult = person # Unpacking
# 
# print(divmod(23,5))

customer = {
    "id": 100,
    "name": "곰돌이사육사",
    "history": [
        {"data" : "2023-05-05", "Product" : "iPhone 14 pro"},
        {"data" : "2024-04-01", "Product" : "iPhone 16 Pro"}
    ]
}