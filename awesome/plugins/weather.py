from nonebot import on_command,CommandSession
import requests

'''
和风天气 API
URL : https://geoapi.heweather.net/v2/city/lookup?{参数}
'''
city_info_api = 'https://geoapi.heweather.net/v2/city/lookup?'
heweather_api = 'https://devapi.heweather.net/v7/weather/now?'
KEY = '015771f141274daa80f1684b5624f1c3'

# on_command 装饰器将函数声明为一个命令处理器
# 这里 weather 为命令的名字，同时允许使用别名[天气][天气预报][查天气]
@on_command('weather',aliases=('天气','天气预报','查天气'))
async def weather(session:CommandSession):
    # 从会话状态（session.state）中获取城市名称（city）,如果当前不存在，则询问用户
    city = session.get('city',prompt='你想查询哪个城市的天气呢？')
    # 获取城市的天气预报
    weather_report = await get_weather_of_city(city)
    # 向用户发送天气预报
    await session.send(weather_report)

async def _(session:CommandSession):
    # 去掉消息首尾的空白字符
    stripped_arg = session.current_arg_text.strip()

    if stripped_arg:
        # 第一次运行参数不为空，表示用户直接将城市名称跟在了命令后面，作为参数传入
        # 例如：天气 厦门
        session.state['city'] = stripped_arg
        return

    if not stripped_arg:
        # 用户没有发送有效的城市名称（而是发送了空白字符），则提示重新输入
        # 这里 session.pause() 将会发送消息并暂停当前会话（该行后面的代码不会被运行）
        session.pause('要查询的城市名称不能为空呢，请重新输入')

    # 如果当前正在向用户询问更多信息（例如本例中的要查询的城市），且用户输入有效，则放入会话状态
    session.state[session.current_arg_key] = stripped_arg




async def get_weather_of_city(city:str) -> str:
    # 这里简单返回一个字符串
    # 实际应用中，这里应该调用返回真实数据的天气 API ,并拼接成天气预报内容
    try:
        city_info_params = {
            'key':KEY,
            'location': city
        }
        city_info_response = requests.get(city_info_api, params=city_info_params)
        city_id = city_info_response.json()['location'][0]['id']

        weather_params = {
            'key': KEY,
            'location': city_id
        }
        weather_response = requests.get(heweather_api,params=weather_params)
        now = weather_response.json()['now']
        push_message = f"【{city}】现在天气{now['text']}" \
                       + f"\n气温:{now['temp']},体感温度:{now['feelsLike']}" \
                       + f"\n吹的是{now['windDir']},风速是{now['windSpeed']}公里/小时,是{now['windScale']}级风呢" \
                       + f"\n能见度{now['vis']}公里，云量{now['cloud']}%"
        return push_message
    except Exception as e:
        print(e)
        return f'抱歉...查询失败了...'
