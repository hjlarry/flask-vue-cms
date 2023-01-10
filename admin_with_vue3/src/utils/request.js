import axios from 'axios'
import { ElMessage, ElMessageBox } from 'element-plus'
import { appStore } from '@/store/app_store'
import { userStore } from '@/store/user_store'

const service = axios.create({
  baseURL: import.meta.env.VITE_BASE_API,
  timeout: 5000
})

service.interceptors.request.use(
  (config) => {
    const aStore = appStore()
    const uStore = userStore()
    if (uStore.token) {
      config.headers.Authorization = 'Bearer ' + uStore.token
    }
    config.headers['Accept-Language'] = aStore.language
    return config
  },
  (error) => {
    return Promise.reject(error)
  }
)

// respone拦截器
service.interceptors.response.use(
  (response) => {
    /**
     * code为非0是抛错 可结合自己业务进行修改
     */
    const res = response.data
    const uStore = userStore()
    if (res.code !== 0) {
      ElMessage({
        message: res.error,
        type: 'error',
        duration: 5 * 1000
      })

      // 50008:非法的token; 50012:其他客户端登录了;  50014:Token 过期了;
      if (res.code === 401 || res.code === 50012 || res.code === 50014) {
        ElMessageBox.confirm(
          '你已被登出，可以取消继续留在该页面，或者重新登录',
          '确定登出',
          {
            confirmButtonText: '重新登录',
            cancelButtonText: '取消',
            type: 'warning'
          }
        ).then(() => {
          uStore.logout()
        })
      }
      return Promise.reject(new Error(res.error || 'Error'))
    } else {
      return response.data
    }
  },
  (error) => {
    console.log('err' + error) // for debug
    if (error.response && error.response.status === 401) {
      uStore.logout()
    }
    ElMessage({
      message: error.message,
      type: 'error',
      duration: 5 * 1000
    })
    return Promise.reject(error)
  }
)

export default service
