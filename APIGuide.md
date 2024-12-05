# maiquery 接口文档

## 游戏数据查询API
> 如果你启用了**持久化存储**，这些API的uid（用户ID）字段都可以直接使用绑定过的其他平台ID替代
### 1. 获取用户信息
`/api/v1/preview/`
#### 请求方式
`GET`
#### 请求参数
| 参数名     | 类型   | 是否必须 | 说明            |
|---------|------|------|---------------|
| uid     | int  | 是    | 用户ID          |
| isLower | bool | 否    | 是否将用户名转换成半角字符 |
#### 返回示例
```json
{
    "userId": 10000000,
    "userName": "舞萌DX",
    "isLogin": false,
    "lastGameId": null,
    "lastRomVersion": "1.41.00",
    "lastDataVersion": "1.40.06",
    "lastLoginDate": "1970-01-01 00:00:00",
    "lastPlayDate": "1970-01-01 00:00:00",
    "playerRating": 15000,
    "nameplateId": 0,
    "iconId": 0,
    "trophyId": 0,
    "isNetMember": 1,
    "isInherit": false,
    "totalAwake": 1919,
    "dispRate": 0,
    "dailyBonusDate": "1970-01-01 09:00:00",
    "headPhoneVolume": null,
    "banState": 0
}
```
## 功能API
## 控制API