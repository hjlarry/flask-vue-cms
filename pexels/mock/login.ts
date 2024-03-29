import { resultSuccess, resultError } from './_util'

const profileData = {
  nickname: '非法操作',
  company: '',
  homePage: '',
  introduction: '',
  vipLevel: 2,
  avatar:
    'http://static10040.snailmobile.com/pc/public/images/package_a50910c.png',
  payResult: false,
  username: 'admin'
}

export default [
  {
    url: '/mock/login',
    method: 'POST',
    response: ({ body }) => {
      if (body.data.username === 'admin' && body.data.password === 'admin') {
        return resultSuccess({ token: 'randomgentoken' })
      }
      return resultError('password missmatch', { code: 5001 })
    }
  },
  {
    url: '/mock/register',
    method: 'POST',
    response: ({ body }) => {
      if (body.data.username === 'admin') {
        return resultSuccess()
      }
      return resultError('reg error', { code: 5002 })
    }
  },
  {
    url: '/mock/info',
    method: 'GET',
    response: ({ headers }) => {
      if (headers.authorization === 'Bearer randomgentoken') {
        return resultSuccess(profileData)
      }
      return resultError('token incorrect', { code: 5003 })
    }
  },
  {
    url: '/mock/info',
    method: 'POST',
    response: () => {
      return resultSuccess()
    }
  }
]
