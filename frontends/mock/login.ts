import { resultSuccess, resultError } from './_util'

export default [
  {
    url: '/mock/login',
    method: 'POST',
    response: ({ body }) => {
      if (body.data.username === 'admin' && body.data.password === 'admin') {
        return resultSuccess()
      }
      return resultError('password missmatch', { code: 5001 })
    }
  }
]
