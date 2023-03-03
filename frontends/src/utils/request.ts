import axios from 'axios'
import type { AxiosInstance, AxiosRequestConfig, AxiosResponse } from 'axios'

import { message as msg } from '@/libs/message'

type Result<T> = {
  code: number
  message: string
  data: T
}

export class Request {
  instance: AxiosInstance
  baseConfig: AxiosRequestConfig = {
    baseURL: import.meta.env.VITE_BASE_API,
    timeout: 5000
  }
  constructor(config: AxiosRequestConfig) {
    this.instance = axios.create(Object.assign(this.baseConfig, config))
    this.instance.interceptors.request.use(
      (config: AxiosRequestConfig) => {
        return config
      },
      (error: any) => {
        return Promise.reject(error)
      }
    )
    this.instance.interceptors.response.use(
      (response: AxiosResponse) => {
        const { code, message, data } = response.data
        if (code === 0) {
          return data
        } else {
          msg('error', message)
          return Promise.reject(new Error(message || 'Error'))
        }
      },
      (error: any) => {
        msg('error', error.response)
        return Promise.reject(error.response)
      }
    )
  }

  public request(config: AxiosRequestConfig): Promise<AxiosResponse> {
    return this.instance.request(config)
  }

  public get(
    url: string,
    config?: AxiosRequestConfig
  ): Promise<AxiosResponse<Result<T>>> {
    return this.instance.get(url, config)
  }

  public post(
    url: string,
    data?: any,
    config?: AxiosRequestConfig
  ): Promise<AxiosResponse<Result<T>>> {
    return this.instance.post(url, data, config)
  }
}

export default new Request({})
