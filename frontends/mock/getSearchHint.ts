import { resultSuccess } from './_util'

const data = {
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

export default [
  {
    url: '/mock/hint',
    method: 'GET',
    response: () => {
      return resultSuccess(data)
    }
  }
]
