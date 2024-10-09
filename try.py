import requests
def get_token(api_key, api_secret):
    url="https://chatglm.cn/chatglm/assistant-api/v1/get_token"
    payload={
        'api_key': api_key,
        'api_secret':api_secret
    }
    response = requests.post(url,json=payload)
    print(response.text)
    if response.status_code==200:
        data=response.json()
        access_token=data['access_token']
        expires_in=data['expires_in']
        return access_token,expires_in
    else:
        print(f"获取access token失败,状态码: {response.status_code}")
        return None, None
    
api_key="53add239d78975d1"
api_secret="fdba3b2ca26202811a510080c70060f7"
access_token,expires_in=get_token(api_key,api_secret)

if access_token:
    print(f"获取成功,access_token:{access_token}")
    print(f"过期时间:{expires_in}秒")