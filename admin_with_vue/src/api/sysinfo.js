import request from '@/utils/request'

export function fetchInfo() {
  return request({
    url: '/sysinfo',
    method: 'get'
  })
}

export function fetchLogList(query) {
  return request({
    url: '/operation_log',
    method: 'get',
    params: query
  })
}

export function deleteLog(data) {
  return request({
    url: '/operation_log/delete',
    method: 'delete',
    data
  })
}
