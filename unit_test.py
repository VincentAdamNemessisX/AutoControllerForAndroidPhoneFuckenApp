# Author: 
# created_time:
from AutoSubmitFromAPI import main

# res = upload_img(
#     "eyJhbGciOiJSUzUxMiJ9.eyJBVFRSX3VzZXJObyI6IjMzMjIwNTAxMDQiLCJzdWIiOiIzMzIyMDUwMTA0IiwiaXNzIjoiY2FzLnNxZ3h5LmVkdS5jbiIsImRldmljZUlkIjoiWmtyeVRZcE5PV2NEQUlBWnhBcTdRS0luIiwiQVRUUl9pZGVudGl0eVR5cGVJZCI6IjRjZmM5NmMwNDAzMTExZWNkZGZlODViMjNjOGFjMDlkIiwiQVRUUl9hY2NvdW50SWQiOiIzOTdjYzU3MDMxMjYxMWVkNWVjNGUwNWZiMGNjNDJlOSIsIkFUVFJfdXNlcklkIjoiMzk2ODdhMjAzMTI2MTFlZDVlYzRlMDVmYjBjYzQyZTkiLCJBVFRSX2lkZW50aXR5VHlwZUNvZGUiOiJTMDIiLCJBVFRSX2lkZW50aXR5VHlwZU5hbWUiOiLlrabnlJ8iLCJBVFRSX29yZ2FuaXphdGlvbk5hbWUiOiIyMuS4k-WNh-acrOS_oeaBr-euoeeQhuS4juS_oeaBr-ezu-e7nzHnj60iLCJBVFRSX3VzZXJOYW1lIjoi6LW16ZOc5petIiwiZXhwIjoxNzE4Nzc5NzQ0LCJBVFRSX29yZ2FuaXphdGlvbklkIjoiMDZfMzMyMjA1MDEiLCJpYXQiOjE3MTYxODc3NDQsImp0aSI6IklkLVRva2VuLWlraG5mZ2pRZWo0dktJUVAiLCJyZXEiOiJjb20uc3Vwd2lzZG9tLnNxZ3h5YXBwIiwiQVRUUl9vcmdhbml6YXRpb25Db2RlIjoiMDZfMzMyMjA1MDEifQ.r3iqUHzmlaVftFYNznz_rTp1YN1yD7P2hOGJ5pTWJOwJN27jQIuYFxfhciylztXiuzZaFpvaBOZoDOmHBmS-cxlsgiBGw0YNPzMB06AXgFRAZxi_2LI5Fh0Qeqmtrrv8L4Eu2Bwk8NrkcmmeTsUt7_LL1YkU84ilAVhLSRiCzxuQqoUssvpVzcmx2SwKkcKYRNyWfHI5q8ILWMotWBmUtD7DJKN975WPoAywLvZOz56FmOrRV9WKClXv3BSHf0nvRq_iDGRdHWwD58TfwDTyx8aeny0PAJceKRy3h0ndAF5BYiZkBtrVFi9_fSEUx4LlEtpqtkKN-FhMybBIvKjlvQ",
#     "./img/1.png")
# print(res)
# print(init_start_time_and_end_time(2022, 2024))
# init_stamp()
# res = submit_data(
#     "eyJhbGciOiJSUzUxMiJ9.eyJBVFRSX3VzZXJObyI6IjMzMjIwNTAxMDQiLCJzdWIiOiIzMzIyMDUwMTA0IiwiaXNzIjoiY2FzLnNxZ3h5LmVkdS5jbiIsImRldmljZUlkIjoiWmtyeVRZcE5PV2NEQUlBWnhBcTdRS0luIiwiQVRUUl9pZGVudGl0eVR5cGVJZCI6IjRjZmM5NmMwNDAzMTExZWNkZGZlODViMjNjOGFjMDlkIiwiQVRUUl9hY2NvdW50SWQiOiIzOTdjYzU3MDMxMjYxMWVkNWVjNGUwNWZiMGNjNDJlOSIsIkFUVFJfdXNlcklkIjoiMzk2ODdhMjAzMTI2MTFlZDVlYzRlMDVmYjBjYzQyZTkiLCJBVFRSX2lkZW50aXR5VHlwZUNvZGUiOiJTMDIiLCJBVFRSX2lkZW50aXR5VHlwZU5hbWUiOiLlrabnlJ8iLCJBVFRSX29yZ2FuaXphdGlvbk5hbWUiOiIyMuS4k-WNh-acrOS_oeaBr-euoeeQhuS4juS_oeaBr-ezu-e7nzHnj60iLCJBVFRSX3VzZXJOYW1lIjoi6LW16ZOc5petIiwiZXhwIjoxNzE4Nzc5NzQ0LCJBVFRSX29yZ2FuaXphdGlvbklkIjoiMDZfMzMyMjA1MDEiLCJpYXQiOjE3MTYxODc3NDQsImp0aSI6IklkLVRva2VuLWlraG5mZ2pRZWo0dktJUVAiLCJyZXEiOiJjb20uc3Vwd2lzZG9tLnNxZ3h5YXBwIiwiQVRUUl9vcmdhbml6YXRpb25Db2RlIjoiMDZfMzMyMjA1MDEifQ.r3iqUHzmlaVftFYNznz_rTp1YN1yD7P2hOGJ5pTWJOwJN27jQIuYFxfhciylztXiuzZaFpvaBOZoDOmHBmS-cxlsgiBGw0YNPzMB06AXgFRAZxi_2LI5Fh0Qeqmtrrv8L4Eu2Bwk8NrkcmmeTsUt7_LL1YkU84ilAVhLSRiCzxuQqoUssvpVzcmx2SwKkcKYRNyWfHI5q8ILWMotWBmUtD7DJKN975WPoAywLvZOz56FmOrRV9WKClXv3BSHf0nvRq_iDGRdHWwD58TfwDTyx8aeny0PAJceKRy3h0ndAF5BYiZkBtrVFi9_fSEUx4LlEtpqtkKN-FhMybBIvKjlvQ",
#     "室内卫生", 1)
# print(res)
# main()
