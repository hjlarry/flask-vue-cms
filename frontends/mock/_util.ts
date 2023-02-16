export function resultSuccess<T = any>(data: T, { message = 'ok' } = {}) {
  return {
    code: 0,
    data,
    message,
    type: 'success'
  }
}

export function resultPageSuccess<T = any>(
  page: number,
  pageSize: number,
  list: T[],
  { message = 'ok' } = {}
) {
  const pageData = pagination(page, pageSize, list)

  return {
    ...resultSuccess({
      list: pageData,
      total: list.length
    }),
    message
  }
}

export function resultError(
  message = 'Request failed',
  { code = 999, result = null } = {}
) {
  return {
    code,
    result,
    message,
    type: 'error'
  }
}

export function pagination<T = any>(
  pageNo: number,
  pageSize: number,
  array: T[]
): T[] {
  const offset = (pageNo - 1) * Number(pageSize)
  return offset + Number(pageSize) >= array.length
    ? array.slice(offset, array.length)
    : array.slice(offset, offset + Number(pageSize))
}
