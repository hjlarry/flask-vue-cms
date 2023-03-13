import { resultSuccess } from './_util'

const hintData = {
  result: [
    'app',
    'app界面',
    'app首页',
    'app logo',
    'app引导页',
    'art deco',
    'app展示',
    'ai',
    'angelababy',
    'app ui'
  ]
}

const hotData = {
  result: [
    {
      id: 'nature photography',
      photo:
        'https://images.pexels.com/photos/2127969/pexels-photo-2127969.jpeg?auto=compress&cs=tinysrgb&dpr=1&fit=crop&h=250&w=360',
      title: '自然摄影'
    },
    {
      id: 'Farm',
      photo:
        'https://images.pexels.com/photos/1832328/pexels-photo-1832328.jpeg?auto=compress&cs=tinysrgb&dpr=1&fit=crop&h=250&w=360',
      title: '农场'
    },
    {
      id: 'food photography',
      photo:
        'https://images.pexels.com/photos/1652312/pexels-photo-1652312.jpeg?auto=compress&cs=tinysrgb&dpr=1&fit=crop&h=250&w=360',
      title: '美食摄影'
    },
    {
      id: 'Afternoon tea',
      photo:
        'https://images.pexels.com/photos/1292862/pexels-photo-1292862.jpeg?auto=compress&cs=tinysrgb&dpr=1&fit=crop&h=250&w=360',
      title: '下午茶'
    },
    {
      id: 'color theme',
      photo:
        'https://images.pexels.com/photos/4711052/pexels-photo-4711052.jpeg?auto=compress&cs=tinysrgb&dpr=1&fit=crop&h=250&w=360',
      title: '颜色'
    },
    {
      id: 'work',
      photo:
        'https://images.pexels.com/photos/2127969/pexels-photo-2127969.jpeg?auto=compress&cs=tinysrgb&dpr=1&fit=crop&h=250&w=360',
      title: '工作'
    },
    {
      id: 'Like a breath of fresh air',
      photo:
        'https://images.pexels.com/photos/7412111/pexels-photo-7412111.jpeg?auto=compress&cs=tinysrgb&dpr=1&fit=crop&h=250&w=360',
      title: '小清新'
    }
  ]
}

export default [
  {
    url: '/mock/hint',
    method: 'GET',
    response: () => {
      return resultSuccess(hintData)
    }
  },
  {
    url: '/mock/hot',
    method: 'GET',
    response: () => {
      return resultSuccess(hotData)
    }
  }
]
